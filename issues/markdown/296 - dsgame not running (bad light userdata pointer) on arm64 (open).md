**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:39_
_Originally opened as: project-topaz/topaz - Issue 296_

----

<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Saturday May 25, 2019 at 00:48 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6027_

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

Compiles without issues on a raspberry pi 3B+ running a 64bit kernel.

When running dsgame, it returns the following before it closes:
[Status] do_init: begin server initialization...		 - [OK]
[24/May] [17:41:00][Status] do_init: map_config is reading		 - [OK]
[24/May] [17:41:00][Status] luautils::init:lua initializing...PANIC: unprotected error in call to Lua API (bad light userdata pointer)

no issues with dsconnect or dssearch.





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:40_

----

<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Sunday May 26, 2019 at 20:33 GMT_

----

Take a read through this comment posting about addressing limitations - [github/LuaJIT/LuaJIT - PR 230Darkstar Issue issuecomment-260205661](github/LuaJIT/LuaJIT - PR 230Darkstar Issue issuecomment-260205661)

Further reading - [https://gitlab.labs.nic.cz/knot/knot-resolver - Issue 216](https://gitlab.labs.nic.cz/knot/knot-resolver - Issue 216)

It is only going to be an issue on a few select platforms, ARM64 being one of them.  I do not know what direction the project should take with regards to Lua and the affected platforms.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:42_

----

<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Jun 03, 2019 at 10:38 GMT_

----

Technical reading for anyone who wants to take a look at this:
github/ahupowerdns/luawrapper - PR 46/files
github/ahupowerdns/luawrapper - PR 45/files
github/ahupowerdns/luawrapper - PR 44/files
http://lua-users.org/lists/lua-l/2011-06/msg00372.html



----
<a href="https://github.com/bluekirby0"><img src="https://avatars3.githubusercontent.com/u/1157452?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [bluekirby0](https://github.com/bluekirby0)**
_Wednesday Jul 15, 2020 at 02:57:11_

----

Duplicated this bug today on raspberry pi 4 (aarch64) running Ubuntu 20.04 LTS 64-bit. Leaving a note here before creating a new issue related to a potential fix.

For reference, the two routes we can take to fix this are to either convert lightuserdata carrying pointers into userdata, or to shift from C API bindings to FFI bindings. Will go into more detail about the second option in a new issue.

```
ubuntu@ubuntu:~/topaz$ ./topaz_game 
[Info] Topaz[Status] do_init: begin server initialization...		 - [OK]
[15/Jul] [02:52:21][Status] do_init: map_config is reading		 - [OK]
[15/Jul] [02:52:21][Status] luautils::init:lua initializing...PANIC: unprotected error in call to Lua API (bad light userdata pointer)

```
