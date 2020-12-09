**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Monday Oct 12, 2020 at 16:57:48_
_Originally opened as: project-topaz/topaz - Issue 1342_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

The procedure for proceeding is as follows.
https://www.bg-wiki.com/bg/San_d%27Oria_Mission_7-2
- Speak with a Gate Guard who will instruct you to go to the garden in the Chateau.
  - Trading 4 crystals to a Conquest NPC will unlock this mission.
- Head for the Chateau and go towards (F-8). You will receive a cutscene.
- Return to the Gate Guard to receive the mission.


The guard's event cutscene is wrong. The event ID "62" is
"Ambrotien : Oh, <playerName>! Hurry to the Chateau d'Oraguille. Something terrible seems to be going on!"
The conversation is not in line with the story because it is a conversation about
It also allows you to receive missions without triggering a "Chateau d'Oraguille" event.

https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Southern_San_dOria/npcs/Ambrotien.lua#L73-L74
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Southern_San_dOria/npcs/Endracion.lua#L72-L73
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Northern_San_dOria/npcs/Grilau.lua#L73-L74

The correct event ID is "1042".
"Ambrotien : Princess Claidie says that the seeds that you brought before have blossomed and she would like you to come and see them."
Also, the "Chateau d'Oraguille" event must be triggered for the mission to occur.

- Ambrotien.lua
```
function onTrigger(player, npc)

        elseif (CurrentMission ~= tpz.mission.id.sandoria.THE_SECRET_WEAPON and pRank == 7 and PresOfPapsqueCompleted == true and getMissionRankPoints(player, 19) == 1 and player:getCharVar("SecretWeaponStatus") < 2) then
            player:startEvent(1042)
function onEventFinish(player, csid, option)

    elseif (csid == 1042) then
        player:setCharVar("SecretWeaponStatus", 1)
```

- Endracion.lua
```
function onTrigger(player, npc)

        elseif (CurrentMission ~= tpz.mission.id.sandoria.THE_SECRET_WEAPON and pRank == 7 and PresOfPapsqueCompleted == true and getMissionRankPoints(player, 19) == 1 and player:getCharVar("SecretWeaponStatus") < 2) then
            player:startEvent(1041)

function onEventFinish(player, csid, option)

    elseif (csid == 1041) then
        player:setCharVar("SecretWeaponStatus", 1)
```

- Grilau.lua
```
function onTrigger(player, npc)

        elseif (CurrentMission ~= tpz.mission.id.sandoria.THE_SECRET_WEAPON and pRank == 7 and PresOfPapsqueCompleted == true and getMissionRankPoints(player, 19) == 1 and player:getCharVar("SecretWeaponStatus") < 2) then
            player:startEvent(1041)

function onEventFinish(player, csid, option)

    elseif (csid == 1041) then
        player:setCharVar("SecretWeaponStatus", 1)
```

Currently, the event occurs immediately after moving to the "Chateau d'Oraguille" area, but this is not accurate.
- Head for the Chateau and go towards (F-8). You will receive a cutscene.

https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Chateau_dOraguille/Zone.lua#L35-L36
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Chateau_dOraguille/Zone.lua#L62-L63

(F-8) so that the cutscene will play as you approach it.

```
function onInitialize(zone)
    zone:registerRegion(1, -95, 0, 75, -85, 5, 85)
end

function onRegionEnter(player, region)
    local regionID = region:GetRegionID()
    if (regionID == 1) then
        if (player:getCharVar("SecretWeaponStatus") == 1) then
            player:startEvent(0)
        end
    end
end
```

