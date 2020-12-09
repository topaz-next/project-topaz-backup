**Labels:**

WIP



<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Thursday Sep 10, 2020 at 01:08:13_
_Originally opened as: project-topaz/topaz - Issue 1091_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Sep 10, 2020 at 01:50:51_

----

Welcome @Dirk-Dieters ! Thanks for PRing this fix.

If possible, I'd like if we please hold this PR as work-in-progress until the remaining errors/requires are remedied so that we can have a single complete fix. :) Would you be willing to add the necessary commits to your branch, and thus this PR, to facilitate that?


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Thursday Sep 10, 2020 at 01:58:00_

----

Perfectly reasonable, I'll take care of that as soon as I can.


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Thursday Sep 10, 2020 at 04:35:27_

----

All load errors are now fixed in my fork. Summary of changes:
Added require line to survival_guide.lua
Added checks for all failing load attempts for disabled expansion zones


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Sep 10, 2020 at 18:14:04_

----

I'm not sure selectively putting ifs around so many pieces of disparate code is the right approach to solving a problem like this; Yes, the startup errors went away but I feel there's unintended collateral damage here. For one, it still leaves stub functions which do nothing and that could be affecting other functions elsewhere which rely on them without anyone knowing until the script tries to run.

If there are certain script files which are **confirmed** to contain _no viable code_ when a certain expansion is disabled and can be safely ignored then perhaps they can either be removed from the startup, or a single `if` could be used to return immediately and not execute the rest of the file.

It also appears that some files are being inadvertently removed (.gitignore)


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Thursday Sep 10, 2020 at 23:43:55_

----

I agree, the kludge is strong. I'll keep testing and watching for any aberrant behavior. 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Sep 11, 2020 at 00:25:09_

----

Instead of touching promyvion.lua, you should just check if COP is enabled in the promyvion Zone.lua files where they call the promyvion init function.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Sep 11, 2020 at 02:42:26_

----

If an expansion isn't enabled, the zone shouldn't be loaded at all.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Sep 13, 2020 at 04:57:38_

----

> If an expansion isn't enabled, the zone shouldn't be loaded at all.

I almost agreed with this but it creates other problems I don't want to deal with. I need zones to exist unless I explicitly disable them in my zone_settings table.


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Sunday Sep 13, 2020 at 17:25:25_

----

I'm going to start fresh and try again.
