**Labels:**

merge ready



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday May 02, 2020 at 19:35:17_
_Originally opened as: project-topaz/topaz - Issue 570_

----

..and an option to apply to mobs that I hope is eventually deprecated by the ability to manually set mobs sj lv range. :smiley: 

The player options also apply to pets with the exception of charm pets, since those are mobs.

if `subjob_ratio` is 1, player subjobs are normal (one half) as in retail. This is the default option.
2 will set cap of two-thirds, so a lv 75 player can have a subjob up to lv 50, or a lv 99 player up to lv66
3 will make subjobs capped even to mainjob.
0 will make subjobs lv 0 and grant nothing.

I did not want to do this as a float value divisor or multiplier for several reasons, not the least of which is explaining to people the proper math with get the ratio they intended.

`include_mob_sj` determines if the adjustments also apply to monsters.

NOTE: since `SetSLevel()` handled the cap in its entirely, all existing attempts to set the subjob should lead back to here and rely on this. However any instance where a previous editor did not know this probably ***already had incorrect sub levels before I changed anything.***

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

