**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Sep 30, 2020 at 11:59:39_
_Originally opened as: project-topaz/topaz - Issue 1220_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

https://github.com/project-topaz/topaz/blob/3bc611df9cace45b9ebd3afe5635aa453fa886b1/scripts/zones/Northern_San_dOria/npcs/Nonterene.lua#L12-L14

If the quest "Exit the Gambler" is QUEST_ACCEPTED, the message of the NPC "Nonterene" should change.

if (player:getQuestStatus(SANDORIA, tpz.quest.id.sandoria.EXIT_THE_GAMBLER) == QUEST_ACCEPTED) then
  player:startEvent(523)
else
  player:startEvent(503)
end

