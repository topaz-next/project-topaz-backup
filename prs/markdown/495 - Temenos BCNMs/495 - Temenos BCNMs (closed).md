**Labels:**

focus



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 15, 2020 at 00:10:57_
_Originally opened as: project-topaz/topaz - Issue 495_

----

All 8 level 75 Temenos zones.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 17:35:30_

----

Could shorten this switch here (and other non-dark elementals) a little by:

```lua
if mobID >= ID.mob.TEMENOS_C_MOB[2] then
    -- Central
else
    local crateID = ID.npc.TEMENOS_E_CRATE[3] + (mobID - ID.mob.TEMENOS_E_MOB[3])
    GetNPCByID(crateID):setPos(mobX, mobY, mobZ)
    tpz.limbus.spawnRandomCrate(crateID, player, "crateMaskF3", battlefield:getLocalVar("crateMaskF3"), true)
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 22:43:31_

----

```lua
if mobID <= ID.mob.TEMENOS_E_MOB[6] + 4 then
    local floor = ((mobID - (ID.mob.TEMENOS_E_MOB[1] + 4)) / 9) + 1
    local crateMask = battlefield:getLocalVar("crateMaskF" .. floor)
    if crateMask == 0 then
        tpz.limbus.handleDoors(battlefield, true, ID.npc.TEMENOS_E_GATE[floor])
    end
else
    -- Central Temenos
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 22:58:55_

----

```lua
elseif mobID >= ID.mob.TEMENOS_C_MOB[2]+9 then
    local element_offset = mobID - ID.mob.TEMENOS_C_MOB[2]+8
    local partner_offset = element_offset % 6 -- Levithan's partner starts at 0
    GetMobByID(ID.mob.TEMENOS_C_MOB[2]):setMod(tpz.mod.FIREDEF - 1 + element_offset)
    if GetMobByID(ID.mob.TEMENOS_C_MOB[2] + 3 + partner_offset):isAlive() then
        DespawnMob(ID.mob.TEMENOS_C_MOB[2] + 3 + partner_offset)
        SpawnMob(ID.mob.TEMENOS_C_MOB[2] + 9 + partner_offset)
    end
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 23:28:13_

----

Can combine these with the random modulo into one:
```lua
if mobID == ID.mob.TEMENOS_N_MOB[1] + (random % 2) then
    -- Chests
end
```

Although, there is a ffxiclopedia and bgwiki conflict:
> [Chests appear after defeating both Goblin Slaughterman.](https://www.bg-wiki.com/bg/Northern_Temenos)

> [The chest dropper is one of the Goblin Slaughterman in the NW corner OR SE corner. ](https://ffxiclopedia.fandom.com/wiki/Temenos_-_Northern_Tower)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 02:43:15_

----

bgwiki says "and" the BRD, ffxiclopedia says "and/or". We'll have to look into this for later.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 03:17:14_

----

Is this a `random == 5` case?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 03:25:16_

----

Do the doors on the 5th floor open after _any_ kill, or a random one (like previous floors)?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 03:36:43_

----

Same question on the _any_ Cryptonberry


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 03:39:22_

----

What are these despawns for?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 04:20:08_

----

Yeah I'll change this, everything I've seen points to either both of them needing to die or just the top one. I can't find any video of someone skipping the first Slaughterman and killing the upstairs one first.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 04:25:26_

----

This looks like the first floor to me, either both of them or just the far one. Same situation, all videos have chests spawning on the BRD after already killing WHM.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 04:36:55_

----

Every video I've seen door opens after first kill.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 04:42:28_

----

Think this is same as the Antican.
From wiki:
`Either the Cryptonberry Designator or Cryptonberry Abductor will open the portal. The lone THF is recommended.`
Recommending the THF implies a choice from any of them.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 05:06:33_

----

I'm not sure what I did here, but it looks wrong. `random` can be 1-6, but doors won't open if it's 1 or 2. Will fix.

Correction: 1 and 2 is handled by the BRD or WHM that doesn't drop the chests.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 05:08:34_

----

I think the issue was I was getting navmesh errors if I don't spawn the pets at the start, and they'll be spawned before they should be (DRG pets) if I don't despawn them.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 06:00:12_

----

I probably should have asked earlier- and I know this was already here - but can we use standard linking mechanics for these situations?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 06:15:55_

----

Usual "this was already here, but...." disclaimer: What happens if a party decides to engage one, hold it, and then kill the linked mob to try to get around the "strength increasing" effect?

(Or a wipe after killing the linked mob.)

We may want to move the "gets stronger" logic to the onDeath of the linked mob.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 06:16:09_

----

Since they link by sight you'd be able to pull from behind 1 at a time. I think they all attack at once, but may be wrong.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 06:22:25_

----

To show I _have_ been paying attention: These are for the Mook Orc DRG and the Boss Yagudo SMN, right?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 06:26:03_

----

Same as before regarding strength/weaken and engaged v death, but this time to the players' detriment. 😄 

(In this case, being aggroed by a boss before the last mook is dead, and then the boss not getting weaker until it re-engages.)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 06:28:46_

----

Yeah that sounds better. I think it's supposed to force a textless 2hr animation too, not sure how to do that.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 06:32:40_

----

> supposed to force a textless 2hr animation too, not sure how to do that.

@59blargedy Time for (Vulture 2)? 😉 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 06:36:21_

----

Yes


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 06:38:32_

----

bgwiki is claiming "random Aern"

> [Time limit is 15 minutes, but killing random Temenos Aerns will give time extensions.](https://www.bg-wiki.com/bg/Central_Temenos_-_Basement)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 06:54:01_

----

I believe it's 1 random Aern in 4 set groups of Aerns.  I currently have it set as the center mob in each of these groups, so does need to be randomized a bit. They also need to have their loot removed from db and manually drop coins based on how many times they RR. 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 07:07:53_

----

Others: I started typing an idea, then spoke with cocosolos on Discord. We might make use of onBattlefieldTick.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 07:17:07_

----

> The follow-up moves after nuclear waste remove elemental resist down?

> im actually not 100% on that

> Then I shall leave a comment for later research


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 07:25:57_

----

I know you haven't touched this, but this comment might be addressed as we're about to scrutinize Proto-Ultima.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Apr 22, 2020 at 13:17:51_

----

i think substitute (id 307) is more commonly used for messageless 2 hour animtion
cat 11 id 307 animation 439 message 0
(the vulture 2 and 3 thing from sea are weird?!?!)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 17:35:30_

----

Could shorten this switch here (and other non-dark elementals) a little by:

```lua
if mobID >= ID.mob.TEMENOS_C_MOB[2] then
    -- Central
else
    local crateID = ID.npc.TEMENOS_E_CRATE[3] + (mobID - ID.mob.TEMENOS_E_MOB[3])
    GetNPCByID(crateID):setPos(mobX, mobY, mobZ)
    tpz.limbus.spawnRandomCrate(crateID, player, "crateMaskF3", battlefield:getLocalVar("crateMaskF3"), true)
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 22:43:31_

----

```lua
if mobID <= ID.mob.TEMENOS_E_MOB[6] + 4 then
    local floor = ((mobID - (ID.mob.TEMENOS_E_MOB[1] + 4)) / 9) + 1
    local crateMask = battlefield:getLocalVar("crateMaskF" .. floor)
    if crateMask == 0 then
        tpz.limbus.handleDoors(battlefield, true, ID.npc.TEMENOS_E_GATE[floor])
    end
else
    -- Central Temenos
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 22:58:55_

----

```lua
elseif mobID >= ID.mob.TEMENOS_C_MOB[2]+9 then
    local element_offset = mobID - ID.mob.TEMENOS_C_MOB[2]+8
    local partner_offset = element_offset % 6 -- Levithan's partner starts at 0
    GetMobByID(ID.mob.TEMENOS_C_MOB[2]):setMod(tpz.mod.FIREDEF - 1 + element_offset)
    if GetMobByID(ID.mob.TEMENOS_C_MOB[2] + 3 + partner_offset):isAlive() then
        DespawnMob(ID.mob.TEMENOS_C_MOB[2] + 3 + partner_offset)
        SpawnMob(ID.mob.TEMENOS_C_MOB[2] + 9 + partner_offset)
    end
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 23:28:13_

----

Can combine these with the random modulo into one:
```lua
if mobID == ID.mob.TEMENOS_N_MOB[1] + (random % 2) then
    -- Chests
end
```

Although, there is a ffxiclopedia and bgwiki conflict:
> [Chests appear after defeating both Goblin Slaughterman.](https://www.bg-wiki.com/bg/Northern_Temenos)

> [The chest dropper is one of the Goblin Slaughterman in the NW corner OR SE corner. ](https://ffxiclopedia.fandom.com/wiki/Temenos_-_Northern_Tower)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 02:43:15_

----

bgwiki says "and" the BRD, ffxiclopedia says "and/or". We'll have to look into this for later.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 03:17:14_

----

Is this a `random == 5` case?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 03:25:16_

----

Do the doors on the 5th floor open after _any_ kill, or a random one (like previous floors)?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 03:36:43_

----

Same question on the _any_ Cryptonberry


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 03:39:22_

----

What are these despawns for?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 04:20:08_

----

Yeah I'll change this, everything I've seen points to either both of them needing to die or just the top one. I can't find any video of someone skipping the first Slaughterman and killing the upstairs one first.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 04:25:26_

----

This looks like the first floor to me, either both of them or just the far one. Same situation, all videos have chests spawning on the BRD after already killing WHM.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 04:36:55_

----

Every video I've seen door opens after first kill.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 04:42:28_

----

Think this is same as the Antican.
From wiki:
`Either the Cryptonberry Designator or Cryptonberry Abductor will open the portal. The lone THF is recommended.`
Recommending the THF implies a choice from any of them.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 05:06:33_

----

I'm not sure what I did here, but it looks wrong. `random` can be 1-6, but doors won't open if it's 1 or 2. Will fix.

Correction: 1 and 2 is handled by the BRD or WHM that doesn't drop the chests.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 05:08:34_

----

I think the issue was I was getting navmesh errors if I don't spawn the pets at the start, and they'll be spawned before they should be (DRG pets) if I don't despawn them.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 06:00:12_

----

I probably should have asked earlier- and I know this was already here - but can we use standard linking mechanics for these situations?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 06:15:55_

----

Usual "this was already here, but...." disclaimer: What happens if a party decides to engage one, hold it, and then kill the linked mob to try to get around the "strength increasing" effect?

(Or a wipe after killing the linked mob.)

We may want to move the "gets stronger" logic to the onDeath of the linked mob.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 06:16:09_

----

Since they link by sight you'd be able to pull from behind 1 at a time. I think they all attack at once, but may be wrong.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 06:22:25_

----

To show I _have_ been paying attention: These are for the Mook Orc DRG and the Boss Yagudo SMN, right?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 06:26:03_

----

Same as before regarding strength/weaken and engaged v death, but this time to the players' detriment. 😄 

(In this case, being aggroed by a boss before the last mook is dead, and then the boss not getting weaker until it re-engages.)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 06:28:46_

----

Yeah that sounds better. I think it's supposed to force a textless 2hr animation too, not sure how to do that.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 06:32:40_

----

> supposed to force a textless 2hr animation too, not sure how to do that.

@59blargedy Time for (Vulture 2)? 😉 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 06:36:21_

----

Yes


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 06:38:32_

----

bgwiki is claiming "random Aern"

> [Time limit is 15 minutes, but killing random Temenos Aerns will give time extensions.](https://www.bg-wiki.com/bg/Central_Temenos_-_Basement)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 22, 2020 at 06:54:01_

----

I believe it's 1 random Aern in 4 set groups of Aerns.  I currently have it set as the center mob in each of these groups, so does need to be randomized a bit. They also need to have their loot removed from db and manually drop coins based on how many times they RR. 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 07:07:53_

----

Others: I started typing an idea, then spoke with cocosolos on Discord. We might make use of onBattlefieldTick.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 07:17:07_

----

> The follow-up moves after nuclear waste remove elemental resist down?

> im actually not 100% on that

> Then I shall leave a comment for later research


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 22, 2020 at 07:25:57_

----

I know you haven't touched this, but this comment might be addressed as we're about to scrutinize Proto-Ultima.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Apr 22, 2020 at 13:17:51_

----

i think substitute (id 307) is more commonly used for messageless 2 hour animtion
cat 11 id 307 animation 439 message 0
(the vulture 2 and 3 thing from sea are weird?!?!)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 23:29:14_

----

> Regarding Carbuncle's decreasing resistances:
> 
> > [Note: Carbuncle has exceptionally high damage taken resistance upon first entering the zone; this is progressively weakened by defeating the six elementals/avatars scattered around the zone.](https://www.bg-wiki.com/bg/Central_Temenos_-_2nd_Floor)
> 
> Is this elemental resistances as coded, or flat physical/magical resistances?

This was already being done with elemental resistance in the Mystic Avatar script, so I just moved it to the elementals. It sounds like it should be damage taken though not elemental resist.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 22, 2020 at 04:39:01_

----

> > Regarding Carbuncle's decreasing resistances:
> > > [Note: Carbuncle has exceptionally high damage taken resistance upon first entering the zone; this is progressively weakened by defeating the six elementals/avatars scattered around the zone.](https://www.bg-wiki.com/bg/Central_Temenos_-_2nd_Floor)
> > 
> > 
> > Is this elemental resistances as coded, or flat physical/magical resistances?
> 
> This was already being done with elemental resistance in the Mystic Avatar script, so I just moved it to the elementals. It sounds like it should be damage taken though not elemental resist.

Probably the element defense mods, which act like damage taken mods of 1 specified element each - the early revisions often mixed these up with resistance rate mods
