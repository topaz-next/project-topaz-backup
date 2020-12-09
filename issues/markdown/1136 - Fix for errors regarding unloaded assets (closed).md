**Labels:**

hold



<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Monday Sep 14, 2020 at 01:44:59_
_Originally opened as: project-topaz/topaz - Issue 1136_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

I tried to make my changes as small as possible, using existing if statements whenever possible.


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Monday Sep 14, 2020 at 01:46:24_

----

#1090 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 14, 2020 at 04:58:36_

----

Hi @Dirk-Dieters! 

I'm not sure what you're trying to achieve here? I saw you make a similar PR a little while ago but didn't get around to looking at it. You have this issue open:

https://github.com/project-topaz/topaz/issues/1090

@TeoTwawki is looking in the right direction:

> it occurs to me that servers that don't allow these zones/expansions/npc's should just be setting that zone sport to zero.

Rather than modifying scripts to not explode when a strange expansion combination is in use, we should not be loading or ticking those zones. I would be inclined to put these checks inside core. 

Perhaps on boot, set flags for each zone that's active/inactive, and at runtime check for if that zone is active and should be ticked here:
https://github.com/project-topaz/topaz/blob/release/src/map/zone.cpp#L783

... or Teo might be right in doing something databasey


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 14, 2020 at 05:23:38_

----

I spoke to Teo about this a little bit: a combination of disabling expansions through settings flags, setting the restrict content flag and setting the ~~zoneip~~ zoneport to 0 for zones you don't want accessible or being ticked will achieve what you want. (we think)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Sep 14, 2020 at 07:22:51_

----

zoneport, not zoneip. https://github.com/project-topaz/topaz/blob/release/sql/zone_settings.sql#L29

anything not on a port your current mapserver is set to handle never gets loaded so the scripts never execute there.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 16, 2020 at 04:51:13_

----

Seems pretty resolved to me - please reach out on #customisation in Discord if you need any more advice about zones etc. (I didn't know this was possible either!)
