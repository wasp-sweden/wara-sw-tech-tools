# WARA-SW: Software Corpus and Offline Tool Evaluation Platform

Aim: Make it easy to evaluate (offline) software tools on existing
Open Source software, with a foucs on software used in the Swedish
industry.

This repository will provide a collection of Open Source projects (via git references), plus infrastructure for evaluating offline software tools on that software.
Tools intended for evaluation include:
- static checkers
- compilers
- (more to come)

This repository is part of the [Wallenberg AI, Autonomous Systems and
Software Program (WASP)](https://wasp-sweden.org/), specifically the
WASP [Research Arena for Software
(WARA-SW)](https://wasp-sweden.org/research/research-arenas/wara-sw/).

## Requirements
- Mainstream Linux distribution
- `bash`
- The dashboard requires Python 3 and Plotly Dash (see below).
- Most packages require compilers or run-time systems; OVE (see below) will report system dependencies as needed.

This repository uses [OVE](https://github.com/Ericsson/ove).
For more information, read the [OVE Tutorial](https://github.com/Ericsson/ove-tutorial).

## Setting up the workspace
To set up the workspace run the oneliner:

    curl -sSL https://raw.githubusercontent.com/Ericsson/ove/master/setup | bash -s WARA-SW https://github.com/wasp-sweden/wara-sw-tech-tools

This will create an OVE workspace directory with the name WARA-SW. Follow the setup script by entering the workspace directory and running `source ove`. You can now clone the repositories of the software corpus by running `ove fetch`. Example:

    $ curl -sSL https://raw.githubusercontent.com/Ericsson/ove/master/setup | bash -s WARA-SW https://github.com/wasp-sweden/wara-sw-tech-tools
    ...
    $ cd WARA-SW
    $ source ove
    OVE f902139 | Ubuntu 20.04 | GNU/Linux
    $ ove fetch
    actor-framework     Cloning into '.../WARA-SW/actor-framework'...
    commons-numbers     Cloning into '.../WARA-SW/commons-numbers'...
    cassandra           Cloning into '.../WARA-SW/cassandra'...
    ...

If you have Docker installed, you can launch a pristine Ubuntu environment for building and testing the corpus projects using `ove docker`. Running `ove list-needs` in this container will list OS dependencies you will need to install using `sudo apt install` (or equivalently).

The corpus can then be used as follows:

1. Run `ove buildme/buildme-parallel` to compile the entire corpus, or specify a subset of the projects to build. Examples:

    $ ove buildme depclean commons_numbers_examples
    $ ove buildme corpus +small +c
    $ ove buildme tools +medium +java

2. Tools can now be invoked using `ove <tool> [subject...]`, e.g. `ove depclean -s commons_numbers_examples` to run DepClean on the Apache Commons Numbers examples. This will result in a JSON report in `results/depclean/default/commons_numbers_examples-<timestamp>.json`.
3. Results can be presented using the TEP dashboard by running `ove dashboard <projects...>`, e.g. `ove dashboard depclean`.

## Docker images
There are Docker images with batteries included that can be used to
quickly get up and running if you just want to check a specific project out. These have
all required dependencies pre-installed and the relevant projects pre-built.

For example, the DepClean on Apache Commons Numbers example from above can be checked out by running:

    $ docker run --rm -it -p 8050:8050 warasw/tep:depclean

Once downloaded, this will launch an OVE shell in the container. You can now immediately run

    $ ove depclean -s commons_numbers_examples

which will generate output in `/ove/results/depclean/simple/commons_numbers_examples-<timestamp>.json`.

Finally, the dashboard can be started using

    $ ove dashboard depclean

and accessed on [localhost:8050](http://localhost:8050/depclean) on the host.
More information about the dashboard can be found [below](#Dashboard).


# Tools

## OVE

[OVE](https://github.com/Ericsson/ove) is gathering git repositories and the knowledge how to build and test them.

## V.A.C.C.I.N.A.T.E.

[V.A.C.C.I.N.A.T.E.](https://github.com/nilsceberg/vaccinate) is a simple test tool that pretends it does useful static analysis.

* **OVE project**: vaccinate
* **Invocation**: `ove vaccinate <subject>`

## DepClean

[DepClean](https://github.com/castor-software/depclean) automatically removes dependencies that are included in your Java dependency tree but are not actually used in the project's code.

* **OVE project**: depclean
* **Invocation**: `ove depclean [-s] <subject>`
  * `-s`: parse default text output instead of writing JSON directly (used for the example dashboard)

## DMCE (Did My Code Execute)
[DMCE](https://github.com/PatrikAAberg/dmce) is a source code level instrumentation tool for C/C++ that enables dynamic code execution tracking without build tool chain dependencies. Probes c/c++ expressions added between two git revisions. Consists of a bunch of bash and python scripts on top of clang-check and git.

* **OVE project**: dmce
* **Invocation**: `ove dmce`

The above command will trigger the help text. Please note that dmce can also be run stand-alone from the git or by installing a debian package. Further instructions can be found on the dmce github page following the link above.

## Adding a new tool

Adding a new tool comprises the following steps:

* Add a Git repository to `revtab`. Edit the `revtab` file manually or use `ove add-repo`:

        $ ove add-repo https://github.com/foobar/toolA toolA main
* Add an entry to `projs`. Edit the `projs` file manually or use `ove add-project`:

        $ ove add-project toolA toolA bootstrap@./autogen.sh configure@./configure build@make
* Create build scripts in `projects/<tool>`. Skip this step if you already specified the build scripts with `ove add-project`.
* Create an invocation script for the tool as `scripts/<tool>`, or on each corpus project to enable the tool for as `projects/<project>/<tool>` if the extra
  flexibility is required. This script should pipe JSON out into `ove-mkresult <tool> <subject> <tag>`, which will create a result file.

The tool should now be able to be invoked on a project as `ove <tool> <subject>`.

See the [Dashboard](#Dashboard) section for information on how to create a dashboard for the tool.


# Corpus

## Apache Commons Numbers
The [Apache Commons Numbers](https://github.com/apache/commons-numbers) project provides number types and utilities.

**OVE project**: commons_numbers_examples

## Cassandra
[Cassandra](https://cassandra.apache.org/_/index.html) is a NoSQL distributed database.

**OVE project**: cassandra

## Doxygen
[Doxygen](https://www.doxygen.nl/index.html) is a documentation generator and static analysis tool for software source trees.

**OVE project**: doxygen

## Git
[Git](https://git-scm.com/)

**OVE project**: git

## Redis
[Redis](https://redis.io/) is an in-memory database that persists on disk.

**OVE project**: redis

# Dashboard

The dashboard is the primary way to graphically view results. Project scripts can include a `dash` script using the TEP (Tool Exploration Platform) library Plotly Dash to create dashboard components.
The following is an excerpt from the V.A.C.C.I.N.A.T.E. dash script that can be used as an example.

```python
subjects = ["cassandra"]

def create_histogram(filename):
	with open(filename) as results_file:
		results = json.load(results_file)
		data = {"characters/line": results["results"]}
		return px.histogram(data), results["meta"]


result_files = [(subject, file) for subject in subjects for file in get_results_files("vaccinate", subject)]

dashboard = Dashboard(title = "V.A.C.C.I.N.A.T.E.")

for (subject, file) in result_files:
	graph, meta = create_histogram(file)
	dashboard.add(Graph(graph, title=subject, meta=meta)
```

