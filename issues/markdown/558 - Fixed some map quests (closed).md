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
