**Labels:**

merge ready



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Thursday May 14, 2020 at 19:21:03_
_Originally opened as: project-topaz/topaz - Issue 620_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

I did a search for mob pools with 0 cmbDelay that were attached to mobs with coordinates.  For each, I infilled some fields from wiki and/or similar pools.  Changes include:

| Mob  | Wiki | Changes  |
| ------------- | ------------- | ------------- |
| Bravo  | [Link](https://ffxiclopedia.fandom.com/wiki/Bravo)  | made SPAWNTYPE_SCRIPTED |
| Ab_xzomit | [Link](https://ffxiclopedia.fandom.com/wiki/Ab'xzomit) | infilled cmbSkill and cmbDelay |
| Aestutaur | [Link](https://ffxiclopedia.fandom.com/wiki/Aestutaur) | infilled cmbSkill and cmbDelay, made linking |
| Akrab | [Link](https://ffxiclopedia.fandom.com/wiki/Akrab) | infilled cmbSkill and cmbDelay |
| Arid_Limule | [Link](https://ffxiclopedia.fandom.com/wiki/Arid_Limule) | infilled cmbSkill and cmbDelay, made BLM, assigned spell list |
| Berserker_Demon | [Link](https://ffxiclopedia.fandom.com/wiki/Berserker_Demon) | infilled cmbSkill and cmbDelay |
| Demon_Befouler | [Link](https://ffxiclopedia.fandom.com/wiki/Demon_Befouler) | infilled cmbSkill and cmbDelay, made DRK, assigned spell list [Fixes #618] |
| Glacial_Imp | [Link](https://ffxiclopedia.fandom.com/wiki/Glacial_Imp) | infilled cmbSkill and cmbDelay, made BLM, made true-aggro and linking, assigned spell list |
| Madthrasher_Zradbodd | [Link](https://ffxiclopedia.fandom.com/wiki/Madthrasher_Zradbodd) | infilled cmbSkill and cmbDelay, made true-aggro linking NM, assigned immunities |
| Snow_Wight | [Link](https://ffxiclopedia.fandom.com/wiki/Snow_Wight) | infilled cmbSkill and cmbDelay, made aggro. Snow Wights can be WAR or BLM. This pool is for WAR. We will need to determine which Snow Wights are BLM from retail, and create a new group and pool for them in another PR later. |
| Spitting_Spider | [Link](https://ffxiclopedia.fandom.com/wiki/Spitting_Spider) | infilled cmbSkill and cmbDelay |



----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday May 14, 2020 at 20:46:56_

----

should we make him a monk? not sure wiki is always right, but that is indicated. I'm new to reviewing so if there are nuances to mob_pools jobs then just let me know!


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday May 14, 2020 at 20:49:36_

----

should its weapon be 7 for scythe instead? not sure if visual representation always equates to actual weapon though. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday May 14, 2020 at 23:30:42_

----

it doesn't. mobs don't have equipment, its just part of their model. He'd do a damage type (slashing, piercing, blunt, h2h) in retail but wouldn't have a "scythe" or  any skill with any weapon type. The attack and accuracy get set in mob_family system and the weapon damage rating and delay are formed from the [mobs level](https://github.com/project-topaz/topaz/blob/5991d15a9a17549ca7a076b7a4a42ee3a26be262/src/map/utils/mobutils.cpp#L72)+dmgMulti and delay fields here in mob_pools, completely ignoring its weapon type field (which afaik only determines if it double swings or not, and possibly wich dmg type to give it by just assuming all swords are slashing etc.)


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday May 14, 2020 at 20:46:56_

----

should we make him a monk? not sure wiki is always right, but that is indicated. I'm new to reviewing so if there are nuances to mob_pools jobs then just let me know!


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday May 14, 2020 at 20:49:36_

----

should its weapon be 7 for scythe instead? not sure if visual representation always equates to actual weapon though. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday May 14, 2020 at 23:30:42_

----

it doesn't. mobs don't have equipment, its just part of their model. He'd do a damage type (slashing, piercing, blunt, h2h) in retail but wouldn't have a "scythe" or  any skill with any weapon type. The attack and accuracy get set in mob_family system and the weapon damage rating and delay are formed from the [mobs level](https://github.com/project-topaz/topaz/blob/5991d15a9a17549ca7a076b7a4a42ee3a26be262/src/map/utils/mobutils.cpp#L72)+dmgMulti and delay fields here in mob_pools, completely ignoring its weapon type field (which afaik only determines if it double swings or not, and possibly wich dmg type to give it by just assuming all swords are slashing etc.)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday May 14, 2020 at 20:38:30_

----

Surprised this didn’t happen sooner, even if _Million Fists_  is hilarious (when its not me).


----
<a href="https://github.com/zircon-tpl"><img src="https://avatars0.githubusercontent.com/u/60901633?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zircon-tpl](https://github.com/zircon-tpl)**
_Friday May 15, 2020 at 01:35:56_

----

Merges by staff into `release` have been disabled for the duration of the Return Home to Vana'diel campaign.

Due to the timing of this submission, I will merge this Pull Request into `release` once it has approval from a second staff member.
