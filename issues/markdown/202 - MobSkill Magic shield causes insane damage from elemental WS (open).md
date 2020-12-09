**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:50:39_
_Originally opened as: project-topaz/topaz - Issue 202_

----

<a href="https://github.com/dwn134"><img src="https://avatars3.githubusercontent.com/u/17234748?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [dwn134](https://github.com/dwn134)**
_Monday Dec 25, 2017 at 01:26 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4422_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30171004_1


**_Server Version_** (type `!revision` in game) **:** Unknown


**_Source Branch_** (master/stable) **:** master


**_Additional Information_** (Steps to reproduce/Expected behavior) **:** a mob that has magic shield ability up will heal from elemental magic instead of doing 0 damage but if you use a ele WS it will show as healed damage but infact take the HP away and for crazy 10k + damage





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:50:40_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Dec 25, 2017 at 01:40 GMT_

----

its the absorb dmg as hp. 
MOD_MAGIC_ABSORB and MOD_FIRE_ABSORB etc, all broken. instead of healing mob you get huge dmg.
 we've been using negative value as heals, somewhere along the line a casting change messed this up.

