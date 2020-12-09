**Labels:**

focus

merge ready



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 06, 2020 at 09:21:35_
_Originally opened as: project-topaz/topaz - Issue 472_

----

- Adjust entry requirements.
- Overhaul limbus.lua.
- Update Limbus NPCs.
- Rewrite armoury crate handling.
- Table Limbus mob/npc IDs.
- Move soap timer from Sagheera.
- Extend pathTo to accept pathflags.
- Add special setup for Limbus mobs.

Note that none of the actual BCNM or mob files are adjusted here, and all zones have been locked to prevent entry.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Apr 06, 2020 at 16:06:20_

----

could use the empty unused string field to identify it by, if the special name is really required.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 06, 2020 at 21:12:25_

----

No need to click or identify these, just using the IDs to set animation for doors.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 13:51:55_

----

charVars default to zero if they're not set; I'm still diving into this, but if you're using this later to determine where players should end up, it may present undesired behavior (because later `getCharVar` calls will return 0 when they fail to find a var)

edit: Where is this getting checked? I can't find it 😅 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Apr 12, 2020 at 17:58:17_

----

Doesn't have to be done now, but we may want to consider a new zoneType for such zones in the future. I think there's a handful more than just Limbus.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Apr 12, 2020 at 18:00:14_

----

Maybe move the definition into the check? Save us a whopping two lines. 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 12:13:22_

----

You're working too hard here~

```lua
-- in limbus.lua
tpz.limbus.prepareCrates = function(ids)
    local crates = {}
    for floor, id in ipairs(ids)
        crates[id] = floor
    end
    return crates
end
tpz.limbus.crate[TEMENOS_W] = tpz.limbus.prepareCrates(ID.npc.TEMENOS_W_CRATE)

-- armory_crate.lua
crate_type = model - 960
local baseID = crateID - crate_type
local floor = tpz.limbus.crate[TEMENOS_W][baseID]
if floor then
    if crate_type == 0 then
        tpz.battlefield.HealPlayers(battlefield)
    elseif crate_type == 1 then
        tpz.limbus.handleLootRolls(battlefield, loot[bfid][floor], nil, npc)
        if floor == 7 then
            battlefield:setLocalVar("cutsceneTimer", 10)
            battlefield:setLocalVar("lootSeen", 1)
        end
    elseif crate_type == 2 then
        tpz.limbus.extendTimeLimit(battlefield, 15, tpz.zone.TEMENOS)
    end
end
```

Puts the looping on first require, instead of every time a casket is opened!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 12:19:03_

----

Same logic as above, but just include disappearing the other two crates on the floor after determining which one you're opening.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 13:06:29_

----

Me: "Hrm, fake chests - this PR is starting to get a little hard to review."
Me: "...Wait, how are we even handling models? They're hard set based on the NPC ID... right?"
_checks_
Me: "Okay, we can do this. We can have random chest models, mimics, pretty code, and without looping. Just... think... and get that review in."
_starts going through Limbus global_
Me: "Nope. Can't get this thoroughly reviewed by Thursday. Punting this to a branch, and I'll open my own PR for logic simplifications. Not gonna make cocosolos put up with my usual nonsense during review of this PR!"


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 13:28:20_

----

Limbus is weird.

I'll want to revisit this ID and area system later.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 13:40:00_

----

Where does this get set? I'm not seeing it in `limbus.enter` or the entry NPCs.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 13, 2020 at 20:19:10_

----

This is checked in the zone.lua to teleport them to the correct side when exiting the battlefield.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 13, 2020 at 20:20:31_

----

Did this originally and you're probably right. I think this function needs some work anyway (should _any_ bcnm mobs be giving direct exp from kills, for example?)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 13, 2020 at 20:28:39_

----

I had this stuff in loops originally, but it was too slow and allowed opening multiple chests by timing correctly or spamming. Some floors change the chest model dynamically.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 13, 2020 at 20:29:14_

----

It gets set when you actually enter the bcnm, so next PR.

edit: limbus.enter is just used to teleport you to the correct side of Apollyon.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 13, 2020 at 20:34:41_

----

This is a weird one, and it may not matter, but all 3 of these zones have different crate mechanics. East has 4 chests and if you get a mimic then there's weird mechanics there, the others have 3. West doesn't depop the other chests, and North has 3 chests and you can only pick 1.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 21:09:09_

----

Okay, that works!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Apr 06, 2020 at 16:06:20_

----

could use the empty unused string field to identify it by, if the special name is really required.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 06, 2020 at 21:12:25_

----

No need to click or identify these, just using the IDs to set animation for doors.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 13:51:55_

----

charVars default to zero if they're not set; I'm still diving into this, but if you're using this later to determine where players should end up, it may present undesired behavior (because later `getCharVar` calls will return 0 when they fail to find a var)

edit: Where is this getting checked? I can't find it 😅 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Apr 12, 2020 at 17:58:17_

----

Doesn't have to be done now, but we may want to consider a new zoneType for such zones in the future. I think there's a handful more than just Limbus.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Apr 12, 2020 at 18:00:14_

----

Maybe move the definition into the check? Save us a whopping two lines. 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 12:13:22_

----

You're working too hard here~

```lua
-- in limbus.lua
tpz.limbus.prepareCrates = function(ids)
    local crates = {}
    for floor, id in ipairs(ids)
        crates[id] = floor
    end
    return crates
end
tpz.limbus.crate[TEMENOS_W] = tpz.limbus.prepareCrates(ID.npc.TEMENOS_W_CRATE)

-- armory_crate.lua
crate_type = model - 960
local baseID = crateID - crate_type
local floor = tpz.limbus.crate[TEMENOS_W][baseID]
if floor then
    if crate_type == 0 then
        tpz.battlefield.HealPlayers(battlefield)
    elseif crate_type == 1 then
        tpz.limbus.handleLootRolls(battlefield, loot[bfid][floor], nil, npc)
        if floor == 7 then
            battlefield:setLocalVar("cutsceneTimer", 10)
            battlefield:setLocalVar("lootSeen", 1)
        end
    elseif crate_type == 2 then
        tpz.limbus.extendTimeLimit(battlefield, 15, tpz.zone.TEMENOS)
    end
end
```

Puts the looping on first require, instead of every time a casket is opened!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 12:19:03_

----

Same logic as above, but just include disappearing the other two crates on the floor after determining which one you're opening.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 13:06:29_

----

Me: "Hrm, fake chests - this PR is starting to get a little hard to review."
Me: "...Wait, how are we even handling models? They're hard set based on the NPC ID... right?"
_checks_
Me: "Okay, we can do this. We can have random chest models, mimics, pretty code, and without looping. Just... think... and get that review in."
_starts going through Limbus global_
Me: "Nope. Can't get this thoroughly reviewed by Thursday. Punting this to a branch, and I'll open my own PR for logic simplifications. Not gonna make cocosolos put up with my usual nonsense during review of this PR!"


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 13:28:20_

----

Limbus is weird.

I'll want to revisit this ID and area system later.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 13:40:00_

----

Where does this get set? I'm not seeing it in `limbus.enter` or the entry NPCs.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 13, 2020 at 20:19:10_

----

This is checked in the zone.lua to teleport them to the correct side when exiting the battlefield.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 13, 2020 at 20:20:31_

----

Did this originally and you're probably right. I think this function needs some work anyway (should _any_ bcnm mobs be giving direct exp from kills, for example?)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 13, 2020 at 20:28:39_

----

I had this stuff in loops originally, but it was too slow and allowed opening multiple chests by timing correctly or spamming. Some floors change the chest model dynamically.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 13, 2020 at 20:29:14_

----

It gets set when you actually enter the bcnm, so next PR.

edit: limbus.enter is just used to teleport you to the correct side of Apollyon.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 13, 2020 at 20:34:41_

----

This is a weird one, and it may not matter, but all 3 of these zones have different crate mechanics. East has 4 chests and if you get a mimic then there's weird mechanics there, the others have 3. West doesn't depop the other chests, and North has 3 chests and you can only pick 1.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 13, 2020 at 21:09:09_

----

Okay, that works!
