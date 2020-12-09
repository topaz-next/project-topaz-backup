**Labels:**

merge ready



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Sunday Jul 19, 2020 at 00:02:49_
_Originally opened as: project-topaz/topaz - Issue 868_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

* Fix item flags, stack size, jobs, and iLevel<sup>1</sup> to match POL extract.

<sup>1</sup>POL is not currently populating iLevel correctly for some items.  Teo and I dug into this, and have a fix pending [here](https://github.com/Windower/POLUtils/pull/39).  However, the QC for this PR was done against a POL extract that included this fix, so the numbers here should be correct.

