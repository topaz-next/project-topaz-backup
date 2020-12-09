**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Saturday Sep 12, 2020 at 12:15:16_
_Originally opened as: project-topaz/topaz - Issue 1104_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 




----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Saturday Sep 12, 2020 at 12:16:11_

----

(feature branch called eco-warrior) 
Norejaie.lua

```
function onTrigger(player, npc)
    local ecoStatus = player:getCharVar("EcoStatus")

    if ecoStatus == 0 and player:getFameLevel(SANDORIA) >= 1 and player:getCharVar("EcoReset") ~= getConquestTally() then
        player:startEvent(677) -- Offer Eco-Warrior quest
    elseif ecoStatus == 1 then
        player:startEvent(679) -- Reminder dialogue to talk to Rojaireaut
    elseif ecoStatus == 3 and player:hasKeyItem(tpz.ki.INDIGESTED_ORE) then
        player:startEvent(681) -- Complete quest
    elseif ecoStatus > 100 then
        player:startEvent(682) -- Already on a different nation's Eco-Warrior
    else
        player:startEvent(680) -- Default dialogue
    end
end
```
The condition "elseif ecoStatus == 3 and player:hasKeyItem(tpz.ki.INDIGESTED_ORE) then" is wrong.
The correct key item should be "tpz.ki.INDIGESTED_STALAGMITE".


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Sunday Sep 13, 2020 at 15:05:11_

----

Thanks for the fix.
