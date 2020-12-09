**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 16, 2020 at 03:16:46_
_Originally opened as: project-topaz/topaz - Issue 345_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

nothing currently really _needs_ this yet, but something I was working on could have been made simpler instead of my using `mobb:getTarget()` to grab a table of everything on its hatelist yesterday when I really just need the current target...and I would wager a retail use case for it will show up eventually.

Oddly the hook (listener) is _inside the binding_ instead of in the spot in battleutils that the binding is triggered from. When the listeners were made they were intended to phase out the bindings, though I personally like the bindings better. ¯\\\_(ツ)\_/¯ 

So..I did this all at the binding itself. It now occurs to me I'm getting the target of a target..The alternative is I go in battleutils where its in the context of the players own attack making the mob itself "PTarget" and adding a param for that entity there like..`luautils::OnCriticalHit(PTarget, this);` and then updating all the calls to match while passing it along as `mob, attacker`. I decided to stop and get some input first, but I am leaning toward doing that instead.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 16, 2020 at 19:49:13_

----

Redid it the way I was talking about last night
