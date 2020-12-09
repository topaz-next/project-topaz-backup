**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Monday Oct 12, 2020 at 01:36:41_
_Originally opened as: project-topaz/topaz - Issue 1333_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

If the quest "Making the Grade" is QUEST_ACCEPTED the message of the NPC should change.

https://github.com/project-topaz/topaz/blob/ce4efc04260c6e325e044cc7e30226e705621d74/scripts/zones/Windurst_Waters/npcs/Pechiru-Mashiru.lua#L15-L25
```
    elseif (player:getQuestStatus(WINDURST, tpz.quest.id.windurst.MAKING_THE_GRADE) == QUEST_ACCEPTED) then
        player:startEvent(445)
```

https://github.com/project-topaz/topaz/blob/ce4efc04260c6e325e044cc7e30226e705621d74/scripts/zones/Windurst_Waters/npcs/Tauwawa.lua#L12-L14
```
require("scripts/globals/quests")

function onTrigger(player, npc)
    if (player:getQuestStatus(WINDURST, tpz.quest.id.windurst.MAKING_THE_GRADE) == QUEST_ACCEPTED) then
        player:startEvent(446)
    else
      player:startEvent(424)
    end
end
```

