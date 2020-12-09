**Labels:**

approved

reviewed



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Sunday Sep 13, 2020 at 17:11:34_
_Originally opened as: project-topaz/topaz - Issue 1128_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Clean up Angelica's NPC script for quest "[A Pose By Any Other Name](https://ffxiclopedia.fandom.com/wiki/A_Pose_by_Any_Other_Name)"

* table the items needed by each job [Fixes #1123]
* local a few variables
* npcUtilify quest complete
* prevent picking up quest if you're already wearing the correct body item
* move setCharVars from onTrigger to onEventFinish

