**Labels:**

merge ready



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Wednesday Feb 19, 2020 at 22:26:14_
_Originally opened as: project-topaz/topaz - Issue 358_

----

getBattlefieldIdByBit is being passed a mask instead of a single battlefield bit, which is then being passed into battlefieldAtCapacity. This fix moves battlefieldAtCapacity to the correct place in findBattlefields and each battlefield is checked individually.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Feb 25, 2020 at 17:42:53_

----

The capacity check isn't for players in the battlefield, but if there are any open arenas (normally out of 3) to host a battle. I'm not sure if they're still supposed to show up in the list if all arenas are occupied, but it ends up doing the same thing: blocking a BCNM from starting if there's no arena to host it.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 25, 2020 at 21:05:38_

----

Letting others know that cocosolos and I spoke; I'll check the all occupied behavior in a few days.
