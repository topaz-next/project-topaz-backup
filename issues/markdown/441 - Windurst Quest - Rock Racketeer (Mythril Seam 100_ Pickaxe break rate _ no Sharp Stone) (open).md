**Labels:**

bug



<a href="https://github.com/Solarsurge"><img src="https://avatars0.githubusercontent.com/u/62639643?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Solarsurge](https://github.com/Solarsurge)**
_Wednesday Mar 25, 2020 at 07:38:11_
_Originally opened as: project-topaz/topaz - Issue 441_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [X] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [X] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Broke 99 consecutive Pickaxes on the Mythril Seam and only able to dig up Mine Gravel.
![img_20200325_025908](https://user-images.githubusercontent.com/62639643/77512666-e2811600-6e49-11ea-849a-2738b54150d9.jpg)
![img_20200325_025912](https://user-images.githubusercontent.com/62639643/77512677-e745ca00-6e49-11ea-9327-00b08ed13fb3.jpg)





----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 25, 2020 at 11:40:07_

----

> only able to dig up Mine Gravel.

That part is normal. the break rate is not.


----
<a href="https://github.com/Solarsurge"><img src="https://avatars0.githubusercontent.com/u/62639643?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Solarsurge](https://github.com/Solarsurge)**
_Wednesday Mar 25, 2020 at 12:08:39_

----

I know it's RNG and mine gravel is definitely more common, so if it's just terrible luck so be it, but after going 0/99 swings on the Sharp Stone I figured I'd mention it just to confirm it's actually in the table for the correct seam.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 25, 2020 at 13:20:33_

----

```lua
require("scripts/globals/npc_util")
-----------------------------------

function onTrade(player, npc, trade)
    if npcUtil.tradeHas(trade, 605) then -- pickaxe
        if player:getFreeSlotsCount() > 0 then
            if math.random() < 0.47 then
                if player:getCharVar("rockracketeer_sold") == 5 then
                    player:startEvent(51, 12, 598) -- Sharp Stone
                else
                    player:startEvent(43, 12, 0, 597) -- Mine Gravel
                end
            else
                player:startEvent(47, 8, 598) -- pickaxe breaks
            end
        else
            player:startEvent(53) -- cannot carry any more
        end
    else
        player:startEvent(32) -- need a pickaxe
    end
end

function onTrigger(player, npc)
    player:startEvent(30, 12, 0, 597)
end

function onEventUpdate(player, csid, option)
end

function onEventFinish(player, csid, option)
    if csid == 51 and npcUtil.giveItem(player, 598) then
        player:confirmTrade()
    elseif csid == 43 and npcUtil.giveItem(player, 597) then
        player:confirmTrade()
    elseif csid == 47 then
        player:confirmTrade()
    end
end
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 25, 2020 at 13:23:18_

----

so, if your rockracketeer_sold var is exactly 5, you will get a sharp stone. otherwise you will always get mine gravel.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 25, 2020 at 13:25:33_

----

IMO, the script needs to take the mining rate settings into account for break rate and success rate to meet expectations


----
<a href="https://github.com/Solarsurge"><img src="https://avatars0.githubusercontent.com/u/62639643?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Solarsurge](https://github.com/Solarsurge)**
_Wednesday Mar 25, 2020 at 16:09:38_

----

I'm not sure what the rockracketeer_sold var possibilities are. I just know you sell the original sharp grey stone (key item) that Nanaa Mihgo gives you to the Goldsmithing guild in Bastok to enable the next part of the quest, where Varun wonders where his stone went, and that finally enables you to mine the Sharp Stone. I've done all that. So, if I'm reading that code correctly, doesn't that mean I should just get the Sharp Stone? Because I didn't.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 25, 2020 at 16:56:08_

----

https://github.com/project-topaz/topaz/search?q=rockracketeer_sold&unscoped_q=rockracketeer_sold

~~I'm not seeing where it is set to 5 actually..~~
[nvm found it](https://github.com/project-topaz/topaz/blob/c52431e2c48516954aa2f5ebbb331238f43cc3d8/scripts/zones/Windurst_Woods/npcs/Varun.lua#L38)
```lua
    if rockRacketeer == QUEST_ACCEPTED and rockRacketeerCS == 3 then
        player:startEvent(100) -- talk about lost stone
    elseif rockRacketeer == QUEST_ACCEPTED and rockRacketeerCS == 4 then
        player:startEvent(101, 0, 598) -- send player to Palborough Mines
    else
        player:startEvent(432)
    end
```
```lua
function onEventFinish(player,csid,option)
    if csid == 100 then
        player:setCharVar("rockracketeer_sold", 4)
    elseif csid == 101 then
        player:setCharVar("rockracketeer_sold", 5)
    elseif csid == 102 and npcUtil.completeQuest(player, WINDURST, tpz.quest.id.windurst.ROCK_RACKETEER, {gil=2100, var="rockracketeer_sold"}) then
        player:confirmTrade()
    end
end
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 25, 2020 at 17:02:49_

----

so you I think need to check what your var is, cos it looks like maybe you missed a step or fell victim to the bug where something in the database doesn't get updated.


----
<a href="https://github.com/Solarsurge"><img src="https://avatars0.githubusercontent.com/u/62639643?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Solarsurge](https://github.com/Solarsurge)**
_Thursday Mar 26, 2020 at 00:20:40_

----

Option 2. It didn't update.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:19:16_

----

@Solarsurge To confirm: Were you able to progress with the quest by trying to speak with Varun again?


----
<a href="https://github.com/Solarsurge"><img src="https://avatars0.githubusercontent.com/u/62639643?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Solarsurge](https://github.com/Solarsurge)**
_Thursday Mar 26, 2020 at 04:51:33_

----

Varun has multiple dialogues depending on where you are in the quest. After speaking with Nanaa Mihgo, you are only supposed to need to talk to Varun once, but it seems you may need to talk to him twice. I just talked to him twice back to back and he gave me two different messages. First about the Sharp Stone, then his original non-quest message. After the repeat original non-quest message, I was able to mine the Sharp Stone.

![Varun1](https://user-images.githubusercontent.com/62639643/77611125-ec168680-6efa-11ea-9ea2-590421c1b127.png)
![Varun2](https://user-images.githubusercontent.com/62639643/77611132-f042a400-6efa-11ea-8320-b378f02434f0.png)
![SharpStone](https://user-images.githubusercontent.com/62639643/77611459-c342c100-6efb-11ea-8a77-a041b29ac988.png)




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Mar 26, 2020 at 16:00:35_

----

possibly optional or reminder message mistakenly set to required via variable updates.
