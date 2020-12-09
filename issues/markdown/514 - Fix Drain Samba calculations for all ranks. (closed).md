**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Wednesday Apr 22, 2020 at 09:08:36_
_Originally opened as: project-topaz/topaz - Issue 514_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/Ranzera"><img src="https://avatars1.githubusercontent.com/u/35186045?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Ranzera](https://github.com/Ranzera)**
_Wednesday Apr 22, 2020 at 20:34:15_

----

This only fixes a tiny portion of the incorrect calculations for drain samba.

This doesn't address the dual wielding (and H2H) issues with drain samba, each weapon strike uses the full delay for the drain calculation. It's not supposed to.
I also can't find any evidence there is a level correction in the calculations. Kujata Reborn has done retail testing and can't find any. This talk page (https://ffxiclopedia.fandom.com/wiki/Talk:Drain_Samba ) doesn't mention it. At this point I think it's not supposed to be there. 

There's also the matter of original implementation arbitrarily deciding to do a multiplication step, when they could have just sent 3, 8 or 14 in the power variable from the ability scripts. We did away with that on Kujata Reborn and just send the actual power. Save CPU cycles where you can~


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Wednesday Apr 22, 2020 at 21:33:05_

----

I agree with that, i noticed the 201 delay dagger when dual wielding was still doing up to 11-12 drain per swing, which doesn't make sense considering it should be 6 drain per hit max.  This fix does get it much closer to how it should be in retail though.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 23, 2020 at 12:43:56_

----

https://www.bg-wiki.com/bg/Category:Samba
Claims its not just the weapon delay, but the post-haste attack speed that is used. meaning haste would effect your drain amounts? someone needs to verify that.

Additionally: in the case of dual wielding 2 weapons of dissimilar delays do we need drain samba calculated per-hit ot the total for both weapons divided by 2 placed on each hit? Neither wiki makes that clear, and the difference may be so small as to go unnoticed unless you specifically are looking for it since the amount will naturally flux by a point or 2.


----
<a href="https://github.com/Ranzera"><img src="https://avatars1.githubusercontent.com/u/35186045?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Ranzera](https://github.com/Ranzera)**
_Thursday Apr 23, 2020 at 18:56:15_

----

True, it's delay after all modifications to attack speed. Per our retail testing, when dual wielding it caps your drain for each weapon at trunc(final_combined_delay / 2).


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Friday Apr 24, 2020 at 00:58:48_

----

Accidentally ruined my first pull request.  My drain samba fix is no longer required as a further improvement of the system is being tracked, and the RSE ammo system will be added in a cleaner PR.
