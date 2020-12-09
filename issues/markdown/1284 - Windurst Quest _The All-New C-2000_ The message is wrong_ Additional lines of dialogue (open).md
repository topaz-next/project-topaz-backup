**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Thursday Oct 08, 2020 at 11:33:56_
_Originally opened as: project-topaz/topaz - Issue 1284_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

If the quest "The All-New C-2000" is QUEST_ACCEPTED the message of the NPC should change.

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Woods/npcs/Boizo-Naizo.lua#L20-L22

```
function onTrigger(player, npc)
    local allNewC2000 = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.THE_ALL_NEW_C_2000)
    if allNewC2000 == QUEST_ACCEPTED then
        player:startEvent(290)
    else
        player:startEvent(275)
    end
end
```

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Woods/npcs/Kororo.lua#L17-L45

```
    if C2000 == QUEST_ACCEPTED then
       player:startEvent(291)

    -- A Greeting Cardian
    elseif C2000 == QUEST_COMPLETED and AGreetingCardian == QUEST_AVAILABLE and player:getFameLevel(WINDURST) >= 3 then
        player:startEvent(296) -- A Greeting Cardian quest start

```

When you complete a quest, the message "You have obtained 200 gil" is displayed twice, but the actual amount of gil increase is 200 gil. (L23, L101)
Also, the rate is not calculated for some of the acquired gil. (L101)

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Woods/npcs/Kopuro-Popuro.lua#L15-L26

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Woods/npcs/Kopuro-Popuro.lua#L97-L104

```
function onEventFinish(player, csid, option)
    -- THE ALL NEW C-2000
    if csid == 285 and option ~= 2 then  -- option 2 is declining the quest for the second question
        player:addQuest(WINDURST, tpz.quest.id.windurst.THE_ALL_NEW_C_2000)
    elseif csid == 292 then
        player:completeQuest(WINDURST, tpz.quest.id.windurst.THE_ALL_NEW_C_2000)
        player:addFame(WINDURST, 80)
        player:addTitle(tpz.title.CARDIAN_TUTOR)
        player:addGil(GIL_RATE*200)
        player:tradeComplete()
```
