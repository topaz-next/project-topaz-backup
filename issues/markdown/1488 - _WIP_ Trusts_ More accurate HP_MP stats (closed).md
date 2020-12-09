**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Monday Nov 09, 2020 at 05:14:38_
_Originally opened as: project-topaz/topaz - Issue 1488_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

![image](https://user-images.githubusercontent.com/1389729/98502645-37e42900-225b-11eb-9aee-8dd4dfbd0d2e.png)

But in all seriousness, I'll be using the calculations for player health:

http://ffxi-stat-calc.sourceforge.net/cgi-bin/ffxistats.cgi?mode=document

and the calculations for monster health (go see `mobutils.cpp`).

The ratios are currently right (Paladins have significantly less MP than White Mages, for instance), but the numbers seem low. So I need to dig into the differences between players and trusts for this (be it stats, gear, race contribution etc.)

**HEFTY REMINDER** That the options to boost trust hp, mp, stats, and skills have existed in `map.conf` for six months. If you don't like the stats becoming more accurate you are encouraged to tweak them to your liking :) 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 09, 2020 at 13:18:47_

----

To be clear: Making something more accurate to retail is not a nerf.

If I see complaints about our pursuit of accuracy, I _will_ start throwing out bans.

The - to be frank, outright whining - from Zach previously trying to make trust MP pools more accurate was toxic, mentally exhausting, and even slowed down development of _completely unrelated_ things.

It will _not_ be tolerated this time.

If there are complaints about trust stat adjustments, they should be based on being inaccurate to retail. If you are unable to show a retail inaccuracy, then you have nothing to say on this matter.
