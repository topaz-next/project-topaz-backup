**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:30_
_Originally opened as: project-topaz/topaz - Issue 142_

----

<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Nov 02, 2016 at 15:11 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3518_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30160831_1

**_Server Version_** (type `revision` in game) **:** ed0d506548576d522bbd7ca9e1ab0d3f49e487c9

**_Source Branch_** (master/stable) **:** master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**

It looks like elemental magic null and absorb mods checks occur twice, once at battleutils.cpp:4239-4244, and again at magic.lua:676-681.


