**Labels:**

crafting



<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [neuromancerxi](https://github.com/neuromancerxi)**
_Thursday Sep 17, 2020 at 05:31:23_
_Originally opened as: project-topaz/topaz - Issue 1147_

----

Adds a check in lua_baseentity to check signature of traded item.
General crafting.lua cleanup
Logic clean-up in Guildmaster scripts
	- Uses actual skill level instead of a generic value of 100
	- Compares against cap for rank instead of arbitrary value
	- Now presents Artisan specific text during test/rank up due to proper values
	- Wires up checks for Expert "quests" for each guild
	- Wires up checks for Guildpoint Key Item
	- Wires up trade check for Rank + Quest active + Guild Key Item + Signed Test item
	- Wires up fail condition for trading unsigned item for Expert test.

Tested all 10 Guild NPCs:
	- Each rank at set intervals (8, 18, 28, etc) for test and rank up
	- Tested failures with unsigned Expert Rank item
	- Tested arbitary signed and unsigned items at various stages

What doesn't work (TODO)
	- The cut scene when you have met the conditions to craft the expert test (Quest Flagged + KI)
	- The CS hangs the client when it gets to (presumably) presenting the recipe to the client
	- As a stand in, I've attached the raw text for each event so the player can get the important details
		- Needs to be signed, name of the craft, ec.

With only one item outstanding I didn't want to hold back the rest of this PR since the rest is fully functional.

Thanks to DHoffryn of Nocturnal Souls for his assistance with the cpp bits.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Sep 17, 2020 at 15:51:08_

----

> 
> So first off, this is formatted beautifully. Real nice.
> 
> What would you think about replacing `signedByTrader` in `lua_baseentity` with `getSignature` inside `lua_item`, and then doing the string comparison back up in the lua? Seems like a saner binding to me.
> 
> I'd like someone to weigh in on this:
> 
> ```
>         --[[  Feeding the proper parameter currently hangs the client in cutscene. This may
>               possibly be due to an unimplemented packet or function (display recipe?) Work
>               around to present dialog to player to let them know the trade is ready to be
>               received by triggering with lower rank up parameters.  ]]--
> ```
> 
> I don't really know how best to deal with it.

We're gonna need a retail cap to check out I think. @zach2good 

Edit: and I agree about `getSignature()`


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Sep 18, 2020 at 06:48:36_

----

I've made that binding for you here: https://github.com/project-topaz/topaz/pull/1153
It should make it into `release` fairly soon. You'll then need to update the instances of `local signed = player:signedByTrader(player,0)` with:
```lua
-- find the item in the trade (or for all items in trade)
local signed = item:getSignature() == player:getName() and 1 or 0
-- remember that Lua true is 0, so "and 1 or 0" converts it to true = 1, false = 0
-- or change your logic later in the function, whichever you prefer
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 19, 2020 at 10:17:51_

----

You're almost there, you want to be using `player:setLocalVar` instead of `player:setCharVar`! CharVars end up in the database and you don't need that here :)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 19, 2020 at 12:05:04_

----

I want to get this in for testing so I'm going to merge this into it's own feature branch and then do those changes myself since they're so small and quick. Thanks for the wonderful contribution! :)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 19, 2020 at 12:19:17_

----

So, I had a quick look to see if I could upgrade parts of this to use LocalVars. I don't fully understand what's meant to be going on with these tracking vars.

**Using Reinberta (Goldsmithing) as an example:**
Is your intent after these quests to leave `GoldsmithingExpertQuest` as 2 forever? Is there a quest that could be completed instead?

The `player:setCharVar("GoldsmithingTraded",1)` logic is OK, it just needs to be a LocalVar so it doesn't live forever if the player somehow bails out in the middle of the CS.

Any further changes now need to be pointed at `feature/crafting_expert_lb`, once they're done I can do a midweek merge into `canary` 👍 

