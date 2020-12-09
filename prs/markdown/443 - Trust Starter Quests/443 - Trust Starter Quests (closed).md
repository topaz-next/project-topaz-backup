**Labels:**

focus

merge ready

reviewed



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday Mar 27, 2020 at 08:25:25_
_Originally opened as: project-topaz/topaz - Issue 443_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

I can't take credit for the layout of the `TrustMemory` or the rank params, that was all @Safhaven!

- Adding the required text ID's
- Tracking casting of trusts in the required zones
- Cipher trading
- Starter quests
- Further trust CS's for all nations

**Tested:**
Windy
Sandy->Windy->Bastok



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Mar 31, 2020 at 23:36:11_

----

Can we put this up higher near the other content/char based settings (caskets, books, outpost warps) ?

Maybe right beneath outposts before the shop section.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 00:36:19_

----

I don't suppose if we know it _has_ to be those two zones, do we?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 00:37:54_

----

Thoughts on maybe having an enum table for trust spell IDs? We're currently using them for the duplicate trust checks, and they'll be used for the onSpawn messages too.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 00:44:41_

----

[`npcutil.completeQuest` can take tables for keyItems and titles to give _and_ take a list of vars to erase~!](https://github.com/project-topaz/topaz/blob/release/scripts/globals/npc_util.lua#L322-L334)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 00:45:29_

----

Got a couple extra spaces here


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 00:46:45_

----

Mission IDs are tabled now~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 00:56:30_

----

A call to `player:getNation()` might simplify these~! 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 01:01:57_

----

I worry that a player won't be able to progress in missions involving Kupipi if they flag the trust quest and then don't go out and summon her.

But these NPCs are a nightmare, and doing the event priority "properly" with the current system would make tracking her associated quests/missions more difficult, so I'm willing to overlook this and say the player should just go and summon her real quick.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 01:08:59_

----

Lua is case-sensitive, and would be upset with `rank3` (unless you want to change `Rank3` to lowercase).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 02:40:52_

----

Tabs!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 02:43:02_

----

This line will need the settings check too;

Might be easiest to wrap the whole thing in a `if ENABLED and lvl >= 5 then` block.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 02:45:13_

----

I can tell it's stubbed, but what might the fameModifier be for?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 02:45:30_

----

More tabs!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 03:28:36_

----

To mark as a TODO: This event will point in the player in the direction of other nation-based trusts they can find (that the player qualifies for). It will probably need either params or an event update (I captured this with an ancient version of EventView which didn't display updates, so would need to check the PV logs).


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 01, 2020 at 07:26:17_

----

All of the first-trust quests name drop the two nearest starter zones, and I think the reminder text also tells you to go there. Also, all of the wikis mention it, but that's not such concrete data. I didn't test on retail to see if it HAS to be those zones, or if summoning anywhere will work. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 01, 2020 at 07:27:03_

----

Yeah, at this point there's going to be 3 places that'll need them, so it may as well happen 🤷‍♂ 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 01, 2020 at 07:28:52_

----

I did try that, but I wasn't getting the keyItem text:
 `npcUtil.completeQuest(player, BASTOK, tpz.quest.id.bastok.TRUST_BASTOK, { ki = tpz.ki.BASTOK_TRUST_PERMIT, var="BastokFirstTrust"}) `


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 01, 2020 at 14:49:16_

----

_cries in 'explained this to past authors' again_

subid on the item. then one call to get the subid instead of maintaining big old enums in multiple places. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 01, 2020 at 18:35:56_

----

@ibm2431 wishlist item: Teo wants script hooks _for players_ instead of just mobs. so we can stuff global player related things into player.lua in an appropriately named function. We have no hooks for players right now, just binding for on level up/down, zonage/login, and charCreation.

This here for trusts are better off in the spell script I think, but it reminded me. figured I better say something before I forget.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 01, 2020 at 19:06:05_

----

There a few different texts, depending on who you trade in. I'll take it out for now because they'll require a lot more mapping to get right.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 02, 2020 at 00:46:26_

----

Retail will trip the trust dialog and then you can click her again for mission dialog, or vice versa. I forget which was first (sorry!) but it didn't lock me out entirely. I just had to click her twice.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Apr 02, 2020 at 07:04:11_

----

Sounds to me like a job for `localVar`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 02, 2020 at 10:49:11_

----

My comment was originally me asking if that was what they were for, but then thought, "That would be incredibly silly, because the trust ID is one of the params - surely those varying lines are tied to that param! _Obviously_ it's for something else, right?"

Yet here we are. Silly SE.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 02, 2020 at 21:22:03_

----

For npcUtil.completeQuest, field name for KI needs to be `keyItem` for it to work


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 02, 2020 at 21:24:16_

----

Maybe set this to 0 until the memories are implemented so people don't get confused~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 02, 2020 at 21:29:30_

----

Line's a _little_ lengthy if you want to throw a break in


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 02, 2020 at 21:39:59_

----

I realize I originally pointed out `getNation()` when I saw the individual checks before, but a thought just occurred: `getRank` returns the player's current nation by default.

And upon checking, it apparently _can't_ give rank for a specific nation. [It was suggested to be added in the comments, but never was](https://github.com/project-topaz/topaz/blob/release/src/map/lua/lua_baseentity.cpp#L6003-L6016).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 02, 2020 at 21:46:50_

----

Now that `lvl` is only being used once (since the ifs were reformed), you can probably just grab the player's level during the `if` 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Apr 03, 2020 at 22:47:06_

----

Wetata dodged your content tag


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Apr 04, 2020 at 06:22:42_

----

Sneaky sneaky


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Mar 31, 2020 at 23:36:11_

----

Can we put this up higher near the other content/char based settings (caskets, books, outpost warps) ?

Maybe right beneath outposts before the shop section.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 00:36:19_

----

I don't suppose if we know it _has_ to be those two zones, do we?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 00:37:54_

----

Thoughts on maybe having an enum table for trust spell IDs? We're currently using them for the duplicate trust checks, and they'll be used for the onSpawn messages too.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 00:44:41_

----

[`npcutil.completeQuest` can take tables for keyItems and titles to give _and_ take a list of vars to erase~!](https://github.com/project-topaz/topaz/blob/release/scripts/globals/npc_util.lua#L322-L334)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 00:45:29_

----

Got a couple extra spaces here


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 00:46:45_

----

Mission IDs are tabled now~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 00:56:30_

----

A call to `player:getNation()` might simplify these~! 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 01:01:57_

----

I worry that a player won't be able to progress in missions involving Kupipi if they flag the trust quest and then don't go out and summon her.

But these NPCs are a nightmare, and doing the event priority "properly" with the current system would make tracking her associated quests/missions more difficult, so I'm willing to overlook this and say the player should just go and summon her real quick.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 01:08:59_

----

Lua is case-sensitive, and would be upset with `rank3` (unless you want to change `Rank3` to lowercase).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 02:40:52_

----

Tabs!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 02:43:02_

----

This line will need the settings check too;

Might be easiest to wrap the whole thing in a `if ENABLED and lvl >= 5 then` block.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 02:45:13_

----

I can tell it's stubbed, but what might the fameModifier be for?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 02:45:30_

----

More tabs!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 01, 2020 at 03:28:36_

----

To mark as a TODO: This event will point in the player in the direction of other nation-based trusts they can find (that the player qualifies for). It will probably need either params or an event update (I captured this with an ancient version of EventView which didn't display updates, so would need to check the PV logs).


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 01, 2020 at 07:26:17_

----

All of the first-trust quests name drop the two nearest starter zones, and I think the reminder text also tells you to go there. Also, all of the wikis mention it, but that's not such concrete data. I didn't test on retail to see if it HAS to be those zones, or if summoning anywhere will work. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 01, 2020 at 07:27:03_

----

Yeah, at this point there's going to be 3 places that'll need them, so it may as well happen 🤷‍♂ 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 01, 2020 at 07:28:52_

----

I did try that, but I wasn't getting the keyItem text:
 `npcUtil.completeQuest(player, BASTOK, tpz.quest.id.bastok.TRUST_BASTOK, { ki = tpz.ki.BASTOK_TRUST_PERMIT, var="BastokFirstTrust"}) `


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 01, 2020 at 14:49:16_

----

_cries in 'explained this to past authors' again_

subid on the item. then one call to get the subid instead of maintaining big old enums in multiple places. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 01, 2020 at 18:35:56_

----

@ibm2431 wishlist item: Teo wants script hooks _for players_ instead of just mobs. so we can stuff global player related things into player.lua in an appropriately named function. We have no hooks for players right now, just binding for on level up/down, zonage/login, and charCreation.

This here for trusts are better off in the spell script I think, but it reminded me. figured I better say something before I forget.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 01, 2020 at 19:06:05_

----

There a few different texts, depending on who you trade in. I'll take it out for now because they'll require a lot more mapping to get right.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 02, 2020 at 00:46:26_

----

Retail will trip the trust dialog and then you can click her again for mission dialog, or vice versa. I forget which was first (sorry!) but it didn't lock me out entirely. I just had to click her twice.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Apr 02, 2020 at 07:04:11_

----

Sounds to me like a job for `localVar`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 02, 2020 at 10:49:11_

----

My comment was originally me asking if that was what they were for, but then thought, "That would be incredibly silly, because the trust ID is one of the params - surely those varying lines are tied to that param! _Obviously_ it's for something else, right?"

Yet here we are. Silly SE.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 02, 2020 at 21:22:03_

----

For npcUtil.completeQuest, field name for KI needs to be `keyItem` for it to work


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 02, 2020 at 21:24:16_

----

Maybe set this to 0 until the memories are implemented so people don't get confused~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 02, 2020 at 21:29:30_

----

Line's a _little_ lengthy if you want to throw a break in


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 02, 2020 at 21:39:59_

----

I realize I originally pointed out `getNation()` when I saw the individual checks before, but a thought just occurred: `getRank` returns the player's current nation by default.

And upon checking, it apparently _can't_ give rank for a specific nation. [It was suggested to be added in the comments, but never was](https://github.com/project-topaz/topaz/blob/release/src/map/lua/lua_baseentity.cpp#L6003-L6016).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 02, 2020 at 21:46:50_

----

Now that `lvl` is only being used once (since the ifs were reformed), you can probably just grab the player's level during the `if` 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Apr 03, 2020 at 22:47:06_

----

Wetata dodged your content tag


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Apr 04, 2020 at 06:22:42_

----

Sneaky sneaky
