**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Wednesday Jun 17, 2020 at 22:56:42_
_Originally opened as: project-topaz/topaz - Issue 743_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [ ] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This branch will implement the two missing Eco-Warrior quests, and refurbish Eco-Warrior Windurst.

Currently Eco-Warrior Windurst has a few bugs and incorrect dialogue/options, commit 6b5d0e6 fixes those and cleans the scripts/variables.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Jun 18, 2020 at 02:08:48_

----

Ready for review at this point.  I'll be bringing the changes into Gold Saucer for testing, please critique as you see fit.

Mob level for each one was a complete guess, so it can be corrected.

Also todo (which I'm unsure how to) from the wiki:  "For [these] fight[s], only those with the level cap can assist in this fight. Anyone else trying to help will receive a message telling them they cannot."


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 05:27:28_

----

>"For [these] fight[s], only those with the level cap can assist in this fight. Anyone else trying to help will receive a message telling them they cannot."

Have you considered the confrontation status? I'm pretty sure if you apply it to the player(s) and mob(s) with the same power value, only those things can attack each other.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 21, 2020 at 05:31:37_

----

@cocosolos Retail does this as part of the lv cap status, which we don't yet support. Need a change in core to check subpower of lv cap when non zero. I can explain further tomorrow its a fairly small edit.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 05:50:39_

----

Can we just add the confrontation status silently instead since the functionality is already there, along side the level cap, like battlefields do?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 21, 2020 at 14:09:32_

----

confrontation status isn't used here, and isn't functionally accurate for this. It didn't exist as a status effect at the time this quest was put int gameplay on retail. Either `CCharEntity::CanAttack` or  `CTargetFind::isMobOwner` would need modified even if you used confrontation, the same place we need the level cap subpower check (when sp != 0). 

Retail has 1 lv cap status effect, but with multiple behaviors: lv cap with only level restricted, and level cap with targeting adjustments. BCNMs, promy zones back when they were uncapped, use just lv cap. Garrison, eco quest, and seasonal events use lv cap with targeting adjustment: mobs that do not have a matching value for the effect can't target you nor you them. This also remind me we're missing the instance member variable to store it on in the mob-entity (or were at the time I hacked my events together), so I just threw the same status effect on to compare with. If you look at retail caps the mob doesn't have a level cap status ever ^^;;


Edit: pardon me I am partially mixing up free-for-all targetting lv caps with party wide targeting lv caps. 3 kinds of caps, with 2 of them decided if you can attack a monster or not (and monster you). My apologies. CTargetFind::validEntity is where the check would go here, which yes does have a check for confrontation already.




----
<a href="https://github.com/zircon-tpl"><img src="https://avatars0.githubusercontent.com/u/60901633?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zircon-tpl](https://github.com/zircon-tpl)**
_Wednesday Aug 05, 2020 at 11:30:06_

----

This pull request has been superseded by #823.
