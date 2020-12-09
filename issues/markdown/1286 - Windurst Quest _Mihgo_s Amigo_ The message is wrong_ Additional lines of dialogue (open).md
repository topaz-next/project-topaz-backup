**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Thursday Oct 08, 2020 at 15:12:05_
_Originally opened as: project-topaz/topaz - Issue 1286_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

When you complete a quest, the message "You have obtained 200 gil" is displayed twice, but the actual amount of gil increase is 200 gil. (L24, L196)
Also, the rate is not calculated for some of the acquired gil. (L196)

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Woods/npcs/Nanaa_Mihgo.lua#L19-L29

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Woods/npcs/Nanaa_Mihgo.lua#L195-L202

```
        -- MIHGO'S AMIGO
    elseif csid == 80 or csid == 81 then
        player:addQuest(WINDURST, tpz.quest.id.windurst.MIHGO_S_AMIGO)
    elseif csid == 88 then
        player:completeQuest(WINDURST, tpz.quest.id.windurst.MIHGO_S_AMIGO)
        player:addTitle(tpz.title.CAT_BURGLAR_GROUPIE)
        player:addGil(GIL_RATE*200)
        player:addFame(NORG, 80)
        player:tradeComplete()
        player:needToZone(true)
```

If the quest "Mihgo's Amigo" is QUEST_ACCEPTED the message of the NPC should change.

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Woods/npcs/Mheca_Khetashipah.lua#L11-L13

```
require("scripts/globals/quests")

function onTrigger(player, npc)
    starstatus = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.MIHGO_S_AMIGO)
    if (starstatus == QUEST_ACCEPTED) then
        player:startEvent(83)
    else
        player:startEvent(426)
    end
end
```

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Woods/npcs/Bopa_Greso.lua#L13-L19

```
function onTrigger(player, npc)
    if player:getQuestStatus(WINDURST, tpz.quest.id.windurst.AS_THICK_AS_THIEVES) == QUEST_ACCEPTED then
        player:startEvent(506) -- Gambling hint
    elseif player:getQuestStatus(WINDURST, tpz.quest.id.windurst.MIHGO_S_AMIGO) == QUEST_ACCEPTED then
        player:startEvent(84)
    else
        player:startEvent(77) -- Standard dialogue
    end
end
```

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Woods/npcs/Wani_Casdohry.lua#L11-L21

```
function onTrigger(player, npc)
    local TwinstoneBonding = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.TWINSTONE_BONDING)
    local MihgosAmigo = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.MIHGO_S_AMIGO)

    if TwinstoneBonding == QUEST_ACCEPTED then
        player:startEvent(489, 0, 13360)
    elseif MihgosAmigo == QUEST_ACCEPTED then
        player:startEvent(86, 0, 498)
    elseif TwinstoneBonding == QUEST_COMPLETED then
        player:startEvent(492, 0, 13360)
    else
        player:startEvent(425)
    end
end
```

