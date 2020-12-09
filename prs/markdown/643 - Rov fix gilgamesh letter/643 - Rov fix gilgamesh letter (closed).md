**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday May 19, 2020 at 03:46:43_
_Originally opened as: project-topaz/topaz - Issue 643_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

gilgamesh letter was not given to chars with subjob locked. Also lion ii was given for RoV quest instead of zeid ii

Thank you Hiro and @ffxijuggalo from Canaria server :cat: 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday May 26, 2020 at 04:56:55_

----

Could we change this to:
```lua
        if npcUtil.giveItem(player, 10160) then -- Cipher: Zeid II
            player:completeMission(ROV, tpz.mission.id.rov.VOLTO_OSCURO)
            player:addMission(ROV, tpz.mission.id.rov.RING_MY_BELL)
        else
            player:setCharVar("ZeidIICipher", 1)
        end
```
and then above change to:
```lua
    elseif player:getCharVar("ZeidIICipher") == 1 then
        if npcUtil.giveItem(player, 10160) then -- Cipher: Zeid II
            player:completeMission(ROV, tpz.mission.id.rov.VOLTO_OSCURO)
            player:addMission(ROV, tpz.mission.id.rov.RING_MY_BELL)
            player:setCharVar("ZeidIICipher", 0)
        end
    elseif RhapsodiesMission == tpz.mission.id.rov.VOLTO_OSCURO then
        player:startEvent(279)
```
apparently RoV doesn't make you rewatch the CS.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday May 26, 2020 at 11:57:59_

----

RoV introduced those sparkle NPCs that store the item you should have gotten - mystic retriever.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 26, 2020 at 20:09:53_

----

Mystic retrievers are used most of the time, but Gilgamesh's door is special and hands it to you directly.

Source: "Rhapsodies: ROV 1-17 ~ ROV 2-2 (Already Meeting COP Reqs)" @ 3:30


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 28, 2020 at 18:40:16_

----

resolving this per @ibm2431 's comments, no changes made.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday May 28, 2020 at 18:48:33_

----

It's still not supposed to make you watch the CS again.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday May 26, 2020 at 04:56:55_

----

Could we change this to:
```lua
        if npcUtil.giveItem(player, 10160) then -- Cipher: Zeid II
            player:completeMission(ROV, tpz.mission.id.rov.VOLTO_OSCURO)
            player:addMission(ROV, tpz.mission.id.rov.RING_MY_BELL)
        else
            player:setCharVar("ZeidIICipher", 1)
        end
```
and then above change to:
```lua
    elseif player:getCharVar("ZeidIICipher") == 1 then
        if npcUtil.giveItem(player, 10160) then -- Cipher: Zeid II
            player:completeMission(ROV, tpz.mission.id.rov.VOLTO_OSCURO)
            player:addMission(ROV, tpz.mission.id.rov.RING_MY_BELL)
            player:setCharVar("ZeidIICipher", 0)
        end
    elseif RhapsodiesMission == tpz.mission.id.rov.VOLTO_OSCURO then
        player:startEvent(279)
```
apparently RoV doesn't make you rewatch the CS.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday May 26, 2020 at 11:57:59_

----

RoV introduced those sparkle NPCs that store the item you should have gotten - mystic retriever.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 26, 2020 at 20:09:53_

----

Mystic retrievers are used most of the time, but Gilgamesh's door is special and hands it to you directly.

Source: "Rhapsodies: ROV 1-17 ~ ROV 2-2 (Already Meeting COP Reqs)" @ 3:30


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 28, 2020 at 18:40:16_

----

resolving this per @ibm2431 's comments, no changes made.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday May 28, 2020 at 18:48:33_

----

It's still not supposed to make you watch the CS again.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday May 19, 2020 at 03:47:51_

----

ugh dunno why the SQL file got include it >.< dunno how to remove it from my PR


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday May 19, 2020 at 04:38:58_

----

yay fixed it =)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday May 26, 2020 at 04:24:12_

----

```lua
        if not player:hasJob(0) then -- Is Subjob Unlocked
            npcUtil.giveKeyItem(player, tpz.ki.GILGAMESHS_INTRODUCTORY_LETTER)
        else
```
Does that not give the key item to players without subjob unlocked?

Edit: This should be ` if player:hasJob(0) == 0 then -- Is Subjob Unlocked`
