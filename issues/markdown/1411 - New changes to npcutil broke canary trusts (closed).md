**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Friday Oct 23, 2020 at 04:55:13_
_Originally opened as: project-topaz/topaz - Issue 1411_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Canary is broken due to keyitem flags changing from "keyItem" to "ki" from trust branch.
When trying to finish Bastok trust quest, the quest will be completed but keyitem never received.
Unsure if there is something else that might break from other branches.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 23, 2020 at 05:14:06_

----

proposed fix:
https://github.com/project-topaz/topaz/pull/1303#discussion_r502866950


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 23, 2020 at 17:21:02_

----

Changed the quests to use ki:
https://github.com/project-topaz/topaz/commit/41ee8b2e0d4ece34e29f2e92da61921af39d62e5

Also patched the function to accept keyItem if there are any leftover somewhere:
https://github.com/project-topaz/topaz/commit/f828092c6ff49a030f331626bf3ac82e915603e8
