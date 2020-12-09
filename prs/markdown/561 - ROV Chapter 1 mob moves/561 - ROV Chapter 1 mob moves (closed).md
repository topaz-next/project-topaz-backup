**Labels:**

merge ready



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday May 01, 2020 at 07:38:06_
_Originally opened as: project-topaz/topaz - Issue 561_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

If I open a WIP PR, maybe it'll shame me into finishing this chunk of work so it can be merged into canary 👀 

UPDATE: I've filled in the missing moves and the bosses are starting to feel a bit more right. They will at least not sit around like potatoes doing 0 damage all the time. 

It looks like some of the animations are missing/wrong (but nothing is borked), so as work item for me later is to get more caps of these fights so I can fix them.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday May 01, 2020 at 11:48:34_

----

just a heads up: outer parens aren't needed
```lua
if not target isPC() then
```
works


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday May 03, 2020 at 07:50:22_

----

This is what I get for aggressive copy/paste...


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 07:51:32_

----

:spaghetti: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday May 06, 2020 at 10:55:30_

----

Check for Soul Voice here is in the script for Lunatic Voice instead of Entice~ 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday May 06, 2020 at 11:05:35_

----

After merge someone will have to file an issue so we don't forget that this aspect isn't implemented.

We do have damage type immunities, but those are "set and forget" in nature, and the methods involved with making them temporary would be ugly. Will need dedicated effects for them in the future so limited duration can be baked into the initial call.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday May 06, 2020 at 18:17:07_

----

was going to approve this but got confused by changing these values to 0 - does that mean no target? should it be 4 for target enemy for these two entries? apologies if i am missing something!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday May 06, 2020 at 18:32:26_

----

That column corresponds to mob_skill_aoe:
https://github.com/project-topaz/topaz/blob/release/sql/mob_skills.sql#L33

I can't find the enum that describes it, but 0 is single-target:
https://github.com/project-topaz/topaz/blob/4d09173b57dd5867dd3997436fa3ee66eeea0fbb/src/map/mobskill.cpp#L61


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday May 06, 2020 at 18:47:55_

----

ahh just me misreading the sql lines - sorry about that, thought it was mob_valid_target


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday May 01, 2020 at 11:48:34_

----

just a heads up: outer parens aren't needed
```lua
if not target isPC() then
```
works


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday May 03, 2020 at 07:50:22_

----

This is what I get for aggressive copy/paste...


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 07:51:32_

----

:spaghetti: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday May 06, 2020 at 10:55:30_

----

Check for Soul Voice here is in the script for Lunatic Voice instead of Entice~ 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday May 06, 2020 at 11:05:35_

----

After merge someone will have to file an issue so we don't forget that this aspect isn't implemented.

We do have damage type immunities, but those are "set and forget" in nature, and the methods involved with making them temporary would be ugly. Will need dedicated effects for them in the future so limited duration can be baked into the initial call.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday May 06, 2020 at 18:17:07_

----

was going to approve this but got confused by changing these values to 0 - does that mean no target? should it be 4 for target enemy for these two entries? apologies if i am missing something!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday May 06, 2020 at 18:32:26_

----

That column corresponds to mob_skill_aoe:
https://github.com/project-topaz/topaz/blob/release/sql/mob_skills.sql#L33

I can't find the enum that describes it, but 0 is single-target:
https://github.com/project-topaz/topaz/blob/4d09173b57dd5867dd3997436fa3ee66eeea0fbb/src/map/mobskill.cpp#L61


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday May 06, 2020 at 18:47:55_

----

ahh just me misreading the sql lines - sorry about that, thought it was mob_valid_target


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday May 01, 2020 at 14:34:32_

----

omg aweome :D now with this the ROV branch can be merged into canary :+1: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday May 06, 2020 at 11:14:25_

----

Actually, does Siren have a spell list?
