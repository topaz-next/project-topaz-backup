**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Friday Oct 30, 2020 at 02:36:06_
_Originally opened as: project-topaz/topaz - Issue 1456_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

I noticed this doing classic Dynamis. The spell "death" has no further restrictions on itself, so bosses who have it on their spell list can select it on par with any other spell as if it was Rasp or Aero. I feel this is generally speaking an issue in the selection of magic spells on mobs, where there's no difference being made in the tier of spells.

What's even worse though, the Dynamis bosses seem to absolutely spam it and give it preference over other spells they should cast, like Breakga, Graviga etc. It's not that they don't cast anything else (after all their lists are correct), but about eight out of ten times or maybe even nine, they'll cast death as long as they have mp > 666. This is weird to me, because there is no obvious reason they should choose death more often than any other spell. Yet they clearly do.

Apparently there's different conditions on different mobs for the use of this spell to begin with. Some get access to it after a certain amount of HP, some after rereasing several times and others just have free access at all times. Diabolos for example can cast it quite frequently supposedly. I have watched a lot of classic Dynamis videos today though, and it's clear that these don't. ~~Instead they will absolutely [spam TP moves](https://www.youtube.com/watch?v=OfpFEbL6q70) probably due to very high regain and/or low TP trigger (video from april last year, only three people constantly hitting, doesn't even get to cast because of TP preference...)~~(wrong reference)

I also checked Dynamis Lord and he uses the rest of his list a bit more often, but still uses death way too frequently.

I wanted to propose a math.random condition right inside of "death.lua" but this would then just return and not cast any other spell when called, and as mentioned, death gets called almost always. Super weird.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 30, 2020 at 03:01:14_

----

its a combination of our lack of any per-spell cooldowns for mobs (thus allowing same spell to be chosen again when the mobs global cast timer is up) and the spell selection code not matching how retail chooses spells.

Here is the logic for spell selection:
https://github.com/project-topaz/topaz/blob/e5750c30b8685a198661a8743ea92a13c91fee83/src/map/ai/controllers/mob_controller.cpp#L392

https://github.com/project-topaz/topaz/blob/8648c4071c1885ad1a388d74e7f868e39df2f75e/src/map/mob_spell_container.cpp#L123

There are a few mobmod's that influence selection on a category basis: Ga's, buffs, Cures... On the monsters AI engage they have a higher chance of using a Ga spell currently.

Keep in mind anytime we leave stuff up to just random numbers, streaks are normal - you can randomly get the same numbers repeatedly and if that didn't happen its a sign its not actually random. Human brains give patters meaning, CPUs do not. People tend to think that streaks in random sequential events are rare and remarkable. When they actually encounter streaks, they tend to consider the underlying process as non-random. That isn't to say there is no problem but rather to say we probably wnat to find out asmuch as we can about how retail chooses the spell in this situation, rather than just relying on random numbers - there definitely is a problem (several in fact) and the frequency with with a mob pulls DEATH out of its hat is abnormal (have witnessed first hand,  and suspect something is causing it to be weighted towards it in some way) but I have no freaking clue what to suggest to to fix the selection. 

I don't think returning out with the deciding factor of it being a _second_ random roll is a good solution even temporary. Like I said, random can have streaks. Maybe for now, set a locallVar containing a timestamp on the mob on casting, and check that in the spell check to simulate a "death cooldown". That would still be a band-aid though.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Friday Oct 30, 2020 at 05:45:59_

----

Great pointers there Teo. So, apparently there's something off here further down the road (in `mob_spell_container.cpp`):

1. All spells from the spell list are roughly categorized (fair enough)
2. AoE spells are those who have it's aoe flag set higher than 0 and can target the current enemy (ok)
3. Any other spell that can target the enemy is considered a damage spell (wait what?) -- This makes debuffs "damage" spells
4. Then there's three more categories for white magic spells (-na, cures and buffs)

So funnily enough next up there's something in there which I also wanted to point out in another issue: `::GetAggroSpell()`
If the mob has any spell that can target the enemy it will always start the encounter with a spell. Priority is given to -ga spells based upon `MOBMOD_GA_CHANCE` which apparently has to be set to make the roll possible. Else, any "damage" spell (or well, debuffs too I guess) will be selected to immediately cast when aggro'ed.
This is simply not accurate. I think it can be generally observed on retail that monsters will not *necessarily* cast when aggro'ed. This is especially true for NMs from what I can see in captures and videos. This is apart from this issue though, but it is interesting nonetheless.

So despite the accuracy of the former, for now if the mob has no `MOBMOD_GA_CHANCE` set (or it is extremely low), it will practically always open with a spell from the collected "damage" spells vector. (Death anyone?)

**HOW THE ISSUE ARISES**

Throughout the fight `::GetSpell()` determines the actual roll of the various spells given in a spell list.
This is where I'd argue that the thinking behind this function is not well designed. It is a strict top to bottom priority list.

1. Make a roll for heals above all if HP is low in relation to `MOBMOD_HP_HEAL_CHANCE`
2. Make a roll for -na spells if they exist in relation to `MOBMOD_NA_CHANCE`
3. Make a roll for AoE spells in relation to `MOBMOD_GA_CHANCE`
4. Make a roll for "buffs" in relation to `MOBMOD_BUFF_CHANCE`

Until here, I'd say it's fair enough to prioritize *based on a mobMod*. Because that's what you want to achieve by setting such a modifier to begin with.
If all of these mods are 0, they'll all fail. This the default case (all exceptions failed). Now for the funny part.
The next conditions are all called in that default case situation and are blocking each condition further down:

5. Do not roll, instead use any of the "damage" spells (again, debuffs count I guess...)
6. If there is absolutely no "damage" (debuff anyone?) in the spell list, do not roll, instead use a "buff" if it exists
7. If there is absolutely no damage or buff in the list, use a -ga spell instead (interesting order)
8. If there is absolutely none of the above, use a cure...
9. If there's not even a cure,...return...

So this part is bad in my opinion. I simply changed 7. with 5. so -ga spells would block all the others, recompiled, and low and behold, the dyna bosses would suddenly spam their -ga spells and *not once* cast "death" (because the CPU only knows conditions, and there is no exceptional one for "damage" spells). This affects *way* more mobs though. If a mob has no modifier for this or a very low one, there's no real roll for any of the spells, it's strictly prioritized. Maybe the idea here was to have a low default `MOBMOD_GA_CHANCE` to use more damage spells by default, but the "death" example shows a flaw here.

This can be observed so well on the dyna bosses because they only have several AoE spells, and one "damage" spell, but since they very obviously lack a decent modifier (must be very low because they very occasionally do cast a -ga spell) they'll just spam "death" (their only "damage" spell) because that's where the condition ends. The only other two moves they will use are their TP moves, which is fine.

Again, this is extremely simple to reproduce/test/debug by simply swapping these around.

**TL;DR**
I'd argue these hard failing conditions should be refactored to something more sensible. Maybe something like:

1. Try to use a buff above all else if the buff is not active
2. Try to use any other spell but make a roll and give highest percentage to "damage", then "-ga" then "cure" spells (if any exist)

In the case of "death": remove the spell from the corresponding lists and add it individually to each mob that uses it with individual trigger percentage (even if that meant two rolls). You could argue to simply raise `MOBMOD_GA_CHANCE` on these mobs, but I'd say that "death" must not be considered to be on the same level as "Aero", "Rasp" or "Blind", and making exceptions for a single spell is not the right place here.

This whole issue applies to other high tier spells like "Meteor" or "Impact" (or whatever spells some bosses and HNMs may use nowadays) too actually. There is absolutely no difference being made between any of the single-target "attack" (even including debuffs) spells.

If you find any of what I said to be wrong, dumb or questionable, feel free to call me out, it's late, I'm new to the project, but that's what I mean to see here.



----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Friday Oct 30, 2020 at 21:54:06_

----

The following is a proposal for a sensible workaround on a per-mob basis for "Death" casting mobs.
**The issue with the design of the core function `CMobSpellContainer::GetSpell()` remains.**

- Remove "Death" from spell list
This prevents the possibility of opening instantly with death cause it is no more on the "damage" spell list for `::GetAggroSpell()`
- Make a roll on every cast made by the mob for a chance on being able to cast "Death"
- When this chance is met the first time, cast "Death" shortly (10s) thereafter
This gives the possibility of seeing "Death" 10 seconds after the very first cast. Maybe not a good idea?
- After that first cast, set recast time to 2 minutes

```LUA
function onMobFight(mob, target)
    local deathSpellEnabled = mob:getLocalVar("deathSpellEnabled")
    local deathSpellTimeout = mob:getLocalVar("deathSpellTimeout")
    local deathSpellCounter = mob:getLocalVar("deathSpellCounter")

    -- DEBUG
    if deathSpellEnabled == 1 then
        printf("%dseconds left until Death!", deathSpellTimeout - os.time())
    end

    -- Trigger "Death" spell
    if notBusy(mob) and deathSpellEnabled == 1 and os.time() > deathSpellTimeout then
        mob:castSpell(367, target) -- cast "Death"
        mob:setLocalVar("deathSpellEnabled", 0) -- make it unavailable
        mob:setLocalVar("deathSpellCounter", deathSpellCounter + 1) -- increase counter
        printf("Death was disabled and counter increased by one!") -- DEBUG
        printf("Death has been cast %d times now.", deathSpellCounter) -- DEBUG
    end

    -- Make a roll on every cast to enable "Death" spell
    -- Currently this makes more than a dozen rolls because of onMobFight() firing way too often
    -- This is known and worked on as of late October 2020
    -- TODO: Could be adjusted once onMobFight() rate is fixed
    -- TODO: Could check if the current cast is "Death" to prevent a roll on itself
    if mob:getCurrentAction() == tpz.act.MAGIC_CASTING and deathSpellEnabled == 0 then
        if math.random(100) < 5 then -- keep it low because maaaany rolls
            mob:setLocalVar("deathSpellEnabled", 1) -- flag the spell as available
            if deathSpellCounter > 0 then
                mob:setLocalVar("deathSpellTimeout", os.time() + 120) -- after first use set a sensible recast time
                printf("Death was enabled and will be cast in 120 seconds!") -- DEBUG
            else
                mob:setLocalVar("deathSpellTimeout", os.time() + 10) -- first use, just avoid instant double cast
                printf("Death was enabled and will be cast in 10 seconds!") -- DEBUG
            end
        end
    end
end

local function notBusy(mob)
    local action = mob:getCurrentAction()
    if
        action == tpz.act.MOBABILITY_START or
        action == tpz.act.MOBABILITY_USING or
        action == tpz.act.MOBABILITY_FINISH or
        action == tpz.act.MAGIC_CASTING
    then
        return false
    else
        return true
    end
end
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 30, 2020 at 23:30:56_

----

what did onMobFight ever do to you to be abused like that? :cry: 


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Friday Oct 30, 2020 at 23:42:20_

----

Hahaha, sorry, I do see why onMobFight() is undesirable...I'm open for any suggestions. After all this is not a PR.
Thing is, if you simply block the spell from its script with a localVar like you mentioned, there's two apparent and huge downsides:
- The spell will instantly get called on aggro due to the core function being funny
- you have no fine control over what mob can use it more or less frequently


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 30, 2020 at 23:52:46_

----

btw. Over**seer**'s Tombstone (in your vid) and Over**lord**'s Tombstone are 2 diff mobs that don't have necessarily the same spell lists.

Have yet to see the one in Dyna D cast _at all_

And it looks to me the reason for deaths high frequency is it is considered a damage spell and the only damage spell it has, while the recast (Graviga, Bindga, Paralyga, and Sleepga.) are debuffs with lower priority. I don't blame the previous coder(s) for this - what would you guess it should categorize as, I mean, _it instant kills you_. We can test this theory by cranking up debuff chance and reducing dmg spell cast via mobmods.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Oct 30, 2020 at 23:54:05_

----

1. onMobFight fires each combat tick - this will not be changed. If the _combat tick rate_ is "too fast" then it needs to be adjusted at the AI level, as it affects more than just scripting calls.
2. If something inside onMobFight is "too often", then onMobFight is being used wrong.
3. Rates should never be deliberately defined based on how often a check fires. We already have this trap for TP use. It's wrong, and the methodology needs to die.
4. We're not putting special Death logic in individual mobFights. If necessary, mobs can have their own spell script, and it should probably be a mixin.
5. BLM mobs cast on aggro. The behavior is in core because its observable on retail.
6. The video you linked is Divergence - the mob spams TP because [it has no spells](https://www.bg-wiki.com/bg/Overseer%27s_Tombstone).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Oct 31, 2020 at 00:03:47_

----

Core link re: [mob spell scripts and onMonsterMagicPrepare](https://github.com/project-topaz/topaz/blob/e5750c30b8685a198661a8743ea92a13c91fee83/src/map/ai/controllers/mob_controller.cpp#L370-L386)

(Assuming there's a problem that can only be solved on the individual mob level.)


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Saturday Oct 31, 2020 at 00:15:00_

----

As mentioned, the mobs in question could also simply have their MOBMOD_GA_CHANCE increased in the database so they'd roll more frequently on -ga spells. Actually this would be the least intrusive workaround to the topic. The fact that all mobs without that mobmod (or a very low value) block -ga spells, remains.

How about just changing the GA_CHANCE for now and open a separate issue for the core function?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 31, 2020 at 00:16:38_

----

> I thought I pointed exactly that out pretty verbosely? 

damage spell doens't mean ga spell


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Thursday Nov 05, 2020 at 04:27:20_

----

I consider this resolved.
For any future reference:
`tpz.mobMod.SEVERE_SPELL_CHANCE` can now be used to adjust the rate with which "Death" and similar deadly spells can be cast.
See the details of #1469
