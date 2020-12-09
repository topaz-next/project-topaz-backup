**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Sep 11, 2020 at 18:05:57_
_Originally opened as: project-topaz/topaz - Issue 1098_

----

Nbu_Latteh.lua
----------------------------------------------------------------------------------------------------
function onTrigger(player, npc)

    elseif (pFame < 2 and momTheAdventurer ~= QUEST_ACCEPTED and questStatus == 0) then
        player:startEvent(230)

    elseif (pFame >= 2 and player:getQuestStatus(BASTOK, tpz.quest.id.bastok.THE_SIGNPOST_MARKS_THE_SPOT) == QUEST_AVAILABLE) then
        player:startEvent(235)
----------------------------------------------------------------------------------------------------
If pFame is 2 or more, skip "Mom, the Adventurer?", "The Signpost Marks the Spot" begins.
In retail, "Mom, the Adventurer?" > "The Signpost Marks the Spot" should be a quest that needs to be digested in order.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Sep 11, 2020 at 18:08:12_

----

This is actually what retail DOES...my new mule did it and could from then on never get the original quest ever even though he'd never done it. ***however*** I would consider changing this an acceptable departure from retail because that's obviously a) dumb that you can miss a quest forever and b) confusing as all hell.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Friday Sep 11, 2020 at 18:43:50_

----

Is this something we want to consider a bug?  It'd be an easy fix... otherwise this should be closed.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Sep 11, 2020 at 19:03:01_

----

I think we should fix it even if its technically retail, for the reasons I stated above


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 04:24:29_

----

So do we just make it so that "The Signpost Marks the Spot" is unlocked by completing "Mom, the Adventurer?" and having fame level 2+?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Sep 13, 2020 at 06:31:45_

----

I would say just allow it to be flagged if its still "available" for now.


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Oct 07, 2020 at 11:29:40_

----

https://github.com/project-topaz/topaz/blob/abfe5dda545545f060a761e894c79d55239ada02/scripts/zones/Bastok_Markets/npcs/Nbu_Latteh.lua#L17-L40

I think the following amendment is a idea.

function onTrigger(player, npc)
    local pFame = player:getFameLevel(BASTOK)
    local momTheAdventurer = player:getQuestStatus(BASTOK, tpz.quest.id.bastok.MOM_THE_ADVENTURER)
    local theSignpostMarksTheSpot = player:getQuestStatus(BASTOK, tpz.quest.id.bastok.THE_SIGNPOST_MARKS_THE_SPOT)
    local questStatus = player:getCharVar("MomTheAdventurer_Event")

    if (player:needToZone()) then
        player:startEvent(127) -- chat about my work
    elseif (momTheAdventurer == QUEST_AVAILABLE) then
        player:startEvent(230)
    elseif (momTheAdventurer == QUEST_ACCEPTED) then
        if (player:seenKeyItem(tpz.ki.LETTER_FROM_ROH_LATTEH)) then
            player:startEvent(234)
        elseif (player:hasKeyItem(tpz.ki.LETTER_FROM_ROH_LATTEH)) then
            player:startEvent(233)
        else
            player:startEvent(231)
        end
    elseif (pFame >= 2 and theSignpostMarksTheSpot == QUEST_AVAILABLE) then
        player:startEvent(235)
    elseif (theSignpostMarksTheSpot == QUEST_ACCEPTED) then
        player:startEvent(231)
    else
        player:startEvent(127)
    end
end

Also, while Nbu Latteh is on a quest, the NPC "Parnika" message will change.

https://github.com/project-topaz/topaz/blob/abfe5dda545545f060a761e894c79d55239ada02/scripts/zones/Bastok_Markets/npcs/Parnika.lua#L10-L12

    local momTheAdventurer = player:getQuestStatus(BASTOK, tpz.quest.id.bastok.MOM_THE_ADVENTURER)
    local theSignpostMarksTheSpot = player:getQuestStatus(BASTOK, tpz.quest.id.bastok.THE_SIGNPOST_MARKS_THE_SPOT)

    if (momTheAdventurer == QUEST_ACCEPTED or theSignpostMarksTheSpot == QUEST_ACCEPTED) then
        player:startEvent(232)
    else
        player:startEvent(136)
    end




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 08, 2020 at 14:27:06_

----

tip:

if you use ```lua  it will color your code


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 08, 2020 at 14:27:40_

----

```lua
if (player:needToZone()) then
    player:startEvent(127) -- chat about my work
elseif (momTheAdventurer == QUEST_AVAILABLE) then
    player:startEvent(230)
elseif (momTheAdventurer == QUEST_ACCEPTED) then
    if (player:seenKeyItem(tpz.ki.LETTER_FROM_ROH_LATTEH)) then
        player:startEvent(234)
    elseif (player:hasKeyItem(tpz.ki.LETTER_FROM_ROH_LATTEH)) then
        player:startEvent(233)
    else
        player:startEvent(231)
    end
elseif (pFame >= 2 and theSignpostMarksTheSpot == QUEST_AVAILABLE) then
    player:startEvent(235)
elseif (theSignpostMarksTheSpot == QUEST_ACCEPTED) then
    player:startEvent(231)
else
    player:startEvent(127)
end
```


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Oct 09, 2020 at 00:23:37_

----

Thanks for the tips.
I will try to use it in the future.

