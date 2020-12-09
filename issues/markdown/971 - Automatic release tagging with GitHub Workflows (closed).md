**Labels:**

hold

reviewed



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Tuesday Aug 18, 2020 at 13:38:25_
_Originally opened as: project-topaz/topaz - Issue 971_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Seeing as I'm on a big GitHub Workflows hype at the moment, I thought it would be interesting to try and automate some stuff.

Logic:
- Runs on the 1st and 14th day of the month at midnight
- Checks the year+month, if it is the same, increment the next number by 1 for the version number
- If different, it's a new month, set to 01
- Tag with new version number
- Get list of merges and contributors from the last tag to this new tag
- Make release notes from these lists

> Example release notes:
### R202008-02
**Merges:**

(bdf076b9c6) Merge pull request #928 from wrenffxi/client-update - Client update 30200731_2

**This release was made possible by the hard work of:**

wrenffxi

> Big Example
https://github.com/zach2good/topaz/releases/tag/R202008-01


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Wednesday Aug 19, 2020 at 03:37:16_

----

Sweet! :+1: 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 06:38:50_

----

**TODO:**
- Tag every week instead of 2 weeks
- Publish changelists between new and previous tags as draft so a staff can sanity check them
- Verify only on canary or release branches
- Break out long-living branches to `feature/x` to make their lifetime clear
- Rewrite in python for portability


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 21, 2020 at 14:36:35_

----

Will come back to this another time, no use leaving zombie PRs open
