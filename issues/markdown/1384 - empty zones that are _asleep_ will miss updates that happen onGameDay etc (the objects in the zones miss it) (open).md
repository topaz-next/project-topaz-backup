**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 17, 2020 at 20:51:44_
_Originally opened as: project-topaz/topaz - Issue 1384_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Example: enter Sacrarium and see the wrong days door/floor configuration because its running whatever the last update it saw was. we need  something to update these zones when they awaken from sleep.



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 17, 2020 at 20:55:41_

----

I was looking at these systems today, commenting so I'm reminded of this later (Zone OnCountIncrease CreateTimer, add lua binding there) 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Saturday Oct 17, 2020 at 21:27:29_

----

Just wanna clarify that the stuff in `onGameDay` still gets run when the zone is empty, the problem with Sacrarium is that it calls `setAnimation` which relies on the AI controller to update the entity, which is what gets killed when a zone empties.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 17, 2020 at 21:48:24_

----

> Just wanna clarify that the stuff in `onGameDay` still gets run when the zone is empty, the problem with Sacrarium is that it calls `setAnimation` which relies on the AI controller to update the entity, which is what gets killed when a zone empties.

Yeah I think before the great AI rewrite when a zone "woke up" the 1st tick was supposed to make all the AI do an immediate update with whatever happened during the zones sleep happening all immediately. No idea if that ever worked correctly, but that was what had been intended.
