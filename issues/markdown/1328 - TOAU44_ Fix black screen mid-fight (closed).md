**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 17:46:08_
_Originally opened as: project-topaz/topaz - Issue 1328_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes: https://github.com/project-topaz/topaz/issues/1180
Superceeds: https://github.com/project-topaz/topaz/pull/1260

The order of events was wrong, so you ended up getting attacked while you were in CS. This ends up breaking your cs and results in you being trapped in a black screen.

Also discovered that `entityvsetPos()` doesn't correctly accept a table - like it is programmed to do. Gonna make an issue for that. Skirting around that here for now by using the table's members.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 12, 2020 at 04:51:20_

----

Yeah, things just got confused by the setPos binding being screwwy with the return table from getEntryPos :(
