**Labels:**



<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Friday Oct 16, 2020 at 04:23:47_
_Originally opened as: project-topaz/topaz - Issue 1371_

----

CP value was removed from outposts table in error, which caused crashes when adding the CP reward for doing supply run missions. Simply restoring the old version of the table, which does not affect the recent fix to Outpost warping costs or any other function.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 16, 2020 at 04:33:14_

----

Whats the relation to the PR that removed these?
https://github.com/project-topaz/topaz/pull/1020


----
<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Friday Oct 16, 2020 at 04:35:45_

----

> Whats the relation to the PR that removed these?
> #1020

Was discovered that the removal of the CP values causes a crash when finishing a supply run here:
https://github.com/project-topaz/topaz/blob/f3eabf8efd92216b018c37753a88bdf878b8af72/scripts/globals/conquest.lua#L1112




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 16, 2020 at 04:41:06_

----

CI is dead because... Microsoft? Seems fine to me
