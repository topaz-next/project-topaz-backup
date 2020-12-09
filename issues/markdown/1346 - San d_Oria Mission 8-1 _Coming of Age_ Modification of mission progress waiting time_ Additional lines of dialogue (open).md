**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Tuesday Oct 13, 2020 at 03:25:44_
_Originally opened as: project-topaz/topaz - Issue 1346_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

1. Modification of mission progress waiting time
The mission progression procedure is as follows.
https://www.bg-wiki.com/bg/San_d%27Oria_Mission_8-1
- Return to Halver.
- Wait one earth minute, and then zone in to Northern San d'Oria for another cutscene.

The mission progress waiting time is 1 minute. In topaz, the old specification of days passing in Earth time is used.
Also in this connection, while waiting for the mission to progress, you can talk to the guards and they will have a conversation with you to inform you of events in Northern San d'Oria.

2. Although not required for mission progression, there is an event in the middle of the mission where if you visit Trion and Pieuje rooms (Door:Prince Royal's Rm and Door:Prince Regent's Rm in (H-7) and (H-8) respectively), they will each tell you about their feelings for their sister.

3. Halver's conversation will change as the mission progresses.


Here are the proposed amendments.

1. Modification of mission progress waiting time
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Chateau_dOraguille/npcs/Halver.lua#L200-L202
```
    elseif (csid == 102) then
        finishMissionTimeline(player, 3, csid, option)
        player:setCharVar("Wait1MinuteM8-1_timer", os.time() + 60) -- 1 minute earth time
```
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Northern_San_dOria/Zone.lua#L61-L62
```
    elseif (player:hasCompletedMission(SANDORIA, tpz.mission.id.sandoria.COMING_OF_AGE) and
            player:getCharVar("Mission8-1Completed") ~= 1 and os.time() >= player:getCharVar("Wait1MinuteM8-1_timer")) then
```
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Northern_San_dOria/Zone.lua#L110-L112
```
    elseif csid == 16 then
        player:setCharVar("Wait1MinuteM8-1_timer", 0)
        player:setCharVar("Mission8-1Completed", 1)
```
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Southern_San_dOria/npcs/Ambrotien.lua#L75-L78
```
        elseif (CurrentMission == tpz.mission.id.sandoria.THE_SECRET_WEAPON and player:getCharVar("SecretWeaponStatus") == 3) then
            player:startEvent(1044)
        elseif (player:hasCompletedMission(SANDORIA, tpz.mission.id.sandoria.COMING_OF_AGE) and player:getCharVar("Mission8-1Completed") ~= 1) then
            if (os.time() < player:getCharVar("Wait1MinuteM8-1_timer")) then
                -- (textID: 7333) 
            else
                player:startEvent(1046)
            end
        elseif (CurrentMission ~= tpz.mission.id.sandoria.NONE) then
            player:startEvent(2001) -- Have mission already activated
```
(textID: 7333) The following is an automatic translation of the Japanese client's message. They are slightly different from the messages of our English clients.
Ambrotien : I'm currently busy preparing for the coming of age ceremony for Princess Crady. I'm sorry, but you'll have to come back to me in a little while. There's no guarantee that anyone else will not take advantage of this opportunity to enter the country.

https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Southern_San_dOria/npcs/Endracion.lua#L74-L77
```
        elseif (CurrentMission == tpz.mission.id.sandoria.THE_SECRET_WEAPON and player:getCharVar("SecretWeaponStatus") == 3) then
            player:startEvent(1043)
        elseif (player:hasCompletedMission(SANDORIA, tpz.mission.id.sandoria.COMING_OF_AGE) and player:getCharVar("Mission8-1Completed") ~= 1) then
            if (os.time() < player:getCharVar("Wait1MinuteM8-1_timer")) then
                -- (textID: 7333) 
            else
                player:startEvent(1045)
            end
        elseif (CurrentMission ~= tpz.mission.id.sandoria.NONE) then
            player:startEvent(1001) -- Have mission already activated
```
(textID: 7333) The following is an automatic translation of the Japanese client's message. They are slightly different from the messages of our English clients.
Endracion : I'm currently busy preparing for the coming of age ceremony for Princess Crady. I'm sorry, but you'll have to come back to me in a little while. There's no guarantee that anyone else will not take advantage of this opportunity to enter the country.

https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Northern_San_dOria/npcs/Grilau.lua#L75-L78
```
        elseif (CurrentMission == tpz.mission.id.sandoria.THE_SECRET_WEAPON and player:getCharVar("SecretWeaponStatus") == 3) then
            player:startEvent(1043)
        elseif (player:hasCompletedMission(SANDORIA, tpz.mission.id.sandoria.COMING_OF_AGE) and player:getCharVar("Mission8-1Completed") ~= 1) then
            if (os.time() < player:getCharVar("Wait1MinuteM8-1_timer")) then
                -- (textID: XXXX) 
            else
                player:startEvent(1045)
            end
        elseif (CurrentMission ~= tpz.mission.id.sandoria.NONE) then
            player:startEvent(1001) -- Have mission already activated
```
I didn't get the ID number.
(textID: XXXX) The following is an automatic translation of the Japanese client's message. They are slightly different from the messages of our English clients.
Grilau : I'm currently busy preparing for the coming of age ceremony for Princess Crady. I'm sorry, but you'll have to come back to me in a little while. There's no guarantee that anyone else will not take advantage of this opportunity to enter the country.

2. Although not required for mission progression, there is an event in the middle of the mission where if you visit Trion and Pieuje rooms (Door:Prince Royal's Rm and Door:Prince Regent's Rm in (H-7) and (H-8) respectively), they will each tell you about their feelings for their sister.

https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Chateau_dOraguille/npcs/_6h0.lua#L90-L93
```
        -- San d'Oria 8-1 "Coming of Age"
        elseif (currentMission == tpz.mission.id.sandoria.COMING_OF_AGE) then
            player:startEvent(64)
        -- Default dialogue
        else
            player:startEvent(522)
        end
```

https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Chateau_dOraguille/npcs/_6h1.lua#L49-L52
```
        -- San d'Oria 8-1 "Coming of Age"
        elseif (currentMission == tpz.mission.id.sandoria.COMING_OF_AGE) then
            player:startEvent(75)
        -- Default dialogue
        else
            player:startEvent(522)
        end
```

3. Halver's conversation will change as the mission progresses.
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Chateau_dOraguille/npcs/Halver.lua#L67-L71
```
        -- Mission San d'Oria 8-1 Coming of Age --
        elseif (currentMission == tpz.mission.id.sandoria.COMING_OF_AGE and MissionStatus == 3 and player:hasKeyItem(tpz.ki.DROPS_OF_AMNIO)) then
            player:startEvent(102)
        elseif (currentMission == tpz.mission.id.sandoria.COMING_OF_AGE and MissionStatus == 1) then
            player:startEvent(58)
        elseif (currentMission == tpz.mission.id.sandoria.COMING_OF_AGE and MissionStatus == 2) then
            --  (textID: 6794, tpz.ki.DROPS_OF_AMNIO) 
```
 (textID: 6794, tpz.ki.DROPS_OF_AMNIO) The following is an automatic translation of the Japanese client's message. They are slightly different from the messages of our English clients.
Halver : I'd like you to bring me some sheep water from the Fountain of Kings in the Quicksand Cave. Princess Crady has often told me about your work. And it's a solid response to that.
