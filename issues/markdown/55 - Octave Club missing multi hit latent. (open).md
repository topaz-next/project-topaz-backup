**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:20_
_Originally opened as: project-topaz/topaz - Issue 55_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Deadwing888](https://github.com/Deadwing888)**
_Thursday Oct 15, 2015 at 02:24 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2267_

----

http://ffxiclopedia.wikia.com/wiki/Octave_Club




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:21_

----

<a href="https://github.com/RunAwayDSP"><img src="https://avatars3.githubusercontent.com/u/6879206?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [RunAwayDSP](https://github.com/RunAwayDSP)**
_Saturday Oct 17, 2015 at 16:50 GMT_

----

an update on this, it does have MOD_DOUBLE_ATTACK   25  LATENT_JOB_LEVEL_EVEN   it does not have a mod for 2-8 attacks on level is divisible by 8




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:22_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Saturday Oct 17, 2015 at 21:20 GMT_

----

Why would someone give it double attack modifier, that's wrong because it applies on WS. The existing level latents need to be refactored into one latent where the parameter of the latent is the level divisor (special case for 1 being odd level), though the multiple of 13 at night latent needs to be separate.

I couldn't quite find where to add the extra swings so I never did anything with it.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:23_

----

<a href="https://github.com/whasf"><img src="https://avatars3.githubusercontent.com/u/6373706?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [whasf](https://github.com/whasf)**
_Saturday Nov 21, 2015 at 05:29 GMT_

----

Could be a core issue?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:25_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Saturday Nov 21, 2015 at 07:11 GMT_

----

It definitely needs to be implemented into the core somewhere. A new mod to contain the extra amount of hits, and then rework the existing level latents to be one mod (excl. the multiple of 13 at night one) to use the level as the parameter (and 1 for odd level). I was going to do that but I never could figure out where the max possible swings/round is read from the DB.


