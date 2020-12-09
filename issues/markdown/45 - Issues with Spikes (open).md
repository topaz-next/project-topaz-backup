**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:59_
_Originally opened as: project-topaz/topaz - Issue 45_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Deadwing888](https://github.com/Deadwing888)**
_Thursday Sep 17, 2015 at 22:59 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2095_

----

1) Retail phalanx mitigates damage from spikes the same way it would a melee hit or magic spell. Darkstar phalanx seems to currently have no effect on spikes.
2) If a low level mob were to hit a high level PL with spikes, it should render the exp for this mob null for the party. (it currently does not)
3) Spikes do not seem to resist as much as they should vs higher level monsters (I'm sorry this is so vague)
~~4) Dread spikes should wear off after half of the caster's HP has been drained. (I'm told it does not)~~
5) Duelist's tights currently do not boost damage from spikes.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:01_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Friday Sep 18, 2015 at 00:25 GMT_

----

Spikes has many issues, actually.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:02_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Sep 18, 2015 at 21:35 GMT_

----

> Spikes has many issues, actually.

Hozu You should open us an issue report for all the things wrong with spikes. Bullet point list encourage.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:03_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Friday Sep 18, 2015 at 21:57 GMT_

----

Oh I'm not sure I know of all of the issues, but I can ask around. What I do know is that gear that has spikes has a 100% proc rate, and the effect proc rate on curse "spikes" from gear is way too damn high. Dread spikes does not have an cap on the damage absorbed, though that wasn't too broken until SE made it last for 3 mins. I did not know about the phalanx issue, though.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:04_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Sep 18, 2015 at 22:26 GMT_

----

> What I do know is that gear that has spikes has a 100% proc rate,

What? I am certain that's not coded that way. Barring possibility somebody added new stuff and set the database entry for it wrong there shouldn't be any 100% rate gear (unless its retail 100%). There's a mod setting proc rate and the core code handling it hasn't been touched in like a year. github/DarkstarProject/darkstar/blob/master/src/map/modifier.hDarkstar Issue L540

Maybe someone used wrong mod set (one is for gear, the other for the spell only - they are separate because if you use the wrong one the values stack).




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:05_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Friday Sep 25, 2015 at 19:19 GMT_

----

Dread Spikes should absorb up to 50% of the max HP the caster has upon casting it, before mods. Reprisal behaves in a similar manner and works correctly in that regard.

Due to the duration extension, DRK can currently loop Dread Spikes and becomes effectively immune to melee attacks.

https://www.bg-wiki.com/bg/Dread_Spikes




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:07_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Wednesday Oct 14, 2015 at 17:38 GMT_

----

Another issue with Dread Spikes - if you die to a melee attack with it active, you'll be healed afterwards and cause a zombie glitch.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:08_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Wednesday Oct 14, 2015 at 17:50 GMT_

----

I'll fix that zombie issue, it's a big issue.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:09_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Friday Oct 16, 2015 at 23:22 GMT_

----

github/DarkstarProject/darkstar/commit/1559417cb47e932791e1d1479c8efe04bd9ce443 fixes the no cap to Dread Spikes. Other issues remain.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:12:10_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jan 23, 2017 at 06:39 GMT_

----

Self assigned, I'm 90% into reworking both spikes and additional effects.

2019 edit : spongebob 2 years later voice, still not completed. add effects mostly done in a branch but haven't gotten to spikes yet

