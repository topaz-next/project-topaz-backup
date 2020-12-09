**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:25:19_
_Originally opened as: project-topaz/topaz - Issue 85_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Hozu](https://github.com/Hozu)**
_Friday Jan 22, 2016 at 18:15 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2661_

----

Notably, Jupiter's Staff uses MOD_CRITHITRATE, which causes it to grant the 15% crit rate bonus to ranged attacks as well. NIN using dual Fudo gets +6% crit instead of +3% each, or Senju/Fudo becomes +9% crit instead of +6%/+3% each. There is currently no existing mod for applying the crit rate to a specific weapon.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:25:20_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Friday Jan 22, 2016 at 18:27 GMT_

----

Worth noting that we can't just change the existing mod because there are
weapons that give the bonus to both (but it might be only augments, id have
to double check that)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:25:22_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Friday Jan 22, 2016 at 21:22 GMT_

----

The existing mod should remain as-is because it's used for Mighty Strikes and non-weapons that boost crit rate (Hachiryu Haramaki, among others).




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:25:24_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Friday Jan 22, 2016 at 21:29 GMT_

----

I suppose what I meant was we can't programmatically remove crit rate from
other weapons unless it's confirmed to just be augments that apply to both




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:25:25_

----

<a href="https://github.com/Scavenge"><img src="https://avatars2.githubusercontent.com/u/9778206?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Scavenge](https://github.com/Scavenge)**
_Monday Jan 25, 2016 at 18:25 GMT_

----

i don't know the intricacies of how mods work, but I do know there are mods that are specific to your mainhand only.  there is a +damage mod on an augment that will only put the +damage on your mainhand weapon even if it's on your offhand weapon, which caused crazy kinds of ws damage.  off the top of my head I believe it was mod 45.  if it's possible for that mod to affect a specific slot, maybe one can be designed to affect only the specific slot it's in if it's a weapon, and otherwise apply to all weapon slots?  might be getting too optimistic




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:25:26_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Monday Jan 25, 2016 at 18:45 GMT_

----

there is no mod that puts main hand dmg if you equip it in your offhand.  MOD_MAIN_DMG_RATING is always translated to the offhand version if equipped in the other slot

and like I said earlier, there are weapons that increase the crit rate of every weapon, so we can't do what you were hoping anyways


