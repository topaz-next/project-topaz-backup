**Labels:**



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 11, 2020 at 17:04:22_
_Originally opened as: project-topaz/topaz - Issue 1327_

----

This branch should live in Canary for _a while_ before going into release.

See #831 for more information, including my previous self-review of the PR.

`fix-elements` branch has been updated to be release-mergable again, including anything referencing elements which I knew was pending back then (open or freshly merged PRs). Hat tip to @Xaver-DaRed for making it so I didn't need to touch synthutils. Don't need to update code referencing elements and weekdays if no such code exists!

I've also browsed through PRs that have landed in release since July looking for things that might reference elements. Most results were resolved during merge conflict resolution, but here's [one perfect example of the power of having your elements be actual elements instead of days of the week](https://github.com/project-topaz/topaz/commit/997e4b6f0366b906f0f9b0692ed04fc3a74dadae).

Not gonna lie: Something is _probably_ broken. I've done my best, but change at this fundamental of a level doesn't come easy. I'll be watching Issue reports.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [ `best of my ability`] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 17:12:41_

----

I had been desperately hoping you would revive this PR, especially because I want it for GEO related shenanigans. I've done a couple of spot-reviews in the past, and one or two now. I'll put this on the top of my review pile so it can get some battle testing in `canary` ⭐ 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Oct 14, 2020 at 04:12:57_

----

I was hoping that the addition in #1355 wouldn't trigger a merge conflict, but here we are!

I'll wait for an approval before changing all the commit hashes on you~


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 16, 2020 at 14:25:40_

----

Looks good, fire away!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Oct 16, 2020 at 14:25:55_

----

Just waiting for the button to turn green!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Oct 16, 2020 at 14:36:25_

----

Alright canary servers, this is a brutal change. But it must be done to correct tons of things at the fundamental level. 💦 

**If you can think of _anything_ in the game that has anything to do with an element, a day of the week, or weather, you should be sure to test if this merge broke it.**

If you're playing on a canary server, encounter something which you suspect might be because of this merge, and want to open an issue, be sure to specify in the PR that it's canary-post-this and tag me.
