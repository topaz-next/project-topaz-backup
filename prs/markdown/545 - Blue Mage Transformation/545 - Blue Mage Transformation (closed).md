**Labels:**

focus

merge ready



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Apr 29, 2020 at 01:08:02_
_Originally opened as: project-topaz/topaz - Issue 545_

----

Currently a WIP. Only thing ready is Lathuya's logic. I need to verify that the order of the quest is correct, also one thing i am having issues is the zone:registerRegion and onZoneIn for it as i just added a testing print to player to make sure that the area is correct and i do not get any feedback.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 03:42:49_

----

We already know Omens is completed here in the eventFinish because we checked for it during the onTrigger 😉

(Will need to break 720 and 721 into different checks to account for one "starting" the quest and the other being the reminder)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 03:51:24_

----

The very _first_ divination for Waoud during Transformations is 720. The hint during the first stage (ie: progress == 1) is event 721.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 04:29:25_

----

Will it be possible to speak to Waoud after Transformations was accepted but _without_ being on stage 2? If not, can eliminate the stage check and only see if it's been accepted.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:01:04_

----

When the Soulflayer_NM skill list is merged, I'll give `blue-mage` a merge from `release`, and then you can use that skill list ID (234) instead


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:01:34_

----

And with skill list ID 234, you wouldn't need to define a new list here~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:05:51_

----

For Immortal Shield, see `effects/magic_shield.lua`. It seems to be used in `abilities/rampart`, `mobskills/mana_screen`, `mobskills/polar_bulwark`, and `mobskills/spectral_barrier`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:29:33_

----

We might able able to fill Immortal Mind out with a volunteer brave enough to eat a bunch of nukes from some soulflayers


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:30:57_

----

You can save two lines by setting msg to be `SKILL_NO_EFFECT` right here when you define it, and then override it down below if dispel > 0.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:31:10_

----

Don't need these outer parens 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:42:58_

----

You can use npcUtil.popFromQM to spawn the soulflayer and lock out the spawn point so that other people can't use the QM to spawn a second soulflayer (and forcibly despawning one that might be up).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:43:57_

----

Without a way to lock out the spawning point, I suspect that malicious players would be able to prevent another player from getting their win 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:47:03_

----

If using popFromQM to spawn the soulflayer, you won't need to check to see if the soulflayer is spawned, because the QM won't be available to interact with~!

I'm also not finding a source that the two CSes leading up to the soulflayer are optional~ 😅 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:47:42_

----

But the script says it's 21~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:50:32_

----

You might want an outer-wrapping if check for all this logic to see if the player is on or has completed Transformations 😉 

Or alternatively: Check if a "remaining AF" is >= 1.

Checking that currentTask isn't 0 might be a good idea too~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 12:12:12_

----

And I think total crafted pieces here would be `3 - countMaskBits(BLUAFremaining)`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 12:15:48_

----

Let's pop a charVar for `[BLUAF]Remaining` here, with a value of 7. Then we can use it as a "reverse mask" that the player will eventually set to 0 (and clear from the db).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 12:18:31_

----

Let's do server admins some favors and standardize the vars to all start with something like `[BLUAF]` so they can be found in one spot

`[BLUAF]Current`, `[BLUAF]Payment`, `[BLUAF]Resting`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 12:29:46_

----

Then after you give the item, you can check if `[BLUAF]Remaining` is 0. If it is, you can delete _all_ BLU AF associated variables (like Resting Day), so there are _zero_ vars leftover when a BLU has finished crafting all their items.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 12:39:51_

----

Shorter alternative:
```lua
if option >= 2 and option <= 9 then
    local updateType = option % 3
    if updateType == 2 then
        -- Choosing a piece
        local piece = 2 ^ math.floor(option / 4)
        -- Make sure the player isn't trying to cheat somehow
        if bit.band(piece, player:getCharVar("[BLUAF]Remaining")) > 0 then
            player:setCharVar("[BLUAF]Current", 2 ^ piece)
            player:updateEvent(0, craftingItems[currentTask][1], craftingItems[currentTask][2], craftingItems[currentTask][3], craftingItems[currentTask][4])
        end
    else
        -- Needs payment
        player:updateEvent(0, craftingItems[currentTask][5], craftingItems[currentTask][6])
    end
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 12:56:20_

----

This is equivalent to checking if  `current task > 1`~

(Ie: No need to count the bits)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 13:01:51_

----

Then `[BLUAF]Available` could be set to `[BLUAF]Available - (2 ^ (currentTask - 1))`

(Or: You wouldn't need a "positive-oriented" list of things you've crafted, because you instead have a "negative-oriented" list of things remaining to _be_ crafted)

This would mean adjusting the final piece to have a key of 3 in your craftingItems table (so all the pieces / tasks line up). I want to say this shouldn't be a problem, as `LathuyaCraftingList_Mask` seems to only be used as a table key (and mask bit manipulation which we're changing), and isn't used for any CS or param offsets (you already calculate those based on the total number of pieces crafted).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 13:11:06_

----

Won't this always result in an 8th param of 3 (same as the Jubbah)?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 13:22:48_

----

Should probably be transformationsProgress == 3 😉 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 04:20:21_

----

didn't we have some weird discussions of what an AF was beforehand that went into a tangent when trying to explain what AF2 was? lol


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 04:31:27_

----

no cause they are not completed in order, if you complete the the 1st and 2nd item then it will result in 7- 1 - 2 = 4
if you complete the 1st and 3rd item then it will be 7 - 1 - 4 =  2
if you complete the 2nd and 3rd it will be 7 - 2 - 4 = 1
then depending on that it will pass the 1st 2nd or 3rd options (sorry i don't make sense explaining here but we can get on a video call and i can explain better)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 04:32:31_

----

i thought the check on eventfinish was needed for prevent cheating (unless i got told wrong before xD)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 09:11:22_

----

Oh, because `craftedPieces` is the pieces crafted, not `totalCraftedPieces`.

I was reading the second line as `currentTask = 7 - totalCraftedPieces`

So nevermind~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 09:12:38_

----

If you want to make the tag `[BLUAF1]`, you'd have my _full_ support~! 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 09:16:20_

----

"it depends"

If the check was done to _start_ the event, then a recheck on eventFinish is redundant (ie: quest progress before firing event). A player can't cheat an event start.

But if the initial startEvent _didn't_ require a certain check, and the check only becomes relevant due to a player's choice during it, then that thing should be checked onFinish before messing with it (ie: gil). A player _can_ cheat an option choice.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 16:27:09_

----

regarding 721 and 720, they are the same cutscene so i didnt add 720.

Removing check with questcompleted as requested.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 16:28:15_

----

both the hint and start of transformations are exactly the same one, this is why i didnt include one of the cutscenes.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 16:30:39_

----

I'm unsure, that would require a volunteer to talk to waoud after each step is completed


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 16:32:37_

----

this will require further testing as you have mentioned these CS are not optional. For example, wiggo's capture only shows the 2nd CS on that area and not the 1st one.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday May 11, 2020 at 06:28:51_

----

It looks like the order is always Caedarva Mire exit -> Mt Zhayolm exit. Currently both of these can be skipped the way char vars are being checked at the QM and NM.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday May 11, 2020 at 06:46:13_

----

Is this being used anywhere?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday May 11, 2020 at 18:49:07_

----

Nope, it _was_ but I guess I accidentally left it in there when reworking it; will remove. Nice eye~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 03:42:49_

----

We already know Omens is completed here in the eventFinish because we checked for it during the onTrigger 😉

(Will need to break 720 and 721 into different checks to account for one "starting" the quest and the other being the reminder)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 03:51:24_

----

The very _first_ divination for Waoud during Transformations is 720. The hint during the first stage (ie: progress == 1) is event 721.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 04:29:25_

----

Will it be possible to speak to Waoud after Transformations was accepted but _without_ being on stage 2? If not, can eliminate the stage check and only see if it's been accepted.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:01:04_

----

When the Soulflayer_NM skill list is merged, I'll give `blue-mage` a merge from `release`, and then you can use that skill list ID (234) instead


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:01:34_

----

And with skill list ID 234, you wouldn't need to define a new list here~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:05:51_

----

For Immortal Shield, see `effects/magic_shield.lua`. It seems to be used in `abilities/rampart`, `mobskills/mana_screen`, `mobskills/polar_bulwark`, and `mobskills/spectral_barrier`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:29:33_

----

We might able able to fill Immortal Mind out with a volunteer brave enough to eat a bunch of nukes from some soulflayers


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:30:57_

----

You can save two lines by setting msg to be `SKILL_NO_EFFECT` right here when you define it, and then override it down below if dispel > 0.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:31:10_

----

Don't need these outer parens 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:42:58_

----

You can use npcUtil.popFromQM to spawn the soulflayer and lock out the spawn point so that other people can't use the QM to spawn a second soulflayer (and forcibly despawning one that might be up).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:43:57_

----

Without a way to lock out the spawning point, I suspect that malicious players would be able to prevent another player from getting their win 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:47:03_

----

If using popFromQM to spawn the soulflayer, you won't need to check to see if the soulflayer is spawned, because the QM won't be available to interact with~!

I'm also not finding a source that the two CSes leading up to the soulflayer are optional~ 😅 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:47:42_

----

But the script says it's 21~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 09:50:32_

----

You might want an outer-wrapping if check for all this logic to see if the player is on or has completed Transformations 😉 

Or alternatively: Check if a "remaining AF" is >= 1.

Checking that currentTask isn't 0 might be a good idea too~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 12:12:12_

----

And I think total crafted pieces here would be `3 - countMaskBits(BLUAFremaining)`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 12:15:48_

----

Let's pop a charVar for `[BLUAF]Remaining` here, with a value of 7. Then we can use it as a "reverse mask" that the player will eventually set to 0 (and clear from the db).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 12:18:31_

----

Let's do server admins some favors and standardize the vars to all start with something like `[BLUAF]` so they can be found in one spot

`[BLUAF]Current`, `[BLUAF]Payment`, `[BLUAF]Resting`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 12:29:46_

----

Then after you give the item, you can check if `[BLUAF]Remaining` is 0. If it is, you can delete _all_ BLU AF associated variables (like Resting Day), so there are _zero_ vars leftover when a BLU has finished crafting all their items.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 12:39:51_

----

Shorter alternative:
```lua
if option >= 2 and option <= 9 then
    local updateType = option % 3
    if updateType == 2 then
        -- Choosing a piece
        local piece = 2 ^ math.floor(option / 4)
        -- Make sure the player isn't trying to cheat somehow
        if bit.band(piece, player:getCharVar("[BLUAF]Remaining")) > 0 then
            player:setCharVar("[BLUAF]Current", 2 ^ piece)
            player:updateEvent(0, craftingItems[currentTask][1], craftingItems[currentTask][2], craftingItems[currentTask][3], craftingItems[currentTask][4])
        end
    else
        -- Needs payment
        player:updateEvent(0, craftingItems[currentTask][5], craftingItems[currentTask][6])
    end
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 12:56:20_

----

This is equivalent to checking if  `current task > 1`~

(Ie: No need to count the bits)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 13:01:51_

----

Then `[BLUAF]Available` could be set to `[BLUAF]Available - (2 ^ (currentTask - 1))`

(Or: You wouldn't need a "positive-oriented" list of things you've crafted, because you instead have a "negative-oriented" list of things remaining to _be_ crafted)

This would mean adjusting the final piece to have a key of 3 in your craftingItems table (so all the pieces / tasks line up). I want to say this shouldn't be a problem, as `LathuyaCraftingList_Mask` seems to only be used as a table key (and mask bit manipulation which we're changing), and isn't used for any CS or param offsets (you already calculate those based on the total number of pieces crafted).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 13:11:06_

----

Won't this always result in an 8th param of 3 (same as the Jubbah)?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 05, 2020 at 13:22:48_

----

Should probably be transformationsProgress == 3 😉 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 04:20:21_

----

didn't we have some weird discussions of what an AF was beforehand that went into a tangent when trying to explain what AF2 was? lol


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 04:31:27_

----

no cause they are not completed in order, if you complete the the 1st and 2nd item then it will result in 7- 1 - 2 = 4
if you complete the 1st and 3rd item then it will be 7 - 1 - 4 =  2
if you complete the 2nd and 3rd it will be 7 - 2 - 4 = 1
then depending on that it will pass the 1st 2nd or 3rd options (sorry i don't make sense explaining here but we can get on a video call and i can explain better)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 04:32:31_

----

i thought the check on eventfinish was needed for prevent cheating (unless i got told wrong before xD)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 09:11:22_

----

Oh, because `craftedPieces` is the pieces crafted, not `totalCraftedPieces`.

I was reading the second line as `currentTask = 7 - totalCraftedPieces`

So nevermind~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 09:12:38_

----

If you want to make the tag `[BLUAF1]`, you'd have my _full_ support~! 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 09:16:20_

----

"it depends"

If the check was done to _start_ the event, then a recheck on eventFinish is redundant (ie: quest progress before firing event). A player can't cheat an event start.

But if the initial startEvent _didn't_ require a certain check, and the check only becomes relevant due to a player's choice during it, then that thing should be checked onFinish before messing with it (ie: gil). A player _can_ cheat an option choice.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 16:27:09_

----

regarding 721 and 720, they are the same cutscene so i didnt add 720.

Removing check with questcompleted as requested.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 16:28:15_

----

both the hint and start of transformations are exactly the same one, this is why i didnt include one of the cutscenes.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 16:30:39_

----

I'm unsure, that would require a volunteer to talk to waoud after each step is completed


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 16:32:37_

----

this will require further testing as you have mentioned these CS are not optional. For example, wiggo's capture only shows the 2nd CS on that area and not the 1st one.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday May 11, 2020 at 06:28:51_

----

It looks like the order is always Caedarva Mire exit -> Mt Zhayolm exit. Currently both of these can be skipped the way char vars are being checked at the QM and NM.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday May 11, 2020 at 06:46:13_

----

Is this being used anywhere?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday May 11, 2020 at 18:49:07_

----

Nope, it _was_ but I guess I accidentally left it in there when reworking it; will remove. Nice eye~!


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Apr 30, 2020 at 18:44:44_

----

I'm done with the quest :cat: 

Only thing missing are:
* 2 mob attacks for the NM that are missing, there were 3 missing attacks before but added one weird one that removes all buffs lol.
* correct location params for onRegionEnter for both optional cutscenes. Since they were options i didn't think it was really a stopped.

Now I'm at the mercy of a review. Please @UynGH @59blargedy remove the WIP tag and change it to ready for review :cat2: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday May 04, 2020 at 17:15:59_

----

You'll have a dedicated skill list ID to use after #584 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 16:35:43_

----

I'm burnt out after writing this quest. Please make the required changes.
Sorry for my candor.
I'll try to focus on small quests from now on.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 18:14:55_

----

Sure thing! Things like this _can_ be pretty grinding.

You're not in this all by yourself~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday May 11, 2020 at 01:41:26_

----

Pushed a commit to flip the "orientation" of the charVars for AF crafting to start at max and go towards zero, making sure all associated vars are gone when the player has crafted all the AF pieces.

And I tested it too! I have made sure that my changes didn't break kain's code and cause this to happen:
![discord](https://user-images.githubusercontent.com/13112942/81516797-af76e100-9328-11ea-80a5-e394eb7664b3.png)


As it's my own code, I'll tag @cocosolos in case they want to look at the most recent commit.

I intend to push another commit later for the other small things (hopefully tomorrow) .


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 12, 2020 at 00:53:40_

----

Pushed a second commit for various fixes and cleanup, including the Undersea regions and CSes. Had to rework Waoud and Whitegate a little after trying them as non-BLU and naked (respectively) caused unexpected behavior.

I set the Soulflayer to use the skill list ID that will be available to it in `release`. This branch is _way_ overdue for a update from `release` (switching to it stills need to deal with non-ignored confs). I'll do that merge after this PR is merged into blue-mage, and I'll uncomment Reprobation then.

I'm okay with merging this without Immortal Shield and Immoral Mind being scripted. We can add those later (after some testing on retail for Immortal Mind). Can potentially hold off on a `blue-mage` -> `canary` merge if those two missing skills are a concern for balance/"earn it" reasons.
