**Labels:**

focus

improvement



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 08, 2020 at 12:57:28_
_Originally opened as: project-topaz/topaz - Issue 824_

----

Many Blue Magic spell scripts have been defining a `scattr` param:
- https://github.com/project-topaz/topaz/blob/blue-mage/scripts/globals/spells/bluemagic/1000_needles.lua#L30
- https://github.com/project-topaz/topaz/blob/blue-mage/scripts/globals/spells/bluemagic/bludgeon.lua#L30
- https://github.com/project-topaz/topaz/blob/blue-mage/scripts/globals/spells/bluemagic/power_attack.lua#L30

Despite duplicate enum definitions for skillchains in the file (which is how I came across this), this param is never referenced in [the `bluemagic` global](https://github.com/project-topaz/topaz/blob/blue-mage/scripts/globals/bluemagic.lua).

"What if it gets used in core?"

The spell scripts pass the params table to [BluePhysicalSpell](https://github.com/project-topaz/topaz/blob/blue-mage/scripts/globals/bluemagic.lua#L56-L115) and [BlueFinalAdjustments](https://github.com/project-topaz/topaz/blob/blue-mage/scripts/globals/bluemagic.lua#L219-L241). Neither of these functions hand the `params` table to a core function.

Additionally, mass-find for `scattr` over the entire project only returns the individual spell scripts defining their attributes. No results in core.

The [Chain Affinity ability script](https://github.com/project-topaz/topaz/blob/blue-mage/scripts/globals/abilities/chain_affinity.lua) only applies the [Chain Affinity effect](https://github.com/project-topaz/topaz/blob/blue-mage/scripts/globals/effects/chain_affinity.lua).

Per mass-find, [all this effect does in lua is apply additional fTP and multipliers to the damage](https://github.com/project-topaz/topaz/blob/blue-mage/scripts/globals/bluemagic.lua#L91-L101).

Core does use the Chain Affinity effect; it [checks for the effect on cast finish and applies the in-core spell object's skillchain attributes](https://github.com/project-topaz/topaz/blob/release/src/map/entities/charentity.cpp#L727-L729) which [get set by `setPrimarySkillchain`](https://github.com/project-topaz/topaz/blob/release/src/map/spell.cpp#L509) while [loading the spell from blue_spell_list table](https://github.com/project-topaz/topaz/blob/release/src/map/spell.cpp#L478-L481).

So Blue Mages can skillchain with Chain Affinity as it's handled by Core and the spells' special SQL table. But the duplicate skillchain property definitions in lua do absolutely nothing.

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

