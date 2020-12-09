**Labels:**



<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Lynnea1320](https://github.com/Lynnea1320)**
_Saturday Feb 15, 2020 at 00:29:39_
_Originally opened as: project-topaz/topaz - Issue 340_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 17:55:30_

----

Add npcUtil function please elseif csid == 520 and npcutil.giveitem(player, 4376) then
Reduces the risk of full inv. problems


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 17:58:57_

----

Since this only occurs once dont really need to make it a global


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 18:01:33_

----

No need to local this since it only occurs once


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 18:04:32_

----

No need for the message when using npcutil


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 18:04:49_

----

NpcUtil


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 18:07:28_

----

Should this last even have some sort of ending var or complete progress so you dont get stuck in a loop here. Or is this last cs its default text when done forever?


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 18:08:16_

----

Should we move this to a function inside of the global onmobdeathex?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Feb 15, 2020 at 23:27:40_

----

To illustrate - `npcUtil.giveItem` returns a boolean if it was successful or not, so if you set your variable in an if check based on the call, you guarantee you're only advancing the quest if the player received the item:
```lua
if npcUtil.giveItem(player, {4376, 6}) then
    player:setCharVar("TutorialProgress", 2)
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Feb 15, 2020 at 23:31:38_

----

Usage would be `npcUtil.giveKeyItem(player, tpz.ki.CONQUEST_PROMOTION_VOUCHER)`.

`giveKeyItem` adds the key item and then calls the message special for you.

(The reason that the base adding and messageSpecial aren't combined into one is for instances where retail gives the item without the message or vice versa.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Feb 15, 2020 at 23:39:18_

----

The thought crossed my mind when I first saw this. But my understanding of the quest is that the player needs to kill mobs in a certain zone, and I don't know if we should be doing specific zone checks on every kill all players do for just one quest.

(I already dislike how the DRK quest, the only thing using onmobdeathex, is currently handled; but it'd be quite a rework to make me happy with it.)

We will probably need zone/region wide kill checks at some point. I don't know if that'd be something worth doing at this point. (But would certainly approve of the effort if someone felt particularly inspired.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 16, 2020 at 00:24:23_

----

My assumption is that it's the default text when done forever.

@Xephera char_vars are (currently) saved to the SQL DB as individual rows for each character on a "as set" basis - they're not in the DB upon character creation, and when the var is set to zero for a char, the row in the SQL DB is deleted. Hence, we try to avoid "forever vars" when possible, by trying to think if we can frame the var in a way so that it can _eventually_ be deleted instead of being cursed to exist forever in the table.

Ex: As currently written, with the way the tutorial var is "framed", when a character completes the tutorial, that's a var - or, row in the char_vars table - which will always exist forever.

Normally you can check for a quest being complete to avoid this problem, but you don't (currently) have the luxury available for this "non-quest". What can be done to avoid this is by setting the Tutorial var to 1 on character creation in [player/CharCreate](https://github.com/project-topaz/topaz/blob/master/scripts/globals/player.lua#L123), and then when the tutorial is complete, set the variable to 0. When checking to see if a tutorial NPC should use their forever-after "you're done with the tutorial" event, do so when the variable is 0 (ie: not in the db - getCharVar returns 0 when the variable isn't set).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 16, 2020 at 00:25:32_

----

You're already checking for `tutorial == 3` down below, so you can move this inner code-block down there and save yourself an `if` 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 16, 2020 at 00:55:42_

----

To clarify KnowOne's comment about not needing to define the variable, you can instead do:
```lua
if not player:hasKeyItem(tpz.ki.DEM_GATE_CRYSTAL) then
```
down here, instead of assigning it up there when you're only using it once.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 16, 2020 at 00:58:14_

----

For integers that represent some identifier like a player's job, or a skill type, we try to use the enums so it's more immediately apparent what the code is doing:
```lua
for i = tpz.skill.HAND_TO_HAND, tpz.skill.STAFF do
```
Also by using enums wherever possible, if those values need to change in the future, it's easier to do mass-finds and replaces for those tabled enums instead of vanilla integers 😄 

There's a whole plethora of enums for various things; you can find most of them in [the status global](https://github.com/project-topaz/topaz/blob/master/scripts/globals/status.lua).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 16, 2020 at 01:01:15_

----

`getCharVar` will always return 0 if the variable isn't in the DB, so you don't need to check if it's `nil` here.

(But good looking out for this sort of thing! The binding is just a little weird 😉 )


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 16, 2020 at 01:27:48_

----

One thing we have inherited - until we get a functional modding system set up - are a list of [global settings in a lua file that server operators can modify](https://github.com/project-topaz/topaz/blob/master/scripts/globals/settings.lua) to adjust things like the rate characters earn Exp and Gil.

These settings have had a history of contention - developers having to worry about them adds to the settings' accruing technical debt, but server operators have a valid need to be able to easily adjust things from just the one file. So to avoid another fight over settings, I think that until we get the modding system, we should plan to keep using them where we know they might be expected.

_That backstory out of the way_, what I'm trying to say is:
`player:addExp(1200 * EXP_RATE)` is preferred, so a server admin can increase the Exp this (and all other) quests grant without having to edit all the individual files.

(And `player:addGil(1000 * GIL_RATE` too)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 16, 2020 at 02:45:27_

----

if you did a zone check, that check would still exec to determine true/fall for _every kill game wide._

drk quest kills can be done on any mob in the entire game so that does make sense. it could have been done like breaking a latent except for the 2nd quest that includes kills from the first one making that annoying. In the future maybe a pseudo additional effect on that item. But I'm rewriting those and that's a global too after that, so I don't think you want to go from _every mob killed_ into _every swing_ checking quest stuff.

The best answer for tutorial mobs is probably to either wrap them like regimes do, or use a mixin :disappointed: 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 16, 2020 at 02:46:30_

----

he means variable

variables are good when the data you are variablizing:
* changes
* gets used multiple times
* would make the line where its used wider

Since this data is static the line doesn't change and it is used only once, its cool to do it in-line.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 17:55:30_

----

Add npcUtil function please elseif csid == 520 and npcutil.giveitem(player, 4376) then
Reduces the risk of full inv. problems


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 17:58:57_

----

Since this only occurs once dont really need to make it a global


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 18:01:33_

----

No need to local this since it only occurs once


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 18:04:32_

----

No need for the message when using npcutil


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 18:04:49_

----

NpcUtil


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 18:07:28_

----

Should this last even have some sort of ending var or complete progress so you dont get stuck in a loop here. Or is this last cs its default text when done forever?


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 18:08:16_

----

Should we move this to a function inside of the global onmobdeathex?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Feb 15, 2020 at 23:27:40_

----

To illustrate - `npcUtil.giveItem` returns a boolean if it was successful or not, so if you set your variable in an if check based on the call, you guarantee you're only advancing the quest if the player received the item:
```lua
if npcUtil.giveItem(player, {4376, 6}) then
    player:setCharVar("TutorialProgress", 2)
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Feb 15, 2020 at 23:31:38_

----

Usage would be `npcUtil.giveKeyItem(player, tpz.ki.CONQUEST_PROMOTION_VOUCHER)`.

`giveKeyItem` adds the key item and then calls the message special for you.

(The reason that the base adding and messageSpecial aren't combined into one is for instances where retail gives the item without the message or vice versa.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Feb 15, 2020 at 23:39:18_

----

The thought crossed my mind when I first saw this. But my understanding of the quest is that the player needs to kill mobs in a certain zone, and I don't know if we should be doing specific zone checks on every kill all players do for just one quest.

(I already dislike how the DRK quest, the only thing using onmobdeathex, is currently handled; but it'd be quite a rework to make me happy with it.)

We will probably need zone/region wide kill checks at some point. I don't know if that'd be something worth doing at this point. (But would certainly approve of the effort if someone felt particularly inspired.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 16, 2020 at 00:24:23_

----

My assumption is that it's the default text when done forever.

@Xephera char_vars are (currently) saved to the SQL DB as individual rows for each character on a "as set" basis - they're not in the DB upon character creation, and when the var is set to zero for a char, the row in the SQL DB is deleted. Hence, we try to avoid "forever vars" when possible, by trying to think if we can frame the var in a way so that it can _eventually_ be deleted instead of being cursed to exist forever in the table.

Ex: As currently written, with the way the tutorial var is "framed", when a character completes the tutorial, that's a var - or, row in the char_vars table - which will always exist forever.

Normally you can check for a quest being complete to avoid this problem, but you don't (currently) have the luxury available for this "non-quest". What can be done to avoid this is by setting the Tutorial var to 1 on character creation in [player/CharCreate](https://github.com/project-topaz/topaz/blob/master/scripts/globals/player.lua#L123), and then when the tutorial is complete, set the variable to 0. When checking to see if a tutorial NPC should use their forever-after "you're done with the tutorial" event, do so when the variable is 0 (ie: not in the db - getCharVar returns 0 when the variable isn't set).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 16, 2020 at 00:25:32_

----

You're already checking for `tutorial == 3` down below, so you can move this inner code-block down there and save yourself an `if` 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 16, 2020 at 00:55:42_

----

To clarify KnowOne's comment about not needing to define the variable, you can instead do:
```lua
if not player:hasKeyItem(tpz.ki.DEM_GATE_CRYSTAL) then
```
down here, instead of assigning it up there when you're only using it once.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 16, 2020 at 00:58:14_

----

For integers that represent some identifier like a player's job, or a skill type, we try to use the enums so it's more immediately apparent what the code is doing:
```lua
for i = tpz.skill.HAND_TO_HAND, tpz.skill.STAFF do
```
Also by using enums wherever possible, if those values need to change in the future, it's easier to do mass-finds and replaces for those tabled enums instead of vanilla integers 😄 

There's a whole plethora of enums for various things; you can find most of them in [the status global](https://github.com/project-topaz/topaz/blob/master/scripts/globals/status.lua).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 16, 2020 at 01:01:15_

----

`getCharVar` will always return 0 if the variable isn't in the DB, so you don't need to check if it's `nil` here.

(But good looking out for this sort of thing! The binding is just a little weird 😉 )


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 16, 2020 at 01:27:48_

----

One thing we have inherited - until we get a functional modding system set up - are a list of [global settings in a lua file that server operators can modify](https://github.com/project-topaz/topaz/blob/master/scripts/globals/settings.lua) to adjust things like the rate characters earn Exp and Gil.

These settings have had a history of contention - developers having to worry about them adds to the settings' accruing technical debt, but server operators have a valid need to be able to easily adjust things from just the one file. So to avoid another fight over settings, I think that until we get the modding system, we should plan to keep using them where we know they might be expected.

_That backstory out of the way_, what I'm trying to say is:
`player:addExp(1200 * EXP_RATE)` is preferred, so a server admin can increase the Exp this (and all other) quests grant without having to edit all the individual files.

(And `player:addGil(1000 * GIL_RATE` too)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 16, 2020 at 02:45:27_

----

if you did a zone check, that check would still exec to determine true/fall for _every kill game wide._

drk quest kills can be done on any mob in the entire game so that does make sense. it could have been done like breaking a latent except for the 2nd quest that includes kills from the first one making that annoying. In the future maybe a pseudo additional effect on that item. But I'm rewriting those and that's a global too after that, so I don't think you want to go from _every mob killed_ into _every swing_ checking quest stuff.

The best answer for tutorial mobs is probably to either wrap them like regimes do, or use a mixin :disappointed: 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 16, 2020 at 02:46:30_

----

he means variable

variables are good when the data you are variablizing:
* changes
* gets used multiple times
* would make the line where its used wider

Since this data is static the line doesn't change and it is used only once, its cool to do it in-line.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Feb 15, 2020 at 00:32:37_

----

```
ibm2431: Well, this branch says it's two commits ahead
ibm2431: If those items are really supposed to be there
ibm2431: We'd take those too
ibm2431: So if it's easier for you, you can just fork/PR from that 
and that shop will become updated on our master too as a side-effect
ibm2431: I'll add a note on the PR saying I approved
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Feb 15, 2020 at 00:39:13_

----

I have also already stated that I would make style-guide edits, so any reviews from others can ignore those~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Feb 15, 2020 at 10:33:48_

----

Pushed style guide associated changes!

I'll give this a proper review tomorrow~


----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Saturday Feb 15, 2020 at 18:16:24_

----

I think I left the commented old code I was referencing in the bottom of Gulldago's code as well, oops! Didn't notice it until now.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 18:51:44_

----

I also see these 3 npcs being 1 file in a tutorial global whith just a difference of csid base and shift. They all have the same code with just different csids and in same order correct?
