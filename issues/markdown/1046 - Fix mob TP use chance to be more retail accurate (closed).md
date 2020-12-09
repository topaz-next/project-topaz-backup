**Labels:**

reviewed



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Monday Aug 31, 2020 at 05:44:57_
_Originally opened as: project-topaz/topaz - Issue 1046_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes #184 

Mobs will now use their TP moves "somewhat randomly" as expected when their HPP is > 25% and TP is between 1000-2999.

Thanks to @Kreidos for some feedback along the way.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Aug 31, 2020 at 06:09:17_

----

As I mentioned on the discord, the 0.7% per tick seems a tad low to me. That'd be roughly a 40% chance to use a skill within 30 seconds. I leave it to someone with better retail knowledge than I to say whether this feels about right!

Good work, nonetheless. :+1: 


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Monday Aug 31, 2020 at 06:13:32_

----

> 
> 
> As I mentioned on the discord, the 0.7% per tick seems a tad low to me. That'd be roughly a 40% chance to use a skill within 30 seconds. I leave it to someone with better retail knowledge than I can say whether this feels about right!

Upped to .92% per tick, which equates almost exactly to a 50% chance for the mob to use a skill within the first 30 seconds of it having 1000 tp.

For you non-statistics people:  Probability of a skill occuring at this rate within 75 ticks (or 30 seconds) = 1 - (1 - .0092)^75 = 0.5000


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 31, 2020 at 11:43:04_

----

Ahh, makes sense now.. the tick rate used to be a larger time interval. when it decreased, the more frequent tp use was a side effect.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Monday Aug 31, 2020 at 15:35:00_

----

we can do this, but i am not sure it is quite right. my  understanding is that tp usage is hp percentage based, above 50 mobs use tp at 3k, below 50 at 2k, below 25 at 1k. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 31, 2020 at 18:29:24_

----

he's got it back to what it used to be in any case. whether it ever should have had randomness, someone can prove/disprove that easily enough on retail just feeding a mob tp repeatedly and that'd be easy to change later.
