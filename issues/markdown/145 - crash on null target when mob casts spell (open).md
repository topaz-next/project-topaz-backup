**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:04_
_Originally opened as: project-topaz/topaz - Issue 145_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Nov 16, 2016 at 21:02 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3545_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30161004_1

**_Server Version_** (type `revision` in game) **:**
002ccd97d118f6faa79d28b56c42cb11bc929a38

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
Server this happened on is about one month out of date and I can't give you a good recent crash dump. I didn't see a commit since then that addresses this, but I could swear we saw this problem a long time ago and had already fixed..

_Anyway_, someone was making a mob repeatedly cast a spell via `exec` when the server crashed with PCastTarget being nullptr at line 483 of mob_controller.cpp

I haven't at all looked at this and don't intend to make a pr for it right now, just passing on info.

