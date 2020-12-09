**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Thursday Oct 08, 2020 at 10:56:35_
_Originally opened as: project-topaz/topaz - Issue 1283_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

This quest has different messages depending on the items you trade.
The current combination of items and messages seems to be the opposite. (L21, L23)

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Woods/npcs/Tapoh_Lihzeh.lua#L13-L26

```
    -- PAYING LIP SERVICE
    elseif player:getQuestStatus(WINDURST, tpz.quest.id.windurst.PAYING_LIP_SERVICE) >= QUEST_ACCEPTED then
        if npcUtil.tradeHas(trade, {{912, 3}}) then
            player:startEvent(479, 0, 912, 1016, 0, 0)
        elseif npcUtil.tradeHas(trade, {{1016, 2}}) then
            player:startEvent(479, 0, 912, 1016, 0, 1)
        end
    end
```





