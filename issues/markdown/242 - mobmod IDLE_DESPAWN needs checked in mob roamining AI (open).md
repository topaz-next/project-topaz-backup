**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:36_
_Originally opened as: project-topaz/topaz - Issue 242_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Nov 07, 2018 at 14:18 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5377_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
n/a

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
The mobmod for despawning idle mobs is currently only checked after a mob disengages. We need to check it when the monster is idle/roaming so that instances of mobs spawning unclaimed and then never being claimed will also "time out" (or have 2 mods, and rename things a bit..).

**The parameter on spawnMob() is not usable for this since that would cause mobs to INSTANTLY despawn in many situations the very second claim is lost due to the fact that timer begins _onSpawn_ and is never reset. mobmod IDLE_DESPAWN was created expressly because as I was told "we don't want to change how that parameter works". So using that is not an option.**


