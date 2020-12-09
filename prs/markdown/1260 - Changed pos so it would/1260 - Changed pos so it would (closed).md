**Labels:**

reviewed



<a href="https://github.com/nsabott"><img src="https://avatars0.githubusercontent.com/u/25453121?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [nsabott](https://github.com/nsabott)**
_Monday Oct 05, 2020 at 19:28:28_
_Originally opened as: project-topaz/topaz - Issue 1260_

----

Changed the pos so that it leaves the character outside the instance afterwards, having it at <0, 0, 0, 0, zoneId) was causing issues with the cutscene displaying properly, it would freeze.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Oct 05, 2020 at 20:31:55_

----

Is this cs supposed to play here? [This video](https://youtu.be/SLr-slWFjxQ?t=954) looks like its supposed to play when Alexander spawns.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 09, 2020 at 19:13:00_

----

Yeah, this moves the order of the CS to the end of the battle, instead of between phases. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 10, 2020 at 06:06:25_

----

v isn't accessible until you're inside the loop


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 10, 2020 at 06:07:02_

----

Be careful not to introduce full or half-tabs, only 4x spaces for indentation please


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Oct 05, 2020 at 20:31:55_

----

Is this cs supposed to play here? [This video](https://youtu.be/SLr-slWFjxQ?t=954) looks like its supposed to play when Alexander spawns.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 09, 2020 at 19:13:00_

----

Yeah, this moves the order of the CS to the end of the battle, instead of between phases. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 10, 2020 at 06:06:25_

----

v isn't accessible until you're inside the loop


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 10, 2020 at 06:07:02_

----

Be careful not to introduce full or half-tabs, only 4x spaces for indentation please


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Oct 06, 2020 at 06:24:26_

----

If this was the fix to the black screen in this fight I'm going to lose my mind, it's the one thing I didn't try! 😆 

Please check your styling: 4 space indents, no tabs, etc.
https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md#general-code-guidlines-all-languages
