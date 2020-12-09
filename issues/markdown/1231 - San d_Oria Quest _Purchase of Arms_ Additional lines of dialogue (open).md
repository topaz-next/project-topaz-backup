**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Oct 02, 2020 at 12:23:01_
_Originally opened as: project-topaz/topaz - Issue 1231_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- []x checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

If the quest "Purchase of Arms" is QUEST_ACCEPTED, the message of the NPC should change.

https://github.com/project-topaz/topaz/blob/50e64bd5fa324a22e260b5c79a3213fb3510d186/scripts/zones/Southern_San_dOria/npcs/Helbort.lua#L17-L29

    if (player:getFameLevel(SANDORIA) >= 2 and quest_fas == QUEST_COMPLETED and quest_poa == QUEST_AVAILABLE) then
        player:startEvent(594)  -- Start quest A Purchase of Arms
    elseif (quest_poa == QUEST_ACCEPTED) then
        if (player:hasKeyItem(tpz.ki.WEAPONS_RECEIPT) == false) then
          player:showText(npc, ID.text.XXXX)
        else
          player:startEvent(607) -- Finish A Purchase of Arms quest
       end
    else
        player:startEvent(593)  -- Standard Dialog
    end

"ID.text.XXXX" has the value "7975".

https://github.com/project-topaz/topaz/blob/50e64bd5fa324a22e260b5c79a3213fb3510d186/scripts/zones/Jugner_Forest/npcs/Alexius.lua#L14-L20

    if player:hasKeyItem(tpz.ki.WEAPONS_ORDER) then
        player:startEvent(5)
    elseif player:hasKeyItem(tpz.ki.WEAPONS_RECEIPT) then
        player:showText(npc, ID.text.XXXX, tpz.ki.WEAPONS_RECEIPT)
    elseif player:getCharVar("sinHunting") == 3 then
        player:startEvent(10)
    end

"ID.text.XXXX" has the value "7886".



