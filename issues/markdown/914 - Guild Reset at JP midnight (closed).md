**Labels:**

crafting

hold



<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [jarmengaud](https://github.com/jarmengaud)**
_Friday Jul 31, 2020 at 16:23:02_
_Originally opened as: project-topaz/topaz - Issue 914_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

(this is @ Tokenr on Discord, btw!)

Should solve:
Fixes https://github.com/project-topaz/topaz/issues/750
Fixes https://github.com/project-topaz/topaz/issues/875
and the first item of:
https://github.com/project-topaz/topaz/issues/22

The way the guild rank items are set up, the reset must happen on JP midnight, independant on server timezone.



----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Jul 31, 2020 at 16:34:59_

----

Looks good to me. If you want to add "Fixes" in front of the 2 issues mentioned in your description, GitHub will automatically close them when this merges. :)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Jul 31, 2020 at 16:43:28_

----

Also, if I'm not mistaken I think the offset feature was removed due to "doing nothing" when the vanadiel epoch feature was implemented, so perhaps #22 could be marked Fixes as well.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Sep 28, 2020 at 16:25:23_

----

Just so I and others don't forget, I mentioned to @jarmengaud on Discord that I've already written system-timezone-agnostic JST timekeeping functions, as my upcoming RoE Phase 3 work relies on correct JST time for doing daily/timed record scheduling. I will try to find time to clean up and PR that code separately so he can use it. Should make this fix as easy as moving 1 line of code from local midnight block to the new JST midnight one. (Or if we want, ditch the whole local midnight block entirely)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Tuesday Sep 29, 2020 at 16:52:12_

----

Superseded by #1215
