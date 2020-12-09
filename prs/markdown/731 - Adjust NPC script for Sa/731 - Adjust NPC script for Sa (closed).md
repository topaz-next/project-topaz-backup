**Labels:**

approved



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Monday Jun 15, 2020 at 21:10:28_
_Originally opened as: project-topaz/topaz - Issue 731_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Improves some of the code for these three mission giver npcs, and updates Ranperre's final rest to require only a zone.  Closes Issue #724 

These npcs can be further improved, and on this mission some "MissionStatus" vars are skipped (namely 6 was deleted here because it didn't quite make sense), but the quest is in working order.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Jun 16, 2020 at 20:37:45_

----

Is there anything preventing the player from repeating this CS every time they click this?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Jun 16, 2020 at 20:40:10_

----

Can you change these to:
```lua
    if
        player:getCurrentMission(SANDORIA) == tpz.mission.id.sandoria.RANPERRE_S_FINAL_REST and
        player:getCharVar("MissionStatus") == 1 and
        GetMobByID(ID.mob.CORRUPTED_SOFFEIL):isDead() and
        GetMobByID(ID.mob.CORRUPTED_ULBRIG):isDead()
    then
```


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Tuesday Jun 16, 2020 at 21:14:45_

----

no, thanks for pointing that out... it needs to check if they have the KI or not, since that's what flags the next part


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jun 16, 2020 at 22:24:27_

----

![](https://i.pinimg.com/236x/b8/bc/9d/b8bc9dd3b884e7198236d559f417f37d--dude-wheres-my-car-movie-lines.jpg)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jun 16, 2020 at 22:25:10_

----

(syntax error)


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Tuesday Jun 16, 2020 at 22:25:14_

----

rip


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Jun 16, 2020 at 20:37:45_

----

Is there anything preventing the player from repeating this CS every time they click this?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Jun 16, 2020 at 20:40:10_

----

Can you change these to:
```lua
    if
        player:getCurrentMission(SANDORIA) == tpz.mission.id.sandoria.RANPERRE_S_FINAL_REST and
        player:getCharVar("MissionStatus") == 1 and
        GetMobByID(ID.mob.CORRUPTED_SOFFEIL):isDead() and
        GetMobByID(ID.mob.CORRUPTED_ULBRIG):isDead()
    then
```


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Tuesday Jun 16, 2020 at 21:14:45_

----

no, thanks for pointing that out... it needs to check if they have the KI or not, since that's what flags the next part


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jun 16, 2020 at 22:24:27_

----

![](https://i.pinimg.com/236x/b8/bc/9d/b8bc9dd3b884e7198236d559f417f37d--dude-wheres-my-car-movie-lines.jpg)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jun 16, 2020 at 22:25:10_

----

(syntax error)


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Tuesday Jun 16, 2020 at 22:25:14_

----

rip


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Monday Jun 15, 2020 at 21:20:04_

----

Nyu just informed me that #638 PR fixes this same issue;
Also seems to be a duplicate issue #245, so this would close both.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Tuesday Jun 16, 2020 at 00:04:59_

----

This turned into more of an overhaul than I originally expected, so I developed a flow chart that helped me go through the MissionStatus char variables:
![image](https://user-images.githubusercontent.com/37684138/84717308-56532c00-af2a-11ea-8626-c183f98eefae.png)

