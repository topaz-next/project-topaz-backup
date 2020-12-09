**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Thursday Oct 08, 2020 at 08:24:43_
_Originally opened as: project-topaz/topaz - Issue 1281_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

If the quest "The Postman Always K.O.'s Twice" is QUEST_ACCEPTED the message of the NPC should change.

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Port_Windurst/npcs/Tohopka.lua#L13-L15

```
require("scripts/globals/settings")
require("scripts/globals/quests")
```
```
function onTrigger(player, npc)
    starstatus = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.TO_CATCH_A_FALLIHG_STAR)
    if (starstatus == QUEST_ACCEPTED) then
        player:startEvent(198, 0, 546, 868)
    else
        player:startEvent(358)
    end
end
```

