**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Oct 11, 2020 at 01:39:18_
_Originally opened as: project-topaz/topaz - Issue 1314_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Adds a missing dialogue to Justinius while searching for Ulmia in Promathia mission 2-4 "An Eternal Melody".
Closes #864 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 04:58:51_

----

I couldn't be bothered to argue in the other PR, but since you like this pattern - let me ask you to modify how you use it:
```lua
    local copCurrentMission = player:getCurrentMission(COP)
    local copMissionStatus = player:getCharVar("PromathiaStatus")
    local copMissions = tpz.mission.id.cop
```

Granted, _this_ NPC is COP only, but this line:
```lua
if currentMission == missions.DISTANT_BELIEFS and missionStatus == 3 then
```
Gives nothing away if you don't already know what `DISTANT_BELIEFS` is.

**I think the point I'm trying and struggling to word clearly is:**
Aggressively cleaning up is great, optimising to reduce horizontal footprint is great, but not if they come with the cost of reducing information immediately available to the reader.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 04:58:51_

----

I couldn't be bothered to argue in the other PR, but since you like this pattern - let me ask you to modify how you use it:
```lua
    local copCurrentMission = player:getCurrentMission(COP)
    local copMissionStatus = player:getCharVar("PromathiaStatus")
    local copMissions = tpz.mission.id.cop
```

Granted, _this_ NPC is COP only, but this line:
```lua
if currentMission == missions.DISTANT_BELIEFS and missionStatus == 3 then
```
Gives nothing away if you don't already know what `DISTANT_BELIEFS` is.

**I think the point I'm trying and struggling to word clearly is:**
Aggressively cleaning up is great, optimising to reduce horizontal footprint is great, but not if they come with the cost of reducing information immediately available to the reader.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 05:29:55_

----

Great, thanks for baring with me :)
