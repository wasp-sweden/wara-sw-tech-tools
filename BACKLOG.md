# Backlog

## Milestone 2: demonstrator demonstrator
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
- **Milestone 2** completed: demonstrator demonstrator up and running

## Milestone 3: scale to breadth and fix all bugs that are in the way (more C/C++ corpus projects and tools)
- prestudy for dynamic tools in Milestone 4


# Completed

+ **Milestone 1** completed: 1 tool running on one corpus code base

# Stakeholders

## C/C++

(no current stakeholders)

## Java

- Static Analysis
  - Alexandru Dura (LTH)
  - tbd

- Dynamic Analysis
  - Noric Couderc (LTH)
