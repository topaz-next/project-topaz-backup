**Labels:**



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Saturday May 16, 2020 at 00:37:06_
_Originally opened as: project-topaz/topaz - Issue 628_

----

Current mission ID was being truncated to 8 bits in core previously, but now uses the full 16 bits available. Not having a current mission sets current mission ID to `-1` or `65535` which was being truncated to `255` previously. This should be `65535` now.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday May 16, 2020 at 00:46:27_

----

[`!checkmission` also needs adjustments to account for this.](https://github.com/project-topaz/topaz/blob/release/scripts/commands/checkmission.lua#L49)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Saturday May 16, 2020 at 01:12:09_

----

Thanks, fixed!
