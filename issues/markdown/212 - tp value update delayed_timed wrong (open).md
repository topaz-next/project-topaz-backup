**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:33_
_Originally opened as: project-topaz/topaz - Issue 212_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Feb 21, 2018 at 04:44 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4573_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
n/a

**_Server Version_** (type `!revision` in game) **:** 
github/DarkstarProject/darkstar/commit/876eb2674a7df073422b4095745ae5e2deae5d32

**_Source Branch_** (master/stable) **:** 
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
TP display appears to be updated at the begging of an action instead of the end? I am likely not describing this right.

Use pop perfect dodge on yourself and the enemy. now use a weaponskill and miss. Your TP will not set to zero. you actually do not have the TP, its just the display didn't update. the next time it updates it'll show you that zero. Its a step behind whats actually there. Probably something simple like one line of an update packet send out of place.

