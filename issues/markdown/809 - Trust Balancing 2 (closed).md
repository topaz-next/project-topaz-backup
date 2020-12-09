**Labels:**

focus

merge ready



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday Jul 05, 2020 at 09:55:44_
_Originally opened as: project-topaz/topaz - Issue 809_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

- Fixes the recent "Trust Balancing" patch with something a little less borked.
- Fixes trust's TP decaying while they rest

TODO:
Bring trust HP/MP down to something reasonable, per "job". Further modifications can be made per-trust using Mods if needed 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jul 05, 2020 at 14:45:30_

----

> Bring trust HP/MP down to something reasonable, per "job". Further modifications can be made per-trust using Mods if needed

on normal mobs this would be group tables lv x family system value, since trusts don't have a group its just being based on lv they get from the player, but teh family system value still exists. There should be multiple usable families for these. The oens mimicking player race are already done but I don't know if their job in pool is taken into account at all currently (it probably should (?), even for regular non-trust mobs, if it does not already)
