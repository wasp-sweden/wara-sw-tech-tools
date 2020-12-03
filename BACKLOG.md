# Backlog

## Milestone 1: 1 tool running on one corpus code base
+ [A,N] try out github: ericsson/ove-tutorial
+ [C] set up wara-sw-tech-tools, give permissions
+ [C] determine static analysis interchange format: OASIS SARIF https://sarifweb.azurewebsites.net/
  (implementations exist for C#, Python)
+ [A,N] set up one C/C++ project so that it can be downloaded, built, tested
+ [C] build initial list of intended corpus projects
+ [C] build initial list of intended baseline tools
+ [A,N] get one corpus project running, testing
+ [A,N] merge current branches and publish the one-liner
- [N] get clang-tidy running, testing
- [] be able to run tool on corpus project and produce readable results
- **Milestone 1** completed: 1 tool running on one corpus code base

## Milestone 2: demonstrator demonstrator
- [N] formulate our requirements for the output format
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
- [M] try dist build
- [] c/c++ cache (ccache etc)
- **Milestone 2** completed: demonstrator demonstrator up and running

## Milestone 3: scale to breadth and fix all bugs that are in the way (more C/C++ corpus projects and tools)
- prestudy for dynamic tools in Milestone 4
