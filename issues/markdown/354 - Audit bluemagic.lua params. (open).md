**Labels:**

bug

focus



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Feb 19, 2020 at 06:35:20_
_Originally opened as: project-topaz/topaz - Issue 354_

----

Theres a Lua table called `params` passed to a few functions in `bluemagic.lua`, however a few of the parameters are unused.

We should either:

- Remove them
   - If so, they could always be added back later when properly implemented.
- Update the code to properly reference them
    - If so, audit all spells to make sure they set the proper values, now that it's used.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Feb 19, 2020 at 06:36:47_

----

`params.tpmod` and the `TPMOD_*` enum-like values are unused, but set in most tests.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Feb 19, 2020 at 06:37:13_

----

`params.azuretp` is unused, but set in most tests.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Feb 19, 2020 at 06:39:28_

----

`params.dmgtype` is used but undocumented and not used uniformly.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Feb 19, 2020 at 06:39:50_

----

`params.tMultiplier` is set in many tests (although not all). It's used in code but not documented in the comment on the method where it's used.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Feb 19, 2020 at 06:41:03_

----

`params.offcratiomod` is not documented, but is used in `cannonball.lua`.


----
<a href="https://github.com/SirGouki"><img src="https://avatars3.githubusercontent.com/u/11664236?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [SirGouki](https://github.com/SirGouki)**
_Wednesday Feb 19, 2020 at 07:08:32_

----

The latter choice should be done instead of the former.  They are likely in there in preparation for finishing the spells, so removing them doesn't make sense.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 19, 2020 at 11:55:50_

----

Related: #351 
