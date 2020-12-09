**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Saturday Oct 17, 2020 at 16:51:51_
_Originally opened as: project-topaz/topaz - Issue 1383_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

It occurs by the following procedure.
1. You have not received the Jeuno quest "Rubbish Day".
2. You have received the Windurst quest "Making Amens!".
3. Talk to "Mashira" in "Garlaige Citadel".
4. The dialog displays the option "I want to throw away Magic trash", 
which is strange. For reason 1, I don't have the Key item "Magic trash".

It seems that "2" is correct, not "0", as the parameter that changes the options. (L22)
https://github.com/project-topaz/topaz/blob/e6001c7f89923cb9773e98c25daa72b230171371/scripts/zones/Garlaige_Citadel/npcs/Mashira.lua#L16-L27

I think that the following four patterns should be branched according to the state of the two quests.
```
function onTrigger(player, npc)
    local rubbishDay = player:getQuestStatus(JEUNO, tpz.quest.id.jeuno.RUBBISH_DAY)
    local makingAmens = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.MAKING_AMENS)

    if ((rubbishDay == QUEST_ACCEPTED and player:getCharVar("RubbishDayVar") == 0) and 
        (makingAmens ~= QUEST_ACCEPTED or player:hasKeyItem(tpz.ki.BROKEN_WAND) == true)) then
        player:startEvent(11, 1) -- only For the quest "Rubbish day"
    elseif ((rubbishDay ~= QUEST_ACCEPTED or player:getCharVar("RubbishDayVar") ~= 0) and
        (makingAmens == QUEST_ACCEPTED and player:hasKeyItem(tpz.ki.BROKEN_WAND) == false)) then
        player:startEvent(11, 2, 937) -- only For the quest "Making Amens"
    elseif (rubbishDay == QUEST_ACCEPTED and player:getCharVar("RubbishDayVar") == 0 and
        makingAmens == QUEST_ACCEPTED and player:hasKeyItem(tpz.ki.BROKEN_WAND) == false) then
        player:startEvent(11) -- For the quest "Rubbish day" / "Making Amens"
    else
        player:startEvent(11, 3) -- Standard dialog and menu
    end
end

```



----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Saturday Oct 17, 2020 at 18:25:11_

----

I'll fix it a little.

```
function onTrigger(player, npc)
    local rubbishDay = player:getQuestStatus(JEUNO, tpz.quest.id.jeuno.RUBBISH_DAY)
    local makingAmens = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.MAKING_AMENS)

    if (rubbishDay == QUEST_ACCEPTED and player:getCharVar("RubbishDayVar") == 0 and
        makingAmens == QUEST_ACCEPTED and player:hasKeyItem(tpz.ki.BROKEN_WAND) == false) then
        player:startEvent(11) -- For the quest "Rubbish day" / "Making Amens"
    elseif (rubbishDay == QUEST_ACCEPTED and player:getCharVar("RubbishDayVar") == 0) then
        player:startEvent(11, 1) -- only For the quest "Rubbish day"
    elseif (makingAmens == QUEST_ACCEPTED and player:hasKeyItem(tpz.ki.BROKEN_WAND) == false) then
        player:startEvent(11, 2, 937) -- only For the quest "Making Amens"
    else
        player:startEvent(11, 3) -- Standard dialog and menu
    end
end
```
