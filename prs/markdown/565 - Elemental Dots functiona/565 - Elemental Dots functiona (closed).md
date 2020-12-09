**Labels:**

merge ready



<a href="https://github.com/Brierre"><img src="https://avatars3.githubusercontent.com/u/20527593?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Brierre](https://github.com/Brierre)**
_Saturday May 02, 2020 at 01:39:09_
_Originally opened as: project-topaz/topaz - Issue 565_

----

…own tested on player casts and mob casts. Duration merits also working.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 02:30:22_

----

FLAG_ERASABLE is a nil value
tpz.effectFlag.ERASABLE would have been 2, but I do not no why you'd set that argument to the value of an effect flag enum. Sorry I didn't catch that earlier. :x


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 02:30:22_

----

FLAG_ERASABLE is a nil value
tpz.effectFlag.ERASABLE would have been 2, but I do not no why you'd set that argument to the value of an effect flag enum. Sorry I didn't catch that earlier. :x


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday May 02, 2020 at 14:33:28_

----

As the original author of the code this person is fixing, I support this PR. Don't know how I glitched so hard and didn't just expand the original function.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday May 02, 2020 at 16:02:00_

----

Note: We eventually still need to separate the dot from the stat down. While basing both off the power value works out using this function on the black mage spells it does not work accurately for the mob skills that inflict these status effects.

This is a pre-existing problem separate from what is being fixed however. 


----
<a href="https://github.com/Brierre"><img src="https://avatars3.githubusercontent.com/u/20527593?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Brierre](https://github.com/Brierre)**
_Sunday May 03, 2020 at 02:05:53_

----

@TeoTwawki I've made a change to the magic.lua that should allow the dots to scale instead of the prescribed levels in the first commit (which will make Gates of Hades, etc. have the proper values).  I am unsure how to squish that in here so that it is clean.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 02:18:34_

----

we prolly later (you don't need to just because of me) make it possible to send a different value than what the formula based on dot dmg is. Like we have dia/bio sending diff dot and status down by having one stored in power and the other in subpower. Just so that if you need to, you _can_ break the pattern without having to do workarounds. We'd still do what you are doing now by default.

(this should merge as is, imo, with possible exception to the FLAG_ERASABLE argument because I dunno what thats doing yet)
