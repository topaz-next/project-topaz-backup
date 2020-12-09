**Labels:**

merge ready



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Apr 11, 2020 at 06:18:18_
_Originally opened as: project-topaz/topaz - Issue 486_

----

The only TODO left here is to handle the cutscene 37
which happens after you have geomancer unlocked. It
allows the user to re-buy the Matre Bell. It needs
more research to determine how to handle the
`player:updateEvent(....)` during `onEventUpdate`.

Also I only implemented one of the /heal areas. I
found conflicting documentation, but seems like
you can rest at any of the Ergon Locus locations.
However I only implemented the one commonly used
in the unlock quest and mentioned in most of the
online wiki guides.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 15:24:01_

----

Can use `tpz.zone.CEIZAK_BATTLEGROUNDS` instead of 261, prevents more "magic numbers" in the codebase~

In my capture of the quest I specifically aborted this one early to go test the other one in the zone. You can see my capture for confirmation that the other locus works and maybe get range/position data.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 15:43:05_

----

We don't need to require the IDs up here on load: instead down below, inside the successful quest status check:

```lua
if target:getCharVar("GEO_DWL_Luopan") == 0 then
    local ID = zones[target:getZoneID()]
    target:messageSpecial(ID.text.GEO_DWL_ARCANE_ENERGY)
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 17:37:47_

----

`setCharVar` saves to SQL so the variable is kept between zones and logging out. Primary purpose is for things like quest status.

For volatile things we don't need to be able to save forever, there's `localVar` (not to be confused with with a lua `local` var - it's confusing I know, and we need to come up with a better name for these type of vars).
`player:setLocalVar("some_name", int_value)`
`player:getLocalVar("some_name", int_value)`
These are stored in memory, and let us be more gentle with the SQL server.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 18:43:38_

----

We can get around doing any checks in the ticks with a timer:

(Disclaimer: I haven't done a timer recently, so my syntax may not be exact; I also don't remember the rules on what args need to be passed into the lambda)

```lua
-- onEffectGain:
if target:getCharVar("GEO_DWL_Luopan") == 0 then
    local timeRequired = math.ceil(some_num_ticks * 3)
    target:setLocalVar("GEO_DWL_Resting", os.time() + timeRequired)
    target:timer(timeRequired * 1000, function()
        local finishTime = target:getLocalVar("GEO_DWL_Resting")
        if finishTime > 0 and os.time() >= finishTime then
            target:messageSpecial(ID.text.GEO_DWL_WARMTH)
            target:setCharVar("GEO_DWL_Luopan", 1)
        end
    end)
end

-- onEffectLose
target:setLocalVar("GEO_DWL_Resting", 0)



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 18:48:20_

----

`true` triggers `hasExactly` - Sylvie will accept the trade even when other junk items are included (see my capture), so you _don't_ want to use `hasExactly` in this case.

(But `npcUtil.tradeHasExactly` will be what we want to use for AF armor forging later, if I recall correctly)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 18:55:26_

----

Indenting a couple spaces off in this block (but the logic looks great)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Apr 13, 2020 at 23:46:07_

----

https://github.com/project-topaz/topaz/wiki/Understanding-variables:--a-brief-guide

/shamelessplug


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Apr 13, 2020 at 23:48:34_

----

@Omnione didn't you say you tried this with a registered region, how'd that go?


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 14, 2020 at 09:58:12_

----

Yep i got it working perfectly, ill DM over the files


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 00:52:50_

----

Ah, good to know. The capture I found on discord didn't demonstrate this.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 00:52:52_

----

Whoops. Fixed.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 00:55:04_

----

Oh, good to know. Never saw this. 

Definitely will use it from now on, when appropriate.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 00:58:19_

----

I'm always favorable of removing hardcoded values. Thanks for the tip!

Apparently 3 luopans work, according to: https://www.bg-wiki.com/bg/Dances_with_Luopans

But I couldn't find video capture of them.

Can you message me your capture on discord? I found one capture on there, but it didn't cover everything I would have preferred. Compared to the RUN capture, it was very minimalist.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 00:59:37_

----

Nice trick. Will use this from now on. Really useful.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 04:24:27_

----

Applied the timer and rewrote the logic based off of some of files.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 04:24:47_

----

The capture had all 3 areas. Added and tested them all.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 18:03:09_

----

Probably meant a `not (target:getCharVar("GEO_DWL_Luopan") == 1)` here instead of `not target:setCharVar("GEO_DWL_Luopan", 1)` 😉 


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 19:24:34_

----

Oh my gosh. Good catch!

I'm surprised this didn't introduce a bug when I ran through the quest.

I'll correct it and re-run through all the quest steps again to ensure it's working as expected. I'll also test this edge case again.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Apr 22, 2020 at 04:58:47_

----

Done.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 22:02:30_

----

For updateEvent params, retail will often send "junk data" as params which aren't required for the event (usually random memory values). We usually try to keep params limited to what we know is the cause of different behavior (so it's easier to tell which params are "important" when debugging in the future).

I toyed with the EventUpdate locally, and param 8 is what determines Sylvie's next line for a chosen option:
```
0 - You can't afford it
1 - Okay here you go
2 - You don't have the inventory space
```

I was a little surprised to find the special inventory space line. While doing a `npcUtil.giveItem` check is usually all one needs to do, Sylvie is special.

Thinking something like:
```lua
local updateParam = 0
if player:getFreeSlotsCount() >= 1 then
    if option == 1 and player:getGil() >= 300000 then
        player:setLocalVar("Sylvie_Matre_Bell", 1)
        updateParam = 1
    elseif option == 2 and player:getCurrency('bayld') >= 150000 then
        player:setLocalVar("Sylvie_Matre_Bell", 2)
        updateParam = 1
    end
else
    updateParam = 2
end

player:updateEvent(0, 0, 0, 0, 0, 0, 0, updateParam)
```

You can still keep `giveItem` inside the `if` for the `onFinish`; you'll need it to give the item anyway!


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Apr 22, 2020 at 22:31:17_

----

Ah,  I see. I just mirrored the exact params for updateEvent from the captures, to be safe.

I'm happy to clean that up, as I think it simplifies the code too by removing the rest of the seemingly magic numbers.

After work I can try to apply this change and play around with it to verify that it works for all edge cases.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Apr 23, 2020 at 03:04:28_

----

Rewrote this. Those params worked great. Please take a look.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 15:24:01_

----

Can use `tpz.zone.CEIZAK_BATTLEGROUNDS` instead of 261, prevents more "magic numbers" in the codebase~

In my capture of the quest I specifically aborted this one early to go test the other one in the zone. You can see my capture for confirmation that the other locus works and maybe get range/position data.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 15:43:05_

----

We don't need to require the IDs up here on load: instead down below, inside the successful quest status check:

```lua
if target:getCharVar("GEO_DWL_Luopan") == 0 then
    local ID = zones[target:getZoneID()]
    target:messageSpecial(ID.text.GEO_DWL_ARCANE_ENERGY)
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 17:37:47_

----

`setCharVar` saves to SQL so the variable is kept between zones and logging out. Primary purpose is for things like quest status.

For volatile things we don't need to be able to save forever, there's `localVar` (not to be confused with with a lua `local` var - it's confusing I know, and we need to come up with a better name for these type of vars).
`player:setLocalVar("some_name", int_value)`
`player:getLocalVar("some_name", int_value)`
These are stored in memory, and let us be more gentle with the SQL server.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 18:43:38_

----

We can get around doing any checks in the ticks with a timer:

(Disclaimer: I haven't done a timer recently, so my syntax may not be exact; I also don't remember the rules on what args need to be passed into the lambda)

```lua
-- onEffectGain:
if target:getCharVar("GEO_DWL_Luopan") == 0 then
    local timeRequired = math.ceil(some_num_ticks * 3)
    target:setLocalVar("GEO_DWL_Resting", os.time() + timeRequired)
    target:timer(timeRequired * 1000, function()
        local finishTime = target:getLocalVar("GEO_DWL_Resting")
        if finishTime > 0 and os.time() >= finishTime then
            target:messageSpecial(ID.text.GEO_DWL_WARMTH)
            target:setCharVar("GEO_DWL_Luopan", 1)
        end
    end)
end

-- onEffectLose
target:setLocalVar("GEO_DWL_Resting", 0)



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 18:48:20_

----

`true` triggers `hasExactly` - Sylvie will accept the trade even when other junk items are included (see my capture), so you _don't_ want to use `hasExactly` in this case.

(But `npcUtil.tradeHasExactly` will be what we want to use for AF armor forging later, if I recall correctly)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 18:55:26_

----

Indenting a couple spaces off in this block (but the logic looks great)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Apr 13, 2020 at 23:46:07_

----

https://github.com/project-topaz/topaz/wiki/Understanding-variables:--a-brief-guide

/shamelessplug


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Apr 13, 2020 at 23:48:34_

----

@Omnione didn't you say you tried this with a registered region, how'd that go?


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 14, 2020 at 09:58:12_

----

Yep i got it working perfectly, ill DM over the files


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 00:52:50_

----

Ah, good to know. The capture I found on discord didn't demonstrate this.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 00:52:52_

----

Whoops. Fixed.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 00:55:04_

----

Oh, good to know. Never saw this. 

Definitely will use it from now on, when appropriate.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 00:58:19_

----

I'm always favorable of removing hardcoded values. Thanks for the tip!

Apparently 3 luopans work, according to: https://www.bg-wiki.com/bg/Dances_with_Luopans

But I couldn't find video capture of them.

Can you message me your capture on discord? I found one capture on there, but it didn't cover everything I would have preferred. Compared to the RUN capture, it was very minimalist.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 00:59:37_

----

Nice trick. Will use this from now on. Really useful.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 04:24:27_

----

Applied the timer and rewrote the logic based off of some of files.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 04:24:47_

----

The capture had all 3 areas. Added and tested them all.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 18:03:09_

----

Probably meant a `not (target:getCharVar("GEO_DWL_Luopan") == 1)` here instead of `not target:setCharVar("GEO_DWL_Luopan", 1)` 😉 


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 19:24:34_

----

Oh my gosh. Good catch!

I'm surprised this didn't introduce a bug when I ran through the quest.

I'll correct it and re-run through all the quest steps again to ensure it's working as expected. I'll also test this edge case again.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Apr 22, 2020 at 04:58:47_

----

Done.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 22:02:30_

----

For updateEvent params, retail will often send "junk data" as params which aren't required for the event (usually random memory values). We usually try to keep params limited to what we know is the cause of different behavior (so it's easier to tell which params are "important" when debugging in the future).

I toyed with the EventUpdate locally, and param 8 is what determines Sylvie's next line for a chosen option:
```
0 - You can't afford it
1 - Okay here you go
2 - You don't have the inventory space
```

I was a little surprised to find the special inventory space line. While doing a `npcUtil.giveItem` check is usually all one needs to do, Sylvie is special.

Thinking something like:
```lua
local updateParam = 0
if player:getFreeSlotsCount() >= 1 then
    if option == 1 and player:getGil() >= 300000 then
        player:setLocalVar("Sylvie_Matre_Bell", 1)
        updateParam = 1
    elseif option == 2 and player:getCurrency('bayld') >= 150000 then
        player:setLocalVar("Sylvie_Matre_Bell", 2)
        updateParam = 1
    end
else
    updateParam = 2
end

player:updateEvent(0, 0, 0, 0, 0, 0, 0, updateParam)
```

You can still keep `giveItem` inside the `if` for the `onFinish`; you'll need it to give the item anyway!


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Apr 22, 2020 at 22:31:17_

----

Ah,  I see. I just mirrored the exact params for updateEvent from the captures, to be safe.

I'm happy to clean that up, as I think it simplifies the code too by removing the rest of the seemingly magic numbers.

After work I can try to apply this change and play around with it to verify that it works for all edge cases.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Apr 23, 2020 at 03:04:28_

----

Rewrote this. Those params worked great. Please take a look.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Apr 11, 2020 at 06:19:35_

----

I wasn't sure the best way to handle the resting. I feel a bit icky about pulling quest info into `scripts/globals/effects/healing.lua`, but it seemed to be the only place I could find to track the user while they are using `/heal`.

I'm open to other suggestions.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Apr 11, 2020 at 07:09:51_

----

Made a few tweaks and re-tested everything.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 01:01:52_

----

Resolved a handful of comments. Will look into applying the changes sent over by @Omnione next.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Monday Apr 20, 2020 at 04:24:07_

----

Applied the timer idea and added the other 2 areas that you can rest within.

Did some thorough testing and the timer idea works great.

The only thing I wish we had was the ability to keep a reference to the timer and cancel it immediately if the rest state ends. As of now it continues and just acts like a no-op on execution in that case.

But the core doesn't seem to support this and I didn't have time to look into adding that for a small optimization. 


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Apr 21, 2020 at 17:06:07_

----

https://youtu.be/3NL-h8TGReM
https://www.dropbox.com/s/4nqthprth9wdaxq/matre%20bell.rar?dl=0
for matre bell dropping and reacquisition


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Apr 21, 2020 at 18:12:19_

----

Thank you for this! Very helpful. I'll update the pull request to handle this case as well.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Apr 22, 2020 at 04:58:41_

----

Adjusted the final comment. And added logic for the matre bell repurchase.

I thoroughly tested out every edge case I could think of. So hopefully it's pretty bug-free now.

Please take another look.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Apr 23, 2020 at 03:04:49_

----

Updated the params and rewrote the logic to be more straightforward for `onEventUpdate`.
