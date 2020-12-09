**Labels:**

reviewed



<a href="https://github.com/Laserstrahl"><img src="https://avatars3.githubusercontent.com/u/59196077?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Laserstrahl](https://github.com/Laserstrahl)**
_Wednesday Nov 04, 2020 at 14:36:13_
_Originally opened as: project-topaz/topaz - Issue 1477_

----

Script to set all skills to the given level.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Nov 04, 2020 at 18:55:05_

----

it would be better to modify the one that caps all skills to have an optional parameter, and default to maxing them out (its current behavior) than to add yet another command that manipulates skills. Since they cap at different levels this isn't all that useful to warrant a new stand alone command.

edit: or even edit the one that sets one skill to accept "all" as a skill name to do this. because naming.



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Nov 06, 2020 at 06:41:50_

----

EDIT: Agree with above, I think the functionality in this script might be useful to some, but not enough to warrant a whole new script.

I'm kinda into modifying the existing `!capallskills`, so that it sets every skill to its max value, and `!capallskills 100` _attempting_ to set every skill to 100, if it can get there.
