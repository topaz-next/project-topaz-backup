**Labels:**

help wanted

reviewed



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Tuesday Jun 16, 2020 at 21:36:04_
_Originally opened as: project-topaz/topaz - Issue 735_

----

Co-contribution credit for diagnosis and fix to cocosolos!

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

DoRoamTick is where the original despawn pet code was when the master dies, this doesn't fire as intended while the pet is in combat.  It's been improved and moved to on Tick so that it's always being checked, regardless of pet combat status.

Tested with BST charmed/jug, shiva, puppet, and wyvern.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jun 16, 2020 at 21:37:27_

----

_Carbuncle: No! I will avenge my summoner!_

:rofl: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Jun 17, 2020 at 06:33:43_

----

that's awesome =) we just experienced this today


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jun 17, 2020 at 09:03:00_

----

Alternatively, `despawnPet` can stay in petutils, and then the type of the master can be checked as a player before calling `detachPet`. We could then call the pet's die() directly here (in all cases) inside `despawnPet`, allowing `despawnPet` to be used by both mob masters and player masters. This would also allow the binding in `lua_baseentity` to be used on mobs without crashing the server.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jun 17, 2020 at 17:47:13_

----

I didn't consider this last night, but aggroed orphaned pets will despawn if aggro is lost through Hide or Warp. So if beastmen pets are governed by pet_controller, we might still need checks in roamTick (still make sure `DetachPet` doesn't get called with a beastman parent).


----
<a href="https://github.com/zircon-tpl"><img src="https://avatars0.githubusercontent.com/u/60901633?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zircon-tpl](https://github.com/zircon-tpl)**
_Thursday Jul 23, 2020 at 04:30:07_

----

@project-topaz/developer : @tankfest has requested assistance in making suggested changes and opening a new Pull Request.
