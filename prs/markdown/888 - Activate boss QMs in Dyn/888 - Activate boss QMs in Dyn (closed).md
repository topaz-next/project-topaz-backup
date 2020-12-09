**Labels:**



<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [jarmengaud](https://github.com/jarmengaud)**
_Saturday Jul 25, 2020 at 05:56:46_
_Originally opened as: project-topaz/topaz - Issue 888_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 25, 2020 at 08:00:31_

----

@wrenffxi  Are the bosses finished?


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Jul 25, 2020 at 08:40:03_

----

I've done no work on Dynamis NMs.  Checking them all for retail-accurate pools and battle mechanics is still on the TODO list #311


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Saturday Jul 25, 2020 at 13:39:54_

----

I was able to fight all 3, and they had their nasty TP moves... so they are not different from main zones bosses according to me.
They give the KI on kill, and drop their tome chapter. They don't drop anything else though I think.
But the idea is above all to access other zones...


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Saturday Jul 25, 2020 at 15:38:43_

----

Well that's not true, the code was there. With this change you can pop the 3 dreamland bosses and get their KI.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 25, 2020 at 15:53:37_

----

Was asking @wrenffxi because of https://github.com/project-topaz/topaz/commit/4e418e22 ~!


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Jul 25, 2020 at 23:55:49_

----

The code to pop the the NMs exists, but the code -for- the NMs doesn't.  That's probably why we have the QMs disabled.

Let's look at Valkurm, the first in order.

Cirrate Christelle:
* Doesn't use Extremely Bad Breath, Fragfrant Breath, Miasmic Breath, or Putrid Breath.
* Mechanics are not coded for using Absorbent Moss, Redolent Root and Odorless Fungus on her.

Lost Fairy Ring:
* Does not have enhanced movement speed.

Lost Nant'ina:
* Does not uses Blow 3 times, then Uppercut 3 times, then Charm.
* Does not do 2000 damage Uppercuts or hit particularly harder than a normal mob of its type.

Lost Steamcroissant:
* I don't even know what special mechanics this NM has, but whatever they are, they aren't coded.

Arch Christelle:
* Missing the same breath attacks as Cirrate Christelle, plus they're supposed to be stronger versions.
* Its melee attacks are supposed to be conal breath attacks.

In short, all dreamworlds bosses, as coded, are push-overs compared to what they're supposed to be.  They're essentially just higher-level versions of basic mobs of their family.  On my old server, a group of 6-10 75-relic-era players would waltz up to Cirrate Christelle and smash her into the sand without first killing any of the minibosses to weaken her.

So by all means, server owners who want to allow progress through Dreamlands can enable the fights, and they "work" in that you can pop, win, get KI, and move on.  But I don't think we should enable them by default, until the battle mechanics for the NMs are coded.

*edit to add: a cleaner solution to prevent NM pops may be to comment out the trades in the zone's IDs.lua, similar to what we do with Abyssea, rather than by hiding the QM NPC*


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Sunday Jul 26, 2020 at 10:44:48_

----

Understood. Though I was hoping that something, temporary and good-enough, could be allowed to at least let people access all Dyna zones.
Dynamis is the oldest end-game content and we still can't access Beaucedine, Xarc & Tavnazia, so we can't get a relic set.
And it seems nobody is working on those

Unfortunately I am not able to make retail-accuracte versions of those NMs.
Speaking of retail server, all dyna but [Divergent] are solo zones and all those NMs are easy solo anyway for a 99 with trusts, whatever their mechanics.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jul 26, 2020 at 19:14:14_

----

> edit to add: a cleaner solution to prevent NM pops may be to comment out the trades in the zone's IDs.lua, similar to what we do with Abyssea, rather than by hiding the QM NPC

@jarmengaud I'd like to suggest we re-purpose this PR into doing that. its a minimal addition to what you already have here.


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Sunday Jul 26, 2020 at 20:54:16_

----

k done. PR title is misleading now though.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jul 27, 2020 at 12:33:21_

----

The title of the PR can be edited. there is a button up top of this webpage for it. Its still technically true: you are activating the NPC, but disabling its script from running.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 29, 2020 at 12:22:45_

----

> I actually prefer all npc's to be initialized if they're supposed to be by default. And if they aren't working yet we just shouldnt have a script for them. (or comment out works too like how it is now) This is just my personal preference and I approve but, you all can decide what's better or more efficient cause that's not my strong point. I just like being able to see and check npc's (model, pos, etc.) at a glance and then not have to restart server to initialize them once I build a script.

My own personal pref is commented out with a note so people know why its not active yet, so we do not lead people into making prs to fix the npc while the mob still isn't fixed. Like happened to this contributor.
