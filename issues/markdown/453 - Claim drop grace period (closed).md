**Labels:**

merge ready



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Tuesday Mar 31, 2020 at 03:52:25_
_Originally opened as: project-topaz/topaz - Issue 453_

----

This adds a short grace period before claim drops and also fixes an issue were rewards are not distributed when proper claim isn't achieved before death. This still isn't 100% as there are some situations where claim does drop instantly, needs more retail testing. Also moved the call to RelinquishClaim from OnDisengage to OnChangeTarget.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


