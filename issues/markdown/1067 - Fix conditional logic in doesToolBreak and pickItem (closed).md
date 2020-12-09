**Labels:**

approved

reviewed



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Saturday Sep 05, 2020 at 20:58:42_
_Originally opened as: project-topaz/topaz - Issue 1067_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

I was just doing some HELM testing on my test server to ensure the mods were properly scripted for break rates, and I noticed a small issue with comparing the random roll to the player's break rate.

If you have break rate on the server set to 100%, there's a 1/100 chance that you would have NOT broken with the old script.  Similarly, for determining if the player got an item if item chance was set to 100%, there was a 1/100 chance the player would not receive an item.

Now at all setting possibilities, the break rate and item pick rate will function as intended.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Sep 05, 2020 at 21:25:59_

----

this probably happened from this code having been the replacement for code that did 0-99 instead of 1-100 in its random rolls back then. thanks for catching and fixing it :+1: 


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 05, 2020 at 22:09:48_

----

> 
> 
> this probably happened from this code having been the replacement for code that did 0-99 instead of 1-100 in its random rolls back then. thanks for catching and fixing it +1

yeah that was another way i was looking at "fixing" this issue, but this way seemed cleaner.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Sep 05, 2020 at 22:26:47_

----

> 
> 
> > this probably happened from this code having been the replacement for code that did 0-99 instead of 1-100 in its random rolls back then. thanks for catching and fixing it :+1:
> 
> yeah that was another way i was looking at "fixing" this issue, but this way seemed cleaner.

definitely. I dislike seeing `math.random(0, 99)` when we mean 1-100 for a percentage anyway! 
