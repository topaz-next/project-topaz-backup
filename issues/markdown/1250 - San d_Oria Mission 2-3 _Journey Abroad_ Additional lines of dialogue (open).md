**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Sunday Oct 04, 2020 at 09:23:53_
_Originally opened as: project-topaz/topaz - Issue 1250_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

While the mission is in progress, the NPC's message should change.

https://github.com/project-topaz/topaz/blob/8b373aa9c64081142a5f24daaac08a9b0b9d7ca8/scripts/zones/Windurst_Woods/npcs/Catalia.lua#L13-L15

```
function onTrigger(player, npc)
    local missionStatus = player:getCharVar("MissionStatus")
    if (player:getCurrentMission(SANDORIA) == tpz.mission.id.sandoria.JOURNEY_TO_WINDURST and missionStatus == 3) then
        player:startEvent(452)
    elseif (player:getCurrentMission(SANDORIA) == tpz.mission.id.sandoria.JOURNEY_ABROAD) then
        if (missionStatus == 7) then
            player:startEvent(459)
        elseif (missionStatus == 11) then
            player:startEvent(470)
        end
    elseif player:getCurrentMission(SANDORIA) == tpz.mission.id.sandoria.JOURNEY_TO_WINDURST2 and (missionStatus == 7 or missionStatus == 8) then
        player:startEvent(465)
    else
      player:startEvent(442)
    end
end
```

https://github.com/project-topaz/topaz/blob/8b373aa9c64081142a5f24daaac08a9b0b9d7ca8/scripts/zones/Windurst_Woods/npcs/Forine.lua#L11-L13

```
function onTrigger(player, npc)
    local missionStatus = player:getCharVar("MissionStatus")
    if (player:getCurrentMission(SANDORIA) == tpz.mission.id.sandoria.JOURNEY_TO_WINDURST and missionStatus == 3) then
        player:startEvent(453)
    elseif (player:getCurrentMission(SANDORIA) == tpz.mission.id.sandoria.JOURNEY_ABROAD) then
        if (missionStatus == 7) then
            player:startEvent(461)
        elseif (missionStatus == 11) then
            player:startEvent(471)
         end
    elseif player:getCurrentMission(SANDORIA) == tpz.mission.id.sandoria.JOURNEY_TO_WINDURST2 and (missionStatus == 7 or missionStatus == 8) then
        player:startEvent(464)
    else
      player:startEvent(445)
    end
end
```
https://github.com/project-topaz/topaz/blob/8b373aa9c64081142a5f24daaac08a9b0b9d7ca8/scripts/zones/Windurst_Woods/npcs/Erpolant.lua#L13-L15
```
function onTrigger(player, npc)
    local missionStatus = player:getCharVar("MissionStatus")
    if (player:getCurrentMission(SANDORIA) == tpz.mission.id.sandoria.JOURNEY_TO_WINDURST and missionStatus == 3) then
        player:startEvent(454)
    elseif (player:getCurrentMission(SANDORIA) == tpz.mission.id.sandoria.JOURNEY_ABROAD) then
        if (missionStatus == 7) then
            player:startEvent(460)
        elseif (missionStatus == 11) then
            player:startEvent(469)
        end
    elseif player:getCurrentMission(SANDORIA) == tpz.mission.id.sandoria.JOURNEY_TO_WINDURST2 and (missionStatus == 7 or missionStatus == 8) then
        player:startEvent(466)
    else
      player:startEvent(444)
    end
end
```

https://github.com/project-topaz/topaz/blob/8b373aa9c64081142a5f24daaac08a9b0b9d7ca8/scripts/zones/Heavens_Tower/npcs/Kupipi.lua#L55-L68

        elseif currentMission == tpz.mission.id.sandoria.JOURNEY_ABROAD and missionStatus == 7 then
            player:startEvent(241)
        else
            player:startEvent(251)
        end

A message is added to NPC "Uu Zhoumo" when the keyItem is lost.

https://github.com/project-topaz/topaz/blob/8b373aa9c64081142a5f24daaac08a9b0b9d7ca8/scripts/zones/Giddeus/npcs/Uu_Zhoumo.lua#L39-L51

    elseif (csid == 42) then
        player:setCharVar("MissionStatus", 6)
        player:delKeyItem(tpz.ki.SHIELD_OFFERING)
        player:messageSpecial(ID.text.XXX, tpz.ki.SHIELD_OFFERING)
    end

"ID.text.XXX" has the value "7333".



----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Monday Oct 05, 2020 at 03:22:22_

----

https://github.com/project-topaz/topaz/blob/b26aa5c6b7a1ee5138b65df1c07b3e1bb5703e35/scripts/zones/Metalworks/npcs/Riault.lua#L13-L15

    local CurrentMission = player:getCurrentMission(SANDORIA)
    local MissionStatus = player:getCharVar("MissionStatus")

    -- San d'Oria Mission 2-3 Part II - Windurst > Bastok
    if (CurrentMission == tpz.mission.id.sandoria.JOURNEY_ABROAD) then
      if (MissionStatus == 8) then 
        player:startEvent(211)
      elseif (MissionStatus == 11) then 
        player:startEvent(212)
      else
        player:startEvent(210)
      end
    else
      player:startEvent(201)
    end

https://github.com/project-topaz/topaz/blob/b26aa5c6b7a1ee5138b65df1c07b3e1bb5703e35/scripts/zones/Metalworks/npcs/Lutia.lua#L13-L15

    local CurrentMission = player:getCurrentMission(SANDORIA)
    local MissionStatus = player:getCharVar("MissionStatus")

    -- San d'Oria Mission 2-3 Part II - Windurst > Bastok
    if (CurrentMission == tpz.mission.id.sandoria.JOURNEY_ABROAD) then
      if (MissionStatus == 8) then 
        player:startEvent(214)
      elseif (MissionStatus == 11) then 
        player:startEvent(215)
      else
        player:startEvent(213)
      end
    else
      player:startEvent(202)
    end

https://github.com/project-topaz/topaz/blob/b26aa5c6b7a1ee5138b65df1c07b3e1bb5703e35/scripts/zones/Metalworks/npcs/Chantain.lua#L13-L15

    local CurrentMission = player:getCurrentMission(SANDORIA)
    local MissionStatus = player:getCharVar("MissionStatus")

    -- San d'Oria Mission 2-3 Part II - Windurst > Bastok
    if (CurrentMission == tpz.mission.id.sandoria.JOURNEY_ABROAD) then
      if (MissionStatus == 8) then 
        player:startEvent(217)
      elseif (MissionStatus == 11) then 
        player:startEvent(218)
      else
        player:startEvent(216)
      end
    else
      player:startEvent(203)
    end

https://github.com/project-topaz/topaz/blob/b26aa5c6b7a1ee5138b65df1c07b3e1bb5703e35/scripts/zones/Southern_San_dOria/npcs/Ambrotien.lua#L55-L61

When "MissionStatus == 11" A cutscene "2007" should occur.

              if (player:getCurrentMission(SANDORIA) == tpz.mission.id.sandoria.JOURNEY_ABROAD and MissionStatus == 11) then
                player:startEvent(2007)

https://github.com/project-topaz/topaz/blob/b26aa5c6b7a1ee5138b65df1c07b3e1bb5703e35/scripts/zones/Chateau_dOraguille/npcs/Halver.lua#L47-L98

After completing the mission, the NPC "Halver" is unresponsive.
You should see the message ID "7080".





----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Oct 07, 2020 at 14:06:46_

----

Fixed it again.

- NPC: Riault
```
function onTrigger(player, npc)

    local CurrentMission = player:getCurrentMission(SANDORIA)
    local MissionStatus = player:getCharVar("MissionStatus")

    if (CurrentMission ~= tpz.mission.id.sandoria.NONE) then
        if (MissionStatus == 3 or MissionStatus == 8) then 
            player:startEvent(211)
        elseif (MissionStatus == 6 or MissionStatus == 11) then 
            player:startEvent(212)
        else
            player:startEvent(210)
        end
    else
      player:startEvent(201)
    end

end
```

- NPC: Lutia
```
function onTrigger(player, npc)

    local CurrentMission = player:getCurrentMission(SANDORIA)
    local MissionStatus = player:getCharVar("MissionStatus")

    if (CurrentMission ~= tpz.mission.id.sandoria.NONE) then
        if (MissionStatus == 3 or MissionStatus == 8) then 
            player:startEvent(214)
        elseif (MissionStatus == 6 or MissionStatus == 11) then 
            player:startEvent(215)
        else
            player:startEvent(213)
        end
    else
        player:startEvent(202)
    end
end
```

- NPC: Chantain
```
function onTrigger(player, npc)

    local CurrentMission = player:getCurrentMission(SANDORIA)
    local MissionStatus = player:getCharVar("MissionStatus")

    if (CurrentMission ~= tpz.mission.id.sandoria.NONE) then
        if (MissionStatus == 3 or MissionStatus == 8) then 
            player:startEvent(217)
        elseif (MissionStatus == 6 or MissionStatus == 11) then 
            player:startEvent(218)
        else
            player:startEvent(216)
        end
    else
        player:startEvent(203)
    end

end
```

- NPC: Savae E Paleade
```
function onTrigger(player, npc)

    local CurrentMission = player:getCurrentMission(SANDORIA)
    local MissionStatus = player:getCharVar("MissionStatus")

    -- San d'Oria Mission 2-3 Part I - Bastok > Windurst
    if (CurrentMission == tpz.mission.id.sandoria.JOURNEY_ABROAD and MissionStatus == 2) then
        player:startEvent(204)
    -- San d'Oria Mission 2-3 Part II - Windurst > Bastok
    elseif (CurrentMission == tpz.mission.id.sandoria.JOURNEY_ABROAD and MissionStatus == 7) then
        player:startEvent(206)
    elseif (CurrentMission == tpz.mission.id.sandoria.JOURNEY_TO_BASTOK2 and MissionStatus == 11) then
        player:startEvent(207)
    -----------------
    elseif (CurrentMission ~= tpz.mission.id.sandoria.NONE) then
        if (MissionStatus == 6 or MissionStatus == 11) then 
            player:startEvent(209)
        else
          player:startEvent(208)
        end
    else
        player:startEvent(200)
    end

end
```
