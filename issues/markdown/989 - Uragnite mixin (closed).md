**Labels:**

reviewed



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Friday Aug 21, 2020 at 03:49:25_
_Originally opened as: project-topaz/topaz - Issue 989_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Creates uragnite mixin and applies to Coralline and Nightmare uragnites.  Mixin includes:

* shell mode, wherein uragnite
    * changes AnimationSub
    * ceases attacking or moving
    * takes greatly reduced damage
    * gains regen
    * uses shell skills
* physical attacks have a chance to push uragnite into shell mode
* uragnite leaves shell mode after some time
* an optional config function that lets you set custom values for most of these things

Fixes #985 



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 15:10:35_

----

They are indeed zero'd OnSpawn


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Aug 22, 2020 at 17:59:59_

----

right but that doesn't look like a problem here. the mixin is just changing them from the zero they start life with here `mob:addListener("SPAWN", "URAGNITE_SPAWN", function(mob)` and it doesn't look like anything relies on them being nonzero at spawntime before that. it would be pretty silly for us to have a spawn hook in the core that execs before the rest of the spawn code cleans out out vars and mods.
