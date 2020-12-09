**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Friday Sep 11, 2020 at 19:31:26_
_Originally opened as: project-topaz/topaz - Issue 1100_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes #1099 


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Friday Sep 11, 2020 at 19:37:36_

----

If you're checking items in the trade via `npcUtil.tradeHas()`, then you should close the trade via `player:confirmTrade()` rather than `player:tradeComplete()`.

confirmTrade will consume only the items you checked for, and will return to player any excess items placed into the trade window.

tradeComplete will consume all items in the trade window.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Friday Sep 18, 2020 at 08:07:41_

----

does he just not respond to trades post quest completion?


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Friday Sep 18, 2020 at 17:16:15_

----

Yes, Nyu confirmed.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Friday Sep 11, 2020 at 19:37:36_

----

If you're checking items in the trade via `npcUtil.tradeHas()`, then you should close the trade via `player:confirmTrade()` rather than `player:tradeComplete()`.

confirmTrade will consume only the items you checked for, and will return to player any excess items placed into the trade window.

tradeComplete will consume all items in the trade window.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Friday Sep 18, 2020 at 08:07:41_

----

does he just not respond to trades post quest completion?


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Friday Sep 18, 2020 at 17:16:15_

----

Yes, Nyu confirmed.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Friday Sep 11, 2020 at 21:24:54_

----

Nyu went through and captured correct behavior and dialogue for this quest.  I think it's 99% retail now.
