**Labels:**

approved



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Wednesday Jun 17, 2020 at 02:04:18_
_Originally opened as: project-topaz/topaz - Issue 736_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

I'll be doing live testing on Gold Saucer over the next few days for this; holding here for critiquing as well.

Thanks to cocosolos for assistance with spawn conditions!


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jun 17, 2020 at 07:46:23_

----

Should just need to change this to `GetMobByID(ID.mob.BACKOO):setRespawnTime(1)`


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jun 17, 2020 at 07:50:43_

----

```lua
local backoo = GetMobByID(ID.mob.BACKOO)
if backoo:getRespawnTime() == 0 then
    backoo:setRespawnTime(1)
else
    DisallowRespawn(ID.mob.BACKOO, false)
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jun 17, 2020 at 10:07:22_

----

Might need a different pool. This is the pool for Koropokkur, which has a skill list of _only_ Wild Oats.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Wednesday Jun 17, 2020 at 20:32:40_

----

Swapped him to Tom Tit Tat's pool, who uses no special abilities outside of standard mandy moves.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jun 17, 2020 at 23:03:03_

----

but then its using all the same pool data as Tom, which may not be correct. More than likely a flag value will be different (probably size bits) and those are stored in pool. Recommend just making a new pool for new mobs.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jun 17, 2020 at 07:46:23_

----

Should just need to change this to `GetMobByID(ID.mob.BACKOO):setRespawnTime(1)`


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jun 17, 2020 at 07:50:43_

----

```lua
local backoo = GetMobByID(ID.mob.BACKOO)
if backoo:getRespawnTime() == 0 then
    backoo:setRespawnTime(1)
else
    DisallowRespawn(ID.mob.BACKOO, false)
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jun 17, 2020 at 10:07:22_

----

Might need a different pool. This is the pool for Koropokkur, which has a skill list of _only_ Wild Oats.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Wednesday Jun 17, 2020 at 20:32:40_

----

Swapped him to Tom Tit Tat's pool, who uses no special abilities outside of standard mandy moves.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jun 17, 2020 at 23:03:03_

----

but then its using all the same pool data as Tom, which may not be correct. More than likely a flag value will be different (probably size bits) and those are stored in pool. Recommend just making a new pool for new mobs.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Wednesday Jun 17, 2020 at 18:34:51_

----

It should be noted that its spawn position input in the database is a rough guesstimate based on what ffxiclopedia had to say.  Could use a capture (should be fairly easy given his regular spawn timing) to determine more accurate spawn coords.

edit: Nyu provided a retail capture for his position, thanks!
