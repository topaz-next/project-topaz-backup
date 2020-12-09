**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Sep 13, 2020 at 23:37:55_
_Originally opened as: project-topaz/topaz - Issue 1134_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Also included: addition to `!speed` command to report values on use, and extra commenting of source.

**I thoroughly tested that the additions I made work, and that I did not break anything that wasn't already broken. Of things that WERE broken _before I got here(!!)_ I will be opening a detailed issue for in the near future.**

Note worthy: I verified on retail that chocobos/mounts are NOT simply double your speed. They are base 40 to the players 50, but the client doubles their "stride" effectively moving them at 80. 1 point of speed is worth 2 when mounted. Likewise flee is not "double speed" as was always thought, but I will go over that in my issue later.



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 14, 2020 at 05:01:29_

----

I... can't believe this is the original binding... would you mind swooping in and changing this to `setSpeed()` or something better?

If it's in 10 million places don't worry about it, it isn't _that_ awful 🙏 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Sep 14, 2020 at 05:06:57_

----

There were actually a lot of the old bindings that "report current" if no input was given, with no get/set. Pretty much anytime it was a member value instead of a function call..

Do we want 2 bindings? They would both be acting on `m_baseentity->speed`
https://github.com/project-topaz/topaz/blob/release/src/map/lua/lua_baseentity.cpp#L5255

A lot about speed need reworked and I thought I'd leave this alone until we do that. This is the tip of the iceberg and it is all ugly imo.



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 14, 2020 at 05:13:57_

----

Yeah, just leave it be for now then 👍 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 14, 2020 at 05:01:29_

----

I... can't believe this is the original binding... would you mind swooping in and changing this to `setSpeed()` or something better?

If it's in 10 million places don't worry about it, it isn't _that_ awful 🙏 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Sep 14, 2020 at 05:06:57_

----

There were actually a lot of the old bindings that "report current" if no input was given, with no get/set. Pretty much anytime it was a member value instead of a function call..

Do we want 2 bindings? They would both be acting on `m_baseentity->speed`
https://github.com/project-topaz/topaz/blob/release/src/map/lua/lua_baseentity.cpp#L5255

A lot about speed need reworked and I thought I'd leave this alone until we do that. This is the tip of the iceberg and it is all ugly imo.



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 14, 2020 at 05:13:57_

----

Yeah, just leave it be for now then 👍 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Sep 13, 2020 at 23:44:58_

----

Realized I said modifier instead of conf, so amended both pr title and commit message.

Modifier was something I tried to do (for that mount quest) but couldn't get working.
