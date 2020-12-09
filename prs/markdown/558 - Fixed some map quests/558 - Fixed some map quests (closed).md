**Labels:**

reviewed



<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Lynnea1320](https://github.com/Lynnea1320)**
_Friday May 01, 2020 at 01:36:01_
_Originally opened as: project-topaz/topaz - Issue 558_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Some weren't giving proper rewards or key item notifications. Will push more as we find them.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 03:08:05_

----

npcUtil isn't displaying the message because [the table key it expects inside the rewards table is `keyItem` instead of `ki`](https://github.com/project-topaz/topaz/blob/release/scripts/globals/npc_util.lua#L348-L350)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 06:59:19_

----

@ibm2431 https://github.com/project-topaz/topaz/blob/release/scripts/globals/keyitems.lua#L3011

`tpz.ki` is equivalent to `tpz.keyItem`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 07:03:22_

----

@Xephera looks like npcUtil.completeQuests() already has exp rate baked in:
https://github.com/project-topaz/topaz/blob/8985d2af68876367592222836db1f8e5b15c8175/scripts/globals/npc_util.lua#L372


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 07:38:52_

----

The _enums_ are equivalent, but the table that npcUtil.completeQuest takes is not~
```lua
    if params["keyItem"] ~= nil then
        npcUtil.giveKeyItem(player, params["keyItem"])
    end
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 07:50:34_

----

Ah, I misunderstood table, thinking ki ***is***  a table (because our "enums" _are_  tables) and totally missed that the argument input here is its _own_  table.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 07:53:45_

----

Yeah, it's confusing. Wondering if npcUtil functions should be tweaked to accept both "ki" and "keyItem" as field names.


----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Sunday May 03, 2020 at 16:01:14_

----

I fixed the exp_rate thing but it doesn't give a key item notification regardless for whatever reason so I'm leaving that part in until we know why.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 21:09:02_

----

`npcUtil.completeQuest(player, SANDORIA, tpz.quest.id.sandoria.EXIT_THE_GAMBLER, {keyItem = tpz.ki.MAP_OF_KING_RANPERRES_TOMB, title = tpz.title.DAYBREAK_GAMBLER, xp = 2000 * EXP_RATE})` didn't work?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday May 08, 2020 at 20:44:40_

----

Just gonna second that
```
player:messageSpecial(ID.text.KEYITEM_OBTAINED, tpz.ki.MAP_OF_KING_RANPERRES_TOMB) -- Map of King Ranperre's Tomb
```
shouldn't be needed if you change
```
npcUtil.completeQuest(player, SANDORIA, tpz.quest.id.sandoria.EXIT_THE_GAMBLER, {ki = tpz.ki.MAP_OF_KING_RANPERRES_TOMB, title = tpz.title.DAYBREAK_GAMBLER, xp = 2000})
```
to
```
npcUtil.completeQuest(player, SANDORIA, tpz.quest.id.sandoria.EXIT_THE_GAMBLER, {keyItem = tpz.ki.MAP_OF_KING_RANPERRES_TOMB, title = tpz.title.DAYBREAK_GAMBLER, xp = 2000})
```
notice the change from `ki = tpz.ki.MAP_OF_KING_RANPERRES_TOMB` to `keyItem = tpz.ki.MAP_OF_KING_RANPERRES_TOMB`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 03:08:05_

----

npcUtil isn't displaying the message because [the table key it expects inside the rewards table is `keyItem` instead of `ki`](https://github.com/project-topaz/topaz/blob/release/scripts/globals/npc_util.lua#L348-L350)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 06:59:19_

----

@ibm2431 https://github.com/project-topaz/topaz/blob/release/scripts/globals/keyitems.lua#L3011

`tpz.ki` is equivalent to `tpz.keyItem`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 07:03:22_

----

@Xephera looks like npcUtil.completeQuests() already has exp rate baked in:
https://github.com/project-topaz/topaz/blob/8985d2af68876367592222836db1f8e5b15c8175/scripts/globals/npc_util.lua#L372


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 07:38:52_

----

The _enums_ are equivalent, but the table that npcUtil.completeQuest takes is not~
```lua
    if params["keyItem"] ~= nil then
        npcUtil.giveKeyItem(player, params["keyItem"])
    end
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 07:50:34_

----

Ah, I misunderstood table, thinking ki ***is***  a table (because our "enums" _are_  tables) and totally missed that the argument input here is its _own_  table.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 07:53:45_

----

Yeah, it's confusing. Wondering if npcUtil functions should be tweaked to accept both "ki" and "keyItem" as field names.


----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Sunday May 03, 2020 at 16:01:14_

----

I fixed the exp_rate thing but it doesn't give a key item notification regardless for whatever reason so I'm leaving that part in until we know why.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 21:09:02_

----

`npcUtil.completeQuest(player, SANDORIA, tpz.quest.id.sandoria.EXIT_THE_GAMBLER, {keyItem = tpz.ki.MAP_OF_KING_RANPERRES_TOMB, title = tpz.title.DAYBREAK_GAMBLER, xp = 2000 * EXP_RATE})` didn't work?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday May 08, 2020 at 20:44:40_

----

Just gonna second that
```
player:messageSpecial(ID.text.KEYITEM_OBTAINED, tpz.ki.MAP_OF_KING_RANPERRES_TOMB) -- Map of King Ranperre's Tomb
```
shouldn't be needed if you change
```
npcUtil.completeQuest(player, SANDORIA, tpz.quest.id.sandoria.EXIT_THE_GAMBLER, {ki = tpz.ki.MAP_OF_KING_RANPERRES_TOMB, title = tpz.title.DAYBREAK_GAMBLER, xp = 2000})
```
to
```
npcUtil.completeQuest(player, SANDORIA, tpz.quest.id.sandoria.EXIT_THE_GAMBLER, {keyItem = tpz.ki.MAP_OF_KING_RANPERRES_TOMB, title = tpz.title.DAYBREAK_GAMBLER, xp = 2000})
```
notice the change from `ki = tpz.ki.MAP_OF_KING_RANPERRES_TOMB` to `keyItem = tpz.ki.MAP_OF_KING_RANPERRES_TOMB`


----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Monday May 04, 2020 at 02:08:07_

----

No, that was what it was before and I'm getting reports for No Message from
players.

On Sun, May 3, 2020 at 5:09 PM TeoTwawki <notifications@github.com> wrote:

> *@TeoTwawki* commented on this pull request.
> ------------------------------
>
> In scripts/zones/Northern_San_dOria/npcs/Aurege.lua
> <https://github.com/project-topaz/topaz/pull/558#discussion_r419160560>:
>
> > @@ -41,6 +41,7 @@ function onEventFinish(player, csid, option)
>      if csid == 521 and player:getQuestStatus(SANDORIA, tpz.quest.id.sandoria.EXIT_THE_GAMBLER) == QUEST_AVAILABLE then
>          player:addQuest(SANDORIA, tpz.quest.id.sandoria.EXIT_THE_GAMBLER)
>      elseif csid == 516 then
> -        npcUtil.completeQuest(player, SANDORIA, tpz.quest.id.sandoria.EXIT_THE_GAMBLER, {ki = tpz.ki.MAP_OF_KING_RANPERRES_TOMB, title = tpz.title.DAYBREAK_GAMBLER, xp = 2000})
> +        npcUtil.completeQuest(player, SANDORIA, tpz.quest.id.sandoria.EXIT_THE_GAMBLER, {ki = tpz.ki.MAP_OF_KING_RANPERRES_TOMB, title = tpz.title.DAYBREAK_GAMBLER, xp = 2000 * EXP_RATE})
> +        player:messageSpecial(ID.text.KEYITEM_OBTAINED, tpz.ki.MAP_OF_KING_RANPERRES_TOMB) -- Map of King Ranperre's Tomb
>
> npcUtil.completeQuest(player, SANDORIA,
> tpz.quest.id.sandoria.EXIT_THE_GAMBLER, {keyItem =
> tpz.ki.MAP_OF_KING_RANPERRES_TOMB, title = tpz.title.DAYBREAK_GAMBLER, xp =
> 2000 * EXP_RATE}) didn't work?
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/project-topaz/topaz/pull/558#discussion_r419160560>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AJIPZIGHUR5J77FAD3XEHDTRPXMPTANCNFSM4MWY77AA>
> .
>



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday May 04, 2020 at 03:32:17_

----

It's always been broken
