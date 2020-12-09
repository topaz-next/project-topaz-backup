**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Sunday Oct 11, 2020 at 12:50:10_
_Originally opened as: project-topaz/topaz - Issue 1325_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

The "Ship bound for Selbina" fare should be free while your quest is being ordered.

https://github.com/project-topaz/topaz/blob/b5203ef0e1025e400888bb8c57ae80be43ce5d9e/scripts/zones/Mhaura/npcs/Felisa.lua#L10-L18
The following modifications will free up the fare.
```
require("scripts/globals/keyitems")
require("scripts/globals/quests")

function onTrigger(player, npc)
    if (player:getZPos() > 38.5) then
      if (player:getQuestStatus(OTHER_AREAS_LOG, tpz.quest.id.otherAreas.HIS_NAME_IS_VALGEIR) == QUEST_ACCEPTED and player:hasKeyItem(tpz.ki.ARAGONEU_PIZZA)) then
          player:startEvent(230)
      else
          player:startEvent(221, player:getGil(), 100)
      end
    else
        player:startEvent(235)
    end
end
```

