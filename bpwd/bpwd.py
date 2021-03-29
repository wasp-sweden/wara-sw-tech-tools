#!/usr/bin/env python3

import argparse
import asyncio
import os
import psutil
import subprocess
import sys

DEFAULT_CPU_WARN_THRESHOLD=10.0
DEFAULT_CPU_TERM_THRESHOLD=101.0 # 50.0
DEFAULT_WATCHDOG_INTERVAL=1

def log(str):
    print(f"[bpwd] {str}")


# Real-time watchdog:

async def watch_processes(child, args):
    try:
        while True:
            await asyncio.sleep(args.cpu_interval)
            for p in psutil.process_iter():
                cpu = p.cpu_percent()
                
                if cpu >= args.cpu_warn:
                    # Ignore if part of the benchmark
                    ppids = [pp.pid for pp in p.parents()]
                    if p.pid == child.pid or child.pid in ppids:
                        continue

                    if cpu >= args.cpu_abort:
                        log(f"warning: process {p.pid} ({p.name()}) exceeded CPU% termination threshold of {args.cpu_abort}: {cpu} %")
                        return "background process tainted results"
                    if cpu >= args.cpu_warn:
                        log(f"warning: process {p.pid} ({p.name()}) exceeded CPU% warning threshold of {args.cpu_warn}: {cpu} %")

    except asyncio.CancelledError:
        log("watchdog stopped")


async def kill_child(task, process):
    process.terminate()
    await task

async def stop_watchdog(task):
    task.cancel()
    await task


# At-start sanity checks: 

class Issue:
    def __init__(self, name, description, args):
        self.name = name
        self.description = description
        self._args = args
        self._ok = False

    def __str__(self):
        return f"{self.name}: {self.description}"

    def check(self):
        pass

    def can_fix(self):
        return False

    def is_resolved(self):
        return self._ok

    def fix(self):
        if not self.is_resolved() and self.can_fix():
            self._fix()
            self.check()
    
    def unfix(self):
        if self.can_fix():
            self._unfix()

class SMTIssue(Issue):
    def __init__(self, args):
        self._smt_changed = False
        super().__init__("SMT", "hyperthreading is enabled", args)

    def check(self):
        with open("/sys/devices/system/cpu/smt/active", "r") as f:
            enabled = int(f.read()) == 1
            log(f"SMT status: {enabled}")
            self._ok = not enabled

    def can_fix(self):
        return True

    def _fix(self):
        try:
            log(f"disabling SMT")
            with open("/sys/devices/system/cpu/smt/control", "w") as f:
                f.write("off\n")
                f.flush()
                self._smt_changed = True
        except Exception as e:
            log(f"failed to automatically disable SMT: {e}")

    def _unfix(self):
        if self._smt_changed:
            log(f"re-enabling SMT")
            with open("/sys/devices/system/cpu/smt/control", "w") as f:
                f.write("on\n")
                f.flush()
                self._smt_changed = True


def smt_fix(args):
    return True

def smt_check(args):
    return Issue("smt", "simultaneous multithreading (hyperthreading) is enabled", smt_fix)

def devil_check(args):
    return Issue("devil", "just here to be annoying")

def log_issues(issues, display_autofix = False):
    for issue in issues:
        if not issue.is_resolved():
            log(f" - [{'OK' if issue.is_resolved() else '!!'}] {issue} {'(auto-fix available)' if display_autofix and issue.can_fix() else ''}")

def count_unresolved(issues):
    return len([issue for issue in issues if not issue.is_resolved()])

def perform_sanity_checks(args):
    issues = [
        SMTIssue(args)
    ]

    for issue in issues:
        issue.check()

    greenlit = True

    if count_unresolved(issues) != 0:
        log(f"detected {count_unresolved(issues)} issues:")
        log_issues(issues, display_autofix=True)

        if args.autofix:
            log(f"attempting to automatically fix issues...")
            for issue in issues:
                issue.fix()

            if count_unresolved(issues) == 0:
                log("all issues fixed")
            else:
                log(f"{count_unresolved(issues)} issues remain:")
                log_issues(issues)

        if count_unresolved(issues) != 0:
            if args.override:
                log("running anyway due to -f/--override flag")
            else:
                log("aborting due to issues")
                greenlit = False

    return greenlit, issues


def parse_args():
    # General
    parser = argparse.ArgumentParser(
        description="Assistance for running a benchmark in accordance with best practices.",
        formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=32))
    parser.add_argument("-f", "--override", action="store_true", help="run regardless of detected issues")
    parser.add_argument("-a", "--autofix", action="store_true", help="try to automatically fix detected issues")

    # CPU percentage watcher
    parser.add_argument("--cpu-interval", type=float, help="interval for measuring CPU percentage", default=DEFAULT_WATCHDOG_INTERVAL)
    parser.add_argument("--cpu-warn", type=float, help="emit a warning when an unrelated process reaches this CPU percentage", default=DEFAULT_CPU_WARN_THRESHOLD)
    parser.add_argument("--cpu-abort", type=float, help="abort the benchmark when an unrelated process reaches this CPU percentage", default=DEFAULT_CPU_TERM_THRESHOLD)

    # Command
    parser.add_argument("command", nargs='+', help="benchmark command to run")

    return parser.parse_args()

async def main():
    args = parse_args()

    greenlit, issues = perform_sanity_checks(args)
    if not greenlit:
        sys.exit(1)

    log("executing " + str(args.command))
    child = await asyncio.create_subprocess_exec(*args.command)
    log(f"child {child.pid} running")

    child_task = asyncio.create_task(child.wait())
    watch_task = asyncio.create_task(watch_processes(child, args))

    done, pending = await asyncio.wait({child_task, watch_task}, return_when=asyncio.FIRST_COMPLETED)
    if watch_task in done:
        log("watchdog raised alarm")
        await kill_child(child_task, child)
        log("watchdog: " + watch_task.result())
    elif child_task in done:
        log("child completed; stopping watchdog")
        await stop_watchdog(watch_task)

    # Restore state modified by automatic fixing
    for issue in issues:
        issue.unfix()

asyncio.run(main())
