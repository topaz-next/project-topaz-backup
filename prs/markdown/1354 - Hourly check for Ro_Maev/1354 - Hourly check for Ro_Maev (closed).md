**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 13, 2020 at 23:00:02_
_Originally opened as: project-topaz/topaz - Issue 1354_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This PR would successfully activate Ro'Maeve's bridges, gates and the fountain not only at exactly 6pm but at any hour that hits full moon between 6pm and (not including) 6am for the remaining amount of time until 6am. The current logic in release only once can activate the whole area at exactly 6pm not thereafter. This is not desirable.
~~It also adds the missing weather condition. The area must have no weather for the full moon to affect the mentioned objects.~~
Furthermore when cleaning up at 6am only the two Moongates should become targetable again.

This was a bummer to debug and test cause the !time command apparently throws off the sync between the in-game shown /clock and the server clock, but nonetheless:
- [x] Tested working locally at several hours, moon phases and weather conditions.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Oct 13, 2020 at 23:53:59_

----

We really should keep the variable rather than repeatedly call the same function. OnGameHour is going to re execute every hour, so the results isn’t able to change before reaching the next place it is checked 


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 13, 2020 at 23:56:12_

----

It won't be called repeatedly at all since we set `setLocalVar("romaeveActive", 1)` though? none of all of that will be called again after firing once. If anything we could put the two locals `moongate` and `romaeveActive` outside of the `onGameHour()` block indeed, so they're not called every hour for no reason.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Oct 13, 2020 at 23:58:47_

----

you have a condition inside of a condition that both ask what the hour is. you can store the function call result instead of calling it twice. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 14, 2020 at 00:00:17_

----

I commented at the line where the 2nd one happens - I'm not talking a bout your loop. But while we're at it, why are we looping for hrs left instead of using >= and <= since we know the exact hr ranges on both sides of 0:00 and 24:00..does the change not land on exactly an hr mark?


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Oct 14, 2020 at 00:11:11_

----

~~On hold for now after talking to @TeoTwawki some more. More changes incoming.~~ Removed all the bloat that was written to calculate the seconds left until 6am needed for `openDoor()`. Now uses `:setAnimation()` instead. Done.
- [x] Tested working locally


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 14, 2020 at 04:09:26_

----

you'll want to define your variables inside onGameHour rather than above/before it, (they aren't being used outside it, so by putting them with it we're restricting them to the [scope ](http://lua-users.org/wiki/ScopeTutorial)they need to be in)

I would also keep the original `local hour = VanadielHour()` that was here before, since there are no earth hours here to accidentally confuse it with.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Oct 14, 2020 at 05:30:16_

----

Are you sure about this? Wouldn't that just mean unnecessary requests being made every 144s completely despite the fact whether it is full moon or whatever hour? For all the lifetime of the server? Because if its not full moon, none of this will get called if not after a server boot. Also I feel that renaming the variable kinda goes against what Zach has been pushing were the code itself should be as explicit as possible at all times.

What I do see is that we should add `romaeveActive == 1` to the clean up condition, so it also only gets called in that specific event, not every day. I had this clear every day rather than unconditionally because I didn't have the flag bit before.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 14, 2020 at 15:00:19_

----

The only ones that wouldn't be being called anyway are the 2 getByID, which even though it is probably ok the vars themselves can be inside a conditional to prevent running them when not needed, but when you have them outside the function like this they exist in a larger scope which I did not catch when you showed me in discord (sorry)

proposed adjustment:
```lua
function onGameHour(zone)
    -- Make Ro'Maeve come to life between 6pm and 6am during a full moon
    local romaeveActive = moongate1:getLocalVar("romaeveActive")
    local vanadielHour = VanadielHour()

    if romaeveActive == 0 and IsMoonFull() and (vanadielHour >= 18 or vanadielHour < 6) then
        local moongate1 = GetNPCByID(ID.npc.MOONGATE_OFFSET)
        local moongate2 = GetNPCByID(ID.npc.MOONGATE_OFFSET + 1)

        -- Loop over the affected NPCs: Moongates, bridges and fountain
        for i = ID.npc.MOONGATE_OFFSET, ID.npc.MOONGATE_OFFSET + 7 do
            GetNPCByID(i):setAnimation(tpz.anim.OPEN_DOOR) -- Open them
        end
        moongate2:untargetable(true)
        moongate1:untargetable(true)
        moongate1:setLocalVar("romaeveActive", 1) -- Make this loop unavailable after firing

    -- Clean up at 6am
    elseif romaeveActive == 1 and vanadielHour == 6 then
        local moongate1 = GetNPCByID(ID.npc.MOONGATE_OFFSET)
        local moongate2 = GetNPCByID(ID.npc.MOONGATE_OFFSET + 1)
        for i = ID.npc.MOONGATE_OFFSET, ID.npc.MOONGATE_OFFSET + 7 do
            GetNPCByID(i):setAnimation(tpz.anim.CLOSE_DOOR)
        end
        moongate2:untargetable(false)
        moongate1:untargetable(false)
        moongate1:setLocalVar("romaeveActive", 0) -- Make loop available again
    end
end
```
it won't matter that we're doing a local define of those npc's in both conditions, because only one of the 2 conditions can be trues and each one is inside the scope of that condition (so no collision, and only one set is used). 

hour and romaeveActive are going to be check every hours anyway.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Oct 14, 2020 at 17:10:03_

----

I for one like that solution very much. Thank you for your patience @TeoTwawki 
Changes were made as proposed.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Oct 14, 2020 at 17:35:52_

----

moongate1 hasn't been defined yet~!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 14, 2020 at 17:39:10_

----

woopsie


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 14, 2020 at 17:39:28_

----

my fault


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 14, 2020 at 17:42:49_

----

```lua
function onGameHour(zone)
    local hour = VanadielHour()

    -- Make Ro'Maeve come to life between 6pm and 6am during a full moon
    if IsMoonFull() and (hour >= 18 or hour < 6) then
        local moongate1 = GetNPCByID(ID.npc.MOONGATE_OFFSET)
        local moongate2 = GetNPCByID(ID.npc.MOONGATE_OFFSET + 1)
        if moongate1:getLocalVar("romaeveActive") == 0 then

            -- Loop over the affected NPCs: Moongates, bridges and fountain
            for i = ID.npc.MOONGATE_OFFSET, ID.npc.MOONGATE_OFFSET + 7 do
                GetNPCByID(i):setAnimation(tpz.anim.OPEN_DOOR) -- Open them
            end
            moongate2:untargetable(true)
            moongate1:untargetable(true)
            moongate1:setLocalVar("romaeveActive", 1) -- Make this loop unavailable after firing
        end

    -- Clean up at 6am
    elseif hour == 6 then
        local moongate1 = GetNPCByID(ID.npc.MOONGATE_OFFSET)
        local moongate2 = GetNPCByID(ID.npc.MOONGATE_OFFSET + 1)
        if moongate1:getLocalVar("romaeveActive") == 1 then
            for i = ID.npc.MOONGATE_OFFSET, ID.npc.MOONGATE_OFFSET + 7 do
                GetNPCByID(i):setAnimation(tpz.anim.CLOSE_DOOR)
            end
            moongate2:untargetable(false)
            moongate1:untargetable(false)
            moongate1:setLocalVar("romaeveActive", 0) -- Make loop available again
        end
    end
end
```
fixed version of what I wrote before


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Oct 14, 2020 at 19:04:59_

----

Sorry, was sleeping myself there. Changed as proposed, kept `vanadielHour` though.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 14, 2020 at 19:16:58_

----

note to self: look into making variables on the zone object itself a thing. if for some reason this one NPC gets lost by something as trivial as an ID shift, the whole thing breaks.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Oct 13, 2020 at 23:53:59_

----

We really should keep the variable rather than repeatedly call the same function. OnGameHour is going to re execute every hour, so the results isn’t able to change before reaching the next place it is checked 


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 13, 2020 at 23:56:12_

----

It won't be called repeatedly at all since we set `setLocalVar("romaeveActive", 1)` though? none of all of that will be called again after firing once. If anything we could put the two locals `moongate` and `romaeveActive` outside of the `onGameHour()` block indeed, so they're not called every hour for no reason.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Oct 13, 2020 at 23:58:47_

----

you have a condition inside of a condition that both ask what the hour is. you can store the function call result instead of calling it twice. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 14, 2020 at 00:00:17_

----

I commented at the line where the 2nd one happens - I'm not talking a bout your loop. But while we're at it, why are we looping for hrs left instead of using >= and <= since we know the exact hr ranges on both sides of 0:00 and 24:00..does the change not land on exactly an hr mark?


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Oct 14, 2020 at 00:11:11_

----

~~On hold for now after talking to @TeoTwawki some more. More changes incoming.~~ Removed all the bloat that was written to calculate the seconds left until 6am needed for `openDoor()`. Now uses `:setAnimation()` instead. Done.
- [x] Tested working locally


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 14, 2020 at 04:09:26_

----

you'll want to define your variables inside onGameHour rather than above/before it, (they aren't being used outside it, so by putting them with it we're restricting them to the [scope ](http://lua-users.org/wiki/ScopeTutorial)they need to be in)

I would also keep the original `local hour = VanadielHour()` that was here before, since there are no earth hours here to accidentally confuse it with.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Oct 14, 2020 at 05:30:16_

----

Are you sure about this? Wouldn't that just mean unnecessary requests being made every 144s completely despite the fact whether it is full moon or whatever hour? For all the lifetime of the server? Because if its not full moon, none of this will get called if not after a server boot. Also I feel that renaming the variable kinda goes against what Zach has been pushing were the code itself should be as explicit as possible at all times.

What I do see is that we should add `romaeveActive == 1` to the clean up condition, so it also only gets called in that specific event, not every day. I had this clear every day rather than unconditionally because I didn't have the flag bit before.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 14, 2020 at 15:00:19_

----

The only ones that wouldn't be being called anyway are the 2 getByID, which even though it is probably ok the vars themselves can be inside a conditional to prevent running them when not needed, but when you have them outside the function like this they exist in a larger scope which I did not catch when you showed me in discord (sorry)

proposed adjustment:
```lua
function onGameHour(zone)
    -- Make Ro'Maeve come to life between 6pm and 6am during a full moon
    local romaeveActive = moongate1:getLocalVar("romaeveActive")
    local vanadielHour = VanadielHour()

    if romaeveActive == 0 and IsMoonFull() and (vanadielHour >= 18 or vanadielHour < 6) then
        local moongate1 = GetNPCByID(ID.npc.MOONGATE_OFFSET)
        local moongate2 = GetNPCByID(ID.npc.MOONGATE_OFFSET + 1)

        -- Loop over the affected NPCs: Moongates, bridges and fountain
        for i = ID.npc.MOONGATE_OFFSET, ID.npc.MOONGATE_OFFSET + 7 do
            GetNPCByID(i):setAnimation(tpz.anim.OPEN_DOOR) -- Open them
        end
        moongate2:untargetable(true)
        moongate1:untargetable(true)
        moongate1:setLocalVar("romaeveActive", 1) -- Make this loop unavailable after firing

    -- Clean up at 6am
    elseif romaeveActive == 1 and vanadielHour == 6 then
        local moongate1 = GetNPCByID(ID.npc.MOONGATE_OFFSET)
        local moongate2 = GetNPCByID(ID.npc.MOONGATE_OFFSET + 1)
        for i = ID.npc.MOONGATE_OFFSET, ID.npc.MOONGATE_OFFSET + 7 do
            GetNPCByID(i):setAnimation(tpz.anim.CLOSE_DOOR)
        end
        moongate2:untargetable(false)
        moongate1:untargetable(false)
        moongate1:setLocalVar("romaeveActive", 0) -- Make loop available again
    end
end
```
it won't matter that we're doing a local define of those npc's in both conditions, because only one of the 2 conditions can be trues and each one is inside the scope of that condition (so no collision, and only one set is used). 

hour and romaeveActive are going to be check every hours anyway.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Oct 14, 2020 at 17:10:03_

----

I for one like that solution very much. Thank you for your patience @TeoTwawki 
Changes were made as proposed.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Oct 14, 2020 at 17:35:52_

----

moongate1 hasn't been defined yet~!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 14, 2020 at 17:39:10_

----

woopsie


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 14, 2020 at 17:39:28_

----

my fault


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 14, 2020 at 17:42:49_

----

```lua
function onGameHour(zone)
    local hour = VanadielHour()

    -- Make Ro'Maeve come to life between 6pm and 6am during a full moon
    if IsMoonFull() and (hour >= 18 or hour < 6) then
        local moongate1 = GetNPCByID(ID.npc.MOONGATE_OFFSET)
        local moongate2 = GetNPCByID(ID.npc.MOONGATE_OFFSET + 1)
        if moongate1:getLocalVar("romaeveActive") == 0 then

            -- Loop over the affected NPCs: Moongates, bridges and fountain
            for i = ID.npc.MOONGATE_OFFSET, ID.npc.MOONGATE_OFFSET + 7 do
                GetNPCByID(i):setAnimation(tpz.anim.OPEN_DOOR) -- Open them
            end
            moongate2:untargetable(true)
            moongate1:untargetable(true)
            moongate1:setLocalVar("romaeveActive", 1) -- Make this loop unavailable after firing
        end

    -- Clean up at 6am
    elseif hour == 6 then
        local moongate1 = GetNPCByID(ID.npc.MOONGATE_OFFSET)
        local moongate2 = GetNPCByID(ID.npc.MOONGATE_OFFSET + 1)
        if moongate1:getLocalVar("romaeveActive") == 1 then
            for i = ID.npc.MOONGATE_OFFSET, ID.npc.MOONGATE_OFFSET + 7 do
                GetNPCByID(i):setAnimation(tpz.anim.CLOSE_DOOR)
            end
            moongate2:untargetable(false)
            moongate1:untargetable(false)
            moongate1:setLocalVar("romaeveActive", 0) -- Make loop available again
        end
    end
end
```
fixed version of what I wrote before


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Oct 14, 2020 at 19:04:59_

----

Sorry, was sleeping myself there. Changed as proposed, kept `vanadielHour` though.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 14, 2020 at 19:16:58_

----

note to self: look into making variables on the zone object itself a thing. if for some reason this one NPC gets lost by something as trivial as an ID shift, the whole thing breaks.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 13, 2020 at 23:26:16_

----

~~Please don't merge yet, I think I have a typo.~~


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Oct 13, 2020 at 23:31:00_

----

We used to have the weather requirement coded, but removed it; I thought this was because specific weather was no longer required in retail.
https://github.com/DarkstarProject/darkstar/issues/3957


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 13, 2020 at 23:49:19_

----

~~Took out the weather check (makes me sad) and removed `math.abs()` from one of the calculations cause not necessary. The subtraction will reliably always be negative, so just multiply by negative.~~ Outdated, see below.

Maybe I can raise awareness for https://github.com/project-topaz/topaz/issues/480 which is related to the content of this PR but not affected by it.
