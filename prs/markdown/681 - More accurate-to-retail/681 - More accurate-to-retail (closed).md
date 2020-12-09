**Labels:**

merge ready



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Jun 03, 2020 at 23:18:13_
_Originally opened as: project-topaz/topaz - Issue 681_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Big thanks to Nyu for running around all these zones and noting aern jobs and their pets.

This is the document we used to identify retail aerns and compare to Topaz aerns:
https://docs.google.com/spreadsheets/d/1miQYoxtuk20sjWEKB-u97q1Fcvg6l55fjN_LQgnjHTQ/edit#gid=0

This PR includes:

* Refactor aern pools.  Combined Eo and Aw to "Indoor_aern" pools.  Ul, Om, and Il'aerns have different flags, so they all get their own pools.
* Make sure every Ul, Om, Eo, Aw, and Il'aern in topaz has a job that matches retail.
* Make sure pets are retail-accurate for all pet-having aerns.
* Fix Ru'aern jobs, flags, animationsub from retail capture. (Garden of Antiquity mission)


