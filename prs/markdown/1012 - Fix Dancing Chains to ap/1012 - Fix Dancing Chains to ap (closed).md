**Labels:**

approved

reviewed



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Thursday Aug 27, 2020 at 19:11:25_
_Originally opened as: project-topaz/topaz - Issue 1012_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Dancing chains is not supposed to damage players, but it is supposed to apply a high drown effect to players in a 10y radius.

To be fixed: CURRENTLY our elemental hp/tic down debuffs get their stat debuff AND hp/tic debuff from the effect power.  Because the power for this is set at 15 hp/tic, the strength stat down is -33.  I doubt it was ever that strong, and this needs to be fixed eventually.

ALSO, the duration was a complete guess.  Needs verification if anyone can snag that... might as well grab the -str debuff amount too ^.^

Thanks to Nireya@GoldSaucer for reporting this.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 28, 2020 at 16:30:21_

----

+1 for that “to be fixed”. We should set dot by power and stats down by subpower just defaulting to current behavior when no subpower is sent. Lets make an issue so we don’t forget it.
