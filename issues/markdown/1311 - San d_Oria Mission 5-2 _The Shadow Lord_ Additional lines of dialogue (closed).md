**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Saturday Oct 10, 2020 at 16:30:34_
_Originally opened as: project-topaz/topaz - Issue 1311_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

After defeating Shadow Lord, the NPC's dialogue should change.

```
require("scripts/globals/missions")

function onTrigger(player, npc)
    local currentMission = player:getCurrentMission(SANDORIA)
    local MissionStatus = player:getCharVar("MissionStatus")
```

https://github.com/project-topaz/topaz/blob/c2aa517599909fa0473f9739861ea8feb432d9ac/scripts/zones/Chateau_dOraguille/npcs/Curilla.lua#L28-L71
```
    elseif (currentMission == tpz.mission.id.sandoria.THE_SHADOW_LORD and MissionStatus == 5) then
        player:startEvent(56)
```

https://github.com/project-topaz/topaz/blob/c2aa517599909fa0473f9739861ea8feb432d9ac/scripts/zones/Chateau_dOraguille/npcs/Rahal.lua#L17-L62
```
    elseif (currentMission == tpz.mission.id.sandoria.THE_SHADOW_LORD and MissionStatus == 5) then
        player:startEvent(77)
```

https://github.com/project-topaz/topaz/blob/c2aa517599909fa0473f9739861ea8feb432d9ac/scripts/zones/Chateau_dOraguille/npcs/Milchupain.lua#L10-L12
```
    if (currentMission == tpz.mission.id.sandoria.THE_SHADOW_LORD and MissionStatus == 5) then
        player:startEvent(33)
    else
      player:startEvent(516)
    end
```

https://github.com/project-topaz/topaz/blob/c2aa517599909fa0473f9739861ea8feb432d9ac/scripts/zones/Chateau_dOraguille/npcs/Aramaviont.lua#L10-L12
```
    if (currentMission == tpz.mission.id.sandoria.THE_SHADOW_LORD and MissionStatus == 5) then
        player:startEvent(12)
    else
      player:startEvent(518)
    end
```

https://github.com/project-topaz/topaz/blob/c2aa517599909fa0473f9739861ea8feb432d9ac/scripts/zones/Chateau_dOraguille/npcs/Arsha.lua#L10-L12
```
    if ((currentMission == tpz.mission.id.sandoria.APPOINTMENT_TO_JEUNO and MissionStatus == 2) or
        (currentMission == tpz.mission.id.sandoria.THE_SHADOW_LORD and MissionStatus == 5)) then
        player:startEvent(85)
    else
        player:startEvent(513)
    end
```

https://github.com/project-topaz/topaz/blob/c2aa517599909fa0473f9739861ea8feb432d9ac/scripts/zones/Chateau_dOraguille/npcs/Chupaile.lua#L10-L12
```
    if ((currentMission == tpz.mission.id.sandoria.APPOINTMENT_TO_JEUNO and MissionStatus == 2) or
        (currentMission == tpz.mission.id.sandoria.THE_SHADOW_LORD and MissionStatus == 5)) then
        player:startEvent(86)
    else
        player:startEvent(514)
    end
```



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 04:34:41_

----

Should be closed with: https://github.com/project-topaz/topaz/pull/1267
