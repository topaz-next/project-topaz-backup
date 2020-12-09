**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:30_
_Originally opened as: project-topaz/topaz - Issue 57_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Deadwing888](https://github.com/Deadwing888)**
_Tuesday Oct 27, 2015 at 15:48 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2338_

----

1) Delay should be 200 rather than 320
2) Should hit harder, 175 combat damage multiplier is in the ballpark.
3) Should double attack at a 10% rate. (Ignore the wiki, he has no triple attack)
4) Movement speed is somewhere between 60 and 80
5) Should not be immune to bind, just very resistant (this was my bad)
6) Needs more magic evasion. My educated guesses say +200 to every element but ice. +100 ice meva. Boost mod_bindres and mod_paralyzeres to 100
7) Builds stun resist. ~10 stuns till it starts resisting ~30 stuns and hit rate is floored (I know there's no good way to do this yet)
8) Missing dread-storm TP move. Benchmark damage 617 to naked 75 rdm no shell. Terror is ~15 sec
9) Fulmination is doing about 20% too much damage
10) Fulmination paralyze is far too weak, I'd say ~85% potency is the target
11) Plague swipe information placeholder (could not test)
12) His wings break (point down rather than up) with critical hits and regrow with time. My rough estimate is 10% chance to break with critical, 8 minute regrowth time.
13) Will only use tourbillion when wings are up.
14) Thunderstrike damage was spot on, but needs a ~3 second stun added
15) Needs noturn flagged: Fossilizing Breath (front) Thunderstrike (front) Plague Swipe (back) Tourbillion (both) Tenebrous mist (both) Dreadstorm (both)
16) Has single target draw in. Uses on his main target when they when they are 12'+ away, or when they make it to the top of the little hill there. He doesn't draw in to him, but instead picks one of a few random points in the valley and draws you in there, meaning he often has to run to where he drew you in.
17) Respawns 48-72 hours after TOD on one hour windows (see cerb's respawn code)
18) Spawns 12-36 hours after the server comes up on 1 hour windows.
19) Has a frosty-breath growl animation every 5 minutes when idle. 

Bonus) In 75 era there was a height check on fulmination and if the mage line was up on the little ledge with tanks down in valley, fulm would not hit them. 

PS) Wiki says he's a thief sub war, I think they're just guessing on that because of the triple attack they think he has. My money is on war/war as he's currently coded.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:31_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Oct 27, 2015 at 15:50 GMT_

----

You can get movement speed from inspecting the 0x0E packet




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:32_

----

<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Wednesday Oct 28, 2015 at 18:37 GMT_

----

<3 I will get on t his sometime later this week!




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:33_

----

<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Oct 29, 2015 at 02:41 GMT_

----

In regards to the height check, Tiamat's inferno blast is the same but I have no idea how to implement any height checking. Any ideas?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:34_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Thursday Oct 29, 2015 at 04:40 GMT_

----

It was the same, was patched in retail circa 2011 same time as khim




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:35_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday Oct 29, 2015 at 15:26 GMT_

----

re: plague swipe, I don't think it's possible to do non-frontal cone attacks.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:36_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Friday Jan 29, 2016 at 15:22 GMT_

----

Any update on this m241dan ?

My shell asks me once a week if we're getting good Khim code soon. Would love to see this happen, let me know what I can do to help.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:37_

----

<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Friday Jan 29, 2016 at 15:35 GMT_

----

Hmmm, I did some of it. Let me dig out the branch and update it and pull request.


