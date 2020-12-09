**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:41_
_Originally opened as: project-topaz/topaz - Issue 265_

----

<a href="https://github.com/chrisalleng"><img src="https://avatars0.githubusercontent.com/u/3527305?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [chrisalleng](https://github.com/chrisalleng)**
_Wednesday Mar 13, 2019 at 03:44 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5791_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [X] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
version 30181205_0

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
Found on Edenxi

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Accepted "Blade of Darkness", equipped chaosbringer
Killed 105 mobs, with only auto attacks
Completed "Blade of Darkness"
Character was not high enough fame to start "Blade of Death"
Character killed another 100 mobs in the same way (total 205)
Character accepts "Blade of Death" quest
Character was not able to complete "Blade of Death" quest by trading the Chaosbringer in Gusgen Mines

poked around a bit, it doesn't look like ChaosbringerKills is incremented unless the player is on the "Blade of Death" or "Blade of Darkness" quests, which I do not believe is correct.  Reference: https://ffxiclopedia.fandom.com/wiki/Blade_of_Death "You need to bring the total number of kills with the Chaosbringer (from the time you first received it) up to 200. As such, kills made before activating this quest count towards the total."

This also matches my memory, but it's been 15 years 😄 

mobs.lua lines 16+ (having trouble with comment spacing, sorry):
```lua
function onMobDeathEx(mob, player, isKiller, isWeaponSkillKill)
    -- Things that happen only to the person who landed killing blow
    if isKiller then
        -- DRK quest - Blade Of Darkness
        if
            (player:getQuestStatus(BASTOK, BLADE_OF_DARKNESS) == QUEST_ACCEPTED or player:getQuestStatus(BASTOK, BLADE_OF_DEATH) == QUEST_ACCEPTED) and
            player:getEquipID(dsp.slot.MAIN) == 16607 and
            player:getVar("ChaosbringerKills") < 200 and
            not isWeaponSkillKill
        then
            player:addVar("ChaosbringerKills", 1)
        end
    end
```

EDIT: Also, it's an incredibly minor technicality, but to be the same as retail other abilities such as Jump shouldn't be counted - I'm not sure if isWeaponSkillKill includes other things like that, though. Frankly, the quest not counting abilities or WS kills was probably a bug in retail in the first place, not sure it's worth the effort of reproducing!



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:43_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 13, 2019 at 11:00 GMT_

----

see https://guides.github.com/features/mastering-markdown/ scroll down to examples (its near the top) and click on code. this will make snippets of code properly readable.

we need isWeaponSkillKill replaced by a more generic set of info about what has happened to the mob so that we don't use half a dozen booleans like that on it instead, for now the only check we have is "was it a ws that killed this?". when we get to implementing magian trials this is going to matter: generic ws kills, specific ws kills, pet kills, magic kills...



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:44_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 13, 2019 at 11:03 GMT_

----

we could fix the kill count of chaos bringer by checking if the 1st of the 2 quests is accepted OR completed prior to the 2nd quest being accepted, if thats how it works. I always thought it was saying that the kills _during_ the 1st quest would still be counted when you did the 2nd quest though. (it was possible to throw the sword away, and then have to re obtain it and do twice as many kills..and you could go over during the 1st quest by a lot) /shrug



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:45_

----

<a href="https://github.com/chrisalleng"><img src="https://avatars0.githubusercontent.com/u/3527305?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [chrisalleng](https://github.com/chrisalleng)**
_Wednesday Mar 13, 2019 at 13:47 GMT_

----

Probably overstepping my knowledge of darkstar and why/how things are done, but I'm not sure you need to check the quest status at all - as far as I know, it's as simple as if a player kills something with an auto attack and has chaosbringer equipped as their weapon, increase counter.  If it's dropped and has to be picked back up (from the zeruhn cutscene, which looks like it should work but I'm not crazy enough to try in a live environment) reset that counter back to 0.

They might have been storing the kills on the sword/item itself in retail or something equally crazy, which would explain why dropping and getting a new one would reset it...

There might be performance concerns or any large other number of reasons to check quest status, of course!  I think you're right and checking if "Blade of Darkness" has been either accepted or completed should work just as well.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:47_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 13, 2019 at 17:05 GMT_

----

~~I just assume we don't want forever check if the player is wielding chaosbringer on every zone of every map server of every mob death for a quest line that may not have even been started (or has been finished already), for every player in existence.~~ _lets not increment vars before/after they matter_ Since you can't have the item (without cheating) without first having flagged the quests (and doesn't need to be counted after the 2nd quest completed), that seems like a good way to narrow it down.

retail prolly does something more like how ws points work on the item itself, except for..not ws. but we've no way to determine that since it wouldn't be apparent to the client, and this was less work to implement anyway.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:48_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Mar 13, 2019 at 17:10 GMT_

----

it would be about the same as checking if the player has started the quest on every zone of every map server of every mob death, they're both just a really quick lookup in an array



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:49_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 13, 2019 at 17:14 GMT_

----

teschnei see edit
we'd still be doing _more_



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:50_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 14, 2019 at 01:54 GMT_

----

Regarding when checks are done, this line got me thinking:
> when we get to implementing magian trials this is going to matter

And what I'll add:
"Should RoE ever be implemented"

I wonder if we should start thinking about a way of doing "dynamic" checks for each player, so that for each player killing a mob we're not checking a large litany of specific equipment or quest activations.

This might be hard to convey without pseudo-code, but store the actual code checks as functions in a table (like how takhlaq and I are doing on quest_rewrite), indexed by some master enumerated key-type (`dsp.killcheck.CHAOSBRINGER`, `dsp.killcheck.MAGIAN666`). Then for each player store as an array/table the current "killchecks" the server should be performing for that player (and update this array/table as players activate or finish quests). On mobdeath, grab that character's killchecks and just array-lookup and execute only the relevant checks for that player. That way we'd only be checking what's relevant for that player instead of every possible check on every kill.

This of course would be overkill just for this Chaosbringer scenario. Just something I wanted to murmur now to think about for the future..!

edit: In attempt to be clear, I'm not saying store the actual function for that player, just store the enum that can be used to look up that function. :sweat_smile: 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:52_

----

<a href="https://github.com/ziaxe427"><img src="https://avatars1.githubusercontent.com/u/48656526?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ziaxe427](https://github.com/ziaxe427)**
_Thursday Apr 04, 2019 at 22:27 GMT_

----

im having a problem with this quest as well i HAVE the quest but and i swear i killed MORE than 100 but im not getting a cutscene for completeing the quest to unlock drk



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:53_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 04, 2019 at 23:22 GMT_

----

> im having a problem with this quest as well i HAVE the quest but and i swear i killed MORE than 100 but im not getting a cutscene for completeing the quest to unlock drk

that was caused by recent changes after the issue was already open, and fixed by PR that was just now merged :+1: 


