**Labels:**

merge ready



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Sunday Apr 05, 2020 at 03:31:16_
_Originally opened as: project-topaz/topaz - Issue 471_

----

Fixes issue with battlefield being marked as won even when timing out
or wiping. Also fixed some issues in airship fight.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 10:30:43_

----

1) Maybe rename this function to "phaseOneDead" or "phaseOneComplete"

2) Can pass in the battlefield directly into the function instead of the mob; the original mob isn't used once inside it


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 08, 2020 at 12:06:06_

----

`phaseChangeReady()` ?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 08, 2020 at 13:09:11_

----

True to both points. I just copied this function from the phase 1 mobs, should I change it there too?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 09, 2020 at 01:24:12_

----

Yeah, "allHeirMobsDead" is even more confusing inside the phase 1 mob files~! 😅 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 10:30:43_

----

1) Maybe rename this function to "phaseOneDead" or "phaseOneComplete"

2) Can pass in the battlefield directly into the function instead of the mob; the original mob isn't used once inside it


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 08, 2020 at 12:06:06_

----

`phaseChangeReady()` ?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 08, 2020 at 13:09:11_

----

True to both points. I just copied this function from the phase 1 mobs, should I change it there too?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 09, 2020 at 01:24:12_

----

Yeah, "allHeirMobsDead" is even more confusing inside the phase 1 mob files~! 😅 
