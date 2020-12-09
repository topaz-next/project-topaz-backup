**Labels:**

improvement



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Thursday Apr 30, 2020 at 05:36:32_
_Originally opened as: project-topaz/topaz - Issue 552_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

**scripts\global\settings.lua:**
TIMEZONE_OFFSET = 9.0 -- Offset from UTC used to determine when JP Midnight is for the server.  Default is JST (+9.0).

**conf\map.conf:**
#Determine when JP midnight is.
vanadiel_time_offset: 8


Redundant settings, only one can/should be used.

Also if possible, maybe an option should be to pick it directly from the OS time.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Apr 30, 2020 at 05:42:18_

----

I think `vanadiel_time_offset` is used to control the in-game time/year, while `TIMEZONE_OFFSET` is used for gating requirements.

Edit: `vanadiel_time_offset` doesn't actually look like it does anything right now, but that seems to have been the intention at one time.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Apr 30, 2020 at 06:38:19_

----

The comments both state they are for determining when "JP midnight" is.  If vanadiel_time_offset isn't used for anything, perhaps it should be removed.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Apr 30, 2020 at 06:44:43_

----

I actually think the ~~setting should maybe be renamed~~ comment should be clarified and the feature implemented. It sounds like it would let you reboot your server and have it be days or years ahead in Vana'diel, and that could be useful.
