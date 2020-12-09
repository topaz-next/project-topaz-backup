**Labels:**

merge ready



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday Mar 27, 2020 at 08:43:51_
_Originally opened as: project-topaz/topaz - Issue 444_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

**Work:**
In hindsight, I shouldn't have been using `CCharEntity` stuff inside `CBattleEntity`. This moves `ForPartyWithTrusts()` into `CCharEntity` and blocks incorrect usage from the lua side with debug break.

**Tested:**
Summoning trusts, the only current use of this function.
Warning is gone 👍 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Mar 27, 2020 at 16:30:39_

----

Instead of debug break, maybe push a nil? Then you can have liberal usage of `for pairs` wherever you want without fear of crashing the server~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Mar 27, 2020 at 16:41:15_

----

Nevermind me, this is a template and isn't returning a table.
