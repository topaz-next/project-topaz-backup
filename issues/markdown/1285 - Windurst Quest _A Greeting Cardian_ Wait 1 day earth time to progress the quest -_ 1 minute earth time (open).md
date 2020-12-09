**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Thursday Oct 08, 2020 at 12:42:04_
_Originally opened as: project-topaz/topaz - Issue 1285_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

You are required to wait one day Earth time to progress your quest.
I think this is an old specification. (L29)
I think the new specs require a 1 minute earth time wait.

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Woods/npcs/Kororo.lua#L17-L33

```
    elseif AGreetingCardian == QUEST_ACCEPTED and AGCcs == 3 then
        if player:needToZone() or os.time() < AGCtime then
            player:startEvent(277) -- standard dialog if JP midnight has not passed
        else
            player:startEvent(298) -- A Greeting Cardian part two
        end
```

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Woods/npcs/Kororo.lua#L50-L57

```
function onEventFinish(player, csid, option)
    -- A Greeting Cardian
    if csid == 296 then
        player:addQuest(WINDURST, tpz.quest.id.windurst.A_GREETING_CARDIAN)
        player:setCharVar("AGreetingCardian_Event", 2)
        player:setCharVar("AGreetingCardian_timer", os.time() + 60) -- 1 minute earth time
        player:needToZone(true) -- wait one day and zone after next step
    elseif csid == 298 then
```

If the quest "A Greeting Cardian" is QUEST_ACCEPTED or QUEST_COMPLETED the message of the NPC should change.

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Waters/npcs/Five_of_Hearts.lua#L12-L14

```
require("scripts/globals/quests")

function onTrigger(player, npc)
    if (player:getQuestStatus(WINDURST, tpz.quest.id.windurst.A_GREETING_CARDIAN) == QUEST_ACCEPTED) then
        player:startEvent(686)
    else
        player:startEvent(273)
    end
end
```

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Walls/npcs/Five_of_Diamonds.lua#L13-L15

```
require("scripts/globals/quests")

function onTrigger(player, npc)
    if (player:getQuestStatus(WINDURST, tpz.quest.id.windurst.A_GREETING_CARDIAN) == QUEST_ACCEPTED) then
        player:startEvent(339)
    else
        player:startEvent(266)
    end
end
```

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Port_Windurst/npcs/Five_of_Clubs.lua#L12-L14

```
require("scripts/globals/quests")

function onTrigger(player, npc)
    if (player:getQuestStatus(WINDURST, tpz.quest.id.windurst.A_GREETING_CARDIAN) == QUEST_ACCEPTED) then
        player:startEvent(448)
    else
      player:startEvent(221)
    end
end
```

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Woods/npcs/Boizo-Naizo.lua#L20-L22

```
function onTrigger(player, npc)
    local allNewC2000 = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.THE_ALL_NEW_C_2000)
    local greetingCardian = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.A_GREETING_CARDIAN)
    if allNewC2000 == QUEST_ACCEPTED then
        player:startEvent(290)
    elseif greetingCardian == QUEST_COMPLETED then
        player:startEvent(307)
    else
        player:startEvent(275)
    end
end
```

