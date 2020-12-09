**Labels:**

approved

reviewed



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Saturday Sep 05, 2020 at 22:21:42_
_Originally opened as: project-topaz/topaz - Issue 1068_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Serket rage timer currently defaults at 20 minutes, but it should be 30.
https://ffxiclopedia.fandom.com/wiki/Serket

Thanks to Eren@GoldSaucer for reporting.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Sunday Sep 06, 2020 at 12:55:39_

----

where did the 20 minutes come from? is it a mob mod in sql to be removed?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 06, 2020 at 13:00:31_

----

@59blargedy The default in the rage mixin:
https://github.com/project-topaz/topaz/blob/release/scripts/mixins/rage.lua#L19
