**Labels:**

merge ready



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Thursday Apr 30, 2020 at 03:39:47_
_Originally opened as: project-topaz/topaz - Issue 550_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Adds timer to spawn for Knight Crabs in Jugner after server reset.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 30, 2020 at 03:48:12_

----

If you want to do the spawn windows, they can be done with 
```
local respawnTime(900 * math.random(1, 12)
```
for 12 windows of 15 min each, though that coukd possibly be written better than how I just did to make it obvious whats going on.

Someday maybe we’ll just fee in window size and total max time to a helper function that spit out the right answer.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Apr 30, 2020 at 03:59:44_

----

i just followed Roc and Simurgh's lead... are they supposed to have precise windows too?


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Apr 30, 2020 at 04:02:22_

----

fixed!  thanks teo


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Apr 30, 2020 at 06:13:23_

----

Wiki says 30 min windows `If Time of death is 6:00pm, the window will begin at 3:05pm the next day and windows will be at the 05 and 35 minute mark.` King Arthro himself should probably also be changed to reflect this. [See Fafnir.](https://github.com/project-topaz/topaz/blob/b72f5d756047375e9123a7cee0a2cb1783c07180/scripts/zones/Dragons_Aery/mobs/Fafnir.lua#L40)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 30, 2020 at 11:45:07_

----

can we use a consistent order of operations in the 2 scripts (and some clarifying paran's) ?  I know they execute the same, but people new to the language might not understand so extra clarity and consistency is good.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 30, 2020 at 03:48:12_

----

If you want to do the spawn windows, they can be done with 
```
local respawnTime(900 * math.random(1, 12)
```
for 12 windows of 15 min each, though that coukd possibly be written better than how I just did to make it obvious whats going on.

Someday maybe we’ll just fee in window size and total max time to a helper function that spit out the right answer.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Apr 30, 2020 at 03:59:44_

----

i just followed Roc and Simurgh's lead... are they supposed to have precise windows too?


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Apr 30, 2020 at 04:02:22_

----

fixed!  thanks teo


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Apr 30, 2020 at 06:13:23_

----

Wiki says 30 min windows `If Time of death is 6:00pm, the window will begin at 3:05pm the next day and windows will be at the 05 and 35 minute mark.` King Arthro himself should probably also be changed to reflect this. [See Fafnir.](https://github.com/project-topaz/topaz/blob/b72f5d756047375e9123a7cee0a2cb1783c07180/scripts/zones/Dragons_Aery/mobs/Fafnir.lua#L40)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 30, 2020 at 11:45:07_

----

can we use a consistent order of operations in the 2 scripts (and some clarifying paran's) ?  I know they execute the same, but people new to the language might not understand so extra clarity and consistency is good.
