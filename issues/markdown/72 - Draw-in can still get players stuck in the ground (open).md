**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:20:45_
_Originally opened as: project-topaz/topaz - Issue 72_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Hozu](https://github.com/Hozu)**
_Monday Dec 21, 2015 at 19:20 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2511_

----

I remember that there was a commit that added a valid navmesh location check, but it doesn't appear to be enough/isn't working properly because players can still get stuck in the ground. Also, while the thing where players get popped up a bit on draw-in was added, it doesn't seem to be enough? I don't know how high it bumps you on retail, but it was noticeable if people know about it. I can't see any vertical height gaining when drawn-in on DSP servers.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:20:47_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Monday Dec 21, 2015 at 19:28 GMT_

----

well, there's kind of a huge problem with how this works: IIRC, moving mobs don't ever change their y position relative to the terrain they are moving over (the only way to do so would be to check the bounds of the navmesh, which is pretty new and probably doesn't do so).  So the problem is that the y value of a mob can't ever really be trusted (especially since the client auto corrects it) - meaning that no matter what we try to offset the draw in position by, it could still be wrong
also, the "height correction" is only 0.5, so you wouldn't notice it




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:20:48_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Monday Dec 21, 2015 at 20:06 GMT_

----

Ah, well that explains the whole problem. :/




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:20:49_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Monday Dec 21, 2015 at 21:49 GMT_

----

It's possible to get the Y position from a point on the navmesh but there is still a chance it'll be in a non-walkable spot. I think a more generous height correction is our best bet.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:20:50_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Monday Dec 21, 2015 at 22:51 GMT_

----

Best to get the y pos from the navmesh and then move it up a bit. No way we
can do it without that




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:20:51_

----

<a href="https://github.com/Scavenge"><img src="https://avatars2.githubusercontent.com/u/9778206?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Scavenge](https://github.com/Scavenge)**
_Monday Jan 04, 2016 at 20:38 GMT_

----

i think setting it to extra height on its exact horizontal coords would be fine, the player just falls, which is kinda like getting 'knocked up' as you get drawn in.  from what i recall it takes an excessive amount of height for falling to not work.  




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:20:52_

----

<a href="https://github.com/dr01d3r"><img src="https://avatars2.githubusercontent.com/u/2850680?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dr01d3r](https://github.com/dr01d3r)**
_Wednesday Jan 13, 2016 at 05:38 GMT_

----

Months ago, I tried doing a height offset with Tiamat draw-in; however, due to the terrain, either the offset was not enough or it caused the player to jump multiple times (multiple draw-ins, i believe).




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:20:54_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 24, 2016 at 01:13 GMT_

----

Additional prob someone just pointed out to me: draw in should place those draw in directly in front of the target. Seems with some larger mobs you land either inside or worse, behind the mob. This is especially bad with stuff like Wymrs given drawn in because **spike Fail**. _That's a not a typo_ 😃 


