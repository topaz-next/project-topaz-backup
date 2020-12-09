**Labels:**

hold



<a href="https://github.com/MarkWaldron"><img src="https://avatars2.githubusercontent.com/u/5213352?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarkWaldron](https://github.com/MarkWaldron)**
_Monday May 18, 2020 at 01:49:31_
_Originally opened as: project-topaz/topaz - Issue 638_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

I've removed the 1 day check and CharVar, and added a zone requirement. 

Closes issue: #245  


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday May 26, 2020 at 04:06:57_

----

Should this be checking `not player:needToZone()`? I'm not sure what these 3 CS's are, but it doesn't look like they're executing correctly and setting the `MissionStatus` var correctly. Everything up until this part looks right.



----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday May 26, 2020 at 04:07:36_

----

I don't think either of these lines are required anymore, once the `MissionStatus` var is correctly being set by the guard.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday May 26, 2020 at 11:50:49_

----

want to avoid needToZone anyway since its global. we can use set/getLocalVar to tell is player zoned since the preceding step..


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday May 26, 2020 at 04:06:57_

----

Should this be checking `not player:needToZone()`? I'm not sure what these 3 CS's are, but it doesn't look like they're executing correctly and setting the `MissionStatus` var correctly. Everything up until this part looks right.



----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday May 26, 2020 at 04:07:36_

----

I don't think either of these lines are required anymore, once the `MissionStatus` var is correctly being set by the guard.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday May 26, 2020 at 11:50:49_

----

want to avoid needToZone anyway since its global. we can use set/getLocalVar to tell is player zoned since the preceding step..


----
<a href="https://github.com/zircon-tpl"><img src="https://avatars0.githubusercontent.com/u/60901633?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zircon-tpl](https://github.com/zircon-tpl)**
_Thursday Jun 25, 2020 at 05:49:22_

----

Hello, MarkWaldron. Thank you for your interest in Project Topaz!

Another Contributor had submitted a Pull Request which addresses the quest in question. That Pull Request was merged, and I have been informed by Staff that it would make the changes in this Pull Request redundant. Therefore I must unfortunately close this Pull Request.

Should you feel that this determination is in error, please do not be afraid to say so!

I apologize on behalf of the project, and hope that this does not discourage you from further contributions.
