**Labels:**

merge ready



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 04:26:31_
_Originally opened as: project-topaz/topaz - Issue 378_

----

Also updated bluemagic.lua to properly default to NONE for
any non-damage dealing spells.

This commit follows updates breath spells to use the BREATH enum value, per:
https://github.com/project-topaz/topaz/issues/377

Fixes https://github.com/project-topaz/topaz/issues/314

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Sunday Feb 23, 2020 at 13:27:16_

----

In the future the breath spells will need the breath enum or another call to bluemagic lua to get its correct formula as it doesnt follow the magical formula at all, not even its magic burst formula


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 23, 2020 at 14:08:55_

----

If we're going to redo BLU soon-ish, I'd say keep breath spells labeled as breath spells, because whether a spell is a breath attack _will_ be accounted for.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 19:17:20_

----

Sounds good. I'll update the breath spells after a rebase. Will also add context to the issue.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 19:38:35_

----

Rebased and updated breath spells to use `attachType.BREATH`.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 04:02:55_

----

Consensus seemed to be that the 3 RANGED spells should be annotated as such. I applied those as well as fixed the two mistakes in the attackTypes.
