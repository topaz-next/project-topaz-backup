**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Oct 09, 2020 at 11:29:52_
_Originally opened as: project-topaz/topaz - Issue 1296_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

- After receiving the mission, the NPC "Abelard" becomes unresponsive.
Insert the following code into "function onTrigger".
```
    elseif player:getCurrentMission(ROV) == tpz.mission.id.rov.SET_FREE then
      player:startEvent(181)
```

- When you trade "Bee Pollen" to NPC "Abelard", the conversation will change depending on whether you have released a support job or not.
The NPC "Isacio" will only be mentioned if the support job is locked.

https://github.com/project-topaz/topaz/blob/34d455a9e7c91b4cd3d21b0cb4a11a253a0d872c/scripts/zones/Selbina/npcs/Abelard.lua#L65-L70

This is controlled by the eighth parameter of StartEvent.
```
    if
        player:getCurrentMission(ROV) == tpz.mission.id.rov.SET_FREE and
        npcUtil.tradeHas(trade,{{9082, 3}}) and
        player:getCharVar("RhapsodiesStatus") == 1
    then
        player:startEvent(178, 0, 0, 0, 0, 0, 0, player:hasJob(0))
    end
```

