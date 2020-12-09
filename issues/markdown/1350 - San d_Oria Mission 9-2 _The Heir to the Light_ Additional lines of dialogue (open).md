**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Tuesday Oct 13, 2020 at 12:32:01_
_Originally opened as: project-topaz/topaz - Issue 1350_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

- Add a line to the "NPC: Arnau" in the "Northern San d'Oria" area.
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Northern_San_dOria/npcs/Arnau.lua#L13-L24
```
function onTrigger(player, npc)
    if (player:getCurrentMission(COP) == tpz.mission.id.cop.THE_ROAD_FORKS and player:getCharVar("EMERALD_WATERS_Status") == 2) then
        player:startEvent(51) --COP event
    elseif (player:getCurrentMission(SANDORIA) == tpz.mission.id.sandoria.SAVE_THE_CHILDREN and player:getCharVar("MissionStatus") < 2) then
        player:startEvent(693)
    elseif (player:hasCompletedMission(SANDORIA, tpz.mission.id.sandoria.SAVE_THE_CHILDREN) and player:getCharVar("OptionalCSforSTC") == 1) then
        player:startEvent(694)
    -- Mission San D'Oria 9-2 The Heir to the Light
    elseif (player:getCurrentMission(SANDORIA) == tpz.mission.id.sandoria.THE_HEIR_TO_THE_LIGHT and player:getCharVar("MissionStatus") <= 1) then
        player:startEvent(3)
    else
        player:startEvent(20)
    end

end
```

- Add a line to the "NPC: Prince Royal's Rm" in the "Chateau d'Oraguille" area.
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Chateau_dOraguille/npcs/_6h0.lua#L49-L51
```
        -- San d'Oria 9-2 "The Heir to the Light" (optional)
        if currentMission == sandyMissions.THE_HEIR_TO_THE_LIGHT then
            if missionStatus > 5 then
                player:startEvent(3)
            elseif missionStatus > 4 then
                player:startEvent(7)
            elseif missionStatus > 1 then
                player:startEvent(2)
            end
```

- Add a line to the "NPC: Door:Prince Regent's Rm" in the "Chateau d'Oraguille" area.
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Chateau_dOraguille/npcs/_6h1.lua#L34-L39
```
    -- San d'Oria 9-2 "The Heir to the Light" (optional)
    elseif
        player:getCurrentMission(SANDORIA) == tpz.mission.id.sandoria.THE_HEIR_TO_THE_LIGHT then
        if player:getCharVar("MissionStatus") > 5 then
            player:startEvent(5)
        elseif player:getCharVar("MissionStatus") > 4 then
            player:startEvent(6)
        elseif player:getCharVar("MissionStatus") > 1 then
            player:startEvent(4)
        end
```
I also have a question about the "Papal Chambers" event in Northern San d'Oria.
The wiki doesn't say exactly what happened, but the "Papal Chambers" event is supposed to happen after completing Sandria mission 9-2 (after reaching rank 10).
https://www.bg-wiki.com/bg/San_d%27Oria_Mission_9-2

However, in the current implementation, it doesn't seem to occur once you reach rank 10, am I wrong?
Also, this event seems to occur many times if you look in the "Papal Chambers", but once you see the event, you should see "Locked". (Text ID: 11514) should appear.
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Northern_San_dOria/npcs/_6fc.lua#L16-L27


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Tuesday Oct 13, 2020 at 13:01:15_

----

Before setting "SandoEpilogue" to "1", there is a process to promote it to RANK 10.
Does that mean that "player:startEvent(50)" can't be executed?

https://github.com/project-topaz/topaz/blob/62431732162ab39ac05b74f6345b7538eae7bb11/scripts/zones/Chateau_dOraguille/npcs/Halver.lua#L183-L197
