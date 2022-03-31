# Backlog

## Milestone X: end-to-end demonstrator example
+ [AN] Pre-built Docker images
+ [MN] build a basic dashboard application
+ [MN] depclean
     + [N] make depclean run and produce output
     + [N] create depclean test dashboard
     + [M] show some actually useful information on dashboard
     + [M] make dashboard look nice
+ [N] record results in some structured manner
     + [N] directory structure
     + [N] metadata
     + [N] handle different formats in some unified way (SARIF is nice but probably doesn't work for everything)
           comment: currently just "unified" by wrapping in a JSON object with metadata
- [MN] package + description: how to build a demonstrator for your tool (consider container image?)
- [MN] get a dashboard instance up on wara-sw.se

## Milestone Y: scale to breadth and fix all bugs that are in the way (more C/C++ corpus projects and tools)
- [] figure out how to maintain some kind of separation between tools and corpus
     - [] repo directory structure
     - [] sort out tags
- [] establish pattern for creating invocation scripts for tools on corpus projects
     - [] idiomatic way to store corpus project information such as classpaths for use by scripts/tools
- [] discuss what formats to use for different kinds of tools (see above)
- [] prestudy for dynamic tools in next Milestone
- [] dashboard result browser

## Tooling:
- Benchmarking Best Practices tool
  - [ ] B1 scan that no cron jobs are scheduled anywhere
  - [N] B2 no heavy BG processes running
  - [ ] B3 no GUI running
  - [ ] B4 CPU frequency governor set to fixed frequency or turboboost disabled
  + [N] B5 hyperthreading disabled
- [ ] Update Dynamic Best practices tool: auto-fix [B1] if possible
- [ ] Update Dynamic Best practices tool: auto-fix [B4] if possible (max frequency)
+ [N] Update Dynamic Best practices tool: auto-fix [B5] if possible
- [ ] Command-line tool "for dummies" who want to run OVE on the ERDC:
  - Script to check/install cloud access setup on client (ask for everything)
  - Spin up ERDC image, run benchmark or test on ERDC, transfer results, shut down image

## Miscellaneous
- [] fix cassandra patch issue in some better way

# Completed

+ **Milestone 1** completed: 1 tool running on one corpus code base

# Research Project Drivers

## C/C++

- tbd
  - Patrik Åberg

## Java

- Static Analysis
  - Alexandru Dura (LTH)
  - tbd

- Dynamic Analysis
  - Noric Couderc (LTH)

