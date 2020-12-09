**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Sunday Oct 18, 2020 at 08:39:11_
_Originally opened as: project-topaz/topaz - Issue 1387_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Previous Quest "Chocobo's Wounds" is missing in the start condition of "Save My Son ".
https://www.bg-wiki.com/bg/Save_My_Son

https://github.com/project-topaz/topaz/blob/66e33e5c39337200edbb106702bddbf492cdb061/scripts/zones/Lower_Jeuno/npcs/_6t2.lua#L50-L52

I think I need to add to the start condition that the quest "Chocobo's Wounds" has been completed.
```
    -- Save My Son
    elseif (ChocobosWounds == QUEST_COMPLETED and player:getQuestStatus(JEUNO, tpz.quest.id.jeuno.SAVE_MY_SON) == QUEST_AVAILABLE and mLvl >= 30) then
        player:startEvent(164)
```



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 18, 2020 at 20:43:02_

----

https://github.com/project-topaz/topaz/commit/bebb549461667233f2587a96647a077c21837ca3#diff-57073c93aa35db0312b9fa027027e07ea229be6a1f9fade46dc85731bc8ec5b2


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 18, 2020 at 20:43:17_

----

Wiki's don't always get updated.


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Monday Oct 19, 2020 at 02:30:36_

----

Thank you for your comment.
OK. Close.
