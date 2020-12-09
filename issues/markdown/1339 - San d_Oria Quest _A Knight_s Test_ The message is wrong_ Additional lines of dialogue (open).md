**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Monday Oct 12, 2020 at 09:42:08_
_Originally opened as: project-topaz/topaz - Issue 1339_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

The message is wrong, Additional lines of dialogue.

https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Southern_San_dOria/npcs/Cahaurme.lua#L14-L23
```
function onTrigger(player, npc)
    if (player:hasKeyItem(tpz.ki.BOOK_OF_TASKS) and player:hasKeyItem(tpz.ki.BOOK_OF_THE_EAST) == false) then
        player:startEvent(633)
    elseif (player:getQuestStatus(SANDORIA, tpz.quest.id.sandoria.A_KNIGHT_S_TEST) == QUEST_ACCEPTED) then
        -- Cahaurme : It may be a tough ordeal, butOnly those who overcome this will leave the nest as knights in good standing. Hang in there. (Text ID: 8002)
    else
        -- Cahaurme : Well done. I hope you will become a great knight.  (Text ID: 8003)
    end
end
```

https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Southern_San_dOria/npcs/Baunise.lua#L15-L22
```
function onTrigger(player, npc)
    if (player:hasKeyItem(tpz.ki.BOOK_OF_TASKS) and player:hasKeyItem(tpz.ki.BOOK_OF_THE_WEST) == false) then
        player:startEvent(634)
    elseif (player:getQuestStatus(SANDORIA, tpz.quest.id.sandoria.A_KNIGHT_S_TEST) == QUEST_ACCEPTED) then
        -- Baunise : Even if you don't understand it at first, don't be in a hurry to think it over. There's plenty of time.  (Text ID: 8005)
    else
        -- Baunise : You did a great job. I knew you could do it. Keep up the good work.  (Text ID: 8006)
    end
end
```
