**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Oct 07, 2020 at 13:32:34_
_Originally opened as: project-topaz/topaz - Issue 1269_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

If the quest "Stardust" is QUEST_ACCEPTED the message of the NPC should change.

https://github.com/project-topaz/topaz/blob/abfe5dda545545f060a761e894c79d55239ada02/scripts/zones/Bastok_Mines/npcs/Drangord.lua#L10-L12

```
    if (player:getQuestStatus(BASTOK, tpz.quest.id.bastok.STARDUST) == QUEST_ACCEPTED) then
        player:startEvent(97)
    else
        player:startEvent(21)
    end
```


