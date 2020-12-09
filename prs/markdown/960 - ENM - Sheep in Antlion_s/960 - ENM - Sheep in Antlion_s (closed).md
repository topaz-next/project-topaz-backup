**Labels:**

reviewed



<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [m241dan](https://github.com/m241dan)**
_Sunday Aug 16, 2020 at 16:21:01_
_Originally opened as: project-topaz/topaz - Issue 960_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:04:35_

----

Should this be local?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:07:57_

----

Good catch! I assume that only `CMobEntity` has access to `getMobMod` otherwise I'd say sling it inside `CBattleEntity::CanRest()`


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:08:39_

----

This function: beautifully aligned


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:08:52_

----

Please fix the alignment here


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:09:00_

----

Please fix the alignment here


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:09:06_

----

Please fix the alignment here


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:09:33_

----

4-space alignment here please, otherwise very nice


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:09:57_

----

Please align all of the IDs


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:10:07_

----

Cool!


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 22, 2020 at 13:38:43_

----

yes


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 22, 2020 at 13:39:51_

----

ya, I'm starting to realize that CLion is not good at catching Lua spacing when my other devs are adding contributions and their IDE seems to be set to tabs. x.x


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 13:42:08_

----

Using my question as the example, maybe plop a comment here saying this is intended so nobody tries to "clean" it


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 22, 2020 at 13:53:19_

----

wait, what do you mean? It "should" be local (I added local, pushing soon).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Aug 22, 2020 at 18:50:45_

----

outer parens not needed.

Also neat. whats this for? 
(as in whats this make possible/easier that our existing randoms and shuffle functionality can't do, coz looks like it was just used to random select positions)
not against it just want to understand better.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 22, 2020 at 19:04:24_

----

WHY ARE YOU AGAINST THIS!?!?!?

just kidding

This ensures that if we roll random from 1 to 6, 6 times, we get 1 2 3 4 5 6 in any order with no repetitions, ie a permutation. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Aug 23, 2020 at 01:34:51_

----

Today I learned when I permute it means I don’t roll the same number twice :+1:


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:04:35_

----

Should this be local?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:07:57_

----

Good catch! I assume that only `CMobEntity` has access to `getMobMod` otherwise I'd say sling it inside `CBattleEntity::CanRest()`


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:08:39_

----

This function: beautifully aligned


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:08:52_

----

Please fix the alignment here


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:09:00_

----

Please fix the alignment here


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:09:06_

----

Please fix the alignment here


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:09:33_

----

4-space alignment here please, otherwise very nice


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:09:57_

----

Please align all of the IDs


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 09:10:07_

----

Cool!


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 22, 2020 at 13:38:43_

----

yes


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 22, 2020 at 13:39:51_

----

ya, I'm starting to realize that CLion is not good at catching Lua spacing when my other devs are adding contributions and their IDE seems to be set to tabs. x.x


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 13:42:08_

----

Using my question as the example, maybe plop a comment here saying this is intended so nobody tries to "clean" it


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 22, 2020 at 13:53:19_

----

wait, what do you mean? It "should" be local (I added local, pushing soon).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Aug 22, 2020 at 18:50:45_

----

outer parens not needed.

Also neat. whats this for? 
(as in whats this make possible/easier that our existing randoms and shuffle functionality can't do, coz looks like it was just used to random select positions)
not against it just want to understand better.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 22, 2020 at 19:04:24_

----

WHY ARE YOU AGAINST THIS!?!?!?

just kidding

This ensures that if we roll random from 1 to 6, 6 times, we get 1 2 3 4 5 6 in any order with no repetitions, ie a permutation. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Aug 23, 2020 at 01:34:51_

----

Today I learned when I permute it means I don’t roll the same number twice :+1:


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 16, 2020 at 04:31:48_

----

```
Conflicting files
scripts/globals/status.lua
sql/mob_groups.sql
sql/mob_pools.sql
src/map/mob_modifier.h
```

I have royally boned this PR by merging master into `feature/enm`, I'm gonna close it and merge your branch directly into `feature/enm` (since it's approved) and resolve the conflicts myself - gotta make sure I keep your commits intact 'yo!
