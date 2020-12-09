**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:00_
_Originally opened as: project-topaz/topaz - Issue 51_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Deadwing888](https://github.com/Deadwing888)**
_Monday Oct 05, 2015 at 23:15 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2184_

----

We did our first King Behemoth with the new code. He felt (sort of) retail, certainly much closer than he was before.

As I mentioned in my King Behemoth Issues post, he should have single target draw-in and only use when people go past the columns on either entrance to the main KB area. I recognize this is tricky to code. Currently he draws people in both single target and whole alliance and he absolutely spams it. It gives the whole fight a very glitchy, non-retail feel.

Long term it'd be cool to see the draw in functioning true to retail, but if that's not realistic in the short term then I think the draw in needs to be turned off entirely.

To echo my other post (if someone want's to close it and focus on this one) the KB issues still at large are:

1) Wild horn and kick out are doing 3x too much damage
2) He still has no ~20% chance en-stun (even though there was a pull request that claimed to have added it) 
3) He still has no 10% triple attack (even though there was a pull request for this too)
4) His delay is 380 when it needs to be 200
5) There is something broken about land kings spawning system across the board. They're supposedly coded pop at a random time 15 minutes to 3 hours after server comes up, but in actuality they always pick near the exact same time to pop. Then after however many days it takes the HQ to pop, typically the NQ pops one more time and the system breaks entirely and nothing spawns until the server restarts. This is true for all 3 kings. Also (on Nasomi at least) sometimes the hq will spawn along with the NQ.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:01_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Oct 06, 2015 at 03:45 GMT_

----

IIRC that one pull never got merged.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:02_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Oct 06, 2015 at 03:47 GMT_

----

I wonder if there's a problem with just making a region at the entrances and having the region tick check the draw-in?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:03_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Oct 06, 2015 at 03:47 GMT_

----

Does he draw in anyone on his hate list who goes past there or just his primary target?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:04_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Tuesday Oct 06, 2015 at 04:02 GMT_

----

Only his primary target




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:06_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Oct 06, 2015 at 04:04 GMT_

----

as long as you can call single target draw-in via script, should be easily doable with regions




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:07_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Tuesday Oct 06, 2015 at 04:10 GMT_

----

If it turns out to be a simple fix with regions I will submit some annotated screenshots for the handful of other mobs that have draw-in regions.




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 14, 2020 at 21:33:52_

----

Most of this is "verification needed" territory now from issue being old AF. 

Delay: may have been edited previously by now, and 200 is an unusual delay for any mob in the 1st place - SE usually does specific values like: 180, 240, 360, 480 and I'd want to see more than someone eyeballing it from a video. If you get something like 179 or 186 I'd say "no, that's 180 delay with latency and or human error" for example

Triple attack: no mod needed if it comes from having a main or subjob set to thf. From the proc rate I would guess thf subjob, which BG wiki lists as a thing for behemoths in general while old wiki lists thf as the mainjob. i fit were mainjob I would expect a much higher proc rate.

Enstun: added today 8/14/220 #951

