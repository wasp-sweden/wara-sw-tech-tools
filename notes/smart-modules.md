# A Chronicle on SmartModules with WARA-SW Tech Tools

## Submodules

We believe that the submodules in the SmartModules experimental setup are better handled using OVE.

`ove gitmodules2revtab` seems to require the modules to be checked out first.

TODO: sm-java also seems to use submodules...

## Namespacing

Avoiding collisions with other corpus projects is probably useful! We'll prefix
our repos with `smartmodules_`.

TODO: should probably do this with sm-java as well.

## Patching

Some software might need minor patches to play nicely with OVE. We've put these in `$OVE_PROJECT_DIR/patches`
and added `patch` scripts to the projects that need it.

TODO: We'll need some way of making sure that they are run (since that won't happen with a `buildme` call). Perhaps
put it in `configure`?

## OVE "Modules"

Many tools tested using the TEP will probably be completely independent,
and keeping track of all of their inter-dependencies in one large `projs` file
will probably get unwieldy rather quickly. Something simple like being able to
do `#include` in the `projs` file would improve that.


## Potential issues

* CoCo submodule refers to a commit that doesn't exist (!?).

* `featureextractor` fails a test with
  ```
  + diff test/temp/CoCoList.csv test/outputs/CoCoList.csv
  diff: test/outputs/CoCoList.csv: No such file or directory
  ```
  but it seems to be deprecated anyway.
