**Labels:**

approved

reviewed



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Sep 22, 2020 at 01:19:26_
_Originally opened as: project-topaz/topaz - Issue 1176_

----

The value for `miniQuestForORB_CS` needs to be set conditionally to prevent being issued again while already on the quest. Not doing so resets the variable on characters that are already on the quest and touch the wall of banishing, ultimately messing up the NPC trigger (will trigger the quest anew and hand out a new white orb).

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Sep 22, 2020 at 07:58:59_

----

Congrats on your first PR! Looks pretty good and sane 👍 
