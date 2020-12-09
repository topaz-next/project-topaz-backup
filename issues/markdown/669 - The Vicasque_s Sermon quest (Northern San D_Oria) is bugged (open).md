**Labels:**



<a href="https://github.com/vyvin"><img src="https://avatars1.githubusercontent.com/u/1476809?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [vyvin](https://github.com/vyvin)**
_Sunday May 31, 2020 at 05:34:35_
_Originally opened as: project-topaz/topaz - Issue 669_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [X] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [X] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Several of the npc's related to this quest have missing or incorrect text.
See https://www.youtube.com/watch?v=VYNz04yf1uQ for some of the correct text.
Abioleget never says anything about trading 70 gil to get the peas.
Andelain says something about waiting 618 minute's instead of only being able to eat 3 blue peas a day



----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday May 31, 2020 at 06:06:07_

----

What do you get when you run
/ver
on your client?


----
<a href="https://github.com/vyvin"><img src="https://avatars1.githubusercontent.com/u/1476809?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [vyvin](https://github.com/vyvin)**
_Sunday May 31, 2020 at 06:10:35_

----

30200327_2

also sorry for the initial crap post...was playing in-game and didn't realize I hadn't had the game in focus XD


----
<a href="https://github.com/vyvin"><img src="https://avatars1.githubusercontent.com/u/1476809?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [vyvin](https://github.com/vyvin)**
_Tuesday Jun 02, 2020 at 05:02:13_

----

I believe the following code should be more accurate to NPC Andelain for his responses.  Not sure on before getting quest or after giving peas, and after turning in to Abioleget.

```
-----------------------------------
require("scripts/globals/settings");
require("scripts/globals/quests");
-----------------------------------
function onTrade(player,npc,trade)
    sermonQuest = player:getQuestStatus(SANDORIA,tpz.quest.id.sandoria.THE_VICASQUE_S_SERMON);

    if (sermonQuest == QUEST_ACCEPTED) then
        count = trade:getItemCount();
        BluePeas = trade:getItemQty(618);
        if (BluePeas == 1 and count == 1 and player:getCharVar("sermonQuestVar") == 0) then
            player:tradeComplete();
            player:showText(npc, 7414);
			player:showText(npc,7416);
            player:startEvent(19);
            player:setCharVar("sermonQuestVar",1);
        elseif (BluePeas > 1 and count == BluePeas) then
            player:showText(npc, 7417,618);
        else
			player:showText(npc, 7415);
		end
    else
        player:showText(npc, 7415);
    end
end;

function onTrigger(player,npc)
	if (sermonQuest == QUEST_ACCEPTED and player:getCharVar("sermonQuestVar") == 0) then
		player:showText(npc,7413,618);
	else
		player:showText(npc,7412);
	end
end;

function onEventUpdate(player,csid,option)
end;

function onEventFinish(player,csid,option)
end;
```

I believe this should fix Abbioleget to more accurately coincide with the quest:

```
-----------------------------------
local ID = require("scripts/zones/Northern_San_dOria/IDs");
require("scripts/globals/settings");
require("scripts/globals/titles");
require("scripts/globals/quests");
-----------------------------------

function onTrade(player,npc,trade)
    if (sermonQuest == QUEST_ACCEPTED) then
        gil = trade:getGil();
        count = trade:getItemCount();
        if (gil == 70 and count == 1) then
            player:tradeComplete();
            player:startEvent(591);
        end
    end
end;

function onTrigger(player,npc)
    sermonQuest = player:getQuestStatus(SANDORIA,tpz.quest.id.sandoria.THE_VICASQUE_S_SERMON);

    if (sermonQuest == QUEST_AVAILABLE) then
        player:startEvent(589);
    elseif (sermonQuest == QUEST_ACCEPTED) then
        if (player:getCharVar("sermonQuestVar") == 1) then
            player:tradeComplete();
            player:startEvent(600);
        else
            player:showText(npc,11243,618,70);
        end
    else
        player:showText(npc,ID.text.ABIOLEGET_DIALOG);
    end
end;

function onEventUpdate(player,csid,option)
end;

function onEventFinish(player,csid,option)

    if (csid == 600) then
        if (player:getFreeSlotsCount() == 0) then
            player:messageSpecial(ID.text.ITEM_CANNOT_BE_OBTAINED,13465);
        else
            player:addItem(13465);
            player:messageSpecial(ID.text.ITEM_OBTAINED, 13465);
            player:addFame(SANDORIA,30);
            player:addTitle(tpz.title.THE_BENEVOLENT_ONE);
            player:setCharVar("sermonQuestVar",0);
            player:completeQuest(SANDORIA,tpz.quest.id.sandoria.THE_VICASQUE_S_SERMON );
        end
    elseif (csid == 589) then
        player:addQuest(SANDORIA,tpz.quest.id.sandoria.THE_VICASQUE_S_SERMON );
    elseif (csid == 591) then
        player:addItem(618);
        player:messageSpecial(ID.text.ITEM_OBTAINED, 618);
    end
end;

```


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Sep 30, 2020 at 00:44:49_

----

Related to this issue, the message of NPC "Andelain" in East Ronfaure is also wrong (L20).

https://github.com/project-topaz/topaz/blob/3bc611df9cace45b9ebd3afe5635aa453fa886b1/scripts/zones/East_Ronfaure/npcs/Andelain.lua#L12-L39

The Right Message
player:showText(npc, 7414)
player:showText(npc, 7416)

Andelain after completing the trade
player:showText(npc, 7416)

Arnau after completing the trade
player:showText(npc, 11248)





----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Sep 30, 2020 at 01:04:57_

----

unrelated to the message being wrong but just want to share: 

almost nothing should ever be using showText, and anything that looks like it should is an event on retail instead. in cases where it is just a line of dialog it should use messageSpecial instead of showText 

showTextis a combination of changing the NPCs rotation value, triggering the exact same  message packet that messageSpecial uses, and then locking the NPCs line of site onto the player that activated it..which results in a hilarious bobble head thing if you move around them repeatedly.


Lots of old code mistakenly uses showText and worse, uses a magic number instead of the human readable textIDs defined per-zone. https://github.com/project-topaz/topaz/blob/3bc611df9cace45b9ebd3afe5635aa453fa886b1/scripts/zones/East_Ronfaure/IDs.lua#L13

So please whoever fixes these, _use/add to the text Ids not the numbers_


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Thursday Oct 01, 2020 at 15:53:32_

----

Thank you for sharing this valuable information.

I will learn more about messageSpecial.
I also understand the use of textID.


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Oct 02, 2020 at 11:37:32_

----

How can I solve the problem of the NPC's name not appearing in the message in player:messageSpecial?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 04, 2020 at 03:21:49_

----

> How can I solve the problem of the NPC's name not appearing in the message in player:messageSpecial?

thats sometimes a sign that its the wrong text ID or shoudl be an event instead of a message, but we do have ways to force the npc name in.

https://github.com/project-topaz/topaz/blob/release/src/map/lua/lua_baseentity.cpp#L492
```cpp
    if (!lua_isnil(L, 6) && lua_isboolean(L, 6))
        showName = (lua_toboolean(L, 6) == 0 ? false : true);
```
if the 6th param of the function is true rather than a number, it force shows the entities name.

We also have `messageName()` and I think 1 other alternate version (same IDs, but diff packet ID) for some special situations. For those confirming which packet retail sent tells us which we should be using. In the case of `messageName()` I believe that only accepts global (aka "basic") ID instead of per-zone IDs.


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Monday Oct 05, 2020 at 03:01:37_

----

We let the NPC "Halver" execute the following code as a trial, but the NPC's name did not appear.
Is there a problem with the code?

function onTrigger(player, npc)
  player:messageSpecial(7080,0,0,0,0,0,1)
end



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 05, 2020 at 16:28:59_

----

the value I called true is not a number. its is a boolean and must be either "true" or "false" without quotes.

Note that this doesn't always work, its dependent on what that message is supposed to actually be (I do -not- mean "what the text says"). Strongly recommend getting someone to retail capture it.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 05, 2020 at 16:48:50_

----

~~P.S. these numbers for the message ID is no longer valid on the latest client. 7414 will show Japanese text because the values have shifted. Another reason to not use the numbers.~~_Ignore that, wrong zone when I checked it. That does happen pretty much every update though._

We have a mostly automated way to update them ones they are included in the text IDs, but I feel it is likely these should not be showtext or message special and most likely should be startEvent (which uses a different ID index). Its pretty rare for the name to be missing with messageSpecial.


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Oct 07, 2020 at 00:35:57_

----

Thanks for the explanation.

I set the sixth parameter of "player:messageSpecial" to "true", but again, the name of the npc is not displayed. Is there a problem with the code?

player:messageSpecial(ID.text.AAVELEON_HEALED, 0, 0, 0, 0, 0, true) -- "My wounds are healed, thanks to you!"

The following example is npc "Aaveleon", I think it's OK to change the orientation of this npc, but do you still think we should use "player:messageSpecial" rather than "player:showText"?

https://github.com/project-topaz/topaz/blob/b402b1b668f865723b11f9699b0b0b09bcf9268b/scripts/zones/West_Ronfaure/npcs/Aaveleon.lua#L20-L30



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 07, 2020 at 00:37:36_

----

see related issue I tagged regarding the NPC who's line that is.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 07, 2020 at 00:40:40_

----

TL;DR Andelain.lua is a hot mess because an author in teh distant past could not get the correct event ID working because of something the core doesn't handle right, and decided to half ass it with showText while still leaving the broken event in place, which freezes the client until you tap the escape key. Those lines are not part of a normal message, so they will not normally show the npc name because the NPC's name would be at the beginning of its dialog, and this is in the middle.


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Oct 07, 2020 at 03:55:21_

----

Thanks for the explanation.
I don't fully understand it yet, but I'd like to look into it, referring to various past cases, etc.
