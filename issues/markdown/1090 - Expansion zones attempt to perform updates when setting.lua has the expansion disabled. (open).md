**Labels:**

good first issue

improvement



<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Wednesday Sep 09, 2020 at 23:57:10_
_Originally opened as: project-topaz/topaz - Issue 1090_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

When loading topaz_game with settings described above, the server reports hundreds of errors as it attempts to implement each survival guide in the world. 

Not all of them, but you get the idea:
![image](https://user-images.githubusercontent.com/35855037/92665808-b99ff080-f2c4-11ea-9cc0-3dca3c000ba5.png)

The guides appear in-game, but when interacting with them, nothing happens on the client end, however, the server reports an additional error:
![image](https://user-images.githubusercontent.com/35855037/92666011-4f3b8000-f2c5-11ea-8e92-9dc8ccd6ecfb.png)


TO REPRODUCE:

in Settings.lua, set the following:
`ENABLE_COP = 0`
...
`RESTRICT_CONTENT = 1`
Launch server

Expected behavior:
Survival guides should either not appear entirely (if they are properly categorized as part of COP), or appear and be functional. (preferably with an additional setting to disable them separately)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Sep 10, 2020 at 00:07:05_

----

It could be possible to disable manuals with a flag... I can't claim to be an expert, however I would suggest that it seems pretty difficult to imagine turning off COP and leaving all the later stuff on. Content from later expansions would expect and *rely* on NPCs and content from the earlier ones at least "existing". This appears, in fact, to be what is happening here. 


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Thursday Sep 10, 2020 at 00:11:17_

----

The same error occurs with all expansions turned off, so it's not something in the later expansions that are expecting the guides to exist, and the guides are even failing to load in vanilla zones, so the problem is deeper than that.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Sep 10, 2020 at 00:23:54_

----

survival_guide.lua references `tpz.teleport` but doesnt require teleports.lua. My guess is that teleports.lua is loaded by some zone/npc that is flagged as a certain expansion, and if it is blocked from loading, survival_guide.lua can't take advantage of that load and fails to load, then the chain reaction.

tldr; `require("scripts/globals/teleports")`


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Sep 10, 2020 at 00:31:12_

----

Indeed. Adding that require fixes some of the errors, but there are still other files with errors due to missing require statements as well when all expansions are disabled.


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Thursday Sep 10, 2020 at 00:42:36_

----

Thanks guides are now functioning with COP off. I'll set up a pull request for the guides, and start bughunting on the others.


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Thursday Sep 10, 2020 at 02:25:01_

----

Would it be too kludgey to just put if statements to check the settings lua for ENABLE_COP = 1 before the lines that are throwing errors in the other scripts?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Sep 10, 2020 at 03:13:23_

----

What other errors are you getting?


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Thursday Sep 10, 2020 at 03:16:50_

----

Errors on attempting to update unloaded Promathia zone onInitialize, onZoneWeatherChange and onGameHour etc.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Sep 10, 2020 at 03:17:29_

----

What errors specifically though? If they're missing requires in global files then that has nothing to do with enabling expansions.


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Thursday Sep 10, 2020 at 03:19:29_

----

For them, it's more than missing globals, (except for a check to the settings global to check whether the zone is disabled) The zones are attempting to update different things which are disabled when their expansion is disabled and "RESTRICT_CONTENT" is on.


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Sunday Sep 13, 2020 at 22:11:58_

----

So I'm glad to see that the survival guide fix got pulled in, As for the other errors, would it be better if the entire zone were not loaded at all, and if so, where in the code would I find the startup sequence for the map server?

Disabling the zone actions via if statements in the LUAs of each zone works, but it's not particularly clean, or efficient.


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Sunday Sep 13, 2020 at 22:23:45_

----

Remaining errors related to disabling expansions:

onGameHour:
`luautils::onGameHour: .\scripts/zones/Misareaux_Coast/globals.lua:17: attempt to index a nil value`
`luautils::onGameHour: .\scripts/zones/Misareaux_Coast/globals.lua:22: attempt to index local 'random' (a nil value)`
`luautils::onGameHour: .\scripts/zones/Misareaux_Coast/globals.lua:30: attempt to index a nil value`
`luautils::onGameHour: scripts/zones/The_Garden_of_RuHmet/Zone.lua:109: attempt to index local 'qm2' (a nil value)`
`luautils::onGameHour: scripts/zones/The_Garden_of_RuHmet/Zone.lua:100: attempt to index local 'qm3' (a nil value)`

OnGameDay:
`luautils::OnZoneWeatherChange: scripts/zones/Uleguerand_Range/Zone.lua:59: attempt to index local 'waterfall' (a nil value)`
`luautils::onGameDay: scripts/zones/Sacrarium/Zone.lua:56: attempt to index a nil value`

OnZoneWeatherChange:
`OnZoneWeatherChange: scripts/zones/Uleguerand_Range/Zone.lua:59: attempt to index local 'waterfall' (a nil value)`
`OnZoneWeatherChange: scripts/zones/Grauberg_[S]/Zone.lua:32: attempt to index local 'npc' (a nil value)`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Sep 13, 2020 at 23:58:16_

----


> So I'm glad to see that the survival guide fix got pulled in, As for the other errors, would it be better if the entire zone were not loaded at all, and if so, where in the code would I find the startup sequence for the map server?
> 
> Disabling the zone actions via if statements in the LUAs of each zone works, but it's not particularly clean, or efficient.

I think making the zone itself not exist will be more trouble than it is worth. Even if we did that, there are bound to be some NPC's within the zone that are form a different expansion anyway, which was the whole reason the settings were created: it was deemed confusing to see newer NPCs in old zones on "classic" or "oldschool" servers, so people wanted them hidden away.

And that was the original intent btw, to HIDE these NPCs, not erase them from existence. The fact they effectively don't exist is why they are nil and I don't think that was worth the small amount of memory saved. If they were just hidden we'd just need to make sure we don't mistakenly auto spawn them later.

For now, as much as I don't like using a bunch of if's to check expansions, I could maybe accept that for things like the above weather and time conditions.. I have to stress I really do not want tons of "if expansion enabled then" laying all over the project those were meant to prevent access at the starting entry point(s) to the expansion and not used at every step of related code.


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Monday Sep 14, 2020 at 01:10:22_

----

You're likely right. It is a good thing that these checks aren't run every tick, so doing 1/2 dozen if checks every minute or so isn't going to cause slowdown. I'll post the changed files in a pull request for review shortly.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Sep 14, 2020 at 02:27:47_

----

it occurs to me that servers that don't allow these zones/expansions/npc's should just be setting that zones [port ](https://github.com/project-topaz/topaz/blob/release/sql/zone_settings.sql#L29)to zero.
