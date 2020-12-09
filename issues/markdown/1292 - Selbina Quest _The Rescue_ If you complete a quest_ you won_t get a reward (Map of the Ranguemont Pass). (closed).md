**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Oct 09, 2020 at 06:17:49_
_Originally opened as: project-topaz/topaz - Issue 1292_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

The parameter ("ki") in "npcUtil.completeQuest" seems to be wrong. (L40)

https://github.com/project-topaz/topaz/blob/5213062798b92405fb84ea90c3399bce75c4bf5e/scripts/zones/Selbina/npcs/Thunder_Hawk.lua#L37-L43

(L40) Use "keyItem" instead of "ki".
```
    elseif csid == 81 and npcUtil.completeQuest(player, OTHER_AREAS_LOG, tpz.quest.id.otherAreas.THE_RESCUE, {fame_area = SELBINA, keyItem = tpz.ki.MAP_OF_THE_RANGUEMONT_PASS, title = tpz.title.HONORARY_CITIZEN_OF_SELBINA, gil = 3000}) then

```
