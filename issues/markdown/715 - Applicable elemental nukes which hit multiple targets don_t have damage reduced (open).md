**Labels:**



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Thursday Jun 11, 2020 at 23:46:14_
_Originally opened as: project-topaz/topaz - Issue 715_

----

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

I'll quote magic.lua itself:

> [local hasMultipleTargetReduction = spellParams.hasMultipleTargetReduction --still unused!!!](https://github.com/project-topaz/topaz/blob/release/scripts/globals/magic.lua#L1325)

The comment is telling the truth. Neither the variable nor the spellParam are referenced. Spells which are supposed to have a damage reduction for hitting multiple targets do not.

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated




