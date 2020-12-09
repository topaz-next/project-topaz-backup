**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:14_
_Originally opened as: project-topaz/topaz - Issue 172_

----

<a href="https://github.com/xipies"><img src="https://avatars3.githubusercontent.com/u/7948457?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [xipies](https://github.com/xipies)**
_Tuesday Apr 04, 2017 at 19:45 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3839_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30170304_1


**_Server Version_** (type `revision` in game) **:**
0ea9e4a


**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
Fight an elemental for an extended period (e.g., skill up archery), wait for weather to change. Specifically I noticed this when weather would change to double weather. Elemental respawns at its original spawn point, still claimed, and with full health again.





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:15_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Apr 04, 2017 at 22:37 GMT_

----

This happens when it changes between single and double weather of the same element, correct?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:16_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 05, 2017 at 17:46 GMT_

----

2 situations where nothing should happen to an elemental: 

- A) the weather changed, but the elemental was engaged to a player

- B) weather changed to diff tier of same element (double/single)

Sounds like code that pops elementals isn't checking that they are already up.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:18_

----

<a href="https://github.com/xipies"><img src="https://avatars3.githubusercontent.com/u/7948457?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [xipies](https://github.com/xipies)**
_Thursday Apr 06, 2017 at 05:00 GMT_

----

This also happened from no weather to weather. I had elemental claimed from when weather was up before. I only noticed this happen when the same weather type was in play. I did not happen to notice/test if weather type changed (e.g., water to lightning).



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:20_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday Apr 06, 2017 at 05:51 GMT_

----

Makes sense. Probably what TeoTwawki said - it's not checking if the elemental is already spawned when it does the weather change stuff.

