**Labels:**

merge ready



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Mar 24, 2020 at 20:16:49_
_Originally opened as: project-topaz/topaz - Issue 438_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits ~~(need a volunteer to test, as I lack time - but I have other mobs using this same code with diff pos's working fine!)~~ tested by Zach

thought: should onPath be a local function?



----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Mar 24, 2020 at 22:50:02_

----

ouch that's a huge array, i take npc path is still borken


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Mar 24, 2020 at 23:09:09_

----

> ouch that's a huge array, i take npc path is still borken

yeah I seriously dislike the way these are handled but doubly so when there are so freakin many points in the array. I probably should have rounded these to nearest rather than truncating as well, but I want to know if he even moves now before messing with that more.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Mar 25, 2020 at 11:38:49_

----

Confirmed, he wanders around as he should 👍 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 25, 2020 at 22:31:03_

----

Culled some intermediate points where only one axis was being changed
[culled.txt](https://github.com/project-topaz/topaz/files/4383940/culled.txt)

