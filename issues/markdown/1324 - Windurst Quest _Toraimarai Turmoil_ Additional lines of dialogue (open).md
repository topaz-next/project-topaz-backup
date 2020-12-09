**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Sunday Oct 11, 2020 at 11:04:25_
_Originally opened as: project-topaz/topaz - Issue 1324_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

If the quest "Toraimarai Turmoil" is QUEST_ACCEPTED the message of the NPC should change.

- Leepe-Hoppe
https://github.com/project-topaz/topaz/blob/daf504aa7a7dae2f39045140739047459ac3865c/scripts/zones/Windurst_Waters/npcs/Leepe-Hoppe.lua#L122-L124
The behavior at the moment, you will see the event ID "345".  (L123)
```
    local turmoil = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.TORAIMARAI_TURMOIL)

    elseif (turmoil == QUEST_ACCEPTED) then
        player:startEvent(790, 0, tpz.ki.RHINOSTERY_CERTIFICATE)
    else
        player:startEvent(345) -- Standard Dialogue?
    end
```
Add a serif pattern to the lowest priority position of the condition.

- Yoran-Oran
https://github.com/project-topaz/topaz/blob/daf504aa7a7dae2f39045140739047459ac3865c/scripts/zones/Windurst_Walls/npcs/Yoran-Oran.lua#L69-L71
The behavior at the moment, you will see the event ID "245".  (70)
```
    local turmoil = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.TORAIMARAI_TURMOIL)

    elseif (turmoil == QUEST_ACCEPTED) then
        player:startEvent(392)
    else
        player:startEvent(245)
    end
```
Add a serif pattern to the lowest priority position of the condition.

- Polikal-Ramikal
https://github.com/project-topaz/topaz/blob/daf504aa7a7dae2f39045140739047459ac3865c/scripts/zones/Windurst_Walls/npcs/Polikal-Ramikal.lua#L12-L14
```
function onTrigger(player, npc)
    local turmoil = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.TORAIMARAI_TURMOIL)
    if (turmoil == QUEST_ACCEPTED) then
        player:startEvent(391)
    else
        player:startEvent(320)
    end
end
```

