**Labels:**

approved



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Tuesday Jun 23, 2020 at 02:02:52_
_Originally opened as: project-topaz/topaz - Issue 760_

----

Sister PR to hunts.lua + other changes coming from Cocosolos/Teo.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [ ] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jun 23, 2020 at 15:37:06_

----

Seeing:
```lua
tpz.hunts.checkHunt(mob, player, 362)
tpz.regime.checkRegime(player, mob, 126, 1, tpz.regime.type.FIELDS)
```
Makes me want to say that we should establish a standardized argument order at some point to avoid inadvertently crossing wires. "Such and such arguments always come before this other argument". There's a lot of combat functions which waffle between `attacker, defender` and `defender, attacker` too.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jun 23, 2020 at 15:40:31_

----

Personal opinion: checkHunt does it better visually because of the order onMobDeath uses. Just “feels right”.

Edit: altho I did originally envision the existing GoV and FoV global being refactored to kill that loop it has and accommodate both hunts and dominion ¯\\\_(ツ)\_/¯



----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Tuesday Jun 23, 2020 at 15:42:33_

----

Indeed, I presume why @Apocarypse structured it so originally. :+1: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jun 23, 2020 at 15:37:06_

----

Seeing:
```lua
tpz.hunts.checkHunt(mob, player, 362)
tpz.regime.checkRegime(player, mob, 126, 1, tpz.regime.type.FIELDS)
```
Makes me want to say that we should establish a standardized argument order at some point to avoid inadvertently crossing wires. "Such and such arguments always come before this other argument". There's a lot of combat functions which waffle between `attacker, defender` and `defender, attacker` too.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jun 23, 2020 at 15:40:31_

----

Personal opinion: checkHunt does it better visually because of the order onMobDeath uses. Just “feels right”.

Edit: altho I did originally envision the existing GoV and FoV global being refactored to kill that loop it has and accommodate both hunts and dominion ¯\\\_(ツ)\_/¯



----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Tuesday Jun 23, 2020 at 15:42:33_

----

Indeed, I presume why @Apocarypse structured it so originally. :+1: 
