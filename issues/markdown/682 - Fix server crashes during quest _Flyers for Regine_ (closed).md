**Labels:**

reviewed



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Jun 04, 2020 at 01:29:06_
_Originally opened as: project-topaz/topaz - Issue 682_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Related to issue #667 

* When receiving multiple stacks of an item -- such as the 15 flyers during this quest -- the player will now only receive one "obtained" mesage for that item.

* Removes the extra message about "You've handed out (x) flyers" from the flyer NPCs, because this message doesn't appear on current retail.

* Fixed some flyer NPCs that were crashing the server when accepting flyers.  Quest can now be completed without issue.

* Fixed some default dialog on a couple flyer NPCs.

*Note: This PR does not add the feature where the player will receive a message when standing close to the correct flyer NPCs.  Therefore, this PR does not entirely address #667*


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 04, 2020 at 01:40:55_

----

```lua
            player:setCharVar("tradeAnswald",0);
            player:setCharVar("tradePrietta",0);
            player:setCharVar("tradeMiene",0);
            player:setCharVar("tradePortaure",0);
            player:setCharVar("tradeAuvare",0);
            player:setCharVar("tradeGuilberdrier",0);
            player:setCharVar("tradeVilion",0);
            player:setCharVar("tradeCapiria",0);
            player:setCharVar("tradeBoncort",0);
            player:setCharVar("tradeCoullene",0);
            player:setCharVar("tradeLeuveret",0);
            player:setCharVar("tradeBlendare",0);
            player:setCharVar("tradeMaugie",0);
            player:setCharVar("tradeAdaunel",0);
            player:setCharVar("tradeRosel",0);
            player:setCharVar("FFR",0);
```
Good lord that is a lot of vars Regine has to zero out. How do you feel about using a mask like stamp hunt and wildcat quests do?

Could also use a single offset to not have to have so many sequential textIDs defined.

> Removes the extra message about "You've handed out (x) flyers" from the flyer NPCs, because this message doesn't appear on current retail.

Trivia: retail removed that when they added the player in range "so and so is interested" thing. I remember the old way of having to just trade macro every NPC till you found them all (or look it up on wiki and not take any breaks mid quest) _cringe_


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Jun 04, 2020 at 01:45:40_

----

This PR's mainly just to fix the crash.  Can definitely update original issue with additional Nice to Haves for this quest.

I'd be happy to tackle neatening up the code, plus adding the "approach" messages, in a later PR.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 04, 2020 at 02:44:49_

----

Thats a funny way to spell “not it” :D

I kid I kid. Thanks for all you do Wren!
