**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Monday Oct 12, 2020 at 14:29:39_
_Originally opened as: project-topaz/topaz - Issue 1340_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

- Add a conversation pattern to the "Door:Prince Royal's Rm" in the area "Chateau d'Oraguille".
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Chateau_dOraguille/npcs/_6h0.lua#L61-L69
```
    elseif (currentMission == tpz.mission.id.sandoria.RANPERRE_S_FINAL_REST) then
        if (missionStatus == 1) then
            player:startEvent(80)
        elseif (player:hasKeyItem(tpz.ki.ANCIENT_SANDORIAN_BOOK)) then
            player:startEvent(79)
        elseif (missionStatus == 5) then
            player:startEvent(21)
        elseif (missionStatus == 6) then
            player:startEvent(50)
        elseif (missionStatus == 7) then
            player:startEvent(49)
        end
```
- Add a conversation pattern to "Halver" in the area "Chateau d'Oraguille".
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Chateau_dOraguille/npcs/Halver.lua#L105-L110
```
        elseif (currentMission == tpz.mission.id.sandoria.JOURNEY_ABROAD) then
            player:startEvent(532)
        elseif (currentMission == tpz.mission.id.sandoria.RANPERRE_S_FINAL_REST) then
            if (MissionStatus == 6) then
              --  Halver : I also thank you, my lord. I felt sick to my stomach whenever the subject of the Dragon King's tomb came up in the Imperial Council. But I still have a mission to visit the mausoleum as the spearhead. Do not relax. (textID: 6765) 
            elseif (MissionStatus == 7) then
              --  Halver : I also thank you, my lord. I felt sick to my stomach whenever the subject of the Dragon King's tomb came up in the Imperial Council. Now, go to the Gatehouse and report to the end of your mission. (textID: 6767) 
            end
        -- Default dialogue 
        else
            player:startEvent(577)
        end
```

- Add a conversation pattern to "Tombstone" in the area "King Ranperre's Tomb".
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/King_Ranperres_Tomb/npcs/Tombstone.lua#L29-L37
```
    if X >= -1 and X <= 1 and Z >= -106 and Z <= -102 then
        if currentMission == tpz.mission.id.sandoria.BAT_HUNT and missionStatus <= 1 then
            player:startEvent(4)
        else
            player:startEvent(2)
        end
    elseif currentMission == tpz.mission.id.sandoria.RANPERRE_S_FINAL_REST and missionStatus == 3 and not player:hasKeyItem(tpz.ki.ANCIENT_SANDORIAN_BOOK) then
        player:startEvent(8)
    else
      -- It looks like the true tomb of King Lampert. (text ID: 7311)
    end
```

- Add a message to pass the KeyItem "Ancient San d'Orian book" to the guard.
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Southern_San_dOria/npcs/Ambrotien.lua#L97-L100
```
    if (csid == 1036) then
        player:delKeyItem(tpz.ki.ANCIENT_SANDORIAN_BOOK)
        player:setLocalVar("RanperresRest", 1) -- set to require a zone
        player:setCharVar("MissionStatus", 4)
        -- I gave him "Ancient San d'Orian book". (Text ID: 7309,  tpz.ki.ANCIENT_SANDORIAN_BOOK)
```
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Southern_San_dOria/npcs/Endracion.lua#L96-L99
```
    if (csid == 1035) then
        player:delKeyItem(tpz.ki.ANCIENT_SANDORIAN_BOOK)
        player:setLocalVar("RanperresRest", 1) -- set to require a zone
        player:setCharVar("MissionStatus", 4)
        -- I gave him "Ancient San d'Orian book". (Text ID: 7309, , tpz.ki.ANCIENT_SANDORIAN_BOOK))
```
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Northern_San_dOria/npcs/Grilau.lua#L97-L100
```
    if (csid == 1035) then
        player:delKeyItem(tpz.ki.ANCIENT_SANDORIAN_BOOK)
        player:setLocalVar("RanperresRest", 1) -- set to require a zone
        player:setCharVar("MissionStatus", 4)
        -- I gave him "Ancient San d'Orian book". (Text ID: 7684, tpz.ki.ANCIENT_SANDORIAN_BOOK)
```



----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 12, 2020 at 19:52:59_

----

@eyes-and-brain I would really like to implement some of these reports but I have a question specific to this one to start:

You completely removed Event(0) from Trion's door, where he actually issues the mission. Was that a slip? The re-ordering seems to fit well.

- String **ID 6767** for the Chateau is "*I commend you for your work on this mission. Now hurry to the gatehouse and report!*" It fits, but differs from your report. 
- String **ID 6765** is "*I commend you for your work on this mission. However, you still have an important task left before you. Now hurry to the tomb and rid the area of any vermin that may be lurking in the darkness.*"
- String **ID 7309** for SSandy is "You handed the ≺item≻ over to the guard." which also is fitting (and better English) but differs.
- String **ID 7311** for Ranperres Tomb is "It appears to be the true resting place of King Ranperre." Also fits but differs.
- There's also a string of ID 7310 right next to this where it only says "It looks like a grave." Looks like it might be the default dialogue for the upper level Tombstone instead of "A waterskin is lying here."

The strings I refer to here were extracted recently with POLUtils (not including the client update from today 10/12/2020). Where do you get your strings from?

Also @developers how am I supposed to implement these if not with `showText()` (I'm referring to Discord talks)? I mean I understand it's just a missing cs ID but how am I supposed to find out when the JSON dumps don't include these? (After all that's what the ID.lua file is for...)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 12, 2020 at 19:56:13_

----

> how am I supposed to find out when the JSON dumps don't include these? 

retail captures.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 12, 2020 at 19:57:16_

----

That would take like 20 years for someone to find the real CS ID from retail for optional and default dialogues like these :s


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 12, 2020 at 20:00:01_

----

naw thats exaggerating a bit its _only_ an average 3 and a half _years_   
/s


###### this sucks someone needs to improve the event ID extractor :cry:


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Monday Oct 12, 2020 at 22:45:30_

----

Thank you for confirming this.

@MarianArlt 
> You completely removed Event(0) from Trion's door, where he actually issues the mission. Was that a slip? The re-ordering seems to fit well.

sorry, "player:startEvent(81)" is required when "missionStatus == 0".  I deleted it by mistake.
`
>The strings I refer to here were extracted recently with POLUtils (not including the client update from today 10/12/2020). Where do you get your strings from?

My method for getting the "Text ID" is to run the test code below and save the text of the output message.
```
for i = x, y do
player:messageSpecial(i);
end
```
Then, if there is a difference between the retail video and NPC message archives on the internet and the message output from Topaz, I try to find the number of the "Text ID" of the retail message in the text archive.

However, I'm using a Japanese client and it automatically translates the Japanese messages, so the messages may be a little different from the English client messages and POLUtils. I apologize for the inconvenience this may cause.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 12, 2020 at 23:04:22_

----

Ah that makes sense then for why they differ, thank you very much for clarification! And no need to apologize at all. I'm just asking so we can get closer to the same state of insight whoever reads/works on these.
