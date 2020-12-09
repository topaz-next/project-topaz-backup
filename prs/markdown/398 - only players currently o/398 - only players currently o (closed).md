**Labels:**

merge ready



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Feb 27, 2020 at 21:31:17_
_Originally opened as: project-topaz/topaz - Issue 398_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes #371 


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 27, 2020 at 21:54:50_

----

mind if we change this to a local var same as the torch ID, if you logout with out touchng you would lose the torch refrence anyway. this particular var check on this line really isnt needed though since we have the other 2 checks.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Feb 27, 2020 at 22:01:16_

----

if you get DC'd do you have to repeat the fight though?


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 27, 2020 at 22:09:41_

----

Would have to anyway becuase it's also checking a local var vet on the torch on popping it and retrieving 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Feb 27, 2020 at 22:31:40_

----

I mean: whats retail do.

just..we're here anyway. ¯\\\_(ツ)\_/¯


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Friday Feb 28, 2020 at 02:07:12_

----

Agree that we should mimic retail.  If someone with access can tell me how it works there, I can code to match.

Until then, how about this new commit?  This saves the torch used to spawn the crediting Spark to each player on the quest who helps kill it.  This way, the particular torch will persist per-player across logouts, or if someone else comes and kills a different Dark Spark before original player has a chance to touch the torch.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 27, 2020 at 21:54:50_

----

mind if we change this to a local var same as the torch ID, if you logout with out touchng you would lose the torch refrence anyway. this particular var check on this line really isnt needed though since we have the other 2 checks.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Feb 27, 2020 at 22:01:16_

----

if you get DC'd do you have to repeat the fight though?


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 27, 2020 at 22:09:41_

----

Would have to anyway becuase it's also checking a local var vet on the torch on popping it and retrieving 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Feb 27, 2020 at 22:31:40_

----

I mean: whats retail do.

just..we're here anyway. ¯\\\_(ツ)\_/¯


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Friday Feb 28, 2020 at 02:07:12_

----

Agree that we should mimic retail.  If someone with access can tell me how it works there, I can code to match.

Until then, how about this new commit?  This saves the torch used to spawn the crediting Spark to each player on the quest who helps kill it.  This way, the particular torch will persist per-player across logouts, or if someone else comes and kills a different Dark Spark before original player has a chance to touch the torch.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Sunday Mar 01, 2020 at 00:57:37_

----

Nyu tested this on retail.  Turns out it doesn't matter which torch is clicked: any of them will give the reward after Dark Spark is killed.  Also, if you kill Dark Spark, then log out and back in, then click a torch, you will be rewarded.

I have updated the PR to match retail testing.
