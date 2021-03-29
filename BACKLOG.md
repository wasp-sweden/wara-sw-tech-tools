# Backlog

## Milestone 2: Java Support
- [CR] Driver projects present their status, determine next steps

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

## Milestone Y: demonstrator demonstrator
- [] search for tools for comparing outputs of these tools and check for input formats
     - csv support for various hand-written tools?
     - search for existing statistical tools that can: aggregate, normalise, classify, sort, plot (bar charts, violin plots etc.), regression analysis and other correlation mechanisms, diffing
- [] decide on standard format
- [] obtain tool output in standard format
- [] support for second tool
- [] diff standard format outputs for tools
- [ALL] "Towards Milestone 3": plan forward
- [] generate html or pdf output for visualising tool output for public consumption
- [] package + description: how to build a demonstrator for your tool (consider container image?)
- [] c/c++ cache (ccache etc)
- **Milestone Y** completed: demonstrator demonstrator up and running


## Milestone Z: scale to breadth and fix all bugs that are in the way (more C/C++ corpus projects and tools)
- prestudy for dynamic tools in next Milestone


# Completed

+ **Milestone 1** completed: 1 tool running on one corpus code base
+ **Prep Milestone X** : initial discussions wrt tool output formats

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

