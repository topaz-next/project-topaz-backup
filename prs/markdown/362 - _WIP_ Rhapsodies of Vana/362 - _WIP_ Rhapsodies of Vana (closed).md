**Labels:**

WIP



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Thursday Feb 20, 2020 at 09:37:12_
_Originally opened as: project-topaz/topaz - Issue 362_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

**TODO:**
Clean up commit history
Verify EXP bonus is suitable
Test Gilgamesh's sub job letter workflow front to back
Address the rest of the PR comments

**Doing in later PRs:**
Balance Ophiotaurus and Siren fights
Other Rhapsody in .* bonuses

**DONE:**
Structure of RoV 1-1 to 1-18 ✔️ 
Handling of Mhuara/Selbina paths ✔️ 
CS's in all starting zones ✔️ 
Undo auto-format in status.lua etc. ✔️ 
Triple check my port didn't squish anyone else's changes ✔️ 
Push to my server and make available for testing ✔️ 
Replace things that were squished in topaz port ✔️ 
KeyItem based subjob handling ✔️ 
Testing: Ring My Bell: First character lockout and use of `rhapsodies.lua`: ✔️ 

**Testing Notes:**
All RoV missions from 1-1 to 1-18 are scripted.
You will need to set ENABLE_ROV to 1
Later on you will need rank 3
Towards the end you will need to set you nation mission to 16 (defeated shadowlord)

**Mhaura path:**
!setplayervar <name> RhapsodiesStatus 2

**Selbina path:**
!setplayervar <name> RhapsodiesStatus 1

**Items for SET_FREE:**
Ekokoko:
!additem 9083 3

Abelard
!additem 9082 3

**Ophiotaurus spawn:**
!setmission 13 20


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 25, 2020 at 21:21:01_

----

When the set constructor PR gets merged, you'll be able to do some wonderful things:
```lua
tpz.rhapsodies.unavailability =
{
    [tpz.rhapsodies.character.PRISHE] = set{
       tpz.mission.id.cop.THE_RITES_OF_LIFE,
       tpz.mission.id.cop.BELOW_THE_ARKS,
    },
    [tpz.rhapsodies.character.TENZEN] = set{
       tpz.mission.id.cop.THE_RITES_OF_LIFE,
       tpz.mission.id.cop.BELOW_THE_ARKS,
    }
}
```

and then... (continued next comment)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 25, 2020 at 22:08:39_

----

```lua
tpz.rhapsodies.requiredCharacters =
{
    [tpz.mission.id.rov.NUMBERING_DAYS] = {
        tpz.rhapsodies.character.PRISHE, 
        tpz.rhapsodies.character.TENZEN
    }
}

tpz.rhapsodies.charactersAvailable = function(player)
    local rov_mission = player:getCurrentMission(ROV)
    for _, char in pairs(tpz.rhapsodies.requiredCharacters[rov_mission]) do
        local expansion_mission = player:getCurrentMission(tpz.rhapsodies.expansion[char])
        if tpz.rhapsodies.unavailability[char][expansion_mission] then
            return false
        end
    end
    return true
end
```

And all the individual `characterAvailable` functions can be cut. When you expect a character check for a mission, you just call the the `tpz.rhapsodies.charactersAvailable(player)` function without having to worry about `and`-ing multiple character checks together.

But you'll have to define a character->expansion lookup table.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 25, 2020 at 22:20:29_

----

Add a character->expansion lookup table here, after defining your character enums:
```lua
tpz.rhapsodies.expansion = 
{
    [tpz.rhapsodies.character.PRISHE] = COP,
    [tpz.rhapsodies.character.APHMAU] = TOAU,
}
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 08:49:26_

----

Putting a note here to double-check later where exactly retail drops you.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 08:54:27_

----

Putting a note here to double-check later where exactly retail drops you.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 09:01:06_

----

These NPCs will still transport you after you complete the mission.

I'll have to post it to the Captures server, but I do have a capture from last year in which I tested it immediately after getting the Rhapsody in White.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 09:04:30_

----

Same here re: transporting after the mission


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 09:38:49_

----

Remember to use the boolean returned by `npcUtil.giveItem` to make sure a player was able to receive an inventory item before you take items from them and complete a quest~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 09:47:56_

----

Mhaura's path needs to be something other than zero, or else the player will be swapping paths if they zone into Selbina~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 09:48:40_

----

And then check for the new Mhaura path variable here


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:00:10_

----

This isn't your fault, but this var is missing a `local`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:03:29_

----

Be sure that the player got their item before advancing here too


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:04:27_

----

Also not your fault, but the `local` is missing here too


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:09:10_

----

Only going to make the following comments on _this_ telepoint, but they apply to the other two as well:


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:18:52_

----

As a general rule, ROV cutscenes overrule all expansion cutscenes. Unfortunately, I don't have a capture testing the ROV/COP interaction here - in the only video I have this early in ROV, I talked to it twice and got the "million pieces" message, so I must not have flagged Below the Arks yet.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:19:55_

----

The requirement here is _rank_ 3, not fame level 3. 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:21:24_

----

You'll need to check for the character's ROV here too, because... (see next)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:24:45_

----

If you trigger the scene with a full inventory, you'll get the full scene, but the mission will not advance because it failed to give you Lion's Cipher. However, unlike other CS events which will play out all over again if you re-trigger the event, the Shattered Telepoint remembers you already viewed the event and just tries to give you the cipher again. When you successfully acquire the Cipher, _then_ you'll advance to the next mission.

You can see this behavior in "Rhapsodies: A Land After Time (1-11) (Full Inventory)".

The behavior has also held true for all other Ciphers ROV has tried to give me when I've remembered to keep full inventory.

So what'll need to be done is something like:
```lua
if npcUtil.giveItem then
    -- advance
else
    player:setCharVar("rhapsodies", 1)
end
```

And then... (next)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:29:20_

----

..back up in the trigger, check for the same mission and the "saw already" var, and then try giving the item again directly (and advancing mission on success) without replaying the CS.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:50:53_

----

So while I can't show the ROV/COP interaction for the Shattered Telepoint, I _can_ show definetively that _all_ of _these_ ROV cutscenes take priority over the ZM 2, in that it's possible to reach ROV 2-19 without the door flagging the ZM 2 CS.

See: "Rhapsodies: ROV 2-18 ~ ROV 2-24 ("Lowest", Lunette) + ZM 2 + COP 4-1" at 23m40s.

I accidentally proved it twice; once with the character already on ROV 2-19, and then when I _tried_ to flag the ZM2 CS with the second character, but got two ROV CSes before finally getting the ZM2 CS because _that_ character was on ROV 1-17 (Volto Oscuro).

It's outside the scope of this PR, but for future reference for anyone interested - this holds true until ROV 2-23. At that point, even if you have a ROV CS at the door, it will choose ZM 2 _first_, and then you'll be blocked on ROV 2-23/2-24 until you clear ZM 3. (See 54m of the same video.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 11:03:16_

----

Confrontation still being used here~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 11:08:08_

----

This bonus appears to be a static exp value being added to the base; instead of adding to the exp multiplier down below:


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 11:09:03_

----

So if I'm reading this right, the ROV KI would only add 30 exp, instead of multiplying by 30%.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 11, 2020 at 12:00:57_

----

the heck is all this?? I was able to tie it all to player and mob in the core the same way bcnm is tied. was much shorter  because I was able to reuse existing code.

(maybe its too early in the morning but I don't follow the purpose of doing all of this lua side)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 11, 2020 at 12:06:05_

----

she's a vera old lady, she forgot to stop being a global var forever ago


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 11, 2020 at 12:17:03_

----

```cpp
        auto RoVbonus = 0;
        for (auto i = 2884; i <= 2892; ++i) // RHAPSODY KI are sequential, so start at WHITE and end at OCHRE
        {
            if (hasKeyItem(PChar, i))
            {
                RoVbonus += 30;
```
```cpp
        bonus += (int32)(exp * (PChar->getMod(Mod::EXP_BONUS) + RoVbonus / 100.0f));
```
should fix that I think


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 11, 2020 at 12:17:52_

----

shouldn't removal on zone already happen by way of effect flags?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 11, 2020 at 16:03:22_

----

yo dude i didn't mean to have you delete all your work - I dunno what you mean to do wid it yet


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 25, 2020 at 21:21:01_

----

When the set constructor PR gets merged, you'll be able to do some wonderful things:
```lua
tpz.rhapsodies.unavailability =
{
    [tpz.rhapsodies.character.PRISHE] = set{
       tpz.mission.id.cop.THE_RITES_OF_LIFE,
       tpz.mission.id.cop.BELOW_THE_ARKS,
    },
    [tpz.rhapsodies.character.TENZEN] = set{
       tpz.mission.id.cop.THE_RITES_OF_LIFE,
       tpz.mission.id.cop.BELOW_THE_ARKS,
    }
}
```

and then... (continued next comment)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 25, 2020 at 22:08:39_

----

```lua
tpz.rhapsodies.requiredCharacters =
{
    [tpz.mission.id.rov.NUMBERING_DAYS] = {
        tpz.rhapsodies.character.PRISHE, 
        tpz.rhapsodies.character.TENZEN
    }
}

tpz.rhapsodies.charactersAvailable = function(player)
    local rov_mission = player:getCurrentMission(ROV)
    for _, char in pairs(tpz.rhapsodies.requiredCharacters[rov_mission]) do
        local expansion_mission = player:getCurrentMission(tpz.rhapsodies.expansion[char])
        if tpz.rhapsodies.unavailability[char][expansion_mission] then
            return false
        end
    end
    return true
end
```

And all the individual `characterAvailable` functions can be cut. When you expect a character check for a mission, you just call the the `tpz.rhapsodies.charactersAvailable(player)` function without having to worry about `and`-ing multiple character checks together.

But you'll have to define a character->expansion lookup table.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 25, 2020 at 22:20:29_

----

Add a character->expansion lookup table here, after defining your character enums:
```lua
tpz.rhapsodies.expansion = 
{
    [tpz.rhapsodies.character.PRISHE] = COP,
    [tpz.rhapsodies.character.APHMAU] = TOAU,
}
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 08:49:26_

----

Putting a note here to double-check later where exactly retail drops you.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 08:54:27_

----

Putting a note here to double-check later where exactly retail drops you.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 09:01:06_

----

These NPCs will still transport you after you complete the mission.

I'll have to post it to the Captures server, but I do have a capture from last year in which I tested it immediately after getting the Rhapsody in White.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 09:04:30_

----

Same here re: transporting after the mission


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 09:38:49_

----

Remember to use the boolean returned by `npcUtil.giveItem` to make sure a player was able to receive an inventory item before you take items from them and complete a quest~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 09:47:56_

----

Mhaura's path needs to be something other than zero, or else the player will be swapping paths if they zone into Selbina~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 09:48:40_

----

And then check for the new Mhaura path variable here


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:00:10_

----

This isn't your fault, but this var is missing a `local`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:03:29_

----

Be sure that the player got their item before advancing here too


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:04:27_

----

Also not your fault, but the `local` is missing here too


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:09:10_

----

Only going to make the following comments on _this_ telepoint, but they apply to the other two as well:


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:18:52_

----

As a general rule, ROV cutscenes overrule all expansion cutscenes. Unfortunately, I don't have a capture testing the ROV/COP interaction here - in the only video I have this early in ROV, I talked to it twice and got the "million pieces" message, so I must not have flagged Below the Arks yet.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:19:55_

----

The requirement here is _rank_ 3, not fame level 3. 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:21:24_

----

You'll need to check for the character's ROV here too, because... (see next)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:24:45_

----

If you trigger the scene with a full inventory, you'll get the full scene, but the mission will not advance because it failed to give you Lion's Cipher. However, unlike other CS events which will play out all over again if you re-trigger the event, the Shattered Telepoint remembers you already viewed the event and just tries to give you the cipher again. When you successfully acquire the Cipher, _then_ you'll advance to the next mission.

You can see this behavior in "Rhapsodies: A Land After Time (1-11) (Full Inventory)".

The behavior has also held true for all other Ciphers ROV has tried to give me when I've remembered to keep full inventory.

So what'll need to be done is something like:
```lua
if npcUtil.giveItem then
    -- advance
else
    player:setCharVar("rhapsodies", 1)
end
```

And then... (next)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:29:20_

----

..back up in the trigger, check for the same mission and the "saw already" var, and then try giving the item again directly (and advancing mission on success) without replaying the CS.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 10:50:53_

----

So while I can't show the ROV/COP interaction for the Shattered Telepoint, I _can_ show definetively that _all_ of _these_ ROV cutscenes take priority over the ZM 2, in that it's possible to reach ROV 2-19 without the door flagging the ZM 2 CS.

See: "Rhapsodies: ROV 2-18 ~ ROV 2-24 ("Lowest", Lunette) + ZM 2 + COP 4-1" at 23m40s.

I accidentally proved it twice; once with the character already on ROV 2-19, and then when I _tried_ to flag the ZM2 CS with the second character, but got two ROV CSes before finally getting the ZM2 CS because _that_ character was on ROV 1-17 (Volto Oscuro).

It's outside the scope of this PR, but for future reference for anyone interested - this holds true until ROV 2-23. At that point, even if you have a ROV CS at the door, it will choose ZM 2 _first_, and then you'll be blocked on ROV 2-23/2-24 until you clear ZM 3. (See 54m of the same video.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 11:03:16_

----

Confrontation still being used here~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 11:08:08_

----

This bonus appears to be a static exp value being added to the base; instead of adding to the exp multiplier down below:


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 11:09:03_

----

So if I'm reading this right, the ROV KI would only add 30 exp, instead of multiplying by 30%.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 11, 2020 at 12:00:57_

----

the heck is all this?? I was able to tie it all to player and mob in the core the same way bcnm is tied. was much shorter  because I was able to reuse existing code.

(maybe its too early in the morning but I don't follow the purpose of doing all of this lua side)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 11, 2020 at 12:06:05_

----

she's a vera old lady, she forgot to stop being a global var forever ago


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 11, 2020 at 12:17:03_

----

```cpp
        auto RoVbonus = 0;
        for (auto i = 2884; i <= 2892; ++i) // RHAPSODY KI are sequential, so start at WHITE and end at OCHRE
        {
            if (hasKeyItem(PChar, i))
            {
                RoVbonus += 30;
```
```cpp
        bonus += (int32)(exp * (PChar->getMod(Mod::EXP_BONUS) + RoVbonus / 100.0f));
```
should fix that I think


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 11, 2020 at 12:17:52_

----

shouldn't removal on zone already happen by way of effect flags?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 11, 2020 at 16:03:22_

----

yo dude i didn't mean to have you delete all your work - I dunno what you mean to do wid it yet
