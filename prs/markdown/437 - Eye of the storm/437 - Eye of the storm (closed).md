**Labels:**



<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [59blargedy](https://github.com/59blargedy)**
_Tuesday Mar 24, 2020 at 04:35:05_
_Originally opened as: project-topaz/topaz - Issue 437_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Mar 24, 2020 at 06:18:04_

----

Amount should just be 24k, loot handling will split it automatically.
https://youtu.be/TlvThE0sM14?t=950


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Mar 24, 2020 at 06:18:44_

----

Duplicate entries?


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Mar 24, 2020 at 13:04:29_

----

yep :( thanks for catching


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Mar 24, 2020 at 13:05:31_

----

got it, wasn't sure how that split worked and thought i would need some getplayercount shenanigans i wasnt prepared yet to do. much easier, thank you!


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Wednesday Mar 25, 2020 at 22:48:07_

----

monstertpmoves isnt needed as a require in all the mob scripts


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Mar 26, 2020 at 03:09:22_

----

they dont have a special ability before death, wiki is just referring to their unique breath attacks. will look at other alterations - wyverns already have boosted movement speed of 50 not sure if they need more but will compare against vid.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Mar 31, 2020 at 00:36:39_

----

Make sure the name matches the mob name (`Lightning_Wyvern`), and sort the skill list ID (1011) to be above the Chaos Wyvern (1012) and I'll hit the button.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Mar 31, 2020 at 00:37:32_

----

Set mod in `onMobFight` or `onMobEngaged`?


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Mar 31, 2020 at 03:57:59_

----

I'm not sure which is right - they basically use it as soon as they see you. if onmobfight is better, will do there. it works as is in terms of testing, but rather do it in the right place if they are different.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Mar 31, 2020 at 05:20:57_

----

onMobEngaged is when the mob aggros (and also when it reaggros); onMobFight is constantly - I believe it's every attack round


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Mar 31, 2020 at 07:38:50_

----

oh yes, i remember now. most definitely how i have it, when it aggros in onmobengaged


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Mar 24, 2020 at 06:18:04_

----

Amount should just be 24k, loot handling will split it automatically.
https://youtu.be/TlvThE0sM14?t=950


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Mar 24, 2020 at 06:18:44_

----

Duplicate entries?


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Mar 24, 2020 at 13:04:29_

----

yep :( thanks for catching


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Mar 24, 2020 at 13:05:31_

----

got it, wasn't sure how that split worked and thought i would need some getplayercount shenanigans i wasnt prepared yet to do. much easier, thank you!


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Wednesday Mar 25, 2020 at 22:48:07_

----

monstertpmoves isnt needed as a require in all the mob scripts


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Mar 26, 2020 at 03:09:22_

----

they dont have a special ability before death, wiki is just referring to their unique breath attacks. will look at other alterations - wyverns already have boosted movement speed of 50 not sure if they need more but will compare against vid.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Mar 31, 2020 at 00:36:39_

----

Make sure the name matches the mob name (`Lightning_Wyvern`), and sort the skill list ID (1011) to be above the Chaos Wyvern (1012) and I'll hit the button.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Mar 31, 2020 at 00:37:32_

----

Set mod in `onMobFight` or `onMobEngaged`?


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Mar 31, 2020 at 03:57:59_

----

I'm not sure which is right - they basically use it as soon as they see you. if onmobfight is better, will do there. it works as is in terms of testing, but rather do it in the right place if they are different.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Mar 31, 2020 at 05:20:57_

----

onMobEngaged is when the mob aggros (and also when it reaggros); onMobFight is constantly - I believe it's every attack round


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Mar 31, 2020 at 07:38:50_

----

oh yes, i remember now. most definitely how i have it, when it aggros in onmobengaged


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Mar 24, 2020 at 05:21:42_

----

the npc_list.sql looks weird, maybe it needed to be rebased? way too many additions/deletions


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Mar 24, 2020 at 13:06:35_

----

> 
> 
> the npc_list.sql looks weird, maybe it needed to be rebased? way too many additions/deletions

I'm not sure what i did or how to fix it. Do you know?


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Mar 24, 2020 at 13:52:11_

----

@kaincenteno i figured out what i did wrong and how to fix it, sorry about that :(


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Friday Mar 27, 2020 at 16:54:56_

----

I checked: riverne, ifrit, gustav, abyssea-grau nms and standard mobs are
75 per npc database. If we need all 30 pools I can go validate each one if
preferred.



On Fri, Mar 27, 2020 at 12:14 PM KnowOne134 <notifications@github.com>
wrote:

> *@KnowOne134* commented on this pull request.
>
> we sure all the mobs in that family are movement of 75 before i say merge?
> i went to my database and filtered all pools that had family 266 and pulled
> up 30 pools, such as Vouivre, Pyrodrake, Hurricane_Wyvern, Bune. to name a
> few
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/project-topaz/topaz/pull/437#pullrequestreview-383003393>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AMRSUMGBEOI47MYV5BIFMMDRJTGH5ANCNFSM4LSLR45A>
> .
>

