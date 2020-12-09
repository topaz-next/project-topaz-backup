**Labels:**

merge ready



<a href="https://github.com/scorchedxi"><img src="https://avatars2.githubusercontent.com/u/32467511?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [scorchedxi](https://github.com/scorchedxi)**
_Monday May 04, 2020 at 08:00:15_
_Originally opened as: project-topaz/topaz - Issue 582_

----

Added three quests, intro to teamwork, intermediate teamwork, and advanced teamwork.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday May 04, 2020 at 09:04:10_

----

```lua
        npcUtil.completeQuest(player, SANDORIA, tpz.quest.id.sandoria.INTRODUCTION_TO_TEAMWORK, {
            item = 13342,
            fame = 80, -- fame defaults to 30 if not set
            title = tpz.title.THIRDRATE_ORGANIZER,
            var = "introToTmwrk_pass"
        })
```
` npcUtil.completeQuest` will do all of this for you. Also check out our [Lua Style Guide](https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md). Haven't really dug in to the logic but it looks like it works, though you could condense some other stuff too, like
```lua
if (player:getRace() == tpz.race.HUME_M and member:getRace() == tpz.race.HUME_M or member:getRace() == tpz.race.HUME_F) then
```
could be
```lua
if (player:getRace() == tpz.race.HUME_M or player:getRace() == tpz.race.HUME_F) and 
    (member:getRace() == tpz.race.HUME_M or member:getRace() == tpz.race.HUME_F) then


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Monday May 04, 2020 at 12:01:18_

----

These can be local vars, no need to set in database as the delete in event finish 


----
<a href="https://github.com/scorchedxi"><img src="https://avatars2.githubusercontent.com/u/32467511?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [scorchedxi](https://github.com/scorchedxi)**
_Monday May 04, 2020 at 17:47:29_

----

Changing to the npcUtil seemed to make my server crash... this is what I have.
```lua
if questIntroToTeamwork == QUEST_ACCEPTED and player:getCharVar("introToTmwrk_pass") == 1 then
                -- check their inventory
                npcUtil.completeQuest(player, SANDORIA, INTRODUCTION_TO_TEAMWORK, {
                  item = {13442},
                  fame = 80,
                  title = tpz.title.THIRDRATE_ORGANIZER,
                  var = {"introToTmwrk_pass"}
                })
```


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday May 04, 2020 at 19:13:46_

----

Sorry, my syntax may have been off. I updated my comment above, should work now. Don't forget to `require("scripts/globals/npc_util")`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 10:03:45_

----

If these events are all implemented into the script now, we no longer need the comments describing them as separate lines~! 😉 

(But do keep the comments describing them when you start them later in the file 😄 )


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 10:06:35_

----

Is there an outgoing event option that the player selects to confirm that they're ready for the check?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 10:12:03_

----

We could save a few CPU cycles (and line space) by assigning locals of the player's race (right after the party size requirement succeeds) and the member's race (inside the for loop), and then check those cached values in the if instead of calling `member:getRace()` each time:
```lua
local mRace = member:getRace()
if (pRace == tpz.race.HUME_M or pRace == tpz.race.HUME_F) and (mRace == tpz.race.HUME_M or mRace == tpz.race.HUME_F) then
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 10:17:21_

----

```lua
end
elseif
```
Will probably make Lua unhappy!


----
<a href="https://github.com/scorchedxi"><img src="https://avatars2.githubusercontent.com/u/32467511?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [scorchedxi](https://github.com/scorchedxi)**
_Thursday May 07, 2020 at 12:55:54_

----

Believe it or not, both options are 0. The 'automated message' packet is what differentiates the response.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday May 08, 2020 at 20:46:30_

----

Close, just need 4 more spaces on line 193.


----
<a href="https://github.com/scorchedxi"><img src="https://avatars2.githubusercontent.com/u/32467511?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [scorchedxi](https://github.com/scorchedxi)**
_Saturday May 09, 2020 at 22:20:57_

----

New to lua, is there a reason why it will make it unhappy? :)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday May 10, 2020 at 06:16:45_

----

It won't, but the indentation is off on line 193 which caused some confusion.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday May 04, 2020 at 09:04:10_

----

```lua
        npcUtil.completeQuest(player, SANDORIA, tpz.quest.id.sandoria.INTRODUCTION_TO_TEAMWORK, {
            item = 13342,
            fame = 80, -- fame defaults to 30 if not set
            title = tpz.title.THIRDRATE_ORGANIZER,
            var = "introToTmwrk_pass"
        })
```
` npcUtil.completeQuest` will do all of this for you. Also check out our [Lua Style Guide](https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md). Haven't really dug in to the logic but it looks like it works, though you could condense some other stuff too, like
```lua
if (player:getRace() == tpz.race.HUME_M and member:getRace() == tpz.race.HUME_M or member:getRace() == tpz.race.HUME_F) then
```
could be
```lua
if (player:getRace() == tpz.race.HUME_M or player:getRace() == tpz.race.HUME_F) and 
    (member:getRace() == tpz.race.HUME_M or member:getRace() == tpz.race.HUME_F) then


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Monday May 04, 2020 at 12:01:18_

----

These can be local vars, no need to set in database as the delete in event finish 


----
<a href="https://github.com/scorchedxi"><img src="https://avatars2.githubusercontent.com/u/32467511?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [scorchedxi](https://github.com/scorchedxi)**
_Monday May 04, 2020 at 17:47:29_

----

Changing to the npcUtil seemed to make my server crash... this is what I have.
```lua
if questIntroToTeamwork == QUEST_ACCEPTED and player:getCharVar("introToTmwrk_pass") == 1 then
                -- check their inventory
                npcUtil.completeQuest(player, SANDORIA, INTRODUCTION_TO_TEAMWORK, {
                  item = {13442},
                  fame = 80,
                  title = tpz.title.THIRDRATE_ORGANIZER,
                  var = {"introToTmwrk_pass"}
                })
```


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday May 04, 2020 at 19:13:46_

----

Sorry, my syntax may have been off. I updated my comment above, should work now. Don't forget to `require("scripts/globals/npc_util")`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 10:03:45_

----

If these events are all implemented into the script now, we no longer need the comments describing them as separate lines~! 😉 

(But do keep the comments describing them when you start them later in the file 😄 )


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 10:06:35_

----

Is there an outgoing event option that the player selects to confirm that they're ready for the check?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 10:12:03_

----

We could save a few CPU cycles (and line space) by assigning locals of the player's race (right after the party size requirement succeeds) and the member's race (inside the for loop), and then check those cached values in the if instead of calling `member:getRace()` each time:
```lua
local mRace = member:getRace()
if (pRace == tpz.race.HUME_M or pRace == tpz.race.HUME_F) and (mRace == tpz.race.HUME_M or mRace == tpz.race.HUME_F) then
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 10:17:21_

----

```lua
end
elseif
```
Will probably make Lua unhappy!


----
<a href="https://github.com/scorchedxi"><img src="https://avatars2.githubusercontent.com/u/32467511?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [scorchedxi](https://github.com/scorchedxi)**
_Thursday May 07, 2020 at 12:55:54_

----

Believe it or not, both options are 0. The 'automated message' packet is what differentiates the response.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday May 08, 2020 at 20:46:30_

----

Close, just need 4 more spaces on line 193.


----
<a href="https://github.com/scorchedxi"><img src="https://avatars2.githubusercontent.com/u/32467511?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [scorchedxi](https://github.com/scorchedxi)**
_Saturday May 09, 2020 at 22:20:57_

----

New to lua, is there a reason why it will make it unhappy? :)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday May 10, 2020 at 06:16:45_

----

It won't, but the indentation is off on line 193 which caused some confusion.
