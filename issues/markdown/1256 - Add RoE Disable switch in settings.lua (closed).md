**Labels:**



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Monday Oct 05, 2020 at 17:29:59_
_Originally opened as: project-topaz/topaz - Issue 1256_

----

This still maintains support for showing the player's Spark amount and giving/removing spark currency (In case any server wants alternate ways to obtain them or custom usage.)

Summary of fail-out conditions when RoE Disabled:
- Client RoE packets won't be replied to (Take record, Remove record, Quest Log.) RoE client menu will be blank.
- RoE Events bail-out immediately.
- No RoE writes to DB

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 05, 2020 at 18:21:44_

----

`clang-format` has been disabled as a check for a while, mysteries continue
