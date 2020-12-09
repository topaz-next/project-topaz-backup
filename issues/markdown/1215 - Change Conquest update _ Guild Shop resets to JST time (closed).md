**Labels:**

crafting



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Tuesday Sep 29, 2020 at 16:16:54_
_Originally opened as: project-topaz/topaz - Issue 1215_

----

+ Move Guild Reset over to JST midnight instead of local.
+ fix + remove single-purpose vars from global Vanatime class.
+ Move Conquest over to JST instead of local time.
+ Migrate Lua over to new JST function for getMidnight.

Fixes #750
Fixes #875
Fixes #22 
Closes #552 

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Tuesday Sep 29, 2020 at 16:22:09_

----

Moved conquest updates over to JST as well, because why not!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Sep 29, 2020 at 20:57:41_

----

Explanation for those not following Discord:
Settings to change when "midnight" occurs can't make in-game things happen _at_ the midnight in an _arbitrary_ timezone - they can only be used to change _your_ midnight _from_ your local midnight _to_ JST, so you can run the server _without having to change your system's timezone_.

Settings to change when in-game midnight "is" (ie: making things happen at midnight in _your local_ timezone) **_can't_** function as desired. **The client is hardcoded to _always expect certain things_ to occur at midnight in JST. No server-side shenanigans can ever change these hardcoded client events and expectations.**


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 29, 2020 at 21:16:46_

----

Before anyone brings up any formerly JP midnight things that now aren't: _those_ ones aren't hardcoded into the event in the client like we're talking about, those just used it for a trigger condition. _Those_ can still change. What time is actually JP Midnight cannot, as ibm2431 has stated.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Sep 29, 2020 at 21:55:45_

----

Basically:
- We can make an NPC accept a trade whenever we want. (trigger condition)
- We can't make guilds change their pattern at any time other than true JST. (hardcoded client expectation)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Tuesday Sep 29, 2020 at 22:03:15_

----

> Before anyone brings up any formerly JP midnight things that now aren't: _those_ ones aren't hardcoded into the event in the client like we're talking about, those just used it for a trigger condition. 

I believe all things should correctly be JST-midnight now, but if things aren't please open issue or discuss on discord; should be very easy to *make* it correct. :)
