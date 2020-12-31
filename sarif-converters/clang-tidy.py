#!/usr/bin/env python3

# Current issues:
# * ruleId extraction isn't great and will likely break (for instance if the message itself contains an opening bracket)
# * handling ANSI colours like this is awful

import json
import sys
import re

text_input = sys.stdin
if len(sys.argv) >= 2:
    text_input = open(sys.argv[1], "r")

# run-clang-tidy hard-codes --use-colors when invoking clang-tidy,
# so we need to consider colors when parsing its output.
pattern = re.compile("^(\x1b\\[0m)?\x1b\\[1m([^:]+):(\\d+):(\\d+): \x1b\\[0m\x1b\\[\\d+;\\d+;\\d+m(warning|note|error): \x1b\\[0m(\x1b\\[1m)?([^[\x1b]+)([^[]*\\[(.+)\\])?")

artifacts = []
artifact_indices = {}
results = []

with text_input:
    for line in text_input.readlines():
        line = line.strip()
        match = re.match(pattern, line)
        if match:
            #print(match.group(2), match.group(3), match.group(4), match.group(5), match.group(7), match.group(9))

            artifact = match.group(2)
            line = int(match.group(3))
            column = int(match.group(4))
            level = match.group(5)
            message = match.group(7).strip()
            rule = match.group(9)

            if artifact not in artifact_indices:
                artifact_indices[artifact] = len(artifacts)
                artifacts.append({
                    "location": {
                        "uri": artifact,
                    }
                })

            artifact_index = artifact_indices[artifact]

            results.append({
                "ruleId": rule or "NOTE",
                "level": level,
                "message": {
                    "text": message,
                },
                "locations": [{
                    "physicalLocation": {
                        "artifactLocation": {
                            "uri": artifact,
                            "index": artifact_index,
                        },
                        "region": {
                            "startLine": line,
                            "startColumn": column,
                        },
                    },
                }],
            })

print(json.dumps({
    "version": "2.1.0",
    "$schema": "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0-rtm.4.json",
    "runs": [{
        "tool": {
            "driver": {
                "name": "clang-tidy",
            },
        },
        "artifacts": artifacts,
        "results": results,
    }],
}, indent=True))
