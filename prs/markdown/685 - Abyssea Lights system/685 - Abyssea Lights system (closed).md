**Labels:**

hold



<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Omnione](https://github.com/Omnione)**
_Thursday Jun 04, 2020 at 19:03:31_
_Originally opened as: project-topaz/topaz - Issue 685_

----

This PR will introduce the visitant light system for Abyssea, it will currently do nothing but control the lights that a player receives after killing a mob in an  Abyssea zone, all mobs have been mapped for the lights they should give, and all light values are as retail unless no information could be found, in which case the value will be an estimate based on other mobs of the same family in the same tier.

The lights that drop will be dependent on the way the mob has been killed as per retail.

All information has been collated and checked on multiple sites and also from retail testing. 

I have included GM commands to add lights and reset lights accordingly (!addlights and !resetlights).

special thanks to Lynnea of then Dawnbreak server for the help on this.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 20:39:04_

----

It looks like these are only being used in their respective blocks below, can we move these definitions down there so we only load the ones we need?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 20:40:00_

----

Can this just `return player:getCurrentRegion() == tpz.region.ABYSSEA`?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 20:49:38_

----

Should this be passing the mob?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 20:50:01_

----

Should `attacker` be `player`? Also is this one called for each member? Then DropLights adds light for each member as well, so are they getting hit twice? Should this check for `isKiller`?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 20:54:16_

----

Will this reset lights if a player logs out then logs back in? Or accepts a tractor? I think light is supposed to persist that, at least logging out, IDK about tractor.


----
<a href="https://github.com/whasf"><img src="https://avatars3.githubusercontent.com/u/6373706?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [whasf](https://github.com/whasf)**
_Thursday Jun 04, 2020 at 21:04:01_

----

I think you will get a lua "nil index" error if selectedLight is nil (you may want to bomb out separately before line 45)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 04, 2020 at 21:09:43_

----

Why chavars when any zoning loses it on retail? setLocalVar() would fit with retail behavior.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 21:12:30_

----

Retail behavior saves lights on logout.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 04, 2020 at 21:16:46_

----

I would handle this information the way we handle mob 2hrs - input passed to a mixin, rather than trying to name every mob in every abyssea zone in a global table like this.

You lose your single central location, but gain a cleaner more efficient code path.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 04, 2020 at 21:21:04_

----

..has it always been that way? Old man brain _swears_ I always lost them if I dc’d


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 04, 2020 at 21:22:47_

----

Seconded.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 21:25:40_

----

Not sure, wikia has this line from 2011,
> Built-up lights are only lost when a character leaves Abyssea. Changing to a different enemy target or logging out/disconnecting does not remove lights, nor do they decay over time.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 04, 2020 at 21:31:59_

----

Sounds like we could potentially store them in a hidden status effect and then flag the effect to be silently lost on zonage - like the Prowess buffs.

Speaking of effects, past me likely did the cruor buffs incorrectly even though they work. >.>;;  (used dummy IDs) I should check that soonish


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 04, 2020 at 21:33:41_

----

Death listener is running on just the killer iirc


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 21:38:29_

----

Yeah I think you're right. Wrong param is being passed still though.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 21:40:13_

----

Actually the DEATH listener only has `mob` and `killer` being passed to it, there is no `isKiller`, and `killer`/`player` can be nil.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Jun 04, 2020 at 22:43:04_

----

man, how do i  do that, i mean i must have to do this stuff by accident, cos i know it was there before, must be lack of sleep.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Jun 04, 2020 at 22:43:28_

----

good call sir's


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Jun 04, 2020 at 22:48:23_

----

hmm, i may have to look into what Teo suggested and add them to visitant status effect maybe?


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Jun 04, 2020 at 22:52:14_

----

oh, thinking about it, i may have to store this in a sql, ugh.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Jun 04, 2020 at 22:56:37_

----

yep, good call, cheers whasf


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Jun 04, 2020 at 23:00:28_

----

Accepting Tractor will remove this effect. (Note that instead of taking you to where Tractor was cast upon you, you will instead end up back at the entry encampment of whatever Abyssea area you were in, with your Visitant status, Abyssea Lights, and mob (EXP or Gil) chain all removed as if you had just entered the area again.) 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 23:04:29_

----

It will reset the lights when they logout then log back in though, which it shouldn't do.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 23:06:02_

----

Status effects and char vars are both stored in the db, char vars read the db every time you use them, so if you keep using them then just make sure you're doing it efficiently as you can.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 23:10:22_

----

You would likely need a different status effect for each light type. You could theoretically fit 3 light types into 1 char var, if you wanna go into that.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Friday Jun 05, 2020 at 00:26:21_

----

i'll think about it tommorow, after i get some sleep, cheers


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Friday Jun 05, 2020 at 00:26:33_

----

done


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Friday Jun 05, 2020 at 00:26:43_

----

fixed


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Friday Jun 05, 2020 at 00:26:55_

----

changed


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Friday Jun 05, 2020 at 00:27:17_

----

fixed now


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Friday Jun 05, 2020 at 00:29:45_

----

ok, ill figure it out tommorow, ty cocosolos


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 00:39:54_

----

Sorry just wanna reopen this because `isKiller` is still there. I just want to make sure someone doesn't see it and think it can be used, since only the mob and the killing player, if any, are passed to this function.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Friday Jun 05, 2020 at 14:36:44_

----

Whoops, i've taken it out now.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 06, 2020 at 02:37:15_

----

```lua

    -- Golden Light
    elseif light == 5 then
```
instead of brick houses for comments


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 06, 2020 at 02:38:43_

----

or enums /shrug


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 06, 2020 at 02:41:58_

----

even if you used every parameter addStatusEffect has I don't think you could cram it all into visitant. so 7 effects or 7 charVars I guess, that you then have to remember to kill anytime player leaves zone in anyway, which makes me think effect route is less effort.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jun 06, 2020 at 05:03:23_

----

I haven't looked at any code, just checking notifications:

Enums~! No magic numbers...!

`tpz.abyssea.light.GOLDEN`


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday Jun 06, 2020 at 21:39:15_

----

This should work like retail now, needs to be tested more, but seems right my end, and works well.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday Jun 06, 2020 at 21:41:44_

----

after disscussing this with others, it seems, the charVar method will be best suited for this task, so this should not be an issue now that the lights should be removed like retail, they stay on death, logout, only reset on zone or timeout or any other means of losing the visitant status.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday Jun 06, 2020 at 21:43:10_

----

All magic numbers should have been replaced with enums now


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Aug 19, 2020 at 14:36:49_

----

```lua
    if target then
        targ = GetPlayerByName(target)
        if not targ then
            error(player, string.format("Player named '%s' not found!", target))
            return
        end
    else
        targ = player
    end
```
would be preferred formatting.

other similar examples using `== nil` and extra parentheses exist in this pr as well. Does not affect functionality, but I thought you'd like to know to save yourself extra typing in the future.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Aug 19, 2020 at 14:39:02_

----

can mark this convo resolved since it has enums now


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Aug 19, 2020 at 14:48:21_

----

https://discordapp.com/channels/639659267003252746/639670779386134548/745655082934337536


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Friday Aug 28, 2020 at 03:46:22_

----

do you want to handle these last two comments as an issue?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 28, 2020 at 04:56:51_

----

nrly..


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 20:39:04_

----

It looks like these are only being used in their respective blocks below, can we move these definitions down there so we only load the ones we need?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 20:40:00_

----

Can this just `return player:getCurrentRegion() == tpz.region.ABYSSEA`?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 20:49:38_

----

Should this be passing the mob?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 20:50:01_

----

Should `attacker` be `player`? Also is this one called for each member? Then DropLights adds light for each member as well, so are they getting hit twice? Should this check for `isKiller`?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 20:54:16_

----

Will this reset lights if a player logs out then logs back in? Or accepts a tractor? I think light is supposed to persist that, at least logging out, IDK about tractor.


----
<a href="https://github.com/whasf"><img src="https://avatars3.githubusercontent.com/u/6373706?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [whasf](https://github.com/whasf)**
_Thursday Jun 04, 2020 at 21:04:01_

----

I think you will get a lua "nil index" error if selectedLight is nil (you may want to bomb out separately before line 45)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 04, 2020 at 21:09:43_

----

Why chavars when any zoning loses it on retail? setLocalVar() would fit with retail behavior.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 21:12:30_

----

Retail behavior saves lights on logout.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 04, 2020 at 21:16:46_

----

I would handle this information the way we handle mob 2hrs - input passed to a mixin, rather than trying to name every mob in every abyssea zone in a global table like this.

You lose your single central location, but gain a cleaner more efficient code path.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 04, 2020 at 21:21:04_

----

..has it always been that way? Old man brain _swears_ I always lost them if I dc’d


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 04, 2020 at 21:22:47_

----

Seconded.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 21:25:40_

----

Not sure, wikia has this line from 2011,
> Built-up lights are only lost when a character leaves Abyssea. Changing to a different enemy target or logging out/disconnecting does not remove lights, nor do they decay over time.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 04, 2020 at 21:31:59_

----

Sounds like we could potentially store them in a hidden status effect and then flag the effect to be silently lost on zonage - like the Prowess buffs.

Speaking of effects, past me likely did the cruor buffs incorrectly even though they work. >.>;;  (used dummy IDs) I should check that soonish


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 04, 2020 at 21:33:41_

----

Death listener is running on just the killer iirc


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 21:38:29_

----

Yeah I think you're right. Wrong param is being passed still though.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 21:40:13_

----

Actually the DEATH listener only has `mob` and `killer` being passed to it, there is no `isKiller`, and `killer`/`player` can be nil.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Jun 04, 2020 at 22:43:04_

----

man, how do i  do that, i mean i must have to do this stuff by accident, cos i know it was there before, must be lack of sleep.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Jun 04, 2020 at 22:43:28_

----

good call sir's


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Jun 04, 2020 at 22:48:23_

----

hmm, i may have to look into what Teo suggested and add them to visitant status effect maybe?


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Jun 04, 2020 at 22:52:14_

----

oh, thinking about it, i may have to store this in a sql, ugh.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Jun 04, 2020 at 22:56:37_

----

yep, good call, cheers whasf


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Jun 04, 2020 at 23:00:28_

----

Accepting Tractor will remove this effect. (Note that instead of taking you to where Tractor was cast upon you, you will instead end up back at the entry encampment of whatever Abyssea area you were in, with your Visitant status, Abyssea Lights, and mob (EXP or Gil) chain all removed as if you had just entered the area again.) 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 23:04:29_

----

It will reset the lights when they logout then log back in though, which it shouldn't do.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 23:06:02_

----

Status effects and char vars are both stored in the db, char vars read the db every time you use them, so if you keep using them then just make sure you're doing it efficiently as you can.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 23:10:22_

----

You would likely need a different status effect for each light type. You could theoretically fit 3 light types into 1 char var, if you wanna go into that.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Friday Jun 05, 2020 at 00:26:21_

----

i'll think about it tommorow, after i get some sleep, cheers


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Friday Jun 05, 2020 at 00:26:33_

----

done


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Friday Jun 05, 2020 at 00:26:43_

----

fixed


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Friday Jun 05, 2020 at 00:26:55_

----

changed


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Friday Jun 05, 2020 at 00:27:17_

----

fixed now


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Friday Jun 05, 2020 at 00:29:45_

----

ok, ill figure it out tommorow, ty cocosolos


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 00:39:54_

----

Sorry just wanna reopen this because `isKiller` is still there. I just want to make sure someone doesn't see it and think it can be used, since only the mob and the killing player, if any, are passed to this function.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Friday Jun 05, 2020 at 14:36:44_

----

Whoops, i've taken it out now.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 06, 2020 at 02:37:15_

----

```lua

    -- Golden Light
    elseif light == 5 then
```
instead of brick houses for comments


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 06, 2020 at 02:38:43_

----

or enums /shrug


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 06, 2020 at 02:41:58_

----

even if you used every parameter addStatusEffect has I don't think you could cram it all into visitant. so 7 effects or 7 charVars I guess, that you then have to remember to kill anytime player leaves zone in anyway, which makes me think effect route is less effort.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jun 06, 2020 at 05:03:23_

----

I haven't looked at any code, just checking notifications:

Enums~! No magic numbers...!

`tpz.abyssea.light.GOLDEN`


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday Jun 06, 2020 at 21:39:15_

----

This should work like retail now, needs to be tested more, but seems right my end, and works well.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday Jun 06, 2020 at 21:41:44_

----

after disscussing this with others, it seems, the charVar method will be best suited for this task, so this should not be an issue now that the lights should be removed like retail, they stay on death, logout, only reset on zone or timeout or any other means of losing the visitant status.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday Jun 06, 2020 at 21:43:10_

----

All magic numbers should have been replaced with enums now


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Aug 19, 2020 at 14:36:49_

----

```lua
    if target then
        targ = GetPlayerByName(target)
        if not targ then
            error(player, string.format("Player named '%s' not found!", target))
            return
        end
    else
        targ = player
    end
```
would be preferred formatting.

other similar examples using `== nil` and extra parentheses exist in this pr as well. Does not affect functionality, but I thought you'd like to know to save yourself extra typing in the future.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Aug 19, 2020 at 14:39:02_

----

can mark this convo resolved since it has enums now


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Aug 19, 2020 at 14:48:21_

----

https://discordapp.com/channels/639659267003252746/639670779386134548/745655082934337536


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Friday Aug 28, 2020 at 03:46:22_

----

do you want to handle these last two comments as an issue?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 28, 2020 at 04:56:51_

----

nrly..


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jun 04, 2020 at 19:17:12_

----

At it again with the giant PRs ;)


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Jun 04, 2020 at 20:30:13_

----

Maybe lol


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Aug 19, 2020 at 14:22:18_

----

@project-topaz/developer @project-topaz/reviewer  this appears to be in a good state and potentially ready for merging. as something on the older side, would love a review.
