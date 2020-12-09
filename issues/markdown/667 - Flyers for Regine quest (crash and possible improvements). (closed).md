**Labels:**

bug

improvement



<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [UynGH](https://github.com/UynGH)**
_Saturday May 30, 2020 at 14:37:38_
_Originally opened as: project-topaz/topaz - Issue 667_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Hello.

Vyvin reported this issue on Discord.

> [...] turning in a flyer to Guilberdrier in Northern San D'Oria for the Fliers for Regine quest crashes my server [...]

I checked on the latest Canary build and compared to this retail video capture of the quest: https://www.youtube.com/watch?v=Se10PQ_nzaY and BGWiki: https://www.bg-wiki.com/bg/Flyers_for_Regine.

~~Trading a Magicmart Flyer indeed crashes topaz_game.exe~~ but I found several possible improvements/differences trying to reproduce this and comparing to the video and Wiki above:

~~When you receive the 15 Magicmart Flyers from Regine (at 1:06 in the video) there should be only one line displayed, obtaining them. On Topaz there's two:
![img_20200530_160619](https://user-images.githubusercontent.com/40763842/83330986-30275e00-a293-11ea-92ac-45d94849cf65.jpg)~~

Every NPC to which you need to trade a fish should say something when you pass near them ("NPC looks over curisouly for a moment.") at 1:36 (and throughout), on Topaz there's none.

~~There's an extra message displayed when you trade a Magicmart Flyer ("You've handed out X flyer(s)!") on Topaz, shouldn't be there at 3:17 (and throughout).
![img_20200529_024101](https://user-images.githubusercontent.com/40763842/83331026-98763f80-a293-11ea-8b4c-c83b1b115961.jpg)~~

Wasn't able to continue the quest because of said crash above but looks like Vyvin fixed it by doing this:
> [...] I edited his lua script to match Capiria's but with his variables for the FFR quest, Also noticed that Coullene's variable was missing an l in hers
this change stopped the crashing, and allowed me to finish the quest

Thank you!

Edit: mostly fixed by https://github.com/project-topaz/topaz/pull/682! Thank you, @wrenffxi.


----
<a href="https://github.com/HoshyRyu"><img src="https://avatars0.githubusercontent.com/u/66328335?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [HoshyRyu](https://github.com/HoshyRyu)**
_Wednesday Jun 03, 2020 at 02:26:33_

----

I am getting the same crash issue having done the same steps and each time crashing the topaz_game.exe. 


----
<a href="https://github.com/vyvin"><img src="https://avatars1.githubusercontent.com/u/1476809?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [vyvin](https://github.com/vyvin)**
_Wednesday Jun 03, 2020 at 04:48:25_

----

This is my Guilberdrier lua file that doesn't crash the server.

```
-----------------------------------
-- Area: Northern San d'Oria
--  NPC: Guilberdrier
-- Involved in Quests: Flyers for Regine, Exit the Gambler
-- !pos -159.082 12.000 253.794 231
-----------------------------------
local ID = require("scripts/zones/Northern_San_dOria/IDs")
require("scripts/globals/settings")
require("scripts/globals/npc_util")
require("scripts/globals/quests")
-----------------------------------

function onTrade(player, npc, trade)
    if (player:getQuestStatus(SANDORIA,tpz.quest.id.sandoria.FLYERS_FOR_REGINE) == QUEST_ACCEPTED) then
        if (trade:hasItemQty(532,1) and trade:getItemCount() == 1 and player:getCharVar("tradeGuilberdrier")) == 0 then
            player:messageSpecial(ID.text.CAPIRIA_DIALOG) -- gave this NPC a generic response to flyer. I don't see a unique one in the extract. need retail capture.
            player:addCharVar("FFR", -1);
			player:setCharVar("tradeGuilberdrier",1);
			player:messageSpecial(ID.text.FLYER_ACCEPTED)
            player:tradeComplete()
        elseif player:getCharVar("tradeGuilberdrier") == 1 then
            player:messageSpecial(ID.text.FLYER_ALREADY)
        end
    end
end

function onTrigger(player, npc)
    local exitTheGambler = player:getQuestStatus(SANDORIA, tpz.quest.id.sandoria.EXIT_THE_GAMBLER)
    local exitTheGamblerStat = player:getCharVar("exitTheGamblerStat")

    if player:getCharVar("thePickpocket") == 1 and not player:getMaskBit(player:getCharVar("thePickpocketSkipNPC"), 4) then
        player:showText(npc, ID.text.PICKPOCKET_GUILBERDRIER)
        player:setMaskBit(player:getCharVar("thePickpocketSkipNPC"), "thePickpocketSkipNPC", 4, true)
    elseif exitTheGambler < QUEST_COMPLETED and exitTheGamblerStat == 0 then
        player:startEvent(522)
    elseif exitTheGambler == QUEST_ACCEPTED and exitTheGamblerStat == 1 then
        player:startEvent(518)
    else
        player:startEvent(514)
    end
end

function onEventUpdate(player, csid, option)
end

function onEventFinish(player, csid, option)
    if csid == 522 and player:getQuestStatus(SANDORIA, tpz.quest.id.sandoria.EXIT_THE_GAMBLER) == QUEST_AVAILABLE then
        player:addQuest(SANDORIA, tpz.quest.id.sandoria.EXIT_THE_GAMBLER)
    elseif csid == 518 then
        npcUtil.completeQuest(player, SANDORIA, tpz.quest.id.sandoria.EXIT_THE_GAMBLER, {ki = tpz.ki.MAP_OF_KING_RANPERRES_TOMB, title = tpz.title.DAYBREAK_GAMBLER, xp = 2000})
    end
end
```


----
<a href="https://github.com/vyvin"><img src="https://avatars1.githubusercontent.com/u/1476809?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [vyvin](https://github.com/vyvin)**
_Wednesday Jun 03, 2020 at 04:50:51_

----

There's also some typo's in Coullene's script for the quest variable.  Mainly missing L's.  This is mine with the fixes

```
-----------------------------------
-- Area: Northern San d'Oria
--  NPC: Coullene
-- Type: Involved in Quest (Flyers for Regine)
-- !pos 146.420 0.000 127.601 231
--
-----------------------------------
local ID = require("scripts/zones/Northern_San_dOria/IDs");
require("scripts/globals/quests");
-----------------------------------

function onTrade(player,npc,trade)
    if (player:getQuestStatus(SANDORIA,tpz.quest.id.sandoria.FLYERS_FOR_REGINE) == QUEST_ACCEPTED) then
        if (trade:hasItemQty(532,1) and trade:getItemCount() == 1 and player:getCharVar("tradeCoullene") == 0) then
            player:messageSpecial(ID.text.COULLENE_DIALOG);
            player:addCharVar("FFR", -1);
            player:setCharVar("tradeCoul1ene",1);
            player:messageSpecial(ID.text.FLYER_ACCEPTED);
            player:tradeComplete();
        elseif (player:getCharVar("tradeCoullene") ==1) then
            player:messageSpecial(ID.text.FLYER_ALREADY);
        end
    end
end;

function onTrigger(player,npc)
    player:showText(npc,ID.text.COULLENE_DIALOG);
end;

function onEventUpdate(player,csid,option)
end;

function onEventFinish(player,csid,option)
end;
```


----
<a href="https://github.com/vyvin"><img src="https://avatars1.githubusercontent.com/u/1476809?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [vyvin](https://github.com/vyvin)**
_Wednesday Jun 03, 2020 at 04:51:46_

----

Note that the fixes aren't exactly retail correct, I did it to just get it working and not crashing my server.


----
<a href="https://github.com/HoshyRyu"><img src="https://avatars0.githubusercontent.com/u/66328335?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [HoshyRyu](https://github.com/HoshyRyu)**
_Thursday Jun 04, 2020 at 02:35:41_

----

Thank you so much for your help and contribution. I had originally listen to your advise and went in there and saw what you meant regarding making it like Capiria, and it worked. Thank you again.


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Saturday Jul 18, 2020 at 17:45:38_

----

Fixed by https://github.com/project-topaz/topaz/pull/789. Wren recently PRd something to clean a lot of NPCs that had the old messages before S-E rewrote the quest (and kain just opened https://github.com/project-topaz/topaz/issues/865 but not related anymore to mine).
