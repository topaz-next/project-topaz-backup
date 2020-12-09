**Labels:**

merge ready



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Jul 02, 2020 at 15:30:37_
_Originally opened as: project-topaz/topaz - Issue 796_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

* remove from scripts/globals, and rewrite in scripts/quests
* make the color data more easily readable
* localVar the variable used in eventUpdate, which removes the need for onEventFinish
* clear the correct charVar on quest completion
* rainbow controlled by localVar on rainbow NPC, which removes need for server variable

update: per feedback,

* ignore weather set by SCH<sup>1</sup>
* use set constructor for color data
* swap order of quest check vs ruby check

<sup>1</sup>Two issues had to be solved here.  First, there wasn't a way to get weather from zone into LUA.  To resolve this, I added a zone:getWeather() binding.  Second, during onZoneIn, the players's zone is not yet set, causing player:getZone() to return null.  To resolve this, I added an optional bool isZoning parameter to player:getZone(), which will instead return the player's destination zone.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 02, 2020 at 15:45:44_

----

thankyouwrenthatscriptnamealwaysbotheredme


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Monday Jul 20, 2020 at 00:04:10_

----

Updated PR per feedback.  Description lists changes.
