**Labels:**



<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [neuromancerxi](https://github.com/neuromancerxi)**
_Thursday Oct 29, 2020 at 21:47:40_
_Originally opened as: project-topaz/topaz - Issue 1454_

----

Modifies/Reorders magic_shield and physical_shield effects and adds new tiers.
Moves Rampart IronWill check to rampart effect.
Modifies the MAGIC_SHIELD check to check which power tier is active before flooring magic.
Adds scripts for Fanatics/Fools Drink/Tonics.
Adds scripts for Carnal/Spiritual Incense.
Adjusts timers to 1s where applicable.
Adjusts scripts to new values where applicable.

**SPECIAL NOTE TO SERVER OPERATORS**: Make sure you check your custom scripts when merging this change. This adjusts the scripts that existed in Topaz at the time of submission, but due to the change in how power is now applied, please make sure any scripts that use apply (and possibly remove) MAGIC_SHIELD and/or PHYSICAL_SHIELD effects use the new values in the effects.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


