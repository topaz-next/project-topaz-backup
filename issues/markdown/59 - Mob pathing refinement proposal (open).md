**Labels:**

improvement



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:54_
_Originally opened as: project-topaz/topaz - Issue 59_

----

<a href="https://github.com/OtianNgocnion"><img src="https://avatars2.githubusercontent.com/u/14980726?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [OtianNgocnion](https://github.com/OtianNgocnion)**
_Monday Nov 02, 2015 at 06:14 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2360_

----

In issue github/DarkstarProject/darkstar - Issue 1835 mobpathing was adjusted, and mobs no longer do the strange dance that they used to do. However, I have a proposal for some refinement. 

Currently, when the server wants to path a mob to its target, it does the following: choose a random point on the circle of radius r centered at the target point x and path to that point. This is done in the function PathAround, line 128 of pathfind.cpp. The random angle is drawn on line 133, and the lastPoint is on lines 135 and 136. 

It's easy to test that this is working as written by simply standing still, pulling a mob, and noticing that it will not path to you, but rather to a random point on that invisible circle of radius distanceFromPoint. 

This behavior is stable, in that it works pretty consistently, but the mobs settle down in a strange way, and still are a little jumpy. So, I propose a refinement:

Scrap the random point thing. Instead, generate a path whose endpoint is the target, and then, starting from the end of the path array, remove points that are within distFromPoint to the target. In english: find a path that goes straight to the target, and then stop before you go within distFromPoint.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:56_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Monday Nov 02, 2015 at 07:50 GMT_

----

Problem: every mob will now stack exactly on one another




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:57_

----

<a href="https://github.com/OtianNgocnion"><img src="https://avatars2.githubusercontent.com/u/14980726?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [OtianNgocnion](https://github.com/OtianNgocnion)**
_Monday Nov 02, 2015 at 08:28 GMT_

----

Good point. If they're coming from the same direction, they would stack. Hmmm.  So we need an implementation of: find a path that goes straight to the target, stop before you go within distfromPoint, and don't stand on your buddies. 

I'm just getting started digging into the code... Do the mobs have any collision or stacking avoidance already implemented? 

If not, I would suggest to identify the "ideal" point above, and then add jitter/noise to it within a smaller sector of the circle. In a sense, this would be the average of my suggestion and the current implementation: find a random point on the distFromPoint circle, but within, say, +/- pi/8 from the "ideal" point that I described in the initial post. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:58_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Monday Nov 02, 2015 at 15:10 GMT_

----

Exactly what kj said. The way it works on retail (from what I have seen) is the mob will run directly towards you, and stop once it's within attacking range. Mobs clumped up will automatically spread around you ever so slightly. I haven't taken the time to implement that because I think the system implemented is acceptable for now.

I feel like this is a low priority issue, is there a reason why you want this changed?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:59_

----

<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Monday Nov 02, 2015 at 15:20 GMT_

----

I will add that the mobs will stack ontop of each other if there is enough of them. I don't know if you guys ever did a cleave party jn abysssa but we'd often position ourselves in corners or against walls and drag the mobs backward along a wall until they stacked ontop of each other for an easy AoE weaponskill.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:00_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Monday Nov 02, 2015 at 15:31 GMT_

----

Yes, but that only happens because they can't move around you (the wall is
in the way)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:01_

----

<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Monday Nov 02, 2015 at 15:36 GMT_

----

However, I think that because when you pull a mob, they aren't already stacked. Their most direct path(on average) will not cause them to stack except only slightly with each other. Now, I get this might not be entirely retail but lord let me tell you, the way it is right now is SUPER annoying to play with. I'd rather see the mobs pseudo stack on pull than deal with Niddhogg's and other Wyrm's squirrelly asses when trying to pull them. Or adjusting Tiamat or Jorm after hate resets. No, it's not high priority but it is highly annoying. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:03_

----

<a href="https://github.com/OtianNgocnion"><img src="https://avatars2.githubusercontent.com/u/14980726?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [OtianNgocnion](https://github.com/OtianNgocnion)**
_Monday Nov 02, 2015 at 15:38 GMT_

----

Agreed  everything that has been said. This is why I was wondering about mob collision detection or stacking avoidance: in retail they _would_ all stack up, and then slowly drift apart like little point charges. 

What do you guys think of the directPoint +/- uniformRV[0,pi/8] thing from post 3? This would mellow the current behavior, without the stacking. (Or maybe pi/16... testing would be required of course. :D )




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:04_

----

<a href="https://github.com/OtianNgocnion"><img src="https://avatars2.githubusercontent.com/u/14980726?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [OtianNgocnion](https://github.com/OtianNgocnion)**
_Monday Nov 02, 2015 at 17:15 GMT_

----

[Just an addendum to say that it's being worked on, with teschnei's issue in mind. Thanks for your feedback!]




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:05_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Monday Nov 02, 2015 at 17:23 GMT_

----

My suggestion is that if time is being spent on it, it'd be to just make it
behave as retail. I don't think they already have collision detection, so
there'd have to be some way of checking that, hopefully with as little
iteration over mob lists as possible




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:06_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Monday Nov 02, 2015 at 19:02 GMT_

----

I'm really glad someone is looking into this, it's actually more annoying than you would think in day-to-day play.

Just like m241dan said it's a more serious problem for wyrms. It took me two full minutes to position Tiamat correctly last night (having to walk the whole time so he maybe doesn't draw us under the map again) Would it be possible to have wyrms path directly to target if the full fix doesn't happen?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:07_

----

<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Monday Nov 02, 2015 at 19:06 GMT_

----

Haha, right? Props to you man, I just shut his draw-in off because sometimes if someone pulled hate it would draw everyone in under ground and then you're basically fubared.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:08_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Monday Nov 02, 2015 at 20:17 GMT_

----

Ok I'll make it match retail




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:09_

----

<a href="https://github.com/OtianNgocnion"><img src="https://avatars2.githubusercontent.com/u/14980726?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [OtianNgocnion](https://github.com/OtianNgocnion)**
_Monday Nov 02, 2015 at 20:42 GMT_

----

Already on it, bendangelo :+1: and happy to make some contributions. Thanks for the comments though.


