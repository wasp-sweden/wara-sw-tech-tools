#!/usr/bin/env python3

import sys

keys = {
    "USED DIRECT DEPENDENCIES": "usedDirect",
    "USED INHERITED DEPENDENCIES": "usedInherited",
    "USED TRANSITIVE DEPENDENCIES": "usedTransitive",
    "POTENTIALLY UNUSED DIRECT DEPENDENCIES": "potentiallyUnusedDirect",
    "POTENTIALLY UNUSED INHERITED DEPENDENCIES": "potentiallyUnusedInherited",
    "POTENTIALLY UNUSED TRANSITIVE DEPENDENCIES": "potentiallyUnusedTransitive",
}

units = {"B": 1, "KB": 10**3, "MB": 10**6, "GB": 10**9, "TB": 10**12}

def parse_size(size):
    number, unit = [string.strip() for string in size.split()]
    return int(float(number)*units[unit])

def parse_dependency(dep):
    parts = dep.split(" (")
    assert(len(parts) == 2)

    name = parts[0]
    size = parse_size(parts[1][:-1])

    return {
        "name": name,
        "size": size,
    }

def read_section():
    output = []
    line = ""
    while True:
        line = sys.stdin.readline()
        if line and line.startswith("\t"):
            output.append(parse_dependency(line.strip()))
        else:
            break
    return (line.strip(), output)

def find_next_section(current):
    name = current.split(" [")[0]

    while name not in keys:
        name = sys.stdin.readline().strip().split(" [")[0]
        if not name:
            break

    if not name:
        return None
    else:
        return keys[name]

output = {}

next_section = find_next_section("")
while next_section:
    (next_line, results) = read_section()

    output[next_section] = results

    next_section = find_next_section(next_line)

print(output)

