**Labels:**

approved



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Thursday Jul 02, 2020 at 18:51:37_
_Originally opened as: project-topaz/topaz - Issue 799_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits
This is untested, needs review and testing (which I'll do eventually).

This fixes climbpix's spawn to be accurate with retail.  No longer does it decide and lock in the ??? position for each player after talking to the mithras at the start of the quest, it varies with day.  Also, talking with Nanaa's friends is supposed to be optional, but the topaz script before made it required, which caused grief for players!


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Jul 02, 2020 at 20:59:28_

----

There's a helper function for this:
```lua
if npc:getLocalVar("[QM]Select") == 1 and npcUtil.popFromQM(player, npc, ID.mob.CLIMBPIX_HIGHRISE, {radius = 1, hide = 0}) then
    player:messageSpecial(ID.text.THF_AF_MOB)
end
```

The popFromQM function will ...
* check if the mob's already spawned
* set the mob's spawn location to near the NPC (within radius of 1 yalm)
* spawn the mob
* claim the mob



----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Friday Jul 03, 2020 at 00:33:34_

----

Thanks, I'll get this added.  This was another quest that I intended to go in and fix something simple, then the scope became much bigger.  I briefly skimmed the gambling portion of the quest; it can likely be improved.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 15, 2020 at 19:30:49_

----

Is Climbpix supposed to spawn multiple times after you have a Grapnel?


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Jul 02, 2020 at 20:59:28_

----

There's a helper function for this:
```lua
if npc:getLocalVar("[QM]Select") == 1 and npcUtil.popFromQM(player, npc, ID.mob.CLIMBPIX_HIGHRISE, {radius = 1, hide = 0}) then
    player:messageSpecial(ID.text.THF_AF_MOB)
end
```

The popFromQM function will ...
* check if the mob's already spawned
* set the mob's spawn location to near the NPC (within radius of 1 yalm)
* spawn the mob
* claim the mob



----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Friday Jul 03, 2020 at 00:33:34_

----

Thanks, I'll get this added.  This was another quest that I intended to go in and fix something simple, then the scope became much bigger.  I briefly skimmed the gambling portion of the quest; it can likely be improved.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 15, 2020 at 19:30:49_

----

Is Climbpix supposed to spawn multiple times after you have a Grapnel?


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Tuesday Jul 07, 2020 at 20:33:02_

----

I should mention thanks to coco for assisting me yet again with part of the scripts for the ???s in this PR.
