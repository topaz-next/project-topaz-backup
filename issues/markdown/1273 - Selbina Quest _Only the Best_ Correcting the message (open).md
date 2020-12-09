**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Thursday Oct 08, 2020 at 02:44:59_
_Originally opened as: project-topaz/topaz - Issue 1273_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

The message about the player's gender has not been affected. (L37, L39)
The item name in the message is missing. (L26, L28, L30)

https://github.com/project-topaz/topaz/blob/abfe5dda545545f060a761e894c79d55239ada02/scripts/zones/Selbina/npcs/Melyon.lua#L14-L41

```
function onTrade(player, npc, trade)
    if
        player:getQuestStatus(JEUNO, tpz.quest.id.jeuno.RIDING_ON_THE_CLOUDS) == QUEST_ACCEPTED and
        player:getCharVar("ridingOnTheClouds_3") == 3 and
        npcUtil.tradeHas(trade, 1127)
    then
        player:setCharVar("ridingOnTheClouds_3", 0)
        npcUtil.giveKeyItem(player, tpz.ki.SOMBER_STONE)
        player:confirmTrade()

    elseif player:getQuestStatus(OTHER_AREAS_LOG, tpz.quest.id.otherAreas.ONLY_THE_BEST) ~= QUEST_AVAILABLE then
        if npcUtil.tradeHas(trade, {{4366, 5}}) then -- La Theine Cabbage x5
            player:startEvent(62, 0, 4366)
        elseif npcUtil.tradeHas(trade, {{629, 3}}) then -- Millioncorn x3
            player:startEvent(63, 0, 629)
        elseif npcUtil.tradeHas(trade, 919) then -- Boyahda Moss x1
            player:startEvent(64, 0, 919)
        end
    end
end

function onTrigger(player, npc)

    local gender = player:getGender()

    if player:getQuestStatus(OTHER_AREAS_LOG, tpz.quest.id.otherAreas.ONLY_THE_BEST) == QUEST_AVAILABLE then
        player:startEvent(60, 4366, 629, 919, gender) -- Start quest "Only the Best"
    else
        player:startEvent(61, 4366, 629, 919, gender) -- During & after completed quest "Only the Best"

    end
end
```

