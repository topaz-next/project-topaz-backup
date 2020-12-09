**Labels:**

bug



<a href="https://github.com/Bargor-Resolute"><img src="https://avatars1.githubusercontent.com/u/61029208?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Bargor-Resolute](https://github.com/Bargor-Resolute)**
_Sunday Mar 15, 2020 at 16:05:42_
_Originally opened as: project-topaz/topaz - Issue 429_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Elemental Sforzo is already coded in the status effect list and is available when you use godmode, but the ability itself is not coded as an ability for runefencer to use natively. 

-----------------------------------
-- Ability: Elemental Sforzo
-- Grants immunity to all magical attacks.
-- Obtained: Runefencer Level 1
-- Recast Time: 1:00:00
-- Duration: 0:00:30
-----------------------------------
require("scripts/globals/settings")
require("scripts/globals/status")
-----------------------------------

function onAbilityCheck(player,target,ability)
    return 0,0
end

function onUseAbility(player,target,ability)
    player:addStatusEffect(tpz.effect.ELEMENTAL_SFORZO,1,0,30)
end






----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 11, 2020 at 03:44:58_

----

Just merged #464 . Thanks for bringing this up, Bargor!
