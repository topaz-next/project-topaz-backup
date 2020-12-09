**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Sep 30, 2020 at 01:28:22_
_Originally opened as: project-topaz/topaz - Issue 1219_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

https://github.com/project-topaz/topaz/blob/3bc611df9cace45b9ebd3afe5635aa453fa886b1/scripts/zones/Northern_San_dOria/npcs/Kuu_Mohzolhi.lua#L47-L67

(L49) player:startEvent(605, player:getGender(), 231, 4);
(L51) player:startEvent(605, player:getGender(), 231, 2);
(L55) player:startEvent(605, player:getGender(), 231, 3);
(L57) player:startEvent(605, player:getGender(), 231, 1);
(L60) player:startEvent(605, player:getGender(), 231, 0);
(L66) player:startEvent(605, player:getGender(), 231, 10);

This issue applies to Mog House exit expansion quests in general (Growing Flowers/A Lady's Heart/Flower Child/Pretty Little Things/Keeping Notes).




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 01, 2020 at 21:26:55_

----

For editor who takes this on: Variablize getGender() so we call it once, use variable in place of the zero.


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Oct 02, 2020 at 11:39:50_

----

Thanks for the advice.
