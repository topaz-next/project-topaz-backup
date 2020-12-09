**Labels:**



<a href="https://github.com/claywar"><img src="https://avatars1.githubusercontent.com/u/12447174?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [claywar](https://github.com/claywar)**
_Wednesday Nov 25, 2020 at 02:36:06_
_Originally opened as: project-topaz/topaz - Issue 1529_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This fix hard-codes mastery rank as 1, and resolves issue with 0x63 status update packet sending incorrect gladiator rank.  As a result, the rank is also set to 0 (Gla).  Several references are added in comments from retail, but appear to have no impact on stability.

Job Info packet has increased in size by two bytes, which has resolved the profile crash, along with the above change.  



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Nov 25, 2020 at 07:31:18_

----

RE the "hacks", I'm fine with that, we don't have that content programmed anyway and there is a note for future readers 👍 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Nov 26, 2020 at 06:46:44_

----

`9 commits` 👀

Content looks fine, I'll just squash these 😆 
