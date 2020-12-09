**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Thursday Oct 08, 2020 at 05:04:20_
_Originally opened as: project-topaz/topaz - Issue 1276_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

The message of NPC "Machitata" is wrong.
"player:messageSpecial" is used (The message is different), but I think "player:startEvent" should be used because there is a cutscene.
Standard Conversation does not exist.

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Waters/npcs/Machitata.lua#L14-L33

```
function onTrigger(player, npc)
    function testflag(set, flag)
        return (set % (2*flag) >= flag)
    end
    hatstatus = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.HAT_IN_HAND)
    if ((hatstatus == 1  or player:getCharVar("QuestHatInHand_var2") == 1) and testflag(tonumber(player:getCharVar("QuestHatInHand_var")), 1) == false) then
        player:startEvent(58);
    else
        player:startEvent(526) -- Standard Conversation
    end
end

function onEventUpdate(player, csid, option)
end

function onEventFinish(player, csid, option)

    if (csid == 58) then  -- Show Off Hat
        player:addCharVar("QuestHatInHand_var", 8)
        player:addCharVar("QuestHatInHand_count", 1)
    end

end
```


