**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:42_
_Originally opened as: project-topaz/topaz - Issue 95_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Hozu](https://github.com/Hozu)**
_Sunday Feb 28, 2016 at 17:41 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2832_

----

**_Client Version_** (type `/ver` in game) **:**
30160203_0

**_Server Version_** (type `revision` in game) **:**
github/DarkstarProject/darkstar/commit/14a1e3d2f81547767a4157fb8d9762a9ff3b99e6

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
http://i.imgur.com/5yj6mea.png I think that image sums it up. On retail you had a line of sight in that situation. There are many locations like that where you should be able to cast on a thing that you don't have a straight path to.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:43_

----

<a href="https://github.com/dazusu"><img src="https://avatars0.githubusercontent.com/u/7009763?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dazusu](https://github.com/dazusu)**
_Sunday Feb 28, 2016 at 19:21 GMT_

----

I'm pretty sure this is something that _can_ be done with recast navmesh's, i agree it's going to be an issue; this is one for bendangelo to assess I think.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:44_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Monday Feb 29, 2016 at 14:41 GMT_

----

This is a tough one. I feel like for players we should trust the clients validation and ignore it on the server. Are there any cases where we need the server to check line of sight?

I think mobs can cast spells without line of sight as well?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:45_

----

<a href="https://github.com/dazusu"><img src="https://avatars0.githubusercontent.com/u/7009763?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dazusu](https://github.com/dazusu)**
_Monday Feb 29, 2016 at 14:54 GMT_

----

Because client validation is allowing people to cast through trees and some walls; when it should not. However, if it's not going to be possible to fix, it might be worth making this additional server an option via conf, or perhaps an option on a per zone basis (so it can be enabled where it is abused, such as for end-game areas).




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:47_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Monday Feb 29, 2016 at 15:29 GMT_

----

we will never ever be "trusting the clients validation", especially since
both ashita and windower have extremely popular plugins that skip the
validation

On Mon, Feb 29, 2016 at 7:54 AM, Liam Conlan notificationsgithub.com
wrote:

> Because client validation is allowing people to cast through trees and
> some walls; when it should not. However, if it's not going to be possible
> to fix, it might be worth making this additional server an option via conf,
> or perhaps an option on a per zone basis (so it can be enabled where it is
> abused, such as for end-game areas).
> 
> —
> Reply to this email directly or view it on GitHub
> github/DarkstarProject/darkstar - Issue 2832Darkstar Issue issuecomment-190245029
> .




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:48_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Monday Feb 29, 2016 at 16:41 GMT_

----

I think that there should be a different check for line of sight - rather than checking if a direct straight path exists between the two entities, check if a line between the two crosses a wall. Or would there be problems with that method?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:49_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Monday Feb 29, 2016 at 16:44 GMT_

----

Pretty sure that's what the raycast does right now. Most likely there's an
invisible wall preventing you from falling into that pit




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:50_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Monday Feb 29, 2016 at 16:49 GMT_

----

Oh... then perhaps the navmeshes need to be modified to have certain areas have a different kind of wall, which also prevents pathing but is ignored for line of sight? One wall in particular I can think of off the top of my head is the fence by the cabin in Misareaux Coast, by where you spawn Boggleman mission NM. On retail I used to kite Gration around it, and I could cast through that fence, but the mob would go around it. Sounds like a lot of work, though.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:51_

----

<a href="https://github.com/dazusu"><img src="https://avatars0.githubusercontent.com/u/7009763?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dazusu](https://github.com/dazusu)**
_Monday Feb 29, 2016 at 17:22 GMT_

----

Hozu - I assume that is exactly the fix, the problem is the amount of work involved in modifying the navmeshes. It would probably need to be done manually (bendangelo can confirm); that's incredibly time intensive... and not fun!

Damn those invisible walls. :(




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:52_

----

<a href="https://github.com/dazusu"><img src="https://avatars0.githubusercontent.com/u/7009763?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dazusu](https://github.com/dazusu)**
_Monday Feb 29, 2016 at 17:24 GMT_

----

Standing on top of a cliff which I can walk off (Dangruff Wadi), I can't cast on a Goblin on the floor below me. I think similar has been reported, but just wanted to note it.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:53_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Tuesday Mar 01, 2016 at 04:34 GMT_

----

Off the top of my head a few additional (75cap endgame) instances in which it would be important to have navmesh preventing movement but not line of sight:

1) Fifth floor in northwest apollyon (for Kaiser Behemoth kite nuke method)
3) Both ledges of the Dragon's Aery pit.
4) The edges of all ramps in sea.
5) The ponds in sky (primarily used for despot kiting)
6) The logs in the Behemoth area of Behemoth's dominion.
7)The small wall drop-offs on the 4 god islands in sky.
8) The ponds in caedarva mire used for ZNM kiting.
9) For Dark Ixion fights: The stairway in southeast East Ronfaure [S]. The cliff edges in Batalia Downs [S], Rolanberry Fields [S], West Sarutabaruta [S]. The wall edges in Fort KNS. The gehtto orcish tower structures in Jugner Forest [S].
10) Ghoyu's Reverie cliff edges (For Sandworm Serket nuke kiting)
11) The Pond at J-12 Map 1 Sea serpent grotto, and the ramp above it (the door is non functional, hakutaku cluster can only be farmed by pulling the singular hecteyes from the ground)
12) The upper wacker at I-8 Mount Zhayolm (a potential spot for mages in the Cerberus fight)
13) The small cliff edge near Khimaira, I-9 Hediva Isle, Caedarva Mire (as a potential spot for mage to stand to dodge fulmination)
14) Dynamis BCD: cliff edges. (For TE nuke --> logoff method)
15) Dynamis Xarc Shadowlord ramps (important for DL zerg) and 3 eye structures.
16) Dynamis Windurst bridges
17) Dynamis Tav Ramps
18) Dynamis Sandy parapets and auction house
19) Dynamis Bastok Ore Street
20) Dynamis Jeuno Palace balcony

I can post this in the navmeshes git and/or break it apart into separate issues as needed. If anything is unclear just ask and I'm happy to explain further.


