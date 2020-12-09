**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Tuesday Oct 06, 2020 at 03:14:55_
_Originally opened as: project-topaz/topaz - Issue 1262_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

If the quest "The Eleventh's Hour" is QUEST_ACCEPTED  the message of the NPC should change.

https://github.com/project-topaz/topaz/blob/70345cb560302e11c08b9afde27f6522b2f1cd74/scripts/zones/Bastok_Mines/npcs/Parraggoh.lua#L15-L33

local TheEleventhsHour = player:getQuestStatus(BASTOK, tpz.quest.id.bastok.THE_ELEVENTH_S_HOUR)

    elseif BeautyAndTheGalka == QUEST_COMPLETED then
        if TheEleventhsHour == QUEST_ACCEPTED then
          player:startEvent(46)
        else
          player:startEvent(12)
        end

https://github.com/project-topaz/topaz/blob/70345cb560302e11c08b9afde27f6522b2f1cd74/scripts/zones/Bastok_Mines/npcs/Pavvke.lua#L27-L39

    local TheEleventhsHour = player:getQuestStatus(BASTOK, tpz.quest.id.bastok.THE_ELEVENTH_S_HOUR)

    if (Fallen == 0    and pLevel >= 12 and pFame >= 2) then
        player:startEvent(90)
    else
        if TheEleventhsHour == QUEST_ACCEPTED then
          player:startEvent(48)
        else
          player:startEvent(75)
        end





