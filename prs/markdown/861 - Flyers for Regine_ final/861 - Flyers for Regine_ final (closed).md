**Labels:**

merge ready



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Jul 18, 2020 at 07:20:32_
_Originally opened as: project-topaz/topaz - Issue 861_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

* subtable npcData for faster lookups
* npcs will no longer look over curiously once you've traded them a flyer
* removed pre-quest dialog from Regine, per video and Nyu's retail testing
* removed npc flyer refusal dialog, per Nyu's retail testing
* localed some variables in npc scripts
* npcs will no longer look over curiously when you're not on the quest [Fixes #865]



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jul 23, 2020 at 22:07:35_

----

Gotta love the checks against variables which were never defined~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jul 23, 2020 at 22:09:16_

----

And easy server crashes due to never having had the quest require!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jul 23, 2020 at 22:12:47_

----

You were just _swimming_ in all the copy-paste code with never-used requires..!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jul 23, 2020 at 22:26:05_

----

@TeoTwawki [got a little _too_ crazy with the require axe-murdering](https://github.com/project-topaz/topaz/commit/1dabc64278c58bd98955185114871a985d2323e6#diff-deeb89c2eb94a5679b39cc32db080314) 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jul 23, 2020 at 22:30:14_

----

I am amused by how many different forms this trade block took.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jul 23, 2020 at 22:34:49_

----

Regine: "I don't want this trash!"


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 24, 2020 at 00:04:48_

----

:scream: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jul 23, 2020 at 22:07:35_

----

Gotta love the checks against variables which were never defined~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jul 23, 2020 at 22:09:16_

----

And easy server crashes due to never having had the quest require!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jul 23, 2020 at 22:12:47_

----

You were just _swimming_ in all the copy-paste code with never-used requires..!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jul 23, 2020 at 22:26:05_

----

@TeoTwawki [got a little _too_ crazy with the require axe-murdering](https://github.com/project-topaz/topaz/commit/1dabc64278c58bd98955185114871a985d2323e6#diff-deeb89c2eb94a5679b39cc32db080314) 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jul 23, 2020 at 22:30:14_

----

I am amused by how many different forms this trade block took.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jul 23, 2020 at 22:34:49_

----

Regine: "I don't want this trash!"


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 24, 2020 at 00:04:48_

----

:scream: 
