**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:12_
_Originally opened as: project-topaz/topaz - Issue 7_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jan 29, 2015 at 04:51 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 866_

----

I dunno what happened, these used to look retailish but now they animate fast and move slow. That kid in south sandy is pretty much crawling, and cactrot rapido looks like he's having a seizure as I pass him by. I should not be outrunning rapido.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:13_

----

<a href="https://github.com/Fiocitrine"><img src="https://avatars1.githubusercontent.com/u/7704601?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Fiocitrine](https://github.com/Fiocitrine)**
_Tuesday Feb 03, 2015 at 21:47 GMT_

----

Rapido is funny. Sometimes he slows down then he'll speed up.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:15_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Sunday Mar 15, 2015 at 12:19 GMT_

----

they slow down at each point on their path, the more points there are the more noticeable it'll be
(easy way to tell is to stalk them and stick prints in their onPath functions in their scripts)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:16_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Monday Apr 06, 2015 at 15:13 GMT_

----

no idea if this will still be an issue when navmeshing is done, so i'll blame it all on bendangelo til then
(apparently i forgot to submit this comment til like 5 mins later)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:17_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Monday May 04, 2015 at 11:41 GMT_

----

at any rate, for mobs it's due to the path being cleared if they're too far from spawn point
so when the pathfind crap checks if the mob is following a path, the path is cleared and a total of ~15 sec delay is added (see: github/DarkstarProject/darkstar/blob/master/src/map/ai/ai_mob_dummy.cppDarkstar Issue L213 github/DarkstarProject/darkstar/blob/master/src/map/ai/ai_mob_dummy.cppDarkstar Issue L2389 github/DarkstarProject/darkstar/blob/master/src/map/ai/helpers/pathfind.cppDarkstar Issue L246)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:18_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Friday May 08, 2015 at 12:26 GMT_

----

I'll take a look into this. Mobs with a scripted path shouldn't be running roaming logic at all.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:20_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Monday Sep 07, 2015 at 05:21 GMT_

----

xdemolish That check only happens on mob disengage, it won't happen when the most first spawns. I think the issue lies in mob speed and the distance between points. Rapido runs much further than most points on his path. Which causes him to stutter as he moves to points.

This has to be looked into more/




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday May 12, 2020 at 02:34:56_

----

This can close, npc pathing issues have changed (there are still issues though, but doesn't match the original description for the most part)

as for rapido it was the pathing is simply very poorly performing. lots of nodes will bog it down, and the run flag makes it even worse (take the run flag off and things move faster - thats not supposed to work that way!)
