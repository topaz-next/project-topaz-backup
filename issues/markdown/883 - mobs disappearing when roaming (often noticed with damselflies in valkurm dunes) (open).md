**Labels:**



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Friday Jul 24, 2020 at 06:19:58_
_Originally opened as: project-topaz/topaz - Issue 883_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

For many years, people camping Valkurm Emperor have noticed damselflies disappearing from the dunes, seemingly at random.  I noticed the same behavior with birds in Battalia, and several other mobs in various zones.

I looked into this years ago on DSP and discovered it was caused by mobs' roaming code -- only with navmesh enabled -- making them roam beyond their [roam_home_radius](https://github.com/project-topaz/topaz/blob/release/src/map/entities/mobentity.h#L267).  When they roam [beyond this radius](https://github.com/project-topaz/topaz/blob/release/src/map/entities/mobentity.cpp#L259), they  [disappear](https://github.com/project-topaz/topaz/blob/release/src/map/ai/controllers/mob_controller.cpp#L765).

This is definitely why they disappear, but I couldn't at that time see anything obvious that would cause them roam that far.  So I just bumped up roam_home_radius from 60 to 120 on our server, which "fixed" the problem, and forgot about it.

However, this still happens on Topaz today, and I believe the problem lies somewhere in this pathfinding code.  I'll link to noteworthy sections of code:

* A damselfly will be set up with MOBMOD_ROAM_DISTANCE of 10 and MOBMOD_ROAM_TURNS of 1 [here](https://github.com/project-topaz/topaz/blob/release/src/map/utils/mobutils.cpp#L698-L716).  I've verified these values in-game:
![image](https://user-images.githubusercontent.com/21246949/88364348-9212ba00-cd50-11ea-8a0e-d89e52a7dd41.png)

* When mobs roam with navmeshes on, they're asked to find a path [here](https://github.com/project-topaz/topaz/blob/release/src/map/ai/helpers/pathfind.cpp#L47-L50).  Their spawn point, roam radius, and roam turns are handed off to this FindRandomPath function.

* FindRandomPath seems to [plot a series of points](https://github.com/project-topaz/topaz/blob/8648c4071c1885ad1a388d74e7f868e39df2f75e/src/map/ai/helpers/pathfind.cpp#L348-L376), starting at their spawn point, and then picking a series of nearby points for each turn, each time starting at the last point picked.

Now, for members of the beastman ecoSystem -- who have [MOBMOD_ROAM_DISTANCE of 20 rather than 10, and MOBMOD_ROAM_TURNS of 5 instead of 1](https://github.com/project-topaz/topaz/blob/release/src/map/utils/mobutils.cpp#L703-L708) -- I can imagine that if you happen to pick points in the same direction, say north, each time from the previous point, this might cause them to roam pretty far.  Remember that only the first plotted point is picked from home+radius.  All subsequent points are picked from last point+radius.  So a chain of points all in the same direction could stretch out, theoretically, 100' north.  This assumes that findRandomPosition is doing what I initially thought: picking a point somewhere in a circle of radius ROAM_DISTANCE from the last point.

However, consider two points.

1. Damselflies only have ROAM_TURNS of 1 and DISTANCE of 10.  So even if you chained FIVE roam turns -- four more than they have -- due north, they still wouldn't roam outside the 60' radius.

2. More importantly, it looks like the value being [passed into this function as `radius`](https://github.com/project-topaz/topaz/blob/8648c4071c1885ad1a388d74e7f868e39df2f75e/src/map/ai/controllers/mob_controller.cpp#L799) is not ROAM_DISTANCE.  It's [ROAM_DISTANCE / 10](https://github.com/project-topaz/topaz/blob/08fcc59f5fc1a5a929037ca24b13ce9cec8f287f/src/map/entities/mobentity.cpp#L462-L465).

This blows up the whole "chained roams put them outside the 60' threshold" theory.  I think the flaw, therefore, is my assumption that findRandomPosition is picking points from within `maxRadius` of `startPosition`.  The code in [this function](https://github.com/project-topaz/topaz/blob/8648c4071c1885ad1a388d74e7f868e39df2f75e/src/map/navmesh.cpp#L298) baffles me -- it's navmesh and polygons and totally Greek to me -- but as I cannot see any other code-based reason for mobs wandering so far, I must assume it's something in this function.  Perhaps the terrain polygons in these particular areas where mobs disappear are large, and that's causing these calculations to pick points more than 60' from the starting points, even given a small radius?






----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 24, 2020 at 11:27:43_

----

do you happen to notice the log getting hit with navmesh errors during this? 


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Friday Jul 24, 2020 at 17:01:40_

----

This has the strange side effect that Valkurm Emperor will pop by itself because one of its PH roamed too far and depoped :-)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 24, 2020 at 18:32:31_

----

> This has the strange side effect that Valkurm Emperor will pop by itself because one of its PH roamed too far and depoped :-)

This is expected - the code to check if the NM is "ready" is in the mobs despawn script. the problem is they despawn when they should not be.

On retail you could, in theory, get VE to pop by repeatably depopping his placeholder. I forget which NM I tested this with, but its  a real thing.
