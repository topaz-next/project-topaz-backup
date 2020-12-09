**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday May 18, 2020 at 15:50:18_
_Originally opened as: project-topaz/topaz - Issue 640_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
So, back when I wrote the initial parts of Grounds of Valor, wiki said the buffs stack up to 11 times. So that's what I did (`#sh*tWikiSays` strikes again). [Wiki has since been updated to correctly reflect that not all the buffs have the same maximum number of times they will stack.](https://ffxiclopedia.fandom.com/wiki/Grounds_of_Valor#Prowesses)

This is an easy to moderate task for someone with the time an inclination to re-code that section to a nice neat table. Past me apologizes for leaving you with an if/else. ~~The prowess effects should also wear off on zoning out but -not- from logging out. This is controlled by effect flags. There was a bug where they would still get removed even when they were not supposed to - I do not know if that was fixed or not. I want to say it had to do with inf duration being "zero" and the effects being wiped out on zone if they had less than a full tick. /shrug~~ 

Here's the stacking info for prowess effects:

Name | Type | Effect | Max level
-- | -- | -- | --
"Killer" effects bonus | Job Trait | Increases "Killer" effects bonus. | 2
Treasure Hunter Bonus | Treasure Hunter | Adds Treasure Hunter+1 for each level attained. | 3
Attack Speed Bonus | Haste | Increases attack speed. | 4
Increased Crystal Yield | Crystals | Increases Crystal drop rate. | 5
Increased Weapon Skill Damage | Attack | Increases Weapon Skill Damage by 2% for Stage 1. | 5
Increased Cure Potency | Cure Potency | Increases Cure Potency. (Level 1 is 4%) | 5
Increased Treasure Casket Discovery | Treasure Casket | Increases encounters. | 5
Increased Magic accuracy and Magic attack | Magic Attack & Magic Accuracy | Increases Magic Attack and Magic Accuracy. | 10
Increased HP and MP | HP & MP | Increases HP and MP. (Level 1 is 3%, Level 11 is about 12.9% of (base) HP and MP) | 11
Enhanced attack and ranged attack | Attack | Increases Attack and Ranged Attack. | 11
Increased combat and magic skill gain | Skill Ups | Increases Combat and magic skill up frequency. | 11
Enhanced accuracy and ranged accuracy | Accuracy | Increases Accuracy and Ranged Accuracy. | 11



As you can see only 4 of them stacked to 11x


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday May 18, 2020 at 15:57:59_

----

@TeoTwawki log off bug was fixed.
