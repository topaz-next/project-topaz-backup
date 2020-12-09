**Labels:**

approved

reviewed



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Aug 20, 2020 at 16:56:23_
_Originally opened as: project-topaz/topaz - Issue 987_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This setting was used in the core for nothing other than being exposed to LUA via checkFovAllianceAllowed binding.

This PR:

* moves the setting into scripts/globals/settings.lua
* makes the setting affect both RoV and GoV.  Requested by Lusiphur.  I can split this into two settings if desired.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 20, 2020 at 17:35:33_

----

> makes the setting affect both RoV and GoV. Requested by Lusiphur. I can split this into two settings if desired.

Unfortunately retail does alliance normally on GoV but not FoV, so a combined setting would give one of them wrong default behavior. Some of the most fun I ever had on retail was mass destroying Bostaunieux Oubliette in an alliance. We had multiple runners go agro half the zone while out 3 sync taru stood near the book. Fun times.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Aug 20, 2020 at 17:46:02_

----

Okay, split into two settings, and default them to GOV: true and FOV: false
