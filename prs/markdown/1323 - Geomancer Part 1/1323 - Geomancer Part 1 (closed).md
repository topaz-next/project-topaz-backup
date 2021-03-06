**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 10:18:48_
_Originally opened as: project-topaz/topaz - Issue 1323_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

After some talk on Discord recently, and me sneaking in my NotorietyContainer, these are the last core changes required for someone to pick up GEO.

This is pretty much the early work me and MrSent did to get GEO up and running, so he is `--author`'d

The plan is to get this into `release`, then someone can start a feature branch from release and start submitting **CHUNKS** of GEO at a time to that feature branch.

**MEGA NOTE:**
The `ModelID` of Luopans should **NOT** be set in Lua, these are only used right now because elemental order isn't consistent yet. This work is on the way. The final signature of `spawnLuopan` should be:
```lua
tpz.geo.spawnLuopan = function(player, target, spell, tick_effect, tick_power, target_type)
```
 
**DONE:**
(Already in release) Geo-Regen effect
Geo-Poison Effect
Geo Global + Spawn Luopan Helper
PetID and Type additions
Luopan Pet Script
Geo-Poison, Geo-Regen, Indi-Poison, Indi-Regen spells
System Messages
Make sure all spell names and file names that have underscores and hyphens are correct

**NOT THIS PR**
Offensive Luopan placement
Bolster 1-Hour


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 11, 2020 at 10:58:54_

----

Regen down is being set in the Lua spawn global (and should probably stay there for ease). I don't remember offhand if [Ecliptic Attrition](https://www.bg-wiki.com/bg/Ecliptic_Attrition) procs on an existing luopan, or if it needs to be used before casting.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 11, 2020 at 11:01:16_

----

Damage mod should probably be added in the Lua global too, if only so people who want to tinker with bubbles can stay in Lua Land.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 11, 2020 at 11:08:16_

----

I'm not going to fight the passed in model argument _for now_, but models _shouldn't_ be an argument for `spawnLuopan` in the Geo- spell scripts. Luopan models are just base model ID (depending if they're supportive or offensive) + the spell's element. When our spell elements are fixed at the fundamental level, all models can be generated by `spawnLuopan` itself. (Although _how_ we inform spawnLuopan of the luopan's intended element will be a _different_ matter.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 11, 2020 at 11:10:43_

----

It'd be real neat if we could pass the spell itself into `spawnLuopan` so we could just ping it to assign its cost instead of needing to pass it into `spawnLuopan`. We could get the luopan's element that way too. But I don't thing spells are currently structured to allow that yet.

**edit** Adding bindings while I'm typing comments is cheating, Zach! 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 11, 2020 at 11:12:17_

----

Because I'm guessing we both dislike the need for this~


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 11:26:17_

----

Agreed!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 11:45:11_

----

I moved all of that configuration stuff into Lua (and the entity flags to SQL), much cleaner!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 11:55:29_

----

I've added some big comments explaining how this should work in the future 👍 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 11, 2020 at 10:58:54_

----

Regen down is being set in the Lua spawn global (and should probably stay there for ease). I don't remember offhand if [Ecliptic Attrition](https://www.bg-wiki.com/bg/Ecliptic_Attrition) procs on an existing luopan, or if it needs to be used before casting.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 11, 2020 at 11:01:16_

----

Damage mod should probably be added in the Lua global too, if only so people who want to tinker with bubbles can stay in Lua Land.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 11, 2020 at 11:08:16_

----

I'm not going to fight the passed in model argument _for now_, but models _shouldn't_ be an argument for `spawnLuopan` in the Geo- spell scripts. Luopan models are just base model ID (depending if they're supportive or offensive) + the spell's element. When our spell elements are fixed at the fundamental level, all models can be generated by `spawnLuopan` itself. (Although _how_ we inform spawnLuopan of the luopan's intended element will be a _different_ matter.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 11, 2020 at 11:10:43_

----

It'd be real neat if we could pass the spell itself into `spawnLuopan` so we could just ping it to assign its cost instead of needing to pass it into `spawnLuopan`. We could get the luopan's element that way too. But I don't thing spells are currently structured to allow that yet.

**edit** Adding bindings while I'm typing comments is cheating, Zach! 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 11, 2020 at 11:12:17_

----

Because I'm guessing we both dislike the need for this~


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 11:26:17_

----

Agreed!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 11:45:11_

----

I moved all of that configuration stuff into Lua (and the entity flags to SQL), much cleaner!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 11:55:29_

----

I've added some big comments explaining how this should work in the future 👍 
