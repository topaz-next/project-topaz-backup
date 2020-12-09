**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:18_
_Originally opened as: project-topaz/topaz - Issue 230_

----

<a href="https://github.com/rheinecatsin"><img src="https://avatars3.githubusercontent.com/u/40339620?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [rheinecatsin](https://github.com/rheinecatsin)**
_Saturday Jul 07, 2018 at 22:02 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5069_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 


**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Demiurge server.

Fish wouldn't spawn by fishing. 

GM had it spawn via console command. (even though that issue was supposedly resolved last year)

Killed it, dropped loot.

Traded loot to Albeche. He oriented me to fisherman in Selbina.

Zaldon  won't accept loot. Talked with him or others before. Tried to trade on same job as I killed NM or as PLD. Nothing happens if I try to trade him the Odontotyrannus.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:20_

----

<a href="https://github.com/whasf"><img src="https://avatars3.githubusercontent.com/u/6373706?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [whasf](https://github.com/whasf)**
_Saturday Jul 07, 2018 at 22:03 GMT_

----

Should open this on demiurge's GitHub, this is for darkstar itself



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:21_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 07, 2018 at 22:05 GMT_

----

I asked them to open here because its not server specific



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:22_

----

<a href="https://github.com/whasf"><img src="https://avatars3.githubusercontent.com/u/6373706?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [whasf](https://github.com/whasf)**
_Saturday Jul 07, 2018 at 22:06 GMT_

----

oh, well then! :)



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:23_

----

<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Jul 07, 2018 at 22:25 GMT_

----

oh that happened to me before, that happens if you have both the giant shellbug and the Odontotyrannus in your inventory on that character. I would say first, send the Odontotyrannus to another character, then turn in the shellbug, then retrieve the Odontotyrannus again from moogle delivery bog, then try trading again. it should work that time



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:25_

----

<a href="https://github.com/rheinecatsin"><img src="https://avatars3.githubusercontent.com/u/40339620?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [rheinecatsin](https://github.com/rheinecatsin)**
_Sunday Jul 08, 2018 at 02:51 GMT_

----

worked, thanks.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:26_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 10, 2018 at 01:58 GMT_

----

```lua
function onTrade(player,npc,trade)
    -- "Flyers for Regine" conditional script
    local FlyerForRegine = player:getQuestStatus(SANDORIA,FLYERS_FOR_REGINE);

    if (player:getQuestStatus(SANDORIA, FATHER_AND_SON) == QUEST_COMPLETED and player:getVar("returnedAilbecheRod") ~= 1) then
        if (trade:hasItemQty(17391,1) == true and trade:getItemCount() == 1) then
            player:startEvent(61); -- Finish Quest "Father and Son" (part2) (trading fishing rod)
        end
    end

    if (player:getVar("aBoysDreamCS") >= 3) then
        if (trade:hasItemQty(17001,1) == true and trade:getItemCount() == 1 and player:hasItem(4562) == false) then
            player:startEvent(15); -- During Quest "A Boy's Dream" (trading bug) madame ?
        elseif (trade:hasItemQty(4562,1) == true and trade:getItemCount() == 1) then
            player:startEvent(47); -- During Quest "A Boy's Dream" (trading odontotyrannus)
        end
    end

    if (FlyerForRegine == 1) then
        local count = trade:getItemCount();
        local MagicFlyer = trade:hasItemQty(532,1);
        if (MagicFlyer == true and count == 1) then
            player:messageSpecial(FLYER_REFUSED);
        end
    end
end;
```
[^ if someone wants to try and rework this, there it is.](github/DarkstarProject/darkstar/blob/b7482aef0fcd8dbbfd5d3025962254aae04cff5b/scripts/zones/Northern_San_dOria/npcs/Ailbeche.luaDarkstar Issue L29)

I especially dislike how this continues to execute code to look at more conditionals after a trade is triggering one (and you obviously can't have 2 different trades at once..) and then relies on hasItem to tell which step you are on to boot.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:27_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 18, 2018 at 22:26 GMT_

----

More fun:
Exoroche checks for 7 or greater to set 8. Ailbeche checks for 6 or greater to set 7. You can potentially get confusion from overwritten variables here..



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:29_

----

<a href="https://github.com/hilts-vaughan"><img src="https://avatars0.githubusercontent.com/u/1079207?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [hilts-vaughan](https://github.com/hilts-vaughan)**
_Saturday Oct 06, 2018 at 16:07 GMT_

----

I am working on this now -- does anyone know if the some of these steps are truly optional? The way this is coded it looks like you would have to trade all the items eventually but the wiki makes it seem like some of the steps are optional. 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:30_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 06, 2018 at 16:10 GMT_

----

> I am working on this now -- does anyone know if the some of these steps are truly optional? The way this is coded it looks like you would have to trade all the items eventually but the wiki makes it seem like some of the steps are optional.

I don't. And the 2 main wikis we have don't seem to agree with each other. prolly best to check https://discord.gg/sX9JgDT and see if someone has or can check it on retail

