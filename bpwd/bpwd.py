#!/usr/bin/env python3

import os
import sys
import subprocess
import psutil
import asyncio

CPU_WARN_THRESHOLD=10.0
CPU_TERM_THRESHOLD=50.0
WATCHDOG_INTERVAL=1

def log(str):
    print(f"[bpwd] {str}")

async def watch_processes(child):
    try:
        while True:
            await asyncio.sleep(WATCHDOG_INTERVAL)
            for p in psutil.process_iter():
                cpu = p.cpu_percent()
                
                if cpu >= CPU_WARN_THRESHOLD:
                    # Ignore if part of the benchmark
                    ppids = [pp.pid for pp in p.parents()]
                    if p.pid == child.pid or child.pid in ppids:
                        continue

                    if cpu >= CPU_TERM_THRESHOLD:
                        log(f"warning: process {p.pid} ({p.name()}) exceeded CPU% termination threshold of {CPU_TERM_THRESHOLD}: {cpu} %")
                        return "background process tainted results"
                    if cpu >= CPU_WARN_THRESHOLD:
                        log(f"warning: process {p.pid} ({p.name()}) exceeded CPU% warning threshold of {CPU_WARN_THRESHOLD}: {cpu} %")

    except asyncio.CancelledError:
        log("watchdog stopped")


async def kill_child(task, process):
    process.terminate()
    await task

async def stop_watchdog(task):
    task.cancel()
    await task

async def main(command):
    print("there is an issue; run anyway?")
    if input("y/N: ") != "y":
        sys.exit(1)

    log("executing " + str(command))
    child = await asyncio.create_subprocess_exec(*command)
    log(f"child {child.pid} running")

    child_task = asyncio.create_task(child.wait())
    watch_task = asyncio.create_task(watch_processes(child))

    done, pending = await asyncio.wait({child_task, watch_task}, return_when=asyncio.FIRST_COMPLETED)
    if watch_task in done:
        log("watchdog raised alarm")
        await kill_child(child_task, child)
        log("watchdog: " + watch_task.result())
    elif child_task in done:
        log("child completed; stopping watchdog")
        await stop_watchdog(watch_task)

asyncio.run(main(sys.argv[1:]))
