**Labels:**

good first issue



<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Thursday Oct 29, 2020 at 12:02:49_
_Originally opened as: project-topaz/topaz - Issue 1452_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Synthesis should fail when players receive damage during combat. Currently it does not affect the outcome of the synth. Evaded attacks should not have an effect on synthesis outcome.

Opened issue per Zach.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 29, 2020 at 12:06:18_

----

I've done about 90s of research, I don't think we have a mechanism for marking items as "un-losable" in a failed synth. If we call doSynthFail (like we do when we're detecting abuse) things like Lu Shangs Rod can be lost - which is not correct in this case.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 31, 2020 at 14:36:46_

----

I don't remember who said it, but we had a vague confirmation that you lose **all** items if you're hit (just like if you force a zone during synth).

I'm happy to shift the "responsibility" of this onto server operators. If a player loses their expensive mats or their "unlosable" items in a synth they were attempting in the middle of a fight: they can explain to their local GM why they deserve their items back 🤡 
