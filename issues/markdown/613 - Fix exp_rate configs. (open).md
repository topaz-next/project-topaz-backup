**Labels:**

improvement



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Tuesday May 12, 2020 at 05:56:26_
_Originally opened as: project-topaz/topaz - Issue 613_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Currently, exp_rate in map.conf multiplies ALL exp received, including exp received from the lua util player:addExp(x).  My understanding is that this should only multiply exp received from kills in the exp_base table.

EXP_RATE in settings.lua supposedly only modifies the quests/FOV/GOV exp, but I haven't tested it.

Both should be in the same config/setting file, and they should be aptly named to eliminate confusion.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday May 12, 2020 at 12:16:44_

----

This is somewhat expected behavior - its poorly documented causing the surprise  so not "expected" by the user, but expected as in it was made this way. The conf is meant to hit -all- exp, the setting was just for quest/books, which is ironic given that at the time the setting  was made quest exp wasn't a thing and books didn't exist yet. Since the exp happing in scripts has to eventually get to that core function to do anything, it gets the conf boost applied as well. 

The conf makes its adjustment ad the core function where all exp must land at, while the lua setting is simply a variable used in scripts as a multiplier (and can actually be used to reduce book exp by setting it less than 1 e.g. 0.5 for half exp) Short of overloading the function to add a bool for "is this script exp?" I dunno how you'd separate them.


----
<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday May 14, 2020 at 06:12:28_

----

If the exp rate is high enough, you can actually gain EXP by dying and being raised.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday May 14, 2020 at 20:35:43_

----

> If the exp rate is high enough, you can actually gain EXP by dying and being raised.

Diff issue with diff cause.


