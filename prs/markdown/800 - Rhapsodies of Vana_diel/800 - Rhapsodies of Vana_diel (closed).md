**Labels:**



<a href="https://github.com/zircon-tpl"><img src="https://avatars0.githubusercontent.com/u/60901633?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zircon-tpl](https://github.com/zircon-tpl)**
_Thursday Jul 02, 2020 at 22:00:46_
_Originally opened as: project-topaz/topaz - Issue 800_

----

Absent new issues prior to then, the `rov` branch is scheduled to be merged into `release` on August 5th, 2020.

This `rov` branch contains implementation for [Rhapsodies of Vana'diel 1-1 through 1-18](https://www.bg-wiki.com/bg/Category:Rhapsodies_of_Vanadiel_Missions).

As on retail, Rhapsodies of Vana'diel will be enabled by default.

During their progression, these missions reward the following Key Items which affect EXP rates:
- [Rhapsody in White](https://www.bg-wiki.com/bg/%22Rhapsody_in_White%22)
- [Rhapsody in Umber](https://www.bg-wiki.com/bg/%22Rhapsody_in_Umber%22)
- [Rhapsody in Azure](https://www.bg-wiki.com/bg/%22Rhapsody_in_Azure%22)

These key items also allow the purchase of items from [Curio Vendor Moogles](https://www.bg-wiki.com/bg/Curio_Vendor_Moogles). These vendors - originally added in #652 - were merged into `release` on June 17th, 2020. They have not been functional in `release` due to the absence of these key items, but will be available to players should they acquire the key items on a server which has these Rhapsodies of Vana'diel missions enabled.

These missions also reward Trust Ciphers which on retail may be exchanged to unlock special trusts. Work on trusts is being developed in a separate `trust` branch, and no trust implementation will be included when `rov` is merged into `release`. Servers which intend to enable trusts may wish to advise players to keep these ciphers until a time which they may be used.

Progression in this storyline will enable players to enter the zone "Escha - Zi'Tah". This zone is currently not implemented, nor is the "Geas Fete" content which occurs in this zone on retail.

This `rov` branch has been in `canary` since May 5th, 2020. It contains work from the following Pull Requests, which may be reviewed by those who are unfamiliar with the history of the branch:
- #362 - Rhapsodies of Vana'diel 1-1 to 1-18 (_zach2good_)
- #561 - ROV Chapter 1 mob moves (_zach2good_)
- #591 - Add Threnody II + add NM Siren's spell list (_ibm2431_)
- #594 - added Mandragora dewdreop for RoV questline (_kaincenteno_)
- #595 - Changed Huge Wasp and Pygmaioi drop rate (_kaincenteno_)
- #643 - Rov fix gilgamesh letter and zeid ii (_kaincenteno_)
- #666 - Rov valor buffs (_kaincenteno_)
- #694 - Field Support fix (_kaincenteno_)
- #697 - Allow Exit from Escha - Zi'Tah (_brianmask_)
- #705 - Fix unable to continue RoV questline (_kaincenteno_)
- #910 - Fix issues with Lion II cipher and some cutscenes (_cocosolos_)
- #911 - ROV fixes relating to Ring My Bell + give ROV missions proper precedence (_ibm2431_)

As Pull Requests were previously reviewed and approved on the individual level, and the branch has been tested by both Staff and multiple servers which run our `canary` branch, the contents of this branch do not require a second review by Staff.

This Pull Request shall be open for discussion should Community Members have questions or concerns regarding this branch. 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jul 08, 2020 at 23:38:10_

----

> This was reported to me, but I haven't had time to look into:
> 
> > On Rov  1-18 mission ring my bell .. when i click on door .. in the server console it says error l[21:59:23][Error] luautils::onTrigger: .\scripts/globals/rhapsodies.lua:323: bad argument 1 to 'pairs' (table expected, got nil)     the door gives no cutscene

`RING_MY_BELL` has no entries `tpz.rhapsodies.requiredCharacters`, so shouldn't be calling `tpz.rhapsodies.charactersAvailable` unless characters need to be added to the table. I think this was discussed at some point and Tenzen is required for this CS?



----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jul 08, 2020 at 23:41:41_

----

I believe this should be checking `player:getCurrentMission(player:getNation()) > 15` and not `player:getFameLevel(player:getNation()) >= 5`.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 09:16:08_

----

Will be resolved by #911 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jul 08, 2020 at 23:38:10_

----

> This was reported to me, but I haven't had time to look into:
> 
> > On Rov  1-18 mission ring my bell .. when i click on door .. in the server console it says error l[21:59:23][Error] luautils::onTrigger: .\scripts/globals/rhapsodies.lua:323: bad argument 1 to 'pairs' (table expected, got nil)     the door gives no cutscene

`RING_MY_BELL` has no entries `tpz.rhapsodies.requiredCharacters`, so shouldn't be calling `tpz.rhapsodies.charactersAvailable` unless characters need to be added to the table. I think this was discussed at some point and Tenzen is required for this CS?



----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jul 08, 2020 at 23:41:41_

----

I believe this should be checking `player:getCurrentMission(player:getNation()) > 15` and not `player:getFameLevel(player:getNation()) >= 5`.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 09:16:08_

----

Will be resolved by #911 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Jul 05, 2020 at 22:38:00_

----

This was reported to me, but I haven't had time to look into:
> On Rov  1-18 mission ring my bell .. when i click on door .. in the server console it says error l[21:59:23][Error] luautils::onTrigger: .\scripts/globals/rhapsodies.lua:323: bad argument 1 to 'pairs' (table expected, got nil)     the door gives no cutscene


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Tuesday Jul 07, 2020 at 09:01:53_

----

> 1-12: ISSUE: Had the cutscene while still being rank 3 in Windurst (used !setrank <player> 3 for 1-7 before), even when 5-2 (Shadow Lord defeated) was needed: https://www.bg-wiki.com/bg/Rhapsodies_of_Vanadiel_Mission_1-12.
1-17: Obtained Cipher of Zeid's alter ego II (issue?) but was unable to start the cutscene from Norg on the Ring My Bell mission (don't know if it was intended that way for now).
Home Points teleport price:
Nothing: 500 gils.
Rhapsody In White: Still 500 gils (should be less).
~~FoV buffs cost (kain's Rov valor buffs #666 PR should be taken in consideration here) (Crawlers' Nest):
Nothing: Reraise 10.
Rhapsody In White: Still 10 (should be 5).~~

This is what I came across when I tested the branch weeks ago. Thank you, zach!

Message edited, I'm sorry for misleading! FoV price is indeed fixed by #666 now.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Jul 11, 2020 at 07:35:19_

----

Dumping this from discord as a reminder:

Kain:
RoV question here. When you get Lion II item. It's currently as player:addItem so it can be missed. Is this on purpose? I heard something about there being another NPC that gives you those trust items if your inventory was full. Can someone confirm if this is the case with Lion II?

Juggalo
```
if npcUtil.giveItem(player, 10159) then-- Cipher: Lion II
    player:completeMission(ROV, tpz.mission.id.rov.A_LAND_AFTER_TIME)
    player:addMission(ROV, tpz.mission.id.rov.FATES_CALL)
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 11, 2020 at 17:39:36_

----

> I heard something about there being another NPC that gives you those trust items if your inventory was full. 

A yeah, the "Resume Point" I think. Pile of sparkles nearby. SE only started doing that as of RoV, instead of repeating the entire CS you can just pick up the item there. Note sure what it does if you've missed multiple items.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 18, 2020 at 18:25:16_

----

#602 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 05:32:53_

----

~~1) Despite SE's chart, you can't get blocked on ROV for being on a mission prior to COP 3-2 until you hit ROV chapter 2 (so a static mission check at that point is fine)
(https://forum.square-enix.com/ffxi/threads/47983-What-should-I-do-if-I-can%E2%80%99t-progress-in-Rhapsodies-of-Vana%E2%80%99diel)~~
~~2) The crystal CS where you get Lion II needs to be checked for params indicating the player's nation progress, since the dialogue changes~~
~~3) The early ROV CSes with Tenzen might change too if you've already met him in COP - I don't think we account for those~~

Items in this comment are resolved.


----
<a href="https://github.com/zircon-tpl"><img src="https://avatars0.githubusercontent.com/u/60901633?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zircon-tpl](https://github.com/zircon-tpl)**
_Saturday Aug 01, 2020 at 05:48:12_

----

I have updated my first post.

**This branch is currently scheduled to be merged into `release` on August 5th, 2020.**

Community Members who would like to ensure that this branch has been fully verified are encouraged to pull this `rov` branch to play through the content!
