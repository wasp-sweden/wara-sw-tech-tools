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
  `curl -sSL https://raw.githubusercontent.com/Ericsson/ove/master/setup | bash -s WARA-SW https://github.com/wasp-sweden/wara-sw-tech-tools`

This will create an OVE workspace directory with the name WARA-SW. Follow the setup script by entering the workspace directory and running `source ove`. You can now clone the repositories of the software corpus by running `ove fetch`.

If you have Docker installed, you can launch a pristine Ubuntu environment for building and testing the corpus projects using `ove docker`. Running `ove list-needs` in this container will list OS dependencies you will need to install using `sudo apt install` (or equivalently).

The corpus can then be used as follows:

1. Run `ove buildme` to compile the entire corpus, or specify a subset of the projects to build (e.g. `ove buildme depclean commons_numbers_examples`).
2. Tools can now be invoked using `ove <tool> [projects...]`, e.g. `ove depclean commons_numbers_examples` to run DepClean on the Apache Commons Numbers examples. This will result in a JSON report in `results/depclean/commons_numbers_examples-<timestamp>.json`.
3. Results can be presented using the TEP dashboard by running `ove dashboard <projects...>`, e.g. `ove dashboard depclean`.

## Docker images
There are Docker images with batteries included that can be used to
quickly get up and running if you just want to check a specific project out. These have
all required dependencies pre-installed and the relevant projects pre-built.

For example, the DepClean on Apache Commons Numbers example from above can be checked out by running:

`docker run --rm -it -p 8050:8050 warasw/tep:depclean`

Once downloaded, this will launch an OVE shell in the container. You can now immediately run

`ove depclean commons_numbers_examples`

which will generate output in `/ove/results/depclean/commons_numbers_examples-<timestamp>.json`.

Finally, the dashboard can be started using

`ove dashboard depclean`

and accessed on [localhost:8050](http://localhost:8050/depclean) on the host.

# Backlog
See the [Backlog](https://github.com/wasp-sweden/wara-sw-tech-tools/blob/main/BACKLOG.md) file for details.

