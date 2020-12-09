**Labels:**



<a href="https://github.com/gweivyth"><img src="https://avatars2.githubusercontent.com/u/37130689?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [gweivyth](https://github.com/gweivyth)**
_Saturday Jun 27, 2020 at 16:01:47_
_Originally opened as: project-topaz/topaz - Issue 777_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Shiva's Claws do not currently have a lua.  Was working on my own project and fixed them, thought I would submit back.

```lua
-----------------------------------------
-- ID: 17492
-- Item: Shiva's Claws
-- Additional Effect: Paralyze
-- Gweivyth
----------------------------------
require("scripts/globals/status")
require("scripts/globals/magic")
require("scripts/globals/msg")
-----------------------------------

function onAdditionalEffect(player, target, damage)
    local chance = 10
    
        if (VanadielDayElement() == tpz.day.ICEDAY) then
        chance = chance+6
end
    if math.random(100) <= chance and applyResistanceAddEffect(player, target, tpz.magic.ele.ICE, 0) > 0.5 then
        target:addStatusEffect(tpz.effect.PARALYSIS, 10, 0, 30)
        return tpz.subEffect.PARALYSIS, tpz.msg.basic.ADD_EFFECT_STATUS, tpz.effect.PARALYSIS
    end

    return 0, 0, 0
end
```
