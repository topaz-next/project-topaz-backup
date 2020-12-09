**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Saturday Oct 10, 2020 at 17:26:46_
_Originally opened as: project-topaz/topaz - Issue 1312_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

If the quest "Curses, Foiled A-Golem!?" is QUEST_ACCEPTED the message of the NPC should change.

https://github.com/project-topaz/topaz/blob/c2aa517599909fa0473f9739861ea8feb432d9ac/scripts/zones/Beaucedine_Glacier/npcs/Torino-Samarino.lua#L38-L41
```
    elseif (FoiledAGolem == QUEST_ACCEPTED) then
        if (player:hasKeyItem(tpz.ki.SHANTOTTOS_NEW_SPELL)) then
            player:startEvent(105)
        elseif (player:getCharVar("foiledagolemdeliverycomplete") == 1) then
            player:startEvent(110)
        else
            player:startEvent(104) -- receive key item
        end
    elseif tuningOutProgress == 7 then
```

https://github.com/project-topaz/topaz/blob/c2aa517599909fa0473f9739861ea8feb432d9ac/scripts/zones/Beaucedine_Glacier/npcs/Potete.lua#L11-L13
```
function onTrigger(player, npc)
    local FoiledAGolem = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.CURSES_FOILED_A_GOLEM)
    if (FoiledAGolem == QUEST_ACCEPTED) then
      if (player:hasKeyItem(tpz.ki.SHANTOTTOS_NEW_SPELL)) then
          player:startEvent(106)
      elseif (player:getCharVar("foiledagolemdeliverycomplete") == 1) then
          player:startEvent(111)
      else
          player:startEvent(102)
      end
    else
      player:startEvent(102)
    end
end
```

https://github.com/project-topaz/topaz/blob/c2aa517599909fa0473f9739861ea8feb432d9ac/scripts/zones/Beaucedine_Glacier/npcs/Leigon-Moigon.lua#L10-L12
```
function onTrigger(player, npc)
    local FoiledAGolem = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.CURSES_FOILED_A_GOLEM)
    if (FoiledAGolem == QUEST_ACCEPTED) then
      if (player:hasKeyItem(tpz.ki.SHANTOTTOS_NEW_SPELL)) then
          player:startEvent(107)
      elseif (player:getCharVar("foiledagolemdeliverycomplete") == 1) then
          player:startEvent(112)
      else
        player:startEvent(103)
      end
    else
      player:startEvent(103)
    end
end
```
