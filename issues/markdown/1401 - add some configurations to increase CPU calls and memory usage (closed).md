**Labels:**



<a href="https://github.com/zanglikun"><img src="https://avatars0.githubusercontent.com/u/61591648?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zanglikun](https://github.com/zanglikun)**
_Wednesday Oct 21, 2020 at 01:51:18_
_Originally opened as: project-topaz/topaz - Issue 1401_

----


I don't know how the topaz project works in the computer hardware, but sometimes, when my friends and I call T5 or Dy, they get stuck, but the server CPU It's only 2% running. It's a bit embarrassing. Maybe it's related to the Internet, but it doesn't get stuck in the picture. This affects the experience very much. So, I asked this question. Ha ha, thank you for your patience


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 21, 2020 at 01:58:22_

----

The bottleneck is usually iops/disk access. The software runs as much cpu and ram as it needs, it just doesn't need more.


----
<a href="https://github.com/zanglikun"><img src="https://avatars0.githubusercontent.com/u/61591648?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zanglikun](https://github.com/zanglikun)**
_Wednesday Oct 21, 2020 at 02:04:16_

----

By the way, can we add comments to the fields in the database table? If so, it will be more convenient for us to go to the DIY server, because many field names are not very intuitive (^ V ^)


----
<a href="https://github.com/zanglikun"><img src="https://avatars0.githubusercontent.com/u/61591648?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zanglikun](https://github.com/zanglikun)**
_Wednesday Oct 21, 2020 at 02:06:08_

----

I went to test the IO pressure of the hard disk first, although I felt that the hard disk was running without pressure Thank u



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Oct 21, 2020 at 03:27:15_

----

With how our current lua system is set up, we ping the disk _a lot_.

Every time a monster dies, we find and execute a lua script from disk. Every time a player swings a weapon, we find and execute the item's lua script. Every time a player casts a spell, we find and execute a lua script from disk.

It's pretty gross. It's something I'd like to push us to start remedying when our current projects calm down a little.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 26, 2020 at 12:16:23_

----

RE: IO Pressure
![image](https://user-images.githubusercontent.com/1389729/97171060-724ac200-1795-11eb-8e62-d090ce008503.png)

A zone is active when a player is in it. Other zones are asleep.

When a zone is active, every mob is calling DoRoamTick or or DoCombatTick, both of which do file reads. This is in addition to additional effects, spells, weaponskills, items, state events etc. All of which do file IO. I'd say that 2/3 of our performance costs come down to bashing the disk, the other 1/3 is pathfinding.

We're looking at both of these right now. 

Profiler support is being worked on in here:
https://github.com/project-topaz/topaz/pull/1432 
