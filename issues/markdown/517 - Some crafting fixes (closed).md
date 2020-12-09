**Labels:**

crafting

merge ready



<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Thursday Apr 23, 2020 at 15:20:57_
_Originally opened as: project-topaz/topaz - Issue 517_

----

- Translated comments
Also added some more

- Made HQ calculations take into account the level of all skills involved in a recipe, not just highest.
Retail sets HQ tiers, depending on the levels of all skills involved. Topaz and DSP on the other hand just does it based on the highest lvl skill.
- Removed unused function

- Made desynths work
  If a recipe is a desynth, Success rate is lowered and HQ rate is raised.

- Removed bias against lighting crystals.
  It was being used a substitute for desynth.

Thanks to Teo for the help. ^^

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 23, 2020 at 15:43:32_

----

> Removed bias against lighting crystals.
Crafting (right now) doesnt check if a recipe is a synth or a desynth.
Desynths are suposed to have a lower success rate and a higher HQ rate.
Currently, it just lowered success rate whenever a Lightning crystal is used, wich isn't correct, since not all recipes that use a lightning crystal are desynths and not all desynths use lightning crystals.

[There is actually a database field for this](https://github.com/project-topaz/topaz/blob/release/sql/synth_recipes.sql#L28) that for completely dumb reasons was never used in the core.

The existing rows in the table will need checked to ensure they have a consistent use of it (some rows may have the incorrect value in that column at present, suggest running a select query to see which ones have it set to `1` and which don't after decide if it will be 1 or 0 to mean "yes its a desynth")


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Apr 23, 2020 at 16:08:37_

----

Does this PR fix https://github.com/project-topaz/topaz/issues/401 ? :cat: 


----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Thursday Apr 23, 2020 at 16:28:59_

----

nope, this doesnt fix #401, although...

double skillUpChance = ((double)baseDiff*(map_config.craft_chance_multiplier - (log(1.2 + charSkill/100))))/10;

this line might have something to do with it


----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Thursday Apr 23, 2020 at 16:40:09_

----

@TeoTwawki suposedly, that value is stored.

line 69 and 70
SELECT ID, KeyItem, Wood, Smith, Gold, Cloth, Leather, Bone, Alchemy, Cook, Result, ResultHQ1, ResultHQ2, ResultHQ3, ResultQty, ResultHQ1Qty, ResultHQ2Qty, ResultHQ3Qty, Desynth

FROM synth_recipes

this takes the values from synth recipe list and this....
line 115

PChar->CraftContainer->setCraftType((uint8)Sql_GetUIntData(SqlHandle, 18)); // Store if it's a desynth

so it should be as easy as pulling the value out of the CraftContainer and doing a few "if" checks here and there, but i suck at programing, so i dont know how to properly write....

if CraftContainer cell18 =1 //if desynth
{
    success  = success/2
}


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 23, 2020 at 16:47:29_

----

If someone actually added it I dunno why they left the crystal check in instead of 
```cpp
if (PChar->CraftContainer->getCraftType() ==  1)
{
    doTheThing;
}
```
According to the snippet you quoted its being fed into `setCraftType()` already, so it should already be there for the matching "get"


----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Thursday Apr 23, 2020 at 17:06:09_

----

gonna test that and see if it works.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 23, 2020 at 19:28:50_

----

Does any wiki mention any diff in HQ rates on desynths? I kinda feel like only mt "break" rate was worse on desynths, but I don't have data so you can't trust me on that.


----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Thursday Apr 23, 2020 at 19:33:44_

----

https://ffxiclopedia.fandom.com/wiki/Desynthesis
"Also, unlike normal crafting, the chances of getting a High Quality result from Desynthesis is greatly increased"

I also read it from various old forums

In the end, this numbers are guess-work and need to be tested and tweaked.

This PR aims to make crafting less cheaty than what we currently have, wich are easy HQs and desynths not being desynths


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 23, 2020 at 20:02:51_

----

 awesome, so actually goes up, not down


----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Wednesday Apr 29, 2020 at 15:06:04_

----

I've updated the comment block and added some to-do things left.
Even then, i'd rather this be reviewed and tested by more people other than me before correcting anything else, mainly to ease any future edits and reviews
