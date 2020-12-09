**Labels:**



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Oct 10, 2020 at 06:56:37_
_Originally opened as: project-topaz/topaz - Issue 1303_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes #1292 

Rather than fixing Thunder Hawk's npcUtil option from **ki** to **keyItem** (See #1292), I decided to go the other way with the fix, and rename the option to **ki** for consistency.  Updated all references in codebase.

Also switched some references to the short-hand **tpz.ki**




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 10, 2020 at 07:01:50_

----

For anyone else passing-by, this is the important change here!

Looks good, thanks! 👍 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 11, 2020 at 05:15:59_

----

I'd really like to see the terms ki and keyItem be interchangeable everywhere. we have a high likelihood of future users using the "wrong" one no matter which we keep, so I'd rather we plan for it than simply swap out. I had thought we already did this for the actual global table, just not for the params we're using in the utils functions 

If the "right" one is nil and the other not, lets just populate/duplicate it over before we do the rest of execution.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 06:14:48_

----

Yeah, agree with this


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 23, 2020 at 17:19:44_

----

@TeoTwawki 
Just for this case:
https://github.com/project-topaz/topaz/commit/f828092c6ff49a030f331626bf3ac82e915603e8


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 10, 2020 at 07:01:50_

----

For anyone else passing-by, this is the important change here!

Looks good, thanks! 👍 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 11, 2020 at 05:15:59_

----

I'd really like to see the terms ki and keyItem be interchangeable everywhere. we have a high likelihood of future users using the "wrong" one no matter which we keep, so I'd rather we plan for it than simply swap out. I had thought we already did this for the actual global table, just not for the params we're using in the utils functions 

If the "right" one is nil and the other not, lets just populate/duplicate it over before we do the rest of execution.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 06:14:48_

----

Yeah, agree with this


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 23, 2020 at 17:19:44_

----

@TeoTwawki 
Just for this case:
https://github.com/project-topaz/topaz/commit/f828092c6ff49a030f331626bf3ac82e915603e8
