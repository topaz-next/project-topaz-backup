**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Feb 18, 2020 at 04:02:59_
_Originally opened as: project-topaz/topaz - Issue 349_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

[Spotted some derp in sunburst.lua](https://github.com/project-topaz/topaz/blob/2943fab983cc1457ce75f15dd9dca9d3bfa21b05/scripts/globals/weaponskills/sunburst.lua#L24)
`params.ele = tpz.magic.ele.DARK params.ele = tpz.magic.ele.LIGHT`
its just always going to be light because its being replaced immediately.
Also reformatted a bit because I dislike wide lines.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Feb 18, 2020 at 04:14:54_

----

same bug was in starburst so just amended to include it to.
