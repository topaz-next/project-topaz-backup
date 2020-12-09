**Labels:**

merge ready



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Jul 01, 2020 at 10:59:50_
_Originally opened as: project-topaz/topaz - Issue 789_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes #667 
Relates to #682 

This PR fixes the remaining issues with quest "Flyers for Regine" and neatens the code.

* When approaching tradable NPCs, you now receive a message "So-and-so looks over curiously for a moment."
* The "looks over curiously" messages are now found by offsets from a base message.
* The after-trading dialog from each NPC is now prefixed with their name.
* Trade progress is now tracked with a single bitmask rather than 15 vars.
* Code for defining approach regions and trading flyers is now contained in scripts/quests/flyers_for_regine



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 12:31:14_

----

I know this was always here, but do we happen to know if the pre-quest CS only happens once _ever_, or just once per zone?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 12:39:28_

----

It might be possible to reduce the number of loops by taking advantage of how every zone always has 5. You'd need a _tiny_ bridge table linking a zone ID to an offset, but once you have it:
```lua
-- pseudo
local zone_offsets = {
  [tpz.zone.PORT_SAN_DORIA] = 0,
  [tpz.zone.NORTHERN_SAN_DORIA] = 1,
}

quests.flyers_for_regine.initZone = function(zone)
local offset = ffr.zoneOffset[zone_id]
for i = offset, offset + 5 do
  local npc = npcData[i]
  registerRegion(npc.region, npc.x)
```

Although it'd only save _just a few_ cycles, so it's up to you.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 12:40:33_

----

regionEnter checks could then use the offsets too, so you're only checking up to 5 regions per check, as opposed to potentially up to 15.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Jul 11, 2020 at 16:40:33_

----

I'm working off a video -- no retail access -- so can't answer this off the top of my head.  I added this question to an already-open Flyers for Regine question I have in the FFXICaptures discord.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Jul 11, 2020 at 16:42:44_

----

I'd like to leave this PR as is for now.  However, I'm going to revisit FFR once I have answers to questions in Captures discord.  When I do the next (last?) FFR PR, I'll include this change too.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 17:05:05_

----

Sounds good - I guess I jumped the gun when coming up with a target branch name for this. 😅 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 15, 2020 at 15:39:14_

----

who knew Regine was a one winged angel? ¯\\_(ツ)\_\/¯


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 12:31:14_

----

I know this was always here, but do we happen to know if the pre-quest CS only happens once _ever_, or just once per zone?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 12:39:28_

----

It might be possible to reduce the number of loops by taking advantage of how every zone always has 5. You'd need a _tiny_ bridge table linking a zone ID to an offset, but once you have it:
```lua
-- pseudo
local zone_offsets = {
  [tpz.zone.PORT_SAN_DORIA] = 0,
  [tpz.zone.NORTHERN_SAN_DORIA] = 1,
}

quests.flyers_for_regine.initZone = function(zone)
local offset = ffr.zoneOffset[zone_id]
for i = offset, offset + 5 do
  local npc = npcData[i]
  registerRegion(npc.region, npc.x)
```

Although it'd only save _just a few_ cycles, so it's up to you.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 12:40:33_

----

regionEnter checks could then use the offsets too, so you're only checking up to 5 regions per check, as opposed to potentially up to 15.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Jul 11, 2020 at 16:40:33_

----

I'm working off a video -- no retail access -- so can't answer this off the top of my head.  I added this question to an already-open Flyers for Regine question I have in the FFXICaptures discord.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Jul 11, 2020 at 16:42:44_

----

I'd like to leave this PR as is for now.  However, I'm going to revisit FFR once I have answers to questions in Captures discord.  When I do the next (last?) FFR PR, I'll include this change too.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 17:05:05_

----

Sounds good - I guess I jumped the gun when coming up with a target branch name for this. 😅 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 15, 2020 at 15:39:14_

----

who knew Regine was a one winged angel? ¯\\_(ツ)\_\/¯
