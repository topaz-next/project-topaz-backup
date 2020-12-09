**Labels:**

bug

focus



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 18, 2020 at 10:00:54_
_Originally opened as: project-topaz/topaz - Issue 351_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

At the top of [the blue magic global file](https://github.com/project-topaz/topaz/blob/3df25d52158be6d44dfe84f198194b6822b5ebb8/scripts/globals/bluemagic.lua), there are [various "TPMOD" globals defined.](https://github.com/project-topaz/topaz/blob/3df25d52158be6d44dfe84f198194b6822b5ebb8/scripts/globals/bluemagic.lua#L4-L9)

A lot of blue magic scripts define their "tpmod" as part of their params:
[Battle Dance](https://github.com/project-topaz/topaz/blob/3df25d52158be6d44dfe84f198194b6822b5ebb8/scripts/globals/spells/bluemagic/battle_dance.lua#L28)
[Cannonball](https://github.com/project-topaz/topaz/blob/3df25d52158be6d44dfe84f198194b6822b5ebb8/scripts/globals/spells/bluemagic/cannonball.lua#L27)
[Foot Kick](https://github.com/project-topaz/topaz/blob/3df25d52158be6d44dfe84f198194b6822b5ebb8/scripts/globals/spells/bluemagic/foot_kick.lua#L27)

This table of params [is then passed](https://github.com/project-topaz/topaz/blob/3df25d52158be6d44dfe84f198194b6822b5ebb8/scripts/globals/spells/bluemagic/cannonball.lua#L44-L45) to [BluePhysicalSpell](https://github.com/project-topaz/topaz/blob/3df25d52158be6d44dfe84f198194b6822b5ebb8/scripts/globals/bluemagic.lua#L55) and [BlueFinalAdjustments](https://github.com/project-topaz/topaz/blob/3df25d52158be6d44dfe84f198194b6822b5ebb8/scripts/globals/bluemagic.lua#L218).

The comment for BluePhysicalSpell [says that "tpmod" is a valid param](https://github.com/project-topaz/topaz/blob/3df25d52158be6d44dfe84f198194b6822b5ebb8/scripts/globals/bluemagic.lua#L38). The function does not reference this value at all. Nothing in the global references or checks the value of a param by this name. This params table also does not seem to be passed off to any binding that might later reference the value in core.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Feb 18, 2020 at 14:56:07_

----

https://www.bg-wiki.com/bg/Calculating_Blue_Magic_Damage
Valuable reference for anyone trying to understand Blue Magic Damage and wants to work on making these retail accurate.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Apr 08, 2020 at 03:28:38_

----

TPMOD_DURATION, is used in the following blue magic spell luas:
- sprout smack
- wild oats
- battle dance
and duration varies with tp would also affect the following spells:
- pinecone bomb
- queasyshroom
- sweeping gouge
- bilgestorm
