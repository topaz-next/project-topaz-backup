**Labels:**

crafting



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Monday Sep 28, 2020 at 17:45:28_
_Originally opened as: project-topaz/topaz - Issue 1211_

----

This adds functions to retrieve JST-based time. It is agnostic to the local timezone setting, only expecting the clock be set correctly for their own local timezone.

Should greatly help PR #914 

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Sep 28, 2020 at 17:47:34_

----

These commented lines are left to avoid future merge conflicts if other functions are moved into these areas before RoE Phase 3 is ready.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Sep 28, 2020 at 17:47:34_

----

These commented lines are left to avoid future merge conflicts if other functions are moved into these areas before RoE Phase 3 is ready.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Sep 28, 2020 at 17:48:53_

----

Awesome! finally real vanatime


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Sep 28, 2020 at 17:55:43_

----

Looks good, I just have one question about the JST midnight function. Am I reading it right that it returns last midnight instead of next midnight? I only ask because the Lua midnight function returns next midnight so there might be some confusion.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Sep 28, 2020 at 17:56:55_

----

> Looks good, I just have one question about the JST midnight function. Am I reading it right that it returns last midnight instead of next midnight? I only ask because the Lua midnight function returns next midnight so there might be some confusion.

It returns the upcoming midnight. However, the easiest way to calculate that is to calculate the previous midnight and add 1 day.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Sep 28, 2020 at 18:05:10_

----

Oh I see, the comment confused me, carry on!


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Sep 28, 2020 at 18:07:31_

----

Thanks for the catch, I didn't notice the comment!
I'm fixing it along with the Win32 builds. :unamused: 


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Sep 28, 2020 at 18:15:26_

----

> I was getting myself all prepared to question your use of `static` until I saw that `time_server` is just a standalone function getting called from the `taskmanager`. Ew. Good call laughing

I love statics when the case is right.<3 
The fact that all the other categories still use class variables unnecessarily still irks me to no end, but :shrug: 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Sep 28, 2020 at 18:18:40_

----

> Hopefully @TeoTwawki will have something interesting to say

something interesting

*ducks and covers*



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 28, 2020 at 18:23:50_

----

_Laughs in windows_


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Sep 28, 2020 at 18:24:46_

----

Guild patterns are hard coded in the client to use JST midnight, and since that's the only thing using midnight it might be worth it to just get rid of that block and call the guild update in the new JST midnight block, I think it only requires 2 changes in guildutils.cpp from `getSysYearDay` to `getJstYearDay`.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Sep 28, 2020 at 18:25:17_

----

_Sees build fail a hair too late_

😱 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 28, 2020 at 18:25:50_

----

> Guild patterns are hard coded in the client to use JST midnight, and since that's the only thing using midnight it might be worth it to just get rid of that block and call the guild update in the new JST midnight block, I think it only requires 2 changes in guildutils.cpp from getSysYearDay to getJstYearDay.

You could close two PRs with this... if you get my drift


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Sep 28, 2020 at 18:28:44_

----

> You could close two PRs with this... if you get my drift

if @jarmengaud is fine with me usurping his PR, I'll move the line up and trash the system local midnight block.
