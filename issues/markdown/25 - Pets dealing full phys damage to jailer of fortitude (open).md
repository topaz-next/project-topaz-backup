**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:42_
_Originally opened as: project-topaz/topaz - Issue 25_

----

<a href="https://github.com/Kthulupwns"><img src="https://avatars1.githubusercontent.com/u/11568537?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Kthulupwns](https://github.com/Kthulupwns)**
_Monday Jun 08, 2015 at 00:55 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 1544_

----

Smn avatars and bst pets dealing unmitigated phys damage to jailer of fortitude, most likely just their damage equation not checking for defense variables.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:43_

----

<a href="https://github.com/Kthulupwns"><img src="https://avatars1.githubusercontent.com/u/11568537?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Kthulupwns](https://github.com/Kthulupwns)**
_Monday Jun 08, 2015 at 01:16 GMT_

----

 setMod(MOD_UDMGPHYS,-95);

added that to onMobEngage , which addresses the effect of the issue, but doesn't fix whats causing the issue, the same problem with chronos in NE Apollyon as well.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:45_

----

<a href="https://github.com/Kthulupwns"><img src="https://avatars1.githubusercontent.com/u/11568537?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Kthulupwns](https://github.com/Kthulupwns)**
_Monday Jun 08, 2015 at 01:39 GMT_

----

And most likely jailer of temperance as well.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:46_

----

<a href="https://github.com/Kthulupwns"><img src="https://avatars1.githubusercontent.com/u/11568537?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Kthulupwns](https://github.com/Kthulupwns)**
_Monday Jun 08, 2015 at 01:40 GMT_

----

Pet's should only be able to deal damage to Jailer of Temperance during his blunt mode phase, but could still use like Predator Claws for Slashing phase and Spinning dive for Piercing phase.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:47_

----

<a href="https://github.com/Scavenge"><img src="https://avatars2.githubusercontent.com/u/9778206?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Scavenge](https://github.com/Scavenge)**
_Thursday Jun 11, 2015 at 18:54 GMT_

----

the version of fortitude on era is my own and likely not what dsp uses, however you can find the code in my own personal repo on this account, under the jailers branch




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:48_

----

<a href="https://github.com/Scavenge"><img src="https://avatars2.githubusercontent.com/u/9778206?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Scavenge](https://github.com/Scavenge)**
_Thursday Jun 11, 2015 at 18:55 GMT_

----

same goes for the rest of the jailers probably




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:49_

----

<a href="https://github.com/Scavenge"><img src="https://avatars2.githubusercontent.com/u/9778206?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Scavenge](https://github.com/Scavenge)**
_Thursday Jun 11, 2015 at 18:58 GMT_

----

also if it is only pets that have this issue, adding a mod to the jailer itself will not fix things because it will affect all incoming damage, not just pets'. there was an issue not that long ago that had wyverns doing full damage even while synced.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:50_

----

<a href="https://github.com/Kthulupwns"><img src="https://avatars1.githubusercontent.com/u/11568537?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Kthulupwns](https://github.com/Kthulupwns)**
_Saturday Jun 13, 2015 at 16:49 GMT_

----

This is on dsp as well as era




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:51_

----

<a href="https://github.com/Kthulupwns"><img src="https://avatars1.githubusercontent.com/u/11568537?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Kthulupwns](https://github.com/Kthulupwns)**
_Saturday Jun 13, 2015 at 16:51 GMT_

----

But its the way pet auto attack damage is calculated against mobs sql "toughness"




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:01:52_

----

<a href="https://github.com/Kthulupwns"><img src="https://avatars1.githubusercontent.com/u/11568537?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Kthulupwns](https://github.com/Kthulupwns)**
_Saturday Jun 13, 2015 at 16:51 GMT_

----

Its just the formula itself


