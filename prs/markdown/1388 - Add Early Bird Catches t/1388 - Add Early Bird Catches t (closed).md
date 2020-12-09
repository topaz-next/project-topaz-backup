**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Oct 18, 2020 at 11:23:06_
_Originally opened as: project-topaz/topaz - Issue 1388_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

_ Was missing spells: Absolute Terror, Horrid Roar and Flame Blast
_ Had a wrong default subanimation in the database blocking all skills
_ Flame Blast has a messed up animation ID, all three versions. I adapted the animation ID of Inferno Blast, they're exactly the same
_ Does draw-in with the known perk of being able to pop out of bounds when drawing in while flying, like Tiamat
_ Opens the battle with a mobskill
_ Goes airborne at 66%HP and then evades all melee attacks
_ Uses a different fire magic based ranged attack while in air as well as Flame Blast and Hurricane Wing
_ Hurricane Wing in the air would be a TODO since I couldn't find the right skill for this. The standard wing is a ground animation
_ Flame Blast can be used only while in air and with full TP
_ Uses Touchdown at 33%HP and returns to all the standard wyrm attacks
_ Also gains increase in Eva, Def and M.Def after landing until death
_ Code is commented where it makes sense

The drops are already working so this would make Early Bird Catches the Wyrm complete.
- [x] Tested locally working extensively


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 18, 2020 at 11:43:28_

----

Can replace with
```lua
if not mob:actionQueueEmpty() then
    return
end
```

To spare yourself assigning isBusy and checking against both it and the actionQueue later.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 18, 2020 at 11:44:00_

----

We have a `mob:getHPP()`~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 18, 2020 at 11:52:33_

----

To whoever might know:
`effectFlag.DEATH` is used to mark status effects that should be removed on death.

Is this necessary for BCNM mobs? I was under the impression mobs were totally destroyed and recreated between fights, so they wouldn't have boosts like these even without the flag.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 18, 2020 at 11:54:16_

----

Judging by the skill list you're using below, I have a feeling this ability should be 954.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 18, 2020 at 11:56:58_

----

I wonder if we should rename the skill list name so it's clear that it's only for the KS99 "Wyrm" and not potentially confused for "All wyrms".


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 18, 2020 at 11:59:01_

----

Judging by the nearby skill IDs, 657 is probably correct (and Touchdown is 956).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 18, 2020 at 12:04:09_

----

This will set it to use Tiamat's alternative skill list, which contains only Inferno Blast - not the Flame Blast you're wanting Wyrm to use.

Others: At some point we should rename this function to include the word "list".


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 18, 2020 at 15:03:37_

----

I ran into this while looking up "Wyrm" on bgwiki...


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 18, 2020 at 20:24:07_

----

every respawn any effects they had in their previous life are gone, except for those specified in onMobInitialize()


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 18, 2020 at 20:27:43_

----

Every wyrm has its own set of skill IDs and there is NO OVERLAP. SE duplicated the IDs each and every time, even if the skill _names_ are identical. So even with the same moveset as Fafnir or Nidhogg, you do not use those IDs. you use the ones specifically for this Wyrm. Which is why faf and nid both have the ones associated with flying even though they do not - duplication! 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 18, 2020 at 20:28:24_

----

my vote for `KS99_Wyrm`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 18, 2020 at 20:30:57_

----

@ibm2431 I propose `mob:meleeSkillList()` Normal melee being 0. Its never unset or even `get`'d so no real point is specifying `set` in its name anyway.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 00:22:51_

----

Funnily 1282 uses animation ID 656 anyways, like ALL the touchdowns do, I don't know why 954 did not (was broken). I fixed that and will use 954 instead.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 00:28:52_

----

That is not supposed to be Flame Blast. Flame Blast is included in the Wyrm's skill list with its own proper ID, had a script created, works as expected and can be used as a normal mobskill during flight.

Tiamat and Wyrm are the only wyrms in Vana'diel that during flight use a fire spit-like magic based regular attack. There's also a wind and an ice version of this. Tiamat uses `SetMobSkillAttack` so I re-used this.

Indeed it brings some issues with it though. I observed and debugged that this actually makes the `mob` use a TP mobskill unconditionally now, using all TP on every regular hit. This is why I was having trouble getting Flame Blast to trigger during flight. The Wyrm would reset TP on every hit. (Tiamat has this very same issue apparently, but is not part of this PR)

Also, Teo you make a point about no overlapping IDs, but Fafnir is apparently using all those skills in its list, when it's most probably supposed to be exclusive to Wyrm by this assumption (all of these are next to Flame Blast, which is exclusive to Wyrm). How should I proceed with this then? I won't change Fafnir in this PR. From scanning through all the wyrm related skills it does actually seem as if Fafnir and Wyrm share these tbh. Nidhogg has its own version of spike flail, and there's nothing in between these. For this PR I'd say I can safely stick to skills 951-958.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 00:30:11_

----

Makes sense. Is already fixed and will be resolved with a future push.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 00:30:37_

----

Fixed and will be resolved with a future push. Thank you for the pointer.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 00:31:29_

----

From latest testing I find that checking only for `actionQueueEmpty()` does not prevent animation overflow. The animation for `AnimationSub(0)` will still overwrite `Touchdown`. This function is called really fast. I propose a mixed use, which from my testing seems to work as expected (Touchdown finishes and then stays on ground). This way I can still remove all the later checks.

```LUA
    -- Testing for actionQueueEmpty() does not prevent overflow
    if action == tpz.act.MOBABILITY_START or action == tpz.act.MOBABILITY_USING or action == tpz.act.MOBABILITY_FINISH then
        isBusy = true -- when the Wyrm is in any stage of using a mobskill
    end
    -- Do nothing if currently doing something else already
    if isBusy then
        return
    end
```



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 19, 2020 at 00:59:00_

----

I had similar probs with other mobs I worked on that changed animation states. What Kjlotus told me was the action queue is basically _never_ empty. I suggest turning it into a local function instead of defined inside onMobFight, and then you can just use it as the condition before other logic executes instead of returning out. `if notBusy() then`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 19, 2020 at 01:07:39_

----

much old stuff is not 100% accurate if that helps make sense of weirdness you see. There should (in the client) be a duplicate for each of them, because the way SE does it on their retail server and the client its associated with the model and thanks to ps2 limitations when they were in the design phase anytime they made a new model it spawned a new copy of everything along with it. So they clone Wyrm and color change it, poof we have Fafnir and they just disable the flight one their aren't using. They do it again and change the colors and strings for the skill names, hello Tiamat and Jormy. 

@Hozu & @MarianArlt 
Kjlotus used an unused blank skill to make Nid's "super buff" because Nid will never use that entry in the list normally, and the other wyrms won't use super buff. Any other Wyrm that does use it shouldn't be teh same list entries Nid uses (again, duplicates)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 19, 2020 at 01:18:02_

----

elaborating a bit:
@MarianArlt basically, in early DSP we did not have teh ability to create additional skill lists, and we tied everything to a mob family ID. tahts since been corrected so we can do mob skill lists per mob just like retail, but not everything form back then is split up or even needs to be (we do not yet have a reason to create multiple separate screwdiver version for different puguils for instance, since they all work as is and players don't know the difference - good enough right?) But somewhere in the master list of skills, there are multiples for many things. I happen to know Wyrms moves are among them having made a bunch of custom ones for another server once upon a time.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 06:53:07_

----

I did as you suggested and outsourced this into its own local function for re-use in later conditions. Works well.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 06:55:33_

----

Can I mark this as resolved or do you want me to create a unique spell with this and then append a skill list entry for `KS99_Wyrm-Flying-Attack` in `mob_skill_lists.sql`?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Oct 19, 2020 at 10:07:12_

----

There aren't skill or magic like regular attacks (category 2). Any time you see a mob appear to use something like that for a "regular attack", they're mobskills (category 11) with a message of 0. They _look_ like a regular attack to a player, but internally they're different.

In this case, setting a skill list ID of 730 will cause it to use Tiamat's Inferno Blast "alt".
![skill](https://user-images.githubusercontent.com/13112942/96431219-bb799f80-11f2-11eb-8500-cc2adebb67fb.png)




----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 15:11:42_

----

I am well aware of that. It seems to be exactly what SetMobSkillAttack() was created for. Quite some wyrms use it. Where are we going with this though?
As mentioned the only thing regarding this original comment I could do is create more duplicates and write a unique skill in form of `flame_blast_alt` (950 could be used for that e.g.) and then append a skill-list with only that skill just like for Tiamat, Ouryu and Jormy. But it's superfluous and as Teo mentioned, it works like this, the user won't note any difference, why duplicate data for this one skill. (Unless you want me to do exactly this, which is why I'm asking.)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 19, 2020 at 19:18:29_

----

With Wyrms SE put minor variations while they were copy pasting, I can see how my use of the word duplicate has caused some confusion. Tiamats skills are no more KS99_Wyrms skills than they are Jormies, but SE _duplicated_ their template Wyrm to create each of them, if hat makes sense, and lead to certain Wyrms having unused entries - like Fafnir isn't going to touchdown cause he never flies, and that one in abyssea never will coz he or she never lands and this is what I was trying to say, Their breaths and blasts are probably not going to be 100% identical even if the same element.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 19, 2020 at 19:19:01_

----

whatever ID retail is using, is the ID we want to use.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 20, 2020 at 07:12:44_

----

@TeoTwawki & @ibm2431  I have an issue with this. As you can see in in the latest commits I have corrected all the Wyrm specific IDs with their corresponding animation IDs and created two additional skill lists. One for TP skills while flying (airborne Hurricane Wing & AoE Flame Blast), and one for the regular attack while flying (Single target Flame Blast). These three animations can be called individually fine and work as expected when called with `useMobAbility()` for example.

**However**: When I set `mob:SetMobSkillAttack(1146)` I would expect the Wyrm to now use skillID `950` as regular attack, which has the correct animationID and the same column values as all the other flying-attack skills (leet, ocher etc.). **But** the mob just won't use anything at all. It just sits there doing nothing now.
I made sure that the database was correct, including the changes, the right IDs etc. The other regular-attack flying skills work fine and the tiamat one even uses the same animationID...

TL;DR
```LUA
mob:SetMobSkillAttack(1146)
```
does absolutely nothing despite having added new skill lists exclusively for this use, using the correct skill, the correct animation ID etc. database double checked.
`mob:setMobMod(tpz.mobMod.SKILL_LIST, 1147)` works...


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 20, 2020 at 13:43:40_

----

@UynGH Did you try to summon trusts in the BCNM? I saw Zach did, but he wasn't the leader 😆 .


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Tuesday Oct 20, 2020 at 16:25:19_

----

Hello! Just checked:
![1](https://user-images.githubusercontent.com/40763842/96615452-92940000-1301-11eb-829f-a7697681c48b.jpg)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 20, 2020 at 16:42:05_

----

Your sacrifice is appreciated. 🖖 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Oct 20, 2020 at 20:41:59_

----

> does absolutely nothing despite having added new skill lists exclusively for this use, using the correct skill, the correct animation ID etc. database double checked.

its expecting a script with the name that is on skill id 950 that is in that skill list: `flame_blast_alt`


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 20, 2020 at 22:02:56_

----

I thought that too, but how is it possible that `inferno_blast_alt`, `sleet_blast_alt` and `ochre_blast_alt` all work **without** having a script?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Oct 20, 2020 at 22:50:26_

----

bold of you to think somebody didn't ~~break~~ "fix" jormy.

try it. copy you blast to the other name and see if it starts blasting.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Oct 21, 2020 at 08:40:01_

----

As a reminder to myself:
https://github.com/project-topaz/topaz/blob/release/src/map/battlefield.h#L34

I need to add RULES_NO_TRUSTS


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Friday Oct 23, 2020 at 20:37:10_

----

Finally resolved after a few days of overthinking and a little chat. Thank you.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 26, 2020 at 12:18:25_

----

I noticed you have the same check in both versions, where as the other wyrms blast moves have the check in only 1 version. I don't know if that is a problem or not honestly,


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 26, 2020 at 21:11:36_

----

Hmm. Now that you say it, it is actually redundant since I created two dedicated sets for flying mode. One for the regular attack and one for TP moves. Since these are explicitly called for flying mode and then changed back, there's actually no real reason to check again. The other flying wyrms don't have a dedicated flying-mode TP set so they need to check for AnimationSub directly in the TP move skills. Whether or not that's good practice and whether or not there's maybe more flying TP moves from what we've seen, could be looked into in another issue.

I removed these checks completely and made it clear in the header comment that those skills should only be used for flying mode skill sets.

Good thing you came across this cause during this testing I also noticed a leftover of flame_blast in the ground skill set, which was removed, and more importantly:

I earlier resolved a merge conflict that was pushed in the meanwhile ( da852bbbfdf871256fb2309968cce70a5a91cd96 &  https://github.com/project-topaz/topaz/commit/0bd3bad899d48dfb4d2785d331bbc36d073f707f ) with changes to the blocking condition of Dragon Breath of being behind, to not being in front. I accepted these changes. But during this testing session today, this did **not** work at all. The skill won't get called anymore. I first observed this, then did some more testing and after just sitting there and counting 0 out of 20 TP uses (in addition to the formerly observed lacking) of dragon breath, I think it is safe to say this does not work.
I reverted this and it did work again.

I reverted this change only for Dragon breath cause it affects this PR. There's a lot of breaths that had that change made though and should be tested.

- [x] Tested working extensively on a local server


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 23:14:51_

----

Can remove the TODO since Wyrm is coded now. 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 23:17:21_

----

Can specify that this version is the grounded version.

Just to clarify, Flame Blast is supposed to be magical and not a breath attack, right? The skill check is okay (ie: can use regardless of where target is)?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 23:19:45_

----

Since `typeEffect` is only used in in the `MobStatusEffectMove` call, you can use `tpz.effect.BLINDNESS` directly in it without an assignment.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 23:21:45_

----

Is this needed? The status effect _should_ already be gone in a new battlefield, since mobs are destroyed and recreated.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 23:22:19_

----

Can set this to be the ID we discovered in the Nidhogg PR~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 23:43:42_

----

I haven't really examined the Early Bird capture, but be forewarned that if this is based on what HP Track spit out, if the mob has regen the numbers might not be accurate. The accuracy could also vary depending on the estimation method it needed to resort to.

Min and Max will just be the minimum and maximum damage it took to kill the mob, so if there was regen involved, the values will be higher than what the mob's HP truly is, as HP Track has no way of knowing DoT or Regen amounts.

Method I stands for Method Interval, in which it attempts to guess an HP based off of percentage differences it saw the mob's HP % change by, and the damage it took to reach those differences. Because it guesses HP in slices over the entire fight and then averages those guesses together, I consider its estimation more trustworthy than...

Method L stands for Method Last. It compares how much HP% the mob had when it was last seen alive, compared to how much damage the mob has taken over the entire battle before the killing blow. If HP Track last saw the mob alive at 3% after seeing exactly 97000 damage dealt, it'll spit out an estimate of 100,000 HP. However, since retail only sends out HPP updates for whole integers, the mob's true HP range could be 99,000~101,000. In this case we could guess SE selected 100,000, but if the exact damage dealt values, and the original mob's max HP value isn't as "clean", this can be harder to guess.

I consider Method Ls slightly less trustworthy because it only examines the battle at one point in time, _and_ while it may sound like a conspiracy theory, I'm not convinced 1% HP is _actually_ 1% HP. I _swear_ the last 1% takes longer to empty on retail than it "should". So if the last time it saw the mob alive was at this "1%" value, then it can come up with higher numbers if the mob really had more of its True HP remaining during "the last 1%" phase.

Obviously retail is going to round up if the mob is _sub_ 1%, which will lead to further inaccuracies. In HP Track's case, the damage it thinks it took to bring a mob down to "1%" (in this case, the total damage it's seen and is assuming is 99% of the mob's HP) could actually be anywhere from 98.1% (mob had 1.9% remaining) to 99.9% (mob had 0.1% remaining).


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 00:13:31_

----

I think you're getting these mixed up. There is no grounded version Flame_Blast ;)
One is single target regular attack (_alt)
and the other (this one) is the TP AoE skill (only while flying!). Yes it's supposed to be magic damage, not breath.
I double emphasized this in the description now.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 00:16:50_

----

The BCNM cleanup should also happen on wipe, that's what you're saying right? I will test this again.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 00:17:40_

----

This is now pretty much a merge conflict with the other PR, should I change this here?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:22:36_

----

bcnm cleanup happens when the bcnm ends for any reason. a wipe and reraise without the bcnm ending will not trigger onMobSpawn again anyway. but when it respawns in a new bcnm, the effect being dleted here will have already been removed by the mob being re-created again.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 00:23:03_

----

Wow, after reading this I'm now more confused than before even though I appreciate the insight. I do get that HP regeneration might mess up readings though. You're very deep into the whole capturing so, I'd appreciate your instructions on this. It sounds like it would be sensible to revert this back to the 45,000 it had before.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:24:04_

----

![image](https://user-images.githubusercontent.com/6871475/97819618-b8ad8e80-1c77-11eb-872e-1b2c71cd74d6.png)
 he's not to high at spawn. never too high. :wink: 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:25:46_

----

can pull your other one into here after it merges and resolve the conflict, or rebase this onto the other one. If you haven't had much practice with rebase, this is a good opportunity (back up your scripts 1st if not confident)


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 00:34:38_

----

Also on a further note: During flight all Wyrms (should) face their target, so directions do not apply and don't need to be checked for indeed.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 01:03:34_

----

I just merged release into this, I'll keep avoiding rebase as long as possible T_T


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 01:11:00_

----

Looked at the capture:
`46728~51180 HP, Est HP: 49644 (Mthd: L)`
Method L is a little odd in that it [compares the total damage it saw (max) to how much HP% it watched get drained](https://github.com/ibm2431/addons/blob/master/capture/hptrack.lua#L83-L84). This is... actually not accurate, so I should fix that. It should be [comparing the _minimum_](https://github.com/ibm2431/addons/blob/master/capture/hptrack.lua#L78) against what it watched get drained.

But we can use the min HP value to look at the problem from the other direction:
The final hit was a Fell Cleave taking off the final 3% of its HP.

It saw 46727 damage done up to that point. The "minimum HP" is "total damage and still living + 1 HP".
```
(Max HP/100) * 97 = 46727
Max HP / 100 = 481.72
Max HP = 48,172
```

Basically, even pretending the Regen never existed, if 46,727 damage brought it down to 3% HP left, then it can't have more than 48,172 HP.

Even if we assumed that the HP% that retail sends out is _floored_:
(Max HP/100) * 96.1 = 46727 (Note: 100 - 96.1 = 3.9)
Max HP / 100 = 486.233
Max HP = 48,623

Unless there was a DoT on it, there's no way its HP can break 48,623.

So while I'd normally be tempted to slap 50,000 on it because it's a nice, even number, it's just not possible. I'd be okay with 45,000 and assuming it got ~3000 HP restored from regen over the 12 minute fight.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 01:19:07_

----

Makes sense and sounds reasonable indeed. Thank you again for laying it out that much. The conversation didn't get marked as outdated, but I adjusted it accordingly.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 01:23:48_

----

Oh, so this version is the one it'll actually display the message for, got it! Carry on!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 18, 2020 at 11:43:28_

----

Can replace with
```lua
if not mob:actionQueueEmpty() then
    return
end
```

To spare yourself assigning isBusy and checking against both it and the actionQueue later.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 18, 2020 at 11:44:00_

----

We have a `mob:getHPP()`~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 18, 2020 at 11:52:33_

----

To whoever might know:
`effectFlag.DEATH` is used to mark status effects that should be removed on death.

Is this necessary for BCNM mobs? I was under the impression mobs were totally destroyed and recreated between fights, so they wouldn't have boosts like these even without the flag.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 18, 2020 at 11:54:16_

----

Judging by the skill list you're using below, I have a feeling this ability should be 954.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 18, 2020 at 11:56:58_

----

I wonder if we should rename the skill list name so it's clear that it's only for the KS99 "Wyrm" and not potentially confused for "All wyrms".


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 18, 2020 at 11:59:01_

----

Judging by the nearby skill IDs, 657 is probably correct (and Touchdown is 956).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 18, 2020 at 12:04:09_

----

This will set it to use Tiamat's alternative skill list, which contains only Inferno Blast - not the Flame Blast you're wanting Wyrm to use.

Others: At some point we should rename this function to include the word "list".


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 18, 2020 at 15:03:37_

----

I ran into this while looking up "Wyrm" on bgwiki...


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 18, 2020 at 20:24:07_

----

every respawn any effects they had in their previous life are gone, except for those specified in onMobInitialize()


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 18, 2020 at 20:27:43_

----

Every wyrm has its own set of skill IDs and there is NO OVERLAP. SE duplicated the IDs each and every time, even if the skill _names_ are identical. So even with the same moveset as Fafnir or Nidhogg, you do not use those IDs. you use the ones specifically for this Wyrm. Which is why faf and nid both have the ones associated with flying even though they do not - duplication! 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 18, 2020 at 20:28:24_

----

my vote for `KS99_Wyrm`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 18, 2020 at 20:30:57_

----

@ibm2431 I propose `mob:meleeSkillList()` Normal melee being 0. Its never unset or even `get`'d so no real point is specifying `set` in its name anyway.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 00:22:51_

----

Funnily 1282 uses animation ID 656 anyways, like ALL the touchdowns do, I don't know why 954 did not (was broken). I fixed that and will use 954 instead.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 00:28:52_

----

That is not supposed to be Flame Blast. Flame Blast is included in the Wyrm's skill list with its own proper ID, had a script created, works as expected and can be used as a normal mobskill during flight.

Tiamat and Wyrm are the only wyrms in Vana'diel that during flight use a fire spit-like magic based regular attack. There's also a wind and an ice version of this. Tiamat uses `SetMobSkillAttack` so I re-used this.

Indeed it brings some issues with it though. I observed and debugged that this actually makes the `mob` use a TP mobskill unconditionally now, using all TP on every regular hit. This is why I was having trouble getting Flame Blast to trigger during flight. The Wyrm would reset TP on every hit. (Tiamat has this very same issue apparently, but is not part of this PR)

Also, Teo you make a point about no overlapping IDs, but Fafnir is apparently using all those skills in its list, when it's most probably supposed to be exclusive to Wyrm by this assumption (all of these are next to Flame Blast, which is exclusive to Wyrm). How should I proceed with this then? I won't change Fafnir in this PR. From scanning through all the wyrm related skills it does actually seem as if Fafnir and Wyrm share these tbh. Nidhogg has its own version of spike flail, and there's nothing in between these. For this PR I'd say I can safely stick to skills 951-958.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 00:30:11_

----

Makes sense. Is already fixed and will be resolved with a future push.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 00:30:37_

----

Fixed and will be resolved with a future push. Thank you for the pointer.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 00:31:29_

----

From latest testing I find that checking only for `actionQueueEmpty()` does not prevent animation overflow. The animation for `AnimationSub(0)` will still overwrite `Touchdown`. This function is called really fast. I propose a mixed use, which from my testing seems to work as expected (Touchdown finishes and then stays on ground). This way I can still remove all the later checks.

```LUA
    -- Testing for actionQueueEmpty() does not prevent overflow
    if action == tpz.act.MOBABILITY_START or action == tpz.act.MOBABILITY_USING or action == tpz.act.MOBABILITY_FINISH then
        isBusy = true -- when the Wyrm is in any stage of using a mobskill
    end
    -- Do nothing if currently doing something else already
    if isBusy then
        return
    end
```



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 19, 2020 at 00:59:00_

----

I had similar probs with other mobs I worked on that changed animation states. What Kjlotus told me was the action queue is basically _never_ empty. I suggest turning it into a local function instead of defined inside onMobFight, and then you can just use it as the condition before other logic executes instead of returning out. `if notBusy() then`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 19, 2020 at 01:07:39_

----

much old stuff is not 100% accurate if that helps make sense of weirdness you see. There should (in the client) be a duplicate for each of them, because the way SE does it on their retail server and the client its associated with the model and thanks to ps2 limitations when they were in the design phase anytime they made a new model it spawned a new copy of everything along with it. So they clone Wyrm and color change it, poof we have Fafnir and they just disable the flight one their aren't using. They do it again and change the colors and strings for the skill names, hello Tiamat and Jormy. 

@Hozu & @MarianArlt 
Kjlotus used an unused blank skill to make Nid's "super buff" because Nid will never use that entry in the list normally, and the other wyrms won't use super buff. Any other Wyrm that does use it shouldn't be teh same list entries Nid uses (again, duplicates)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 19, 2020 at 01:18:02_

----

elaborating a bit:
@MarianArlt basically, in early DSP we did not have teh ability to create additional skill lists, and we tied everything to a mob family ID. tahts since been corrected so we can do mob skill lists per mob just like retail, but not everything form back then is split up or even needs to be (we do not yet have a reason to create multiple separate screwdiver version for different puguils for instance, since they all work as is and players don't know the difference - good enough right?) But somewhere in the master list of skills, there are multiples for many things. I happen to know Wyrms moves are among them having made a bunch of custom ones for another server once upon a time.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 06:53:07_

----

I did as you suggested and outsourced this into its own local function for re-use in later conditions. Works well.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 06:55:33_

----

Can I mark this as resolved or do you want me to create a unique spell with this and then append a skill list entry for `KS99_Wyrm-Flying-Attack` in `mob_skill_lists.sql`?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Oct 19, 2020 at 10:07:12_

----

There aren't skill or magic like regular attacks (category 2). Any time you see a mob appear to use something like that for a "regular attack", they're mobskills (category 11) with a message of 0. They _look_ like a regular attack to a player, but internally they're different.

In this case, setting a skill list ID of 730 will cause it to use Tiamat's Inferno Blast "alt".
![skill](https://user-images.githubusercontent.com/13112942/96431219-bb799f80-11f2-11eb-8500-cc2adebb67fb.png)




----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 15:11:42_

----

I am well aware of that. It seems to be exactly what SetMobSkillAttack() was created for. Quite some wyrms use it. Where are we going with this though?
As mentioned the only thing regarding this original comment I could do is create more duplicates and write a unique skill in form of `flame_blast_alt` (950 could be used for that e.g.) and then append a skill-list with only that skill just like for Tiamat, Ouryu and Jormy. But it's superfluous and as Teo mentioned, it works like this, the user won't note any difference, why duplicate data for this one skill. (Unless you want me to do exactly this, which is why I'm asking.)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 19, 2020 at 19:18:29_

----

With Wyrms SE put minor variations while they were copy pasting, I can see how my use of the word duplicate has caused some confusion. Tiamats skills are no more KS99_Wyrms skills than they are Jormies, but SE _duplicated_ their template Wyrm to create each of them, if hat makes sense, and lead to certain Wyrms having unused entries - like Fafnir isn't going to touchdown cause he never flies, and that one in abyssea never will coz he or she never lands and this is what I was trying to say, Their breaths and blasts are probably not going to be 100% identical even if the same element.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 19, 2020 at 19:19:01_

----

whatever ID retail is using, is the ID we want to use.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 20, 2020 at 07:12:44_

----

@TeoTwawki & @ibm2431  I have an issue with this. As you can see in in the latest commits I have corrected all the Wyrm specific IDs with their corresponding animation IDs and created two additional skill lists. One for TP skills while flying (airborne Hurricane Wing & AoE Flame Blast), and one for the regular attack while flying (Single target Flame Blast). These three animations can be called individually fine and work as expected when called with `useMobAbility()` for example.

**However**: When I set `mob:SetMobSkillAttack(1146)` I would expect the Wyrm to now use skillID `950` as regular attack, which has the correct animationID and the same column values as all the other flying-attack skills (leet, ocher etc.). **But** the mob just won't use anything at all. It just sits there doing nothing now.
I made sure that the database was correct, including the changes, the right IDs etc. The other regular-attack flying skills work fine and the tiamat one even uses the same animationID...

TL;DR
```LUA
mob:SetMobSkillAttack(1146)
```
does absolutely nothing despite having added new skill lists exclusively for this use, using the correct skill, the correct animation ID etc. database double checked.
`mob:setMobMod(tpz.mobMod.SKILL_LIST, 1147)` works...


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 20, 2020 at 13:43:40_

----

@UynGH Did you try to summon trusts in the BCNM? I saw Zach did, but he wasn't the leader 😆 .


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Tuesday Oct 20, 2020 at 16:25:19_

----

Hello! Just checked:
![1](https://user-images.githubusercontent.com/40763842/96615452-92940000-1301-11eb-829f-a7697681c48b.jpg)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 20, 2020 at 16:42:05_

----

Your sacrifice is appreciated. 🖖 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Oct 20, 2020 at 20:41:59_

----

> does absolutely nothing despite having added new skill lists exclusively for this use, using the correct skill, the correct animation ID etc. database double checked.

its expecting a script with the name that is on skill id 950 that is in that skill list: `flame_blast_alt`


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 20, 2020 at 22:02:56_

----

I thought that too, but how is it possible that `inferno_blast_alt`, `sleet_blast_alt` and `ochre_blast_alt` all work **without** having a script?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Oct 20, 2020 at 22:50:26_

----

bold of you to think somebody didn't ~~break~~ "fix" jormy.

try it. copy you blast to the other name and see if it starts blasting.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Oct 21, 2020 at 08:40:01_

----

As a reminder to myself:
https://github.com/project-topaz/topaz/blob/release/src/map/battlefield.h#L34

I need to add RULES_NO_TRUSTS


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Friday Oct 23, 2020 at 20:37:10_

----

Finally resolved after a few days of overthinking and a little chat. Thank you.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 26, 2020 at 12:18:25_

----

I noticed you have the same check in both versions, where as the other wyrms blast moves have the check in only 1 version. I don't know if that is a problem or not honestly,


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 26, 2020 at 21:11:36_

----

Hmm. Now that you say it, it is actually redundant since I created two dedicated sets for flying mode. One for the regular attack and one for TP moves. Since these are explicitly called for flying mode and then changed back, there's actually no real reason to check again. The other flying wyrms don't have a dedicated flying-mode TP set so they need to check for AnimationSub directly in the TP move skills. Whether or not that's good practice and whether or not there's maybe more flying TP moves from what we've seen, could be looked into in another issue.

I removed these checks completely and made it clear in the header comment that those skills should only be used for flying mode skill sets.

Good thing you came across this cause during this testing I also noticed a leftover of flame_blast in the ground skill set, which was removed, and more importantly:

I earlier resolved a merge conflict that was pushed in the meanwhile ( da852bbbfdf871256fb2309968cce70a5a91cd96 &  https://github.com/project-topaz/topaz/commit/0bd3bad899d48dfb4d2785d331bbc36d073f707f ) with changes to the blocking condition of Dragon Breath of being behind, to not being in front. I accepted these changes. But during this testing session today, this did **not** work at all. The skill won't get called anymore. I first observed this, then did some more testing and after just sitting there and counting 0 out of 20 TP uses (in addition to the formerly observed lacking) of dragon breath, I think it is safe to say this does not work.
I reverted this and it did work again.

I reverted this change only for Dragon breath cause it affects this PR. There's a lot of breaths that had that change made though and should be tested.

- [x] Tested working extensively on a local server


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 23:14:51_

----

Can remove the TODO since Wyrm is coded now. 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 23:17:21_

----

Can specify that this version is the grounded version.

Just to clarify, Flame Blast is supposed to be magical and not a breath attack, right? The skill check is okay (ie: can use regardless of where target is)?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 23:19:45_

----

Since `typeEffect` is only used in in the `MobStatusEffectMove` call, you can use `tpz.effect.BLINDNESS` directly in it without an assignment.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 23:21:45_

----

Is this needed? The status effect _should_ already be gone in a new battlefield, since mobs are destroyed and recreated.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 23:22:19_

----

Can set this to be the ID we discovered in the Nidhogg PR~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 23:43:42_

----

I haven't really examined the Early Bird capture, but be forewarned that if this is based on what HP Track spit out, if the mob has regen the numbers might not be accurate. The accuracy could also vary depending on the estimation method it needed to resort to.

Min and Max will just be the minimum and maximum damage it took to kill the mob, so if there was regen involved, the values will be higher than what the mob's HP truly is, as HP Track has no way of knowing DoT or Regen amounts.

Method I stands for Method Interval, in which it attempts to guess an HP based off of percentage differences it saw the mob's HP % change by, and the damage it took to reach those differences. Because it guesses HP in slices over the entire fight and then averages those guesses together, I consider its estimation more trustworthy than...

Method L stands for Method Last. It compares how much HP% the mob had when it was last seen alive, compared to how much damage the mob has taken over the entire battle before the killing blow. If HP Track last saw the mob alive at 3% after seeing exactly 97000 damage dealt, it'll spit out an estimate of 100,000 HP. However, since retail only sends out HPP updates for whole integers, the mob's true HP range could be 99,000~101,000. In this case we could guess SE selected 100,000, but if the exact damage dealt values, and the original mob's max HP value isn't as "clean", this can be harder to guess.

I consider Method Ls slightly less trustworthy because it only examines the battle at one point in time, _and_ while it may sound like a conspiracy theory, I'm not convinced 1% HP is _actually_ 1% HP. I _swear_ the last 1% takes longer to empty on retail than it "should". So if the last time it saw the mob alive was at this "1%" value, then it can come up with higher numbers if the mob really had more of its True HP remaining during "the last 1%" phase.

Obviously retail is going to round up if the mob is _sub_ 1%, which will lead to further inaccuracies. In HP Track's case, the damage it thinks it took to bring a mob down to "1%" (in this case, the total damage it's seen and is assuming is 99% of the mob's HP) could actually be anywhere from 98.1% (mob had 1.9% remaining) to 99.9% (mob had 0.1% remaining).


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 00:13:31_

----

I think you're getting these mixed up. There is no grounded version Flame_Blast ;)
One is single target regular attack (_alt)
and the other (this one) is the TP AoE skill (only while flying!). Yes it's supposed to be magic damage, not breath.
I double emphasized this in the description now.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 00:16:50_

----

The BCNM cleanup should also happen on wipe, that's what you're saying right? I will test this again.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 00:17:40_

----

This is now pretty much a merge conflict with the other PR, should I change this here?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:22:36_

----

bcnm cleanup happens when the bcnm ends for any reason. a wipe and reraise without the bcnm ending will not trigger onMobSpawn again anyway. but when it respawns in a new bcnm, the effect being dleted here will have already been removed by the mob being re-created again.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 00:23:03_

----

Wow, after reading this I'm now more confused than before even though I appreciate the insight. I do get that HP regeneration might mess up readings though. You're very deep into the whole capturing so, I'd appreciate your instructions on this. It sounds like it would be sensible to revert this back to the 45,000 it had before.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:24:04_

----

![image](https://user-images.githubusercontent.com/6871475/97819618-b8ad8e80-1c77-11eb-872e-1b2c71cd74d6.png)
 he's not to high at spawn. never too high. :wink: 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:25:46_

----

can pull your other one into here after it merges and resolve the conflict, or rebase this onto the other one. If you haven't had much practice with rebase, this is a good opportunity (back up your scripts 1st if not confident)


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 00:34:38_

----

Also on a further note: During flight all Wyrms (should) face their target, so directions do not apply and don't need to be checked for indeed.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 01:03:34_

----

I just merged release into this, I'll keep avoiding rebase as long as possible T_T


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 01:11:00_

----

Looked at the capture:
`46728~51180 HP, Est HP: 49644 (Mthd: L)`
Method L is a little odd in that it [compares the total damage it saw (max) to how much HP% it watched get drained](https://github.com/ibm2431/addons/blob/master/capture/hptrack.lua#L83-L84). This is... actually not accurate, so I should fix that. It should be [comparing the _minimum_](https://github.com/ibm2431/addons/blob/master/capture/hptrack.lua#L78) against what it watched get drained.

But we can use the min HP value to look at the problem from the other direction:
The final hit was a Fell Cleave taking off the final 3% of its HP.

It saw 46727 damage done up to that point. The "minimum HP" is "total damage and still living + 1 HP".
```
(Max HP/100) * 97 = 46727
Max HP / 100 = 481.72
Max HP = 48,172
```

Basically, even pretending the Regen never existed, if 46,727 damage brought it down to 3% HP left, then it can't have more than 48,172 HP.

Even if we assumed that the HP% that retail sends out is _floored_:
(Max HP/100) * 96.1 = 46727 (Note: 100 - 96.1 = 3.9)
Max HP / 100 = 486.233
Max HP = 48,623

Unless there was a DoT on it, there's no way its HP can break 48,623.

So while I'd normally be tempted to slap 50,000 on it because it's a nice, even number, it's just not possible. I'd be okay with 45,000 and assuming it got ~3000 HP restored from regen over the 12 minute fight.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 01:19:07_

----

Makes sense and sounds reasonable indeed. Thank you again for laying it out that much. The conversation didn't get marked as outdated, but I adjusted it accordingly.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 01:23:48_

----

Oh, so this version is the one it'll actually display the message for, got it! Carry on!


----
<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Sunday Oct 18, 2020 at 18:21:18_

----

> _ Hurricane Wing in the air would be a TODO since I couldn't find the right skill for this. The standard wing is a ground animation

I believe the "super buff" move used by Nidhogg is supposed to be the aerial Hurricane Wings move.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 00:33:06_

----

@Hozu Thank you for the pointer, I will check on that.
~~Edit: Does not seem to be the case. Super Buff is indeed a buff. Even though it appears next to skills that Wyrm uses I don't know when this would be used. Videos I have watched of the Wyrm fight do not show a similar animation (mob turns blue temporarily, like it was a 2h, possibly Mighty Strikes; the use of this skill also prevents use of other TP moves.) 
(Also see Teo's comment above about this)~~
Just for the records: Hozu was completely right, I just interpreted this based on less insight. The airborne Hurricane Wing got knowingly hijacked and overwritten at some point. This is now corrected.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 19, 2020 at 05:19:07_

----

I've just gotten a `Themis Orb` on retail, so I'll be able to get caps of this soon. I just need to get someone to PL my /DNC so I can try solo it


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 07:13:11_

----

So far so good.
There's a few things that are **not related to this PR** that I _observed and affects all wyrms in general_:

- When out of player range/"too far away" from the mob, the `Touchdown` animation will not display even though the mob uses it
The magical default ranged attacks while flying have a huge range, which is nice, but easily provoke this behavior
- Draw-In while flying makes the mob move a good amount of yalms to the back, even out of bounds (known)
- SetMobSkillAttack() uses up all TP on every attack since it now uses a mobskill as a regular attack; *huge* flaw
From lua_baseentity.h:
`int32 SetMobSkillAttack(lua_State*); // enable/disable using mobskills as regular attacks`
Additionally as ibm and Teo mentioned, it is confusing that this uses a skill list ID instead of a skill
- Almost all wyrm typical attacks in `global/mobskills/` `return 1` if the AnimationSub is not 0
If any wyrm at any point has its AnimationSub changed to something else (and there's several bits for grounded mode), or a different default it will not use any of these skills
This is desirable when flying but Wyrm had a default of 6 (ground) for example and the skill Touchdown sets it to 2 after executing
- ~~For some reason after Touchdown is used mobskills will be used when reaching 1000TP not 3000TP (as when engaging the fight)~~ *(explained by ibm2431 below, I forgot about how this is natural behavior)*

I created a well commented but very dirty workaround for the TP issue which after a lot of testing feels right during the fight and is better than no TP move at all during the flight phase.

**TO DO for this PR**:
- [x] ~~Wait for Zach to make a capture and see what it yields~~
- [x] ~~Set natural magic resistances (Fire & Ice) and weaknesses (Water & Thunder); I'm simply unsure where to do this~~


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 19, 2020 at 10:24:58_

----

>  Set natural magic resistances (Fire & Ice) and weaknesses (Water & Thunder); I'm simply unsure where to do this

this is currently handled by the mob family table row


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Oct 19, 2020 at 10:27:01_

----

`SetMobSkillAttack` functions how it should in that some mobs use multiple mobskills for their regular attack (ex: Shinryu, August). It should definitely be renamed to be more explanatory.

[It should be functioning without needing 3000 TP](https://github.com/project-topaz/topaz/blob/release/src/map/ai/controllers/mob_controller.cpp#L259-L297). If it's not, something is broken.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Oct 19, 2020 at 10:39:38_

----

> For some reason after Touchdown is used mobskills will be used when reaching 1000TP not 3000TP (as when engaging the fight)

Mobs use TP moves sooner depending on their HP. At 100% HP they won't use TP until they're at 3000 TP. The point at which they're forced to use TP is earlier as their HP% goes down (on retail, they use TP at 1000 when below 25%).


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 16:46:11_

----

> [It should be functioning without needing 3000 TP](https://github.com/project-topaz/topaz/blob/release/src/map/ai/controllers/mob_controller.cpp#L259-L297). If it's not, something is broken.


@ibm2431 A humble `print(mob:getTP())` says more than a thousand words:
https://streamable.com/ojrve0
This record was made on a vanilla `release` build (last upstream merge last week) and with the TP hack removed. You can clearly see how once `AnimationSub(1)` plays and `SetMobSkillAttack()` kicks in I'm spamming ranged attack to no avail. Each time a regular attack is used the TP drop to 0.
Hope this helps and maybe someone could check on this.

~~On this note I would also like to point out that **`onMobFight()` fires *way* too often** if one can believe the description in `luautils.h` and `luautils.cpp` where it says:~~
> int32 OnMobFight(CBaseEntity* PMob, CBaseEntity* PTarget);                    // Сalled every 3 sec when a player fight monster

(see comment below) But I still have to make this note that my server calls this 2 to 3 times *every second*, not every 2400ms (2.4s)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 19, 2020 at 19:00:40_

----

> A humble print(mob:getTP()) says more than a thousand words:

And even if the mob has zero tp mobskill as melee will still go off at its specified melee delay interval. That it is erroneously removing tp when it "melee's" is a bug to be fixed, if that is happening (I believe it is).

> On this note I would also like to point out that onMobFight() fires way too often if one can believe the description in

it fires every ~~2400ms~~ _400ms_ exactly, and this is _intentional_.  The comment was written by someone else that I guess never saw the code that times it. (combat tick is running off the universal server tick rate in `CTaskMgr`)

Edit: ~~intentional and retail accurate too~~ I forgot Kj changed it. The global timer still happens at 2400, but mob ai ticks at 400ms.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 20, 2020 at 07:32:19_

----

Latest commits add and correct the following:

- All KS99 Wyrm specific skills were double-checked and assigned their correct values. Missing ones were added and scripted
- Two new skill lists for this Wyrm have been created. One for TP skills during flight, one for the regular attack during flight
- Someone knowingly overwrote the airborne Hurricane Wing with the Nidhogg 2h skill. This has been moved and corrected
- The Wyrm's HP were adjusted to 50,000 instead of 45,000 getting closer to the recent retail capture, Lvl was also corrected
- The Wyrm received two new traits observed in the retail capture: Regain and Regen. Both with sensible values based on stopwatch measurements
- Draw-In was moved to `onSpawn()` because `mod_modifier.h` says so:
`// 1 - player draw in, 2 - alliance draw in -- only add as a spawn mod!`
- `MOBMOD_SKILL_LIST` is now used to set the corresponding new skill set while flying and then restores it after landing
- The TP workaround was removed. It just doesn't work well in every situation. The real issue should be corrected instead
(not related to this PR though!)

TO DO:
- [x] Make Wyrm face target while flying only
- [x] Improve Touchdown behavior


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Thursday Oct 22, 2020 at 01:53:02_

----

Latest commits add and correct the following:

- Flying wyrms face the target while flying, but not on ground; Jormy and Ouryu are probably missing this too
- Touchdown handles TOO_HIGH effect, default attack and animation model
- After landing the new model animation is with wings up, Touchdown did consider this, but wyrm skills did not
- Standard wyrm skills now only block while flying, not during other ground modes like mode 2 after Touchdown
- Touchdown had a wrong close melee range of Bahamut's Touchdown which does not apply; the target can not escape Touchdown AoE due to Draw-In; Jormy and Ouryu are also missing this
- Touchdown is instant without skill cast animation

For reference see [here](https://www.youtube.com/watch?v=grUFfSbNCHU), [here](https://www.youtube.com/watch?v=6PhIvMTLl4o&feature=youtu.be) and [here](https://www.youtube.com/watch?v=j0uyB9NDhTE&feature=youtu.be)

TO DO:
- [x] Change flying attack message from "The Wyrm uses Flame Blast" to "The Wyrm hits target for x points of damage."


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Friday Oct 23, 2020 at 20:38:48_

----

@TeoTwawki Would appreciate a last review for any errors. As far as mechanics go, this is pretty much done now.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 02:00:26_

----

> regression

Edited skill list so only Dragon Breath is in it:
https://youtu.be/YogcdPTTKS4

Did you rebuild?


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 27, 2020 at 04:17:22_

----

Thank you very much for getting back and even providing proof of work @ibm2431 , and even more for pointing me in the right direction. It's the first time I had a newly added global function affect a PR of mine. I should have read way more thoroughly through your PR when it conflicted with this. I apologize.

My build simply didn't find that function of yours. So today I pulled everything in, rebuilt and all is good. I also adapted the Wyrm skills from this PR to use your function instead of the old `isBehind()` and tested them positively.
Also found a typo I made in the database that was fixed.
If you don't see anything else I'd say this is ready now.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Saturday Oct 31, 2020 at 17:38:03_

----

@reviewers Could this be tagged as reviewed and/or approved for merge? This works very well by now, no more changes have been requested. It's just sitting here.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 31, 2020 at 18:30:52_

----

Please remember that it's the weekend and staff/reviewers are volunteers. This will get re-reviewed and/or tested when someone has time. 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Oct 31, 2020 at 18:54:06_

----

dunno if this needs to be tested maybe it could be merged into canary? have a few lv 99 players that can try the fight. Wish we had lots of players to try it on an alliance at 75.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Oct 31, 2020 at 22:48:26_

----

1. GitHub unfortunately doesn't let non-organization members tag the `project-topaz/reviewer` role. This is a different group of people from `reviewer` or `developer` on GitHub. (Those tags _do_ work in our Discord, though!)

2. Zach and I are the only official developers with write access, and PR reviews and merges are only a fraction of what we do. The reason that some PR reviews and merges take time is because we spend that time on things which are higher priority. There's a lot of history behind this - I've struggled with Zircon many, many times on this very subject - but slower reviews is the current solution to the problems the project faces. It's not from lack of effort - Zach and I spend more time on this project than anyone _should_.

Don't worry - I know you haven't claimed it was, MarianArlt. But I've been hearing of low-key complaining recently (not necessarily from you in particular), and this happens to be the most relevant public place for me to say the above since you mentioned review times.

3. kain, I know that you know how our process works. If you want Canaria to have new content sooner, you're going to have to start cherry-picking, merging your own work, and rebranding yourself as no longer being vanilla canary branch. We're not going to be pressured to merge PRs sooner for the benefit of players on a private server.

4. Onto the contents of the PR: I am killing fake "super buff" on any wyrms. I know the history of how it came to be. I do not care about said history, who did it, or the reasoning why. We're not assigning stuff to arbitrary non-captured skill IDs with the _hope_ it won't cause a problem later. It was a boneheaded decision _then_ because of _this exact problem_ it's posing _now_.

The rule I am imposing going forward is that if it's not seen in a capture from the mob a skill is being assigned to, the skill does not get used, period. It doesn't matter if the skill "appears" free. If it hasn't been captured, it's not used. I am so tired of this codebase "faking it" leading to problems down the line (yes, this _is_ [the paralysis bitterness](https://github.com/project-topaz/topaz/issues/327) talking). It either gets done properly, with evidence we can cite, or not at all.

In the context of Nidhogg, we can:
1. Capture; or
2. If necessary, [assign buffs without using a skill](https://github.com/project-topaz/topaz/blob/release/scripts/zones/Temenos/mobs/Proto-Ultima.lua#L21-L35).

If this results in the loss of a 2 hour animation until we better understand the mechanic behind the animation, then so be it. This fake "super buff" skill has already wasted more of our collective time and energy than it should have - time and energy which would be better spent elsewhere.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Nov 01, 2020 at 01:03:25_

----

I appreciate your comment and everything in it. I hope you saw my Discord comment, I totally understand how much work you guys must have. I did think there were more people reviewing though actually. Thanks for clarification.
Since I innocently just moved "super buff" here in this PR, should I rather revert the line where I put it back to original and only keep flying hurricane wing where it belongs?
I don't feel this PR should be made responsible for this and resolve Nidhogg on the fly, so to say.
Would appreciate further instructions, even if it was "handle Nidhogg please".
Could also remove it here as mentioned and open a new issue to document the change and have it there for later.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 01:49:04_

----

Project Meta:

Official project staff are Zircon, Wiggo, Zach, and myself. Since GitHub doesn't allow us to easily list organization/group members, we keep a list of official staff and non-official "contributor groups" in our Discord's `#resources` channel. Wiggo is currently absent (life circumstances), but he stays out of development anyway (he prefers research). Zircon - as our official project lead figurehead - doesn't allow themselves to make development decisions so there isn't an implicit power imbalance should potential development arguments come up. That leaves just me and Zach at the moment as official write-access developers, absent more official staff.

Some contributors are part of our "organization" so they can be placed in non-official-staff contributor groups (`project-topaz/developer`, `project-topaz/researcher`) and can get pinged on things that might interest them ("hey, developers, we're doing this major change", "is there a researcher that might want to look into this?). This has the unfortunate side effect of badging them as a "Member". So while I _do_ love Teo (and others), they don't have merge/write access. And as before, the mentions don't work on GitHub for anyone who isn't member of the parent organization (no doubt to kain's dismay 😉 )

We've been bouncing around ideas of giving such contributors more ways to assist the project (without giving them full repository write access), but GitHub makes this very difficult (as usual). So our ideas on that front have been stalled pending setup of more automated actions/bots.

----

Actual PR:

If Skill ID 956 is the flying version of hurricane wing (as seen from a capture), then it should stay as what you set it as.

If Skill ID 950 is the flying flame blast (again, from a capture) then that should also be kept to what you set it to.

Unless there's been a capture of Skill ID 949, it shouldn't be used for anything at all. If this means Fafnir no longer has a "spare" skill ID for the fake super buff move, that's fine, because we won't be using one. So you can revert Skill ID 949 back to what it used to be. I presume it was previously named Flame Blast because that's its name in the DAT.

We can fix Fafnir to no longer use the _completely fake_ "super buff" skill (currently in skill ID 956) in a separate PR. We may want to time approvals / merges so they both go in at the same time. I'd _like_ a volunteer for handling Fafnir's buffing properly, but if there isn't one soon-ish I can _try_ to find some time (but I've also been trying to focus on some zone performance work recently).


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Nov 01, 2020 at 02:25:58_

----

@ibm2431  yeah I unserstand staff has higher priorities, I was just offering to somehow help if this was due to needing some testing.  I think Instead I'll build it locally and provide feedback from there =)

My apologies if my comment felt as I was pressuring this PR.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Nov 01, 2020 at 07:17:41_

----

> the mentions don't work on GitHub for anyone who isn't member of the parent organization

@ibm2431 additional reason I'm unlikely to notice it:
![image](https://user-images.githubusercontent.com/6871475/97797078-cf0c0980-1be7-11eb-8769-74d0f9463620.png)

Subfolder in my inbox.

That 112 is not even a full weeks worth of unread github notifications. One mention tends to get very buried so even if I did get those, I'd be sure to miss it since I subbed to the projects general notices.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 01:28:01_

----

I'll retarget to a version with post-super-merge release. The current target was branched from before I merged it.

Hey Teo, I'm remembering to retarget the open PR before deleting the target branch this time. 😉 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Nov 04, 2020 at 06:01:23_

----

I'll go through and review this later today 👍 


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Thursday Nov 05, 2020 at 19:11:44_

----

Commenting to add cross reference to #305
