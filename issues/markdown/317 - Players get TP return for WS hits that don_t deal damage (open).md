**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:23_
_Originally opened as: project-topaz/topaz - Issue 317_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 13, 2019 at 16:54 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6241_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** n/a

**_Source Branch_** (master/stable) **:** master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 


TP return for weaponskills is calculated by `tp/hitsLanded`. This is [incremented when a player passes a whiff check for each hit of their weaponskill, and currently does not check the `dmg` that was dealt by the hit](github/DarkstarProject/darkstar/blob/master/scripts/globals/weaponskills.luaDarkstar Issue L53).

**Side note:** [Per-hit damage isn't checked against Stoneskin at this point either](github/DarkstarProject/darkstar/blob/master/scripts/globals/weaponskills.luaDarkstar Issue L34-L40). It _is_ checked against the _total_ damage that is [passed into the defender's takeWeaponSkillDamage](github/DarkstarProject/darkstar/blob/ba4d44dc6039b61c0b217596f9176939930949a9/src/map/utils/battleutils.cppDarkstar Issue L2043-L2047). Though I'm not sure if this distinction is important for _final damage_ (but duplicated hybrid hits come to mind).

I can't say _100%_ that zero-per-hit vs zero-over-whole-WS matters for _TP return_. Or, so long as a weaponskill deals more than zero total damage, if the WS should return TP equivalent to all landed hits, or if it should only return TP for the hits that actually contributed to the total damage. I've been unable to find a clear source.

_BUT_ the player is going to get credit for all non-whiff hits over the entire weaponskill regardless, because [no check against final damage is made before returning the number of hits landed](github/DarkstarProject/darkstar/blob/master/scripts/globals/weaponskills.luaDarkstar Issue L407-L408) back to [the calling weaponskill](github/DarkstarProject/darkstar/blob/master/scripts/globals/weaponskills/asuran_fists.luaDarkstar Issue L36-L37).

(And in my preemptive defense, [this isn't my fault...!](github/DarkstarProject/darkstar/blob/3edcc7b6c22bcf16227a2d3b3cc47da7baa046f2/scripts/globals/weaponskills.luaDarkstar Issue L267-L268))




