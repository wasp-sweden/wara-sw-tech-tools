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

# Requirements
- Mainstream Linux distribution
- `bash`
- Most packages require compilers or run-time systems; OVE (see below) will report system dependencies as needed.

This repository uses [OVE](https://github.com/Ericsson/ove).
For more information, read the [OVE Tutorial](https://github.com/Ericsson/ove-tutorial).

# Setting up the workspace
To set up the workspace run the oneliner:
  `curl -sSL https://raw.githubusercontent.com/Ericsson/ove/master/setup | bash -s WARA-SW https://github.com/wasp-sweden/wara-sw-tech-tools`

This will create an OVE workspace directory with the name WARA-SW. Follow the setup script by entering the workspace directory and running `source ove`. You can now clone the repositories of the software corpus by running `ove fetch`.

If you have Docker installed, you can launch a pristine Ubuntu environment for building and testing the corpus projects using `ove docker`. Running `ove list-needs` in this container will list OS dependencies you will need to install using `sudo apt install` (or equivalently).

The corpus can then be used as follows:

1. Run `ove patch` to apply changes needed by the corpus.
2. Run `ove buildme` to compile the entire corpus, or specify a subset of the projects to build (e.g. `ove buildme spotbugs cassandra`).
3. Tools can now be invoked using `ove <tool> [projects...]`, e.g. `ove spotbugs cassandra` to run SpotBugs on Cassandra. This will result in a SARIF report in `cassandra/cassandra-sb.sarif`.

# Docker images
There are Docker images with batteries included that can be used to
quickly get up and running if you just want to check a specific project out. These have
all required dependencies pre-installed and the relevant projects pre-built.

For example, the SpotBugs on Cassandra example from above can be checked out by running:

`docker run -it warasw/tep:spotbugs`

Once downloaded, this will launch an OVE shell in the container. You can now immediately run

`ove spotbugs cassandra`

which will generate the SARIF report in `/ove/cassandra/cassandra-sb.sarif`.

# Backlog
See the [Backlog](https://github.com/wasp-sweden/wara-sw-tech-tools/blob/main/BACKLOG.md) file for details.

