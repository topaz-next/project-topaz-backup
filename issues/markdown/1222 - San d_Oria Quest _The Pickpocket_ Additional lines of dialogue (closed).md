**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Sep 30, 2020 at 14:01:49_
_Originally opened as: project-topaz/topaz - Issue 1222_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

If the quest "The Pickpocket" is QUEST_ACCEPTED, the message of the NPC  should change.

https://github.com/project-topaz/topaz/blob/8985d2af68876367592222836db1f8e5b15c8175/scripts/zones/West_Ronfaure/npcs/Colmaie.lua#L14-L16

    if (player:getQuestStatus(SANDORIA, tpz.quest.id.sandoria.THE_PICKPOCKET) == QUEST_ACCEPTED) then
      player:showText(npc, 7336)
    else
      player:showText(npc, ID.text.COLMAIE_DIALOG)
    end

https://github.com/project-topaz/topaz/blob/8985d2af68876367592222836db1f8e5b15c8175/scripts/zones/West_Ronfaure/npcs/Laillera.lua#L12-L14

    if (player:getQuestStatus(SANDORIA, tpz.quest.id.sandoria.THE_PICKPOCKET) == QUEST_ACCEPTED) then
      player:showText(npc, 7337)
    else
      player:showText(npc, ID.text.LAILLERA_DIALOG)
    end

https://github.com/project-topaz/topaz/blob/8985d2af68876367592222836db1f8e5b15c8175/scripts/zones/West_Ronfaure/npcs/Palcomondau.lua#L324-L327

    if (player:getQuestStatus(SANDORIA, tpz.quest.id.sandoria.THE_PICKPOCKET) == QUEST_ACCEPTED) then
      player:showText(npc, 7383)
    else
      player:showText(npc, ID.text.PALCOMONDAU_DIALOG)
    end
    --npc:wait(1500)

https://github.com/project-topaz/topaz/blob/5fde2aaa74fc534b59875e3c7825317208ed894a/scripts/zones/West_Ronfaure/npcs/Aaveleon.lua#L20-L31

    if sentrysPerilStatus < QUEST_COMPLETED and tradeFinished ~= 1 then
        player:startEvent(101) -- "Ow! Ouch! Gah... If only I'd remembered that ointment!"
    elseif tradeFinished == 1 and not player:hasItem(601) then
        player:startEvent(126, 601) -- "Did you lose it?"
    else
      if (player:getQuestStatus(SANDORIA, tpz.quest.id.sandoria.THE_PICKPOCKET) == QUEST_ACCEPTED) then
        player:showText(npc, 7365)
      else
        player:showText(npc, ID.text.AAVELEON_HEALED) -- "My wounds are healed, thanks to you!"
      end
  end

https://github.com/project-topaz/topaz/blob/8985d2af68876367592222836db1f8e5b15c8175/scripts/zones/West_Ronfaure/npcs/Zovriace.lua#L1025-L1028

    if (player:getQuestStatus(SANDORIA, tpz.quest.id.sandoria.THE_PICKPOCKET) == QUEST_ACCEPTED) then
      player:showText(npc, 7384)
    else
      player:showText(npc, ID.text.ZOVRIACE_DIALOG)
    end
    npc:wait()

