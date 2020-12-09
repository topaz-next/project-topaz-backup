**Labels:**

approved

reviewed



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Sep 09, 2020 at 07:42:47_
_Originally opened as: project-topaz/topaz - Issue 1084_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Would love a tester to go through genkai completely.

this includes both quests and olde rarab tail GET


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 09, 2020 at 09:03:26_

----

This file is named: `howling_fist.lua .lua ` 👀 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 09, 2020 at 09:06:10_

----

Please format these header areas like the BCNM files:
```lua
...
-- Horlais Peak Level Break
-----------------------------------
require("scripts/globals/battlefield")
require("scripts/globals/npc_util")
require("scripts/globals/quests")
require("scripts/globals/titles")
-----------------------------------

function onBattlefieldTick(battlefield, tick)
...
```

etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 09, 2020 at 09:06:56_

----

Get rid of these extra spaces


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 09, 2020 at 09:07:58_

----

Would probably want to hold off until this is confirmed, but if there aren't any boned being warped then this is _probably fine_.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Sep 09, 2020 at 20:29:29_

----

fixed. sorry i was copy and pasting left and right cuz of the rebase errors that had to create a new branch lol.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Sep 09, 2020 at 20:34:22_

----

Done, sorry for the extra spaces >.<


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Sep 09, 2020 at 20:35:17_

----

luaception lol. fixed =)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Sep 10, 2020 at 05:33:46_

----

animation is just the shiny particles that are being assigned. I think it should be 0 as nothing shows on atori when being used. See https://youtu.be/usNZOGDq5c0?t=2682 but I can't confirm as I been looking at the packet that IBM captured but dunno which packet to look for this animation :cry: 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 09, 2020 at 09:03:26_

----

This file is named: `howling_fist.lua .lua ` 👀 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 09, 2020 at 09:06:10_

----

Please format these header areas like the BCNM files:
```lua
...
-- Horlais Peak Level Break
-----------------------------------
require("scripts/globals/battlefield")
require("scripts/globals/npc_util")
require("scripts/globals/quests")
require("scripts/globals/titles")
-----------------------------------

function onBattlefieldTick(battlefield, tick)
...
```

etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 09, 2020 at 09:06:56_

----

Get rid of these extra spaces


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 09, 2020 at 09:07:58_

----

Would probably want to hold off until this is confirmed, but if there aren't any boned being warped then this is _probably fine_.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Sep 09, 2020 at 20:29:29_

----

fixed. sorry i was copy and pasting left and right cuz of the rebase errors that had to create a new branch lol.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Sep 09, 2020 at 20:34:22_

----

Done, sorry for the extra spaces >.<


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Sep 09, 2020 at 20:35:17_

----

luaception lol. fixed =)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Sep 10, 2020 at 05:33:46_

----

animation is just the shiny particles that are being assigned. I think it should be 0 as nothing shows on atori when being used. See https://youtu.be/usNZOGDq5c0?t=2682 but I can't confirm as I been looking at the packet that IBM captured but dunno which packet to look for this animation :cry: 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 09, 2020 at 09:11:59_

----

IBM gave me a really good explanation of different packet and move types (which I still haven't sat down to read correctly), I wonder if this can kick off the discussion of combining weaponskills.sql and mob_skills.sql

@TeoTwawki thoughts?


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Wednesday Sep 09, 2020 at 18:16:59_

----

My comments with some tests I have made on this branch:
- The Beyond Infinity quest is never flagged active. This prevent getting an Olde Rarab Tail from Degenhard
   When you trade your Seasoning Stone to the moogle, if in the cuscene you select that "You are not ready",
  you should not be teleported to BCNM area but you should have the temp KI and the quest Beyond Infinity should me marked active.
- When you enter the BCNM, you do not lose the temp KI on entry, and as such you are able to retry without checking the moogle again (so I could not test if trading one merit point or 5 High kindred crests work to get back KI)
- Atori does not aggro (should be sight aggro i think)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Sep 09, 2020 at 22:27:24_

----

> IBM gave me a really good explanation of different packet and move types (which I still haven't sat down to read correctly), I wonder if this can kick off the discussion of combining weaponskills.sql and mob_skills.sql
> 
> @TeoTwawki thoughts?

@zach2good  we've had a few talks about this on past issues pr and in discord - merging of a lot of commonality between the 2 needs to eventually happen. the parts that need to be specific to each could still go in same global that'd be fine. But we need to rework things to use an attacker/defender paradigm instead of player/mob or mob/player, migrate some parts out of _character_ utils/entity into _battle_ utils/entity, etc. 

Right now ws global assumes user is always a player, but these ws scripts rightly should use actual ws functionality instead of faking it and guessing numbers to simulate the right dmg. Right now that's not possible, we need to sit down and make it possible. Its gonna be its own project, 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Sep 10, 2020 at 00:06:31_

----

> Atori does not aggro (should be sight aggro i think)

@jarmengaud on retail he stands there till you attack him. Maat does the same thing allowing thf to start with an Sneak Attack even.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Sep 10, 2020 at 00:36:17_

----

> > Atori does not aggro (should be sight aggro i think)
> 
> @jarmengaud on retail he stands there till you attack him. Maat does the same thing allowing thf to start with an Sneak Attack even.

Check https://youtu.be/2ShT8fuvPV4?t=98 No provoke or any abilities were used and he starts attacking tank.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Sep 10, 2020 at 03:48:22_

----

@TeoTwawki 

https://youtu.be/usNZOGDq5c0?t=1544

^ video by IBM :D


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 10, 2020 at 04:53:33_

----

If removing the KI is an issue, it doesn't look like theres any situation where you can enter the BCNM fights and not have the KI removed (or the var set), so you can do it without the check (Like in Limbus entry):
https://github.com/project-topaz/topaz/blob/831b8fecc597405fc5a4e666f1dd684b4aac8526/scripts/zones/Apollyon/bcnms/nw_apollyon.lua#L28-L32

There is no need to fear delKeyItem, keyitems are pretty much just flags assigned to the player that you switch on and off:
```cpp
    void delKeyItem(CCharEntity* PChar, uint16 KeyItemID)
    {
        auto table = KeyItemID / 512;
        PChar->keys.tables[table].keyList[KeyItemID % 512] = false;
    }
```


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Sep 10, 2020 at 05:30:53_

----

> If removing the KI is an issue, it doesn't look like theres any situation where you can enter the BCNM fights and not have the KI removed (or the var set), so you can do it without the check (Like in Limbus entry):
> https://github.com/project-topaz/topaz/blob/831b8fecc597405fc5a4e666f1dd684b4aac8526/scripts/zones/Apollyon/bcnms/nw_apollyon.lua#L28-L32
> 
> There is no need to fear delKeyItem, keyitems are pretty much just flags assigned to the player that you switch on and off:
> 
> ```c++
>     void delKeyItem(CCharEntity* PChar, uint16 KeyItemID)
>     {
>         auto table = KeyItemID / 512;
>         PChar->keys.tables[table].keyList[KeyItemID % 512] = false;
>     }
> ```

I haven't had that issue of the KI not being removed. I have asked @UynGH  to take a look as I havent been able to reproduce. They Var is needed only for people that are currently on the quest otherwise it will leave an orphaned variable that will be never get erased, and we know we don't want that, isn't that right @TeoTwawki ? :smile: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Sep 10, 2020 at 05:36:23_

----

@jarmengaud changes done, atori should now aggro, i havent had issues with the keyitem not being removed, are you sure you are add SOUL_GEM_CLASP and not just SOUL_GEM? I asked @UynGH  to test this BCNM.

About the 
***The Beyond Infinity quest is never flagged active. This prevent getting an Olde Rarab Tail from Degenhard
When you trade your Seasoning Stone to the moogle, if in the cuscene you select that "You are not ready",
you should not be teleported to BCNM area but you should have the temp KI and the quest Beyond Infinity should me marked active.*** I'll try to fix it tomorrow, csid 10045 has WAAAAY lot of options it's been a headache lol


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Thursday Sep 10, 2020 at 15:22:58_

----

Had the same issues as Tokenr.

**Prelude to Puissance**

https://youtu.be/usNZOGDq5c0?t=256 (ibm's video), even if he trade unwanted items with the Seasoning Stone, the Moogle will accept said Stone and complete the quest. On canary (with your PR in) you can only trade Stone only if you want him to accept it.

https://youtu.be/usNZOGDq5c0?t=350: when you have the cutscene with Atori-Tutori (right after trading the Seasoning Stone) and you choose to make him wait, once you talk back to the Moogle (without zoning/flagging something else), he should ask "Are you ready to meet you mak--er, your final challenge, kupo?" (timestamped link). Instead, it replays the cutscene like you just traded the Stone (it should if you flag/do something else, timestamp: https://youtu.be/usNZOGDq5c0?t=597).

**Beyond Infinity (limit break 10)**

No "Obtained key item: Soul gem clasp." message (https://youtu.be/usNZOGDq5c0?t=644) but still listed in temporary key items. Beyond Infinity was not flagged like it should so I was unable to get an Olde Rarab Tail (yet still able to get in the BCNM). Since it wasn't flagged, not able to retry the retail way (https://youtu.be/usNZOGDq5c0?t=1369), instead I just got the same cutscene you get when you trade the Seasoning Stone for Prelude to Puissance. Soul gem clasp not deleted upon the BCNM entry, making it possible to do it endlessly even after defeating Atori-Tutori (Season Stone cutscene in a loop when you talk back to the Moogle).

Also, by comparing with the above video, the cutscene upon defeating him should start right away when his HPs reach 0 (currently it starts when his name disappear).
I got a Kindred Seal from him, I guess I shouldn't. He drops nothing.
I didn't receive any scroll of Instant Warp when I got warped to the BCNM exit (https://youtu.be/usNZOGDq5c0?t=3085).
Missing the "If all party members' HP are still zero after 3 minutes, the party will be removed from the battlefield." message if you fail.

A big thank you to **ibm**.

N.B. Atori-Tutori does aggro now, with your last changes.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Sep 10, 2020 at 23:53:54_

----

> 
> 
> @TeoTwawki
> 
> https://youtu.be/usNZOGDq5c0?t=1544
> 
> ^ video by IBM :D

da fuq. when I want after him on my thf I swear to god he just stood there till I engaged...I need to go rematch him now. Something something mandela effect #BlameTheLHC


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Sep 11, 2020 at 05:48:53_

----

@UynGH  and @jarmengaud :

I have made changes to this to make it as much retail like which has always been my goal =)

- Prelude to Puissance
* Seasoning stone should now be accepted along other random nonsense lol

* extra CS have been added

Beyond Infinity (limit break 10)

* Soul Gem Clasp dialog will not show up as after adding it and teleporting they are done at the same time so it doesnt allow the client a breather (is the same issue with warp 2), @TeoTwawki  mentioned a fix but i'll leave it to someone to fix it as its just a cosmetic issue that is experienced by other teleports too.

* About the CS, thats an issue with all BCNMs ^^;; AFAIK. (Developer please tell me otherwise)

* about the beastman seal drop.... its dropID is set to "0" >.< unsure what could be causing this. >.<

Can you please retest and see all those CS and keyitems work? I tested it myself but would love a second set of eyes <3


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Friday Sep 11, 2020 at 16:41:22_

----

As i said in discord, there is still a missing code line to set the BEYOND_INFINITY quest to ACCEPTED.
Which prevents getting the rarab tail and explain why you dont lose the KI on entry.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Sep 12, 2020 at 03:16:53_

----

Made more changes:

Prelude to Puissance
fixed CS as quest is completed on trade.

Beyond Infinity (limit break 10)

It now is able to be completed if not choosing the selection to not teleport and wait instead.

* issue with Atori not sheating his knucle weapons when attacking and removing it when losing aggro is not implemented. Creating an issue for it.

@zach2good  this is ready for review now, leaving the issue of it dropping seal (sometimes) and the knucle weapon sheating/unsheating to be fixed afterwards as it doesn't break completion of quest. =)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 12, 2020 at 09:34:15_

----

I'm not going to be able review this for a few days, but I'll merge your SQL changes straight into `release` so your changes stop getting trampled 🙏 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Sep 12, 2020 at 14:42:52_

----

don't worry @zach2good . its already conflicting =/ I'll have to rebase and fix it.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Sep 12, 2020 at 15:41:51_

----

yeah tried rebasing, i dunno what went wrong, i'll leave this alone ^^;;


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Saturday Sep 12, 2020 at 16:48:20_

----

Quoting my precedent message to compare what's still going on and what's fixed with the latest commit.

> **Prelude to Puissance**
> 
> https://youtu.be/usNZOGDq5c0?t=256 (ibm's video), even if he trade unwanted items with the Seasoning Stone, the Moogle will accept said Stone and complete the quest. On canary (with your PR in) you can only trade Stone only if you want him to accept it. **Still present**.
> 
> ~~https://youtu.be/usNZOGDq5c0?t=350: when you have the cutscene with Atori-Tutori (right after trading the Seasoning Stone) and you choose to make him wait, once you talk back to the Moogle (without zoning/flagging something else), he should ask "Are you ready to meet you mak--er, your final challenge, kupo?" (timestamped link). Instead, it replays the cutscene like you just traded the Stone (it should if you flag/do something else, timestamp: https://youtu.be/usNZOGDq5c0?t=597)~~. **Fixed**.
> 
> **Beyond Infinity (limit break 10)**
> 
> No "Obtained key item: Soul gem clasp." message (https://youtu.be/usNZOGDq5c0?t=644) but still listed in temporary key items. **Still present**.
~~Beyond Infinity was not flagged like it should so I was unable to get an Olde Rarab Tail (yet still able to get in the BCNM). Since it wasn't flagged, not able to retry the retail way (https://youtu.be/usNZOGDq5c0?t=1369), instead I just got the same cutscene you get when you trade the Seasoning Stone for Prelude to Puissance. Soul gem clasp not deleted upon the BCNM entry, making it possible to do it endlessly even after defeating Atori-Tutori (Season Stone cutscene in a loop when you talk back to the Moogle).~~ **Fixed**.
> 
> Also, by comparing with the above video, the cutscene upon defeating him should start right away when his HPs reach 0 (currently it starts when his name disappear). **Still present**.
> I got a Kindred Seal from him, I guess I shouldn't. He drops nothing. **Still present**.
> ~~I didn't receive any scroll of Instant Warp when I got warped to the BCNM exit (https://youtu.be/usNZOGDq5c0?t=3085).~~ **Fixed**.
> Missing the "If all party members' HP are still zero after 3 minutes, the party will be removed from the battlefield." message if you fail. **Still present**.
> 
> A big thank you to **ibm**.
> 
> N.B. Atori-Tutori does aggro now, with your last changes.

Be aware that all the videos are from retail (thanks to ibm and his captures).

**Olde Rarab Tail mini-quest - Degenhard**

Dialog when checking him a second time after he asked for the materials should be the same as the one he gives you after you traded your stuff once (https://youtu.be/usNZOGDq5c0?t=788), currently he's repeating the first one only.
Repeating the quest quest - **OKAY**.
Same "multi trade" issue (https://youtu.be/usNZOGDq5c0?t=797) as in the Prelude to Puissance quest, quoted from my message above.
Using an Olde Rarab Tail on other mobs should do nothing: https://youtu.be/usNZOGDq5c0?t=1071. Currently I can use it on random mobs (it does nothing but still).

**BCNM**

There's two different versions of the BCNM if you're comparing with YouTube videos.
The old one has different messages, an Hundred Fists animation and when using an Olde Rarab Tail, Atori-Tutori used to run around the arena.
*THIS IS NOT THE TARGETED VERSION*.
https://forum.square-enix.com/ffxi/threads/22099-March-27-2012-(JST)-Version-Update
> [dev1095] Limit Break Quest "Beyond Infinity" Adjustments
> The effect of the Olde Rarab Tail item has been altered.
> Effect duration has been extended.
> Your opponent will be inflicted with Terror during this time.
> Your opponent will not unleash weapon skills immediately after the effect wears off. 
	
I'm losing the Soul gem clasp key item upon entry but no message stating it/no record message/no party limitation message: https://youtu.be/usNZOGDq5c0?t=1510), should be seen if you retry too. instead I'm getting this:
![0](https://user-images.githubusercontent.com/40763842/93000451-e48a7e80-f528-11ea-85a9-3c6cac91b119.jpg)
Which is not present on retail.
Atori-Tutori use H2H animation when hitting, wearing a red glowing H2H weapon. There's no additional effect when he's hitting, missing the additional effect on hit he has on retail, which is *really* potent: https://youtu.be/0AhtvL9nRQw?t=118.
Atori-Tutori used no WSs at all. On retail he use them pretty often, even after a few hits and he does skillchains by using them back to back: https://youtu.be/Q7ncfLXEPNE?t=396. This make it impossible to see if the WSs messages are working.
No message saying he used Hundred Fists but I got one when it wore off, while it should be the other way around: https://youtu.be/usNZOGDq5c0?t=2783. Not having any animation is good tho!

Duration of the Olde Rarab Tail seems to be 1 minute and 33 seconds everytime on retail - **OKAY**:

https://www.youtube.com/watch?v=usNZOGDq5c0:
44:46 > 46:19.
46:30 > 48:03.
https://www.youtube.com/watch?v=0AhtvL9nRQw:
2:07 > 3.40.

Possibility to exit the BCNM and it counts as failing - **OKAY**.
No message when he defeats you: https://youtu.be/usNZOGDq5c0?t=1254. Since there's no 3 minutes delay you're directly teleported out of the BCNM.

**BCNM retry**

Everything went good when trading 5 High Kindred's Crest. - **OKAY**.
I didn't lose the merit point needed when I tried to pay with it (https://youtu.be/usNZOGDq5c0?t=1636 ibm went from 12 to 11) but I was still able to select a location to teleport to.
In both cases I got the "Obtained key item: Soul gem clasp." message correctly when refusing to teleport directly (choosing "Nowhere yet." https://youtu.be/usNZOGDq5c0?t=1440) so you might take a look here to get the message where's it's missing above.
Having 0 merit point in stock will give the High Kindred's Crest message only: https://youtu.be/usNZOGDq5c0?t=2399 - **OKAY**.

Ending CS with the Nomad Moogle after completing the BCNM - **OKAY**.

Bonus: Typos for Horlais Peak and Waughroon Shrine!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 15:05:51_

----

Looks very good and clean.

From Nyu's post it looks like there's still a couple of things left to do. Don't worry about BCNM timers, messaging, despawning etc. Those are all issues with the BCNM system. Try to get all the trading and quest stuff perfect, and maybe the aesthetic things if you can, but those aren't a requirement.
