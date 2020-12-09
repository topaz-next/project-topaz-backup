**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Thursday Nov 26, 2020 at 07:03:15_
_Originally opened as: project-topaz/topaz - Issue 1533_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Check that the entity is char before char-specific things are called on it, tripping debug breaks and other horrors.

Fixes: https://github.com/project-topaz/topaz/issues/1531


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Nov 26, 2020 at 17:21:27_

----

I'm afraid this won't correct whatever the root cause of the crash is.
https://github.com/project-topaz/topaz/blob/36fc2f1b64c80b0b1d159fd142e72aa2dfd1eb55/src/map/lua/lua_baseentity.cpp#L6992
`getEminenceProgress` always returned nil for non-PC entities, as that's handled in Core.

Edit: I realize that since it wasn't a consistent crash on Canaria, it's reasonable to assume that since it didn't crash before or after this fix, it may have been a possible culprit. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Nov 26, 2020 at 17:41:53_

----

I only had a little time to check, but if I remember correctly the crash was on the debug break when a wyvern gets a healing tick.

If we have logic to handle it gracefully, we don't need the debug break in the first place. Pick one style or the other, I don't mind, but mixing both leads to different logic in release and debug builds: which is bad.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Nov 26, 2020 at 17:43:54_

----

I wouldn't call resolving a 100% reproducible crash a "non-fix" either. 👀 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Nov 26, 2020 at 18:31:12_

----

Are/will there be records that need to fire off on non-player entities such as pets, or does anything rely on receiving nil back from the function? 

**if no:** debug break makes sense, since debug breaks exist to tell you during testing (in debug mode..for..debugging..) that you messed up and to check whats calling the function. 

**If yes,** then removing the debug is preferable to inducing a forced crash telling you to check your stuff and hit that pushnil instead.

For now, this is exactly logical to fix the issue. a debug break said we called this on a non pc, we go to where the call is and check that its a pc or not 1st. no more debug break hit. We have _tons_ of bindings that could exit rather then induce a break that do not. the old team thought this was good to force people to look what they called stuff on. I'd personally prefer more things simply not run rather than explode with exceptions to that based on how critical a functions execution is, but that is a can of worms for another day.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Nov 26, 2020 at 18:43:46_

----

Perhaps I misunderstood that the crash was in-fact the debug-if being tripped.

There's no case where a non-player would have any eminence progress to get. This fix works fine in this case but ideally I envisioned getEminenceProgress being safe to call on any entity and you'd simply get nil which is easy to check.

In my mind I mistakenly assumed users would be running release, and in hind-sight I might have left the debug-break for PC out, since calling on a non-PC is technically safe.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Nov 26, 2020 at 18:57:38_

----

users generally should run release. testing generally should happen in debug. :+1: 
