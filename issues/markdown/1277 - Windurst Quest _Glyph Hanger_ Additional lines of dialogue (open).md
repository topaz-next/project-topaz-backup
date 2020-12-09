**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Thursday Oct 08, 2020 at 06:16:45_
_Originally opened as: project-topaz/topaz - Issue 1277_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

If the quest "Glyph Hanger" is QUEST_ACCEPTED the message of the NPC should change.

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Waters/npcs/Serukoko.lua#L7-L15

```
-----------------------------------
local ID = require("scripts/zones/Windurst_Waters/IDs")
require("scripts/globals/settings")
require("scripts/globals/keyitems")
require("scripts/globals/quests")
-----------------------------------

function onTrade(player, npc, trade)
end

function onTrigger(player, npc)
    GlyphHanger = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.GLYPH_HANGER)
    if (GlyphHanger == QUEST_ACCEPTED and player:hasKeyItem(tpz.ki.NOTES_FROM_IPUPU) == false) then
        player:startEvent(383)
    else
        player:startEvent(373)
    end
end
```

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Waters/npcs/Sohdede.lua#L8-L15

```
-----------------------------------
local ID = require("scripts/zones/Windurst_Waters/IDs")
require("scripts/globals/settings")
require("scripts/globals/keyitems")
require("scripts/globals/quests")
-----------------------------------

function onTrade(player, npc, trade)
end

function onTrigger(player, npc)
    GlyphHanger = player:getQuestStatus(WINDURST, tpz.quest.id.windurst.GLYPH_HANGER)
    if (GlyphHanger == QUEST_ACCEPTED and player:hasKeyItem(tpz.ki.NOTES_FROM_IPUPU) == false) then
        player:startEvent(384)
    else
        player:startEvent(374)
    end
end

```
