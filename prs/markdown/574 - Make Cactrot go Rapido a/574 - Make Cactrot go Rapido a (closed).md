**Labels:**

merge ready



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 01:55:36_
_Originally opened as: project-topaz/topaz - Issue 574_

----

- Fixed script logic (onMobRoam to onPath at spawn time, then recurring check to continue pathing in onMobRoam, with onPath sterting the patrol through nodes)
- Greatly reduced pathnodes while re-plotting several of them. These are not 100% accurate.
- nuked MOD_MOVE from  mob_pool_mods.sql and set speed in onMobSpawn instead. I am assuming when wiki says 250% they just mean its movement rate is 250, as they use the terminology interchangeably in many places. If I am wrong, his movement would be 125 assuming a base speed of 50, or 100 assuming a base speed of 40.Honestly none of these feel right, and I suspect he's 150 or 200. But feelings aren't good practice :P

Pending fresh retail captures, an overhaul to the pathing methods, and a change to send the entity update packets more often, this is as good as he gets.

P.S. I also corrected spelling on some unrelated comments my spellchecker caught while I was looking for his mods.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits
_I followed that punk around the desert for **three hours** man. **Three hours!** I got sand in places I didn't know I had, and now I just wanna kick back and enjoy a refreshing cactus cola._


