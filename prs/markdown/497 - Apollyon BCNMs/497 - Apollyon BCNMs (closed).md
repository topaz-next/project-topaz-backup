**Labels:**

focus

merge ready



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 15, 2020 at 02:15:09_
_Originally opened as: project-topaz/topaz - Issue 497_

----

All 6 level 75 Apollyon zones.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 18, 2020 at 19:34:05_

----

As strange as it sounds, I recall hearing that there are issues with pathing if the points are floats.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 18, 2020 at 19:41:54_

----

@project-topaz/researcher  Usual, "is this retail?" question


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 18, 2020 at 21:28:34_

----

0 * 5 = 0 😉 

May need to make your min 1 and adjust starting point accordingly.

(Same goes for Thiazi)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 18, 2020 at 23:51:58_

----

Can put a break here


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Apr 19, 2020 at 04:02:44_

----

Yeah it's either the base mob `ID.mob.APOLLYON_NE_MOB[3]` or some multiple * 5 of it depending how many people are in party and thus mobs to spawn on the next floor. So `math.random(0,1)*5` is 50/50 which mob on the next floor, base mob, or base mob + 5.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 19, 2020 at 04:05:18_

----

I'm still not clear on why but several entities would not move until the value were set to integers, so the bug is real.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Apr 19, 2020 at 04:05:49_

----

Oh, it's not any of the freshly spawned mobs?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Apr 19, 2020 at 04:16:10_

----

This is when the mobs for the next floor spawn and also when we roll to see which one drops what.
```lua
Sweeper -- ID.mob.APOLLYON_NE_MOB[3]+(0*5) potential portal mob
Cleaner -- ID.mob.APOLLYON_NE_MOB[3]+1+(0*5) potential item chest
Cleaner
Cleaner
Cleaner
Sweeper -- ID.mob.APOLLYON_NE_MOB[3]+(1*5) potential portal mob
Cleaner-- ID.mob.APOLLYON_NE_MOB[3]+1+(1*5) potential item chest
Cleaner
Cleaner
Cleaner
Sweeper -- ID.mob.APOLLYON_NE_MOB[3]+(2*5) potential portal mob
Cleaner-- ID.mob.APOLLYON_NE_MOB[3]+1+(2*5) potential item chest
Cleaner
Cleaner
Cleaner
```
The cleaners could maybe be randomized better.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Apr 19, 2020 at 04:18:31_

----

I set the wallhack flag for anything that wasn't moving for me, there were a few that would get stuck on stuff.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 19, 2020 at 04:28:41_

----

wall hack should turn on automatically for mobs that can't get to their next position, maybe thats what broke.


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Sunday Apr 19, 2020 at 17:45:00_

----

10 seconds, just checked on retail!


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Apr 19, 2020 at 21:59:33_

----

This whole pathing thing probably needs to be redone, I just wanted to get the positions down. The 40 seconds is the 30 seconds it takes for it to traverse the path then 10 seconds waiting before moving to next point.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 01:00:16_

----

What's going on here during engage? Are we trying to get the others to stop pathing?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 01:07:42_

----

Does the floor boss not spawn without a Flying Spear being killed?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 20, 2020 at 01:34:38_

----

I may be wrong here, but if you're careful when you spawn into this floor to not get aggro by the one close to where you spawn in, it doesn't look like they start roaming until one of them engages. May need further confirmation. That's what it looked like to me and made sense as some "wake the dead" mechanic.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 20, 2020 at 01:35:15_

----

It's an NPC until someone kills one of the Flying Spears.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 01:41:48_

----

Oh, you told me about this one and I forgot. Sorry!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 03:01:15_

----

I'll have to double-check the elemental behavior, but this is where sets can help you out, with maybe a new helper function in limbus.lua

```lua
-- somewhere.lua
limbus.something.fomor.hume = set{ ID.mob.APOLLYON_SW_MOB[1]+2, ID.mob.APOLLYON_SW_MOB[1]+7 }
limbus.something.elemental.fire = set{ ID.mob.APOLLYON_SW_MOB[4]+2, ID.mob.APOLLYON_SW_MOB[4]+10, ID.mob.APOLLYON_SW_MOB[4]+18}

-- limbus.lua
tpz.limbus.allDead = function(mob, mob_set)
    for id, _ in pairs(mob_set) do
        if not GetMobByID(id):isDead()
            return false
        end
    end
    return true
end

-- fir_bholg.lua
onMobDeath(mob, player, isKiller)
    if race == 1 or race == 2 and limbus.something.fomor.hume[mob:getID()] then
        if tpz.limbus.allDead(mob, limbus.something.fomor.hume) then
            -- chests
        else
            -- portal
        end
    end
end

-- fire_elemental.lua
onMobDeath(mob, player, isKiller)
    if day == 0 and tpz.limbus.allDead(mob, limbus.something.elemental.fire) then
        -- chests
    end
end


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 03:53:12_

----

```lua
if id == leafless then
    -- open portal
else
    local add_mob = GetMobByID(mobID + 7)
    add_mob:setPos(mobX, mobY, mobZ)
    add_mob:setSpawn(mobX, mobY, mobZ)
    add_mob:spawn():updateEnmity(player)
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 03:55:05_

----

I believe this mob might be a sapling 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 03:55:19_

----

So many Dhalmels on this floor~!


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 20, 2020 at 04:10:07_

----

Why did I do this! 🤦‍♂️


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 20, 2020 at 04:38:34_

----

I like what you did, would like to wait till both zones are in the same branch so I can do it all at once.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 04:39:26_

----

This can be cleaner with sets, a helper function, and doing this on the onDeath of the summoned mobs (no need for onMobFight)
```lua
-- somewhere.lua
limbus.something.cs_apollyon.yagudo_wave1 = set { ID.mob.APOLLYON_CS_MOB[3]+3, ID.mob.APOLLYON_CS_MOB[3]+4, ID.mob.APOLLYON_CS_MOB[3]+5 }

limbus.something.cs_apollyon.yagudo_wave2 = set { ID.mob.APOLLYON_CS_MOB[3]+6, ID.mob.APOLLYON_CS_MOB[3]+7, ID.mob.APOLLYON_CS_MOB[3]+8 }

tpz.limbus.handleWave = function(mob, race)
    local battlefield = mob:getBattlefield()
    local wave_var = battlefield:getLocalVar(race .. "_wave")
    local wave_set = limbus.something.cs_apollyon[race .. "_wave" .. wave_var]
    if wave_set[mob:getID()] and tpz.limbus.allDead(wave_set) then
        local next_wave = (wave % 2) + 1
        battlefield:setLocalVar(race .. "_wave", next_wave)
        local next_set = limbus.something.cs_apollyon[race .. "_wave" .. next_wave]
        -- get the boss mob based on race somehow; table lookup, if check, whatever - make it race_boss
        local boss_pos = race_boss:getPos()
        for id, _ in pairs(next_set) do
             local mook = GetMobByID(id)
             mook:setSpawn(boss_pos.x, boss_pos.y, boss_pos.z)
             mook:setPos(boss_pos.x, boss_pos.y, boss_pos.z)
             mook:spawn():setMobMod(tpz.mobMod.SUPERLINK, mob:getShortID())
        end
    end
end

-- all yagudo mook luas
function onMobDeath(mob, player, isKiller)
    tpz.limbus.handleWave(mob, "yagudo")
end

-- beastmen mob boss luas
function onMobFight
    -- Nothing! New waves are handled on death of the mooks!
end


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 04:42:31_

----

This would probably be better in onBattlefieldTick instead of onMobFight~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 04:47:08_

----

I believe `onMobEngaged` gets called again upon successive engages after wipes. So may want to leverage the sets for the wave behavior (will have to check current wave var for the race) with a `limbus.allDead` call to make sure you're not double-spawning a wave after a wipe.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 04:50:44_

----

Will Dee Wapa need a mixin for Astral Flow?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 04:53:13_

----

ffxiclopedia is claiming each of these bosses have different damage type weaknesses and immunities. I'll admit I'm too lazy to check pools, but are these being handled?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 04:57:46_

----

Yeah, some things would probably be best to address when it's all on the same branch for sure. I don't intend to hold either of these Limbus PRs for that reason~

(And I want to start getting hands on with Limbus sooner 😉 )

Just doing reviews for later reference!


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 20, 2020 at 06:07:56_

----

I think they're missing their weakness/resistance since I wasn't sure what values to use.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 20, 2020 at 06:09:43_

----

Yeah I'm not sure why it's not there, the other 2 have them. 🤔


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 23:35:30_

----

What's going on with the skill list check? Will checking form not cover it?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 23:38:27_

----

Do we have to make sure the player is alive before sicking a gunpod on them? 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 23:47:11_

----

I'm wary of hard-set skill list ID checks, and I realize hard-set pool checks aren't much better.

Would a local var be better instead? `if mob:getLocalVar("lasers_active")`

Versions of Omega who should start with active lasers can have it set onMobSpawn, and then versions who activate their lasers later can have the var set on their form change.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 23:48:19_

----

I want to say this should be doing damage (judging by the "additional effect" description on wiki instead of "petrifies target"), but haven't been able to find any information as to how _much_. Marking for later~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 00:49:05_

----

formTime was set to be `os.time()` a little above on L33; I'm not sure if you intend this to be immediately triggered (during the hpp-triggered form change check above), or some set time after the form change is triggered (in which case, the `formTime` wasn't added to or set to the mob)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 03:38:52_

----

While pairs isn't _guaranteed_ to always evaluate in the same order, it will _tend_ to do so, so drops will tend to abort on the first matching item in the list rather than distributed by drop rate.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 03:44:19_

----

Looking at the [spiffy new chart SE has provided us](https://www.bg-wiki.com/bg/Treasure_Hunter), I think these might all be in the Rare category.

But I don't know how these rates apply to the drop groups that gunpods have - could it be that an entire category has a certain rate (ie: Very Common or Common), and then drops within that category are evenly distributed?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 03:49:36_

----

Looks like something weird may have happened with the beastcoin tables here


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 04:16:10_

----

The mission version uses some of the same skills.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 04:29:22_

----

I didn't get any damage message when testing the move, only petrified.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 04:32:41_

----

It triggers the first time right after the block above, then every 60s after that using the `formWait` localvar.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 04:35:06_

----

This group drops 5-6 coins so they each get an individual slot.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 04:38:10_

----

I figured the Gunpod is similar spread as the chests. I was thinking they're probably all even chance but just went with wiki drop rates since that was what everything else was using, and set each group as an equal chance of dropping from the Gunpod.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 04:43:39_

----

Hey @project-topaz/researcher , got a question for ya! (aether didn't see it in capture)

> [Fires aft lasers at players behind user. Additional effects: Petrification](https://ffxiclopedia.fandom.com/wiki/Rear_Lasers)

> [Deals physical damage + Petrification.](https://www.bg-wiki.com/bg/Omega)

Can this move miss? Are the wikis full of lies?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 04:43:59_

----

That's how it's supposed to work, it picks a random group, then rolls for each slot. The first loop through pairs is just to get a max value to roll with, allowing for non-1000 totals, and order doesn't need to be maintained.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 04:44:40_

----

I thought os.time was in seconds though, so on the first loop, formTime would be == os.time()


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 04:47:55_

----

Yeah, but on the second loop through the lootGroup, so long as your random is a high enough roll, you'll always get the first item and break out (below), so actual droprate will be skewed in favor of whichever item is listed in the table first.

edit: Potential confusion point between us: the roll is done once outside the loop


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 04:50:12_

----

Oh, looking again, you do ipair through each of the subtables inside loot[random]; I thought these additional beastcoin tables weren't being stepped through due to being nested too deep.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 04:58:00_

----

You might be right, but the next fight tick formTime will be 0 until it gets set in that block so it triggers then.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 05:00:45_

----

That works~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 05:17:47_

----

Others: Nevermind, we spoke on Discord, and I understand loot bags now.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 05:44:58_

----

Localvar would work just need to set it for mission mob as well.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 18, 2020 at 19:34:05_

----

As strange as it sounds, I recall hearing that there are issues with pathing if the points are floats.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 18, 2020 at 19:41:54_

----

@project-topaz/researcher  Usual, "is this retail?" question


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 18, 2020 at 21:28:34_

----

0 * 5 = 0 😉 

May need to make your min 1 and adjust starting point accordingly.

(Same goes for Thiazi)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 18, 2020 at 23:51:58_

----

Can put a break here


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Apr 19, 2020 at 04:02:44_

----

Yeah it's either the base mob `ID.mob.APOLLYON_NE_MOB[3]` or some multiple * 5 of it depending how many people are in party and thus mobs to spawn on the next floor. So `math.random(0,1)*5` is 50/50 which mob on the next floor, base mob, or base mob + 5.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 19, 2020 at 04:05:18_

----

I'm still not clear on why but several entities would not move until the value were set to integers, so the bug is real.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Apr 19, 2020 at 04:05:49_

----

Oh, it's not any of the freshly spawned mobs?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Apr 19, 2020 at 04:16:10_

----

This is when the mobs for the next floor spawn and also when we roll to see which one drops what.
```lua
Sweeper -- ID.mob.APOLLYON_NE_MOB[3]+(0*5) potential portal mob
Cleaner -- ID.mob.APOLLYON_NE_MOB[3]+1+(0*5) potential item chest
Cleaner
Cleaner
Cleaner
Sweeper -- ID.mob.APOLLYON_NE_MOB[3]+(1*5) potential portal mob
Cleaner-- ID.mob.APOLLYON_NE_MOB[3]+1+(1*5) potential item chest
Cleaner
Cleaner
Cleaner
Sweeper -- ID.mob.APOLLYON_NE_MOB[3]+(2*5) potential portal mob
Cleaner-- ID.mob.APOLLYON_NE_MOB[3]+1+(2*5) potential item chest
Cleaner
Cleaner
Cleaner
```
The cleaners could maybe be randomized better.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Apr 19, 2020 at 04:18:31_

----

I set the wallhack flag for anything that wasn't moving for me, there were a few that would get stuck on stuff.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 19, 2020 at 04:28:41_

----

wall hack should turn on automatically for mobs that can't get to their next position, maybe thats what broke.


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Sunday Apr 19, 2020 at 17:45:00_

----

10 seconds, just checked on retail!


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Apr 19, 2020 at 21:59:33_

----

This whole pathing thing probably needs to be redone, I just wanted to get the positions down. The 40 seconds is the 30 seconds it takes for it to traverse the path then 10 seconds waiting before moving to next point.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 01:00:16_

----

What's going on here during engage? Are we trying to get the others to stop pathing?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 01:07:42_

----

Does the floor boss not spawn without a Flying Spear being killed?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 20, 2020 at 01:34:38_

----

I may be wrong here, but if you're careful when you spawn into this floor to not get aggro by the one close to where you spawn in, it doesn't look like they start roaming until one of them engages. May need further confirmation. That's what it looked like to me and made sense as some "wake the dead" mechanic.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 20, 2020 at 01:35:15_

----

It's an NPC until someone kills one of the Flying Spears.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 01:41:48_

----

Oh, you told me about this one and I forgot. Sorry!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 03:01:15_

----

I'll have to double-check the elemental behavior, but this is where sets can help you out, with maybe a new helper function in limbus.lua

```lua
-- somewhere.lua
limbus.something.fomor.hume = set{ ID.mob.APOLLYON_SW_MOB[1]+2, ID.mob.APOLLYON_SW_MOB[1]+7 }
limbus.something.elemental.fire = set{ ID.mob.APOLLYON_SW_MOB[4]+2, ID.mob.APOLLYON_SW_MOB[4]+10, ID.mob.APOLLYON_SW_MOB[4]+18}

-- limbus.lua
tpz.limbus.allDead = function(mob, mob_set)
    for id, _ in pairs(mob_set) do
        if not GetMobByID(id):isDead()
            return false
        end
    end
    return true
end

-- fir_bholg.lua
onMobDeath(mob, player, isKiller)
    if race == 1 or race == 2 and limbus.something.fomor.hume[mob:getID()] then
        if tpz.limbus.allDead(mob, limbus.something.fomor.hume) then
            -- chests
        else
            -- portal
        end
    end
end

-- fire_elemental.lua
onMobDeath(mob, player, isKiller)
    if day == 0 and tpz.limbus.allDead(mob, limbus.something.elemental.fire) then
        -- chests
    end
end


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 03:53:12_

----

```lua
if id == leafless then
    -- open portal
else
    local add_mob = GetMobByID(mobID + 7)
    add_mob:setPos(mobX, mobY, mobZ)
    add_mob:setSpawn(mobX, mobY, mobZ)
    add_mob:spawn():updateEnmity(player)
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 03:55:05_

----

I believe this mob might be a sapling 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 03:55:19_

----

So many Dhalmels on this floor~!


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 20, 2020 at 04:10:07_

----

Why did I do this! 🤦‍♂️


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 20, 2020 at 04:38:34_

----

I like what you did, would like to wait till both zones are in the same branch so I can do it all at once.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 04:39:26_

----

This can be cleaner with sets, a helper function, and doing this on the onDeath of the summoned mobs (no need for onMobFight)
```lua
-- somewhere.lua
limbus.something.cs_apollyon.yagudo_wave1 = set { ID.mob.APOLLYON_CS_MOB[3]+3, ID.mob.APOLLYON_CS_MOB[3]+4, ID.mob.APOLLYON_CS_MOB[3]+5 }

limbus.something.cs_apollyon.yagudo_wave2 = set { ID.mob.APOLLYON_CS_MOB[3]+6, ID.mob.APOLLYON_CS_MOB[3]+7, ID.mob.APOLLYON_CS_MOB[3]+8 }

tpz.limbus.handleWave = function(mob, race)
    local battlefield = mob:getBattlefield()
    local wave_var = battlefield:getLocalVar(race .. "_wave")
    local wave_set = limbus.something.cs_apollyon[race .. "_wave" .. wave_var]
    if wave_set[mob:getID()] and tpz.limbus.allDead(wave_set) then
        local next_wave = (wave % 2) + 1
        battlefield:setLocalVar(race .. "_wave", next_wave)
        local next_set = limbus.something.cs_apollyon[race .. "_wave" .. next_wave]
        -- get the boss mob based on race somehow; table lookup, if check, whatever - make it race_boss
        local boss_pos = race_boss:getPos()
        for id, _ in pairs(next_set) do
             local mook = GetMobByID(id)
             mook:setSpawn(boss_pos.x, boss_pos.y, boss_pos.z)
             mook:setPos(boss_pos.x, boss_pos.y, boss_pos.z)
             mook:spawn():setMobMod(tpz.mobMod.SUPERLINK, mob:getShortID())
        end
    end
end

-- all yagudo mook luas
function onMobDeath(mob, player, isKiller)
    tpz.limbus.handleWave(mob, "yagudo")
end

-- beastmen mob boss luas
function onMobFight
    -- Nothing! New waves are handled on death of the mooks!
end


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 04:42:31_

----

This would probably be better in onBattlefieldTick instead of onMobFight~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 04:47:08_

----

I believe `onMobEngaged` gets called again upon successive engages after wipes. So may want to leverage the sets for the wave behavior (will have to check current wave var for the race) with a `limbus.allDead` call to make sure you're not double-spawning a wave after a wipe.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 04:50:44_

----

Will Dee Wapa need a mixin for Astral Flow?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 04:53:13_

----

ffxiclopedia is claiming each of these bosses have different damage type weaknesses and immunities. I'll admit I'm too lazy to check pools, but are these being handled?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 04:57:46_

----

Yeah, some things would probably be best to address when it's all on the same branch for sure. I don't intend to hold either of these Limbus PRs for that reason~

(And I want to start getting hands on with Limbus sooner 😉 )

Just doing reviews for later reference!


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 20, 2020 at 06:07:56_

----

I think they're missing their weakness/resistance since I wasn't sure what values to use.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Apr 20, 2020 at 06:09:43_

----

Yeah I'm not sure why it's not there, the other 2 have them. 🤔


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 23:35:30_

----

What's going on with the skill list check? Will checking form not cover it?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 23:38:27_

----

Do we have to make sure the player is alive before sicking a gunpod on them? 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 23:47:11_

----

I'm wary of hard-set skill list ID checks, and I realize hard-set pool checks aren't much better.

Would a local var be better instead? `if mob:getLocalVar("lasers_active")`

Versions of Omega who should start with active lasers can have it set onMobSpawn, and then versions who activate their lasers later can have the var set on their form change.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 20, 2020 at 23:48:19_

----

I want to say this should be doing damage (judging by the "additional effect" description on wiki instead of "petrifies target"), but haven't been able to find any information as to how _much_. Marking for later~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 00:49:05_

----

formTime was set to be `os.time()` a little above on L33; I'm not sure if you intend this to be immediately triggered (during the hpp-triggered form change check above), or some set time after the form change is triggered (in which case, the `formTime` wasn't added to or set to the mob)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 03:38:52_

----

While pairs isn't _guaranteed_ to always evaluate in the same order, it will _tend_ to do so, so drops will tend to abort on the first matching item in the list rather than distributed by drop rate.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 03:44:19_

----

Looking at the [spiffy new chart SE has provided us](https://www.bg-wiki.com/bg/Treasure_Hunter), I think these might all be in the Rare category.

But I don't know how these rates apply to the drop groups that gunpods have - could it be that an entire category has a certain rate (ie: Very Common or Common), and then drops within that category are evenly distributed?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 03:49:36_

----

Looks like something weird may have happened with the beastcoin tables here


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 04:16:10_

----

The mission version uses some of the same skills.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 04:29:22_

----

I didn't get any damage message when testing the move, only petrified.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 04:32:41_

----

It triggers the first time right after the block above, then every 60s after that using the `formWait` localvar.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 04:35:06_

----

This group drops 5-6 coins so they each get an individual slot.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 04:38:10_

----

I figured the Gunpod is similar spread as the chests. I was thinking they're probably all even chance but just went with wiki drop rates since that was what everything else was using, and set each group as an equal chance of dropping from the Gunpod.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 04:43:39_

----

Hey @project-topaz/researcher , got a question for ya! (aether didn't see it in capture)

> [Fires aft lasers at players behind user. Additional effects: Petrification](https://ffxiclopedia.fandom.com/wiki/Rear_Lasers)

> [Deals physical damage + Petrification.](https://www.bg-wiki.com/bg/Omega)

Can this move miss? Are the wikis full of lies?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 04:43:59_

----

That's how it's supposed to work, it picks a random group, then rolls for each slot. The first loop through pairs is just to get a max value to roll with, allowing for non-1000 totals, and order doesn't need to be maintained.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 04:44:40_

----

I thought os.time was in seconds though, so on the first loop, formTime would be == os.time()


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 04:47:55_

----

Yeah, but on the second loop through the lootGroup, so long as your random is a high enough roll, you'll always get the first item and break out (below), so actual droprate will be skewed in favor of whichever item is listed in the table first.

edit: Potential confusion point between us: the roll is done once outside the loop


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 04:50:12_

----

Oh, looking again, you do ipair through each of the subtables inside loot[random]; I thought these additional beastcoin tables weren't being stepped through due to being nested too deep.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 04:58:00_

----

You might be right, but the next fight tick formTime will be 0 until it gets set in that block so it triggers then.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 05:00:45_

----

That works~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 21, 2020 at 05:17:47_

----

Others: Nevermind, we spoke on Discord, and I understand loot bags now.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 05:44:58_

----

Localvar would work just need to set it for mission mob as well.
