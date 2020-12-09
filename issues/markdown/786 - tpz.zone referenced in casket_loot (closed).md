**Labels:**

merge ready



<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ShelbyZ](https://github.com/ShelbyZ)**
_Tuesday Jun 30, 2020 at 20:05:47_
_Originally opened as: project-topaz/topaz - Issue 786_

----

casket_loot.lua should require zone global with its usage of tpz.zone.  I only recently saw this error crop up on a mutli-server setup.  Something must behave differently when running on a single server that the log does not spam errors when loading a zone eligible for caskets.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jun 30, 2020 at 20:12:37_

----

~~is there a specific error message being addressed?~~ due to shenanigans, the zone global is always loaded at all times in all zones - every zone lua and id's lua make sure the table exists and the require is loaded

I phrased that stupidly: whats the error message, is what I mean to ask


----
<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Tuesday Jun 30, 2020 at 20:20:10_

----

![image](https://user-images.githubusercontent.com/1033099/86173057-37c96500-bad4-11ea-87ef-438bfda5590b.png)

This may be related to the split for my setup (298 zones, 1 zone).  If zone global should be available for all lua there is a race condition that code is run before the zone table is available via lua parser


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Jun 30, 2020 at 20:21:00_

----

> the zone global is always loaded at all times in all zones - every zone lua and id's lua make sure the table exists and the require is loaded

That is the `zones` global table, which is different than the `zone.lua` global file. I think the reason that this is happening is that when the zones are loaded, NPCs are loaded, then Mobs, then the actual Zone.lua is checked for init. The zone.lua global is included in the individual Zone.lua files, ~~and because of the order zones are loaded then it's already in memory when it gets to a zone with caskets~~ I have no idea _what_ is loading the zone.lua global, since it appears all npc and mobs and mixins are loaded before any Zone.lua file is accessed. On a split server where the first zone has a the casket zone mixin, that gets loaded before the Zone.lua is loaded which includes the zone.lua global include.




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jun 30, 2020 at 20:29:57_

----

@cocosolos yeah checked it out after getting the error message and its because the caskets lua needed the zone **name** not its table contents, so the require is the simplest fix (it still finds what mixin to look for because it knows where the player is, but theres a set that comes up nil without the require)
