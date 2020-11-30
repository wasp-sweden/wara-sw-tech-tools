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

# Installing and running
To set up the workspace run the oneliner:
  `curl -sSL https://raw.githubusercontent.com/Ericsson/ove/master/setup | bash -s WARA-SW https://github.com/wasp-sweden/wara-sw-tech-tools`

This will create an OVE workspace directory with the name WARA-SW. Follow the setup script by entering the workspace directory and running `source ove`. You can now clone the repositories of the software corpus by running `ove fetch`.

If you have Docker installed, you can launch a pristine Ubuntu environment for building and testing the corpus projects using `ove docker`. Running `ove buildme` in this container will prompt you to install missing dependencies using `sudo apt install`.

Once the corpus is built, `ove systest doxygen-clang-tidy` can be used to run an example invocation of clang-tidy on Doxygen.

For more information, read the [OVE Tutorial](https://github.com/Ericsson/ove-tutorial).

# Backlog
See the [Backlog](https://github.com/wasp-sweden/wara-sw-tech-tools/blob/main/README.md) file for details.

