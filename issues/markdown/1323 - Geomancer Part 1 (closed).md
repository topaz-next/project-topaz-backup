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
