**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Oct 09, 2020 at 12:21:22_
_Originally opened as: project-topaz/topaz - Issue 1297_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

While the mission is in progress, the NPC's dialogue should change.

https://github.com/project-topaz/topaz/blob/bdef7042ccc1791f4e3ae330255fbc5c5b87f1f0/scripts/zones/Norg/npcs/Heillal.lua#L10-L12

```
function onTrigger(player, npc)
    local RhapsodiesMission = player:getCurrentMission(ROV)
    if RhapsodiesMission == tpz.mission.id.rov.THE_BEGINNING then
        player:startEvent(281)
    else
        player:startEvent(64)
    end
end
```

https://github.com/project-topaz/topaz/blob/bdef7042ccc1791f4e3ae330255fbc5c5b87f1f0/scripts/zones/Norg/npcs/Comitiolus.lua#L17-L28
```
function onTrigger(player, npc)
    local tuningOutProgress = player:getCharVar("TuningOut_Progress")
    local RhapsodiesMission = player:getCurrentMission(ROV)

    if tuningOutProgress == 6 then
        player:startEvent(206) -- Declines request to speak to Kamui
    elseif tuningOutProgress == 7 then
        player:startEvent(208) -- Repeat hint for player to go to Beaucedine Glacier
    elseif RhapsodiesMission == tpz.mission.id.rov.THE_BEGINNING then
        player:startEvent(6)
    else
        player:startEvent(72)
    end
end
```

The NPC "Gilgamesh" becomes unresponsive.

https://github.com/project-topaz/topaz/blob/bdef7042ccc1791f4e3ae330255fbc5c5b87f1f0/scripts/zones/Norg/npcs/Gilgamesh.lua#L19-L43

```
    elseif player:getCurrentMission(ROV) == tpz.mission.id.rov.THE_PATH_UNTRAVELED then
        player:startEvent(263)
    end
```




