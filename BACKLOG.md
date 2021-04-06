# Backlog

## SmartModules
- [AN] Import all repositories, set up the directory structure.
+ [AN] Build and run tests for the tools (pretty straightforward except for sm-java / libsm / container-sub).
  + sm-java
  + coco
  + collectionSwitch
- [ ] Run the generated variants that are available once.
- [ ] Make script that can re-build variant that are indicated to work in the Status.org file in the repo (the ones that don't work are tagged as :error:. You can use the existing snippets in the file, but the result might be very copy-pasty.
- [ ] Use the existing code to generate experimental data and plots.
- [ ] I already have some setup for tracking what machine the benchmarks were run on. Find in the code where it is. Suggest improvements
- [ ] See if you can use different JVMs and JVM params.
- [ ] Try out the setup on ERDC.

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
- [AN] Pre-built Docker image

## Milestone 2: Java Support
- [CR] Driver projects present their status, determine next steps

## Milestone Y: demonstrator demonstrator
+ [N] formulate our requirements for the output format
  - mandatory:
    - source location
	- bug category marker
	- human-readable-description
  - optional:
    - AST node
	- links to other relevant source locations
+ [M] try dist build
- [A] check available output formats:
     - https://github.com/Ericsson/codechecker
     - OASIS SARIF
     - what output formats do the existing tools support otherwise?
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

