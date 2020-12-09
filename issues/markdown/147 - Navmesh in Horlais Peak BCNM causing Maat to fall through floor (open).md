**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:11_
_Originally opened as: project-topaz/topaz - Issue 147_

----

<a href="https://github.com/ghost"><img src="https://avatars3.githubusercontent.com/u/10137?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [ghost](https://github.com/ghost)**
_Wednesday Dec 21, 2016 at 10:18 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3593_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30161103_1

**_Server Version_** (type `revision` in game) **:**
eaeff3a81e309499a24e4b728b65cc58afbdd594

**_Source Branch_** (master/stable) **:**
Master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
Maat falls through the floor when running over the hump leading up to the Battlefield.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:12_

----

<a href="https://github.com/gedads"><img src="https://avatars1.githubusercontent.com/u/5845173?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [gedads](https://github.com/gedads)**
_Wednesday Dec 21, 2016 at 18:56 GMT_

----

is it navmesh or wallhack? maat is following you or rejoin you when you're far away? 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:13_

----

<a href="https://github.com/R3P0FFXI"><img src="https://avatars2.githubusercontent.com/u/10148511?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [R3P0FFXI](https://github.com/R3P0FFXI)**
_Wednesday Dec 21, 2016 at 22:58 GMT_

----

gedads it is a Navmesh issue



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:14_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Wednesday Dec 21, 2016 at 23:24 GMT_

----

For whatever reason, all mobs go through the ramp to the middle of the area, presumably on the "ground" below it.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:15_

----

<a href="https://github.com/gedads"><img src="https://avatars1.githubusercontent.com/u/5845173?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [gedads](https://github.com/gedads)**
_Wednesday Jan 04, 2017 at 05:05 GMT_

----

i tried to remove the ground below the stairs, same result, mobs seems to fall once they reach the small edge they need to climb to get to the stairs. navmesh even totally redone with 100% clean path produce the same result



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:16_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jan 04, 2017 at 07:46 GMT_

----

Try building Maat a small "ramp" in the mesh by lifting part of whats already there, so he doesn't try to path through? If he's wallhacking through it and then falling, maybe that'd work.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Mar 19, 2020 at 13:41:29_

----

Just a small update: I did Maat on retail just before the free week ended recently (just before maint in march 10th 2020) and Maat feel through the exact same spot in retail. I had to run back toward the bcnm entrance to him above ground again.

Area was horloise peak.
