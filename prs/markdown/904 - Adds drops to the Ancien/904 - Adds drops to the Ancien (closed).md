**Labels:**

approved



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Tuesday Jul 28, 2020 at 21:34:54_
_Originally opened as: project-topaz/topaz - Issue 904_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

![image](https://user-images.githubusercontent.com/37684138/88724508-7a845a00-d0df-11ea-8f65-2b20ee135c78.png)



----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Jul 29, 2020 at 00:40:42_

----

i think daihanya is more in line with 100 for rate
based on http://ffxidb.com/zones/153/ancient-goobbue
https://ffxiclopedia.fandom.com/wiki/Ancient_Goobbue
these are small sample sizes, however, but 40 seems lowish


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 00:46:23_

----

40 also isn't a valid TH0 bucket~! (50 would be if it were Rare, but I'm leaning towards Uncommon on this one due to the numbers you've posted)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 00:49:34_

----

[FFXIDB has these above 100% rate](http://ffxidb.com/zones/153/ancient-goobbue)

But old wiki is capping it at 100%. Anyone feel like killing Acient Goobbue on retail with full TH?


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Wednesday Jul 29, 2020 at 00:52:29_

----

i didn't understand ffxidb, though i looked at it to base this off of.  TH0 = 10%, but TH2 = 8%?  I put 4% to make topaz's TH2 actually even out at around 10% like it says.  There is a report of someone going 0/27 with TH on it, comments  make it seem very low drop rate.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 01:20:37_

----

Sometimes FFXIDB's different TH values will conflict with each other; I tend to lean towards going with whatever is the higher sample size. (Can see sample sizes on FFXIDB by hovering over the table cell).

In either case, now that TH's exact mechanics are known, new drop percentages should match a designated TH bucket (_which_ bucket is debatable). At the moment our TH code doesn't function like it should, but that'll need to be fixed at the code level, not the data level.

At some point we'll need to go through our existing data and "snap" it to the nearest TH bucket. This'll be a prerequisite _before_ we can properly fix the TH code - we can't implement bucket behavior if we don't have buckets!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 29, 2020 at 01:34:18_

----

LIES! All lies I tell you! That katana is a myth! Doesn't exist!
*cries in terribad luck*


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Wednesday Jul 29, 2020 at 01:34:27_

----

would 50 suffice?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 29, 2020 at 01:37:50_

----

That happens when it _can_ drop a 2nd (or 3rd or 4th) of an item, but at least 1 is 100% rate (the additional ones may or may not also be - not required).

So what the person checking this will need to do, is get enough kills to reliably say how many are 100% and how many total there generally could be.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 02:02:29_

----

Yeah, 50 would align with Rare. Whether it _should_ be Rare is another matter.

As I don't play, I'm not too vested in which it is, so long as it's backed by good evidence.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Jul 29, 2020 at 00:40:42_

----

i think daihanya is more in line with 100 for rate
based on http://ffxidb.com/zones/153/ancient-goobbue
https://ffxiclopedia.fandom.com/wiki/Ancient_Goobbue
these are small sample sizes, however, but 40 seems lowish


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 00:46:23_

----

40 also isn't a valid TH0 bucket~! (50 would be if it were Rare, but I'm leaning towards Uncommon on this one due to the numbers you've posted)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 00:49:34_

----

[FFXIDB has these above 100% rate](http://ffxidb.com/zones/153/ancient-goobbue)

But old wiki is capping it at 100%. Anyone feel like killing Acient Goobbue on retail with full TH?


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Wednesday Jul 29, 2020 at 00:52:29_

----

i didn't understand ffxidb, though i looked at it to base this off of.  TH0 = 10%, but TH2 = 8%?  I put 4% to make topaz's TH2 actually even out at around 10% like it says.  There is a report of someone going 0/27 with TH on it, comments  make it seem very low drop rate.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 01:20:37_

----

Sometimes FFXIDB's different TH values will conflict with each other; I tend to lean towards going with whatever is the higher sample size. (Can see sample sizes on FFXIDB by hovering over the table cell).

In either case, now that TH's exact mechanics are known, new drop percentages should match a designated TH bucket (_which_ bucket is debatable). At the moment our TH code doesn't function like it should, but that'll need to be fixed at the code level, not the data level.

At some point we'll need to go through our existing data and "snap" it to the nearest TH bucket. This'll be a prerequisite _before_ we can properly fix the TH code - we can't implement bucket behavior if we don't have buckets!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 29, 2020 at 01:34:18_

----

LIES! All lies I tell you! That katana is a myth! Doesn't exist!
*cries in terribad luck*


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Wednesday Jul 29, 2020 at 01:34:27_

----

would 50 suffice?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 29, 2020 at 01:37:50_

----

That happens when it _can_ drop a 2nd (or 3rd or 4th) of an item, but at least 1 is 100% rate (the additional ones may or may not also be - not required).

So what the person checking this will need to do, is get enough kills to reliably say how many are 100% and how many total there generally could be.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 02:02:29_

----

Yeah, 50 would align with Rare. Whether it _should_ be Rare is another matter.

As I don't play, I'm not too vested in which it is, so long as it's backed by good evidence.
