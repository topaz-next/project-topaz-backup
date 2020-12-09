**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:40_
_Originally opened as: project-topaz/topaz - Issue 214_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Wiggo32](https://github.com/Wiggo32)**
_Tuesday Feb 27, 2018 at 22:43 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4600_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30171223_0


**_Source Branch_** (master/stable) **:** fae4c89


**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
1. Go anywhere that there are different levels corresponding to separate maps for a zone.
    (I've found Phomiuna Aqueducts to be a good place to see what's happening here)
2. Use widescan to locate mobs and note that you can see mobs on different maps than the one you are currently on. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:42_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Feb 27, 2018 at 22:46 GMT_

----

I've been able to see mobs on diff map floors with widescan on retail so I don't think it checks which map I am on but I am pretty sure we should have a different vertical range limit instead of treating it as a sphere of the widescan value and that would be missing in DSP.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:43_

----

<a href="https://github.com/Rihyuh"><img src="https://avatars2.githubusercontent.com/u/24214123?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Rihyuh](https://github.com/Rihyuh)**
_Monday Mar 05, 2018 at 07:43 GMT_

----

That would be a mesh layer issue? Sorta like when skeletons would come up out of the ground if you fought cemetery cherry and blood aggro went off ^.^



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:44_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Mar 05, 2018 at 07:53 GMT_

----

no, unless someone wants to prove thats how retail does it (checking if there is a floor/cieling between you and every mob in the zone before deciding to show it on the widescan list or not  is highly unlikely).


we probably just need to limit the vertical range - right now your widescan is omnidirectional



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:45_

----

<a href="https://github.com/Rihyuh"><img src="https://avatars2.githubusercontent.com/u/24214123?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Rihyuh](https://github.com/Rihyuh)**
_Tuesday Mar 06, 2018 at 16:53 GMT_

----

Oh word. Didn't realize widescan acted like a sphere in the mechanics. I
had thought it was a distance circumference on a predetermined size based
on job, RNG and BST being larger, that used the mesh layers to separate
level breaks.
Be neat to have a program that would show the volume around the sprite.


On Mar 5, 2018 12:53 AM, "TeoTwawki" <notificationsgithub.com> wrote:

> no, unless someonewants to prove thats how retail does it (checking if
> there is a floor/cieling between you and every mob in the zone before
> deciding to show it on the widescan list or not is highly unlikely).
>
> we probably just need to limit the vertical range - right now your
> widescan is omnidirectional
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 4600Darkstar Issue issuecomment-370336618>,
> or mute the thread
> <github/notifications/unsubscribe-auth/AXF6a1U-bv3b_2fkUFs_jCvUFYdbth3uks5tbO8WgaJpZM4SVxV5>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:47_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Thursday Mar 22, 2018 at 00:37 GMT_

----

So, I've been running around Vanadiel for the past two weeks trying to find mobs that I can see on my map, that 'aren't on my map'... and I think I need a little guidance on where to look. So far the only mobs I can see on my map are the ones that are actually on my map according to where they are standing vs what map I would show if I stood in the same spot. I even went to oztroja in a spot where the maps change and had a yagudo oracle standing 5 yalms away from me and not be on my widescan map, although it's elemental was... =) The closest thing I could get to having mobs not be on my map was when I would see mobs which looked "off the map" because that part of the map is missing so it looked like the mobs were possibly on a different map but in all actuality were still on the map I was on. You can see an example of this at 1:55 on this vid: https://www.youtube.com/watch?v=b_NkFaKp_NE
So, other than that, I need some suggestions for where to look in order to find this widescan occurrence which gets me mobs from a different map on my widescan. 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:48_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Mar 22, 2018 at 00:56 GMT_

----

> So, other than that, I need some suggestions for where to look in order to find this widescan occurrence which gets me mobs from a different map on my widescan

palb. mines usually has floors and ceilings pretty close together in a lot of places. You know the places where if no navmesh, you can agro a turtle that comes down from the ceiling? see if on retail you can find that turtle on widescan. It'd look a lot like it was there with you on widescan but in the room you'd see no turtle because he's on the floor above. That room above you is aprox 5 yalms off I think. If you can't see any turtles on widescan that you can't see on screen outside of ws in that same general area I think that's a good indication something other than height is involved.

we can probably packet cap whats in the widescan list and compare to mob_spawn_points too.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:49_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Thursday Mar 22, 2018 at 01:05 GMT_

----

k, I'll take a run through palborough and capture everything



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:50_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Thursday Mar 22, 2018 at 23:28 GMT_

----

So, I'm convinced that widescan handles which mobs appear on your current map the same way that the map handles which party members appear on your current map. The entity is most likely flagged to be on a 'certain' map based on their position in the zone. And whatever procedure that entails to make sure you are viewing the correct map when you check your map (it has to tell you which map (1, 2, 3, etc.) to look at somehow) that should be the same procedure for every entity be it mob, player, or npc. Here's the video and captures for the ENTIRE Palborough Mines zone with special emphasis on the places where the maps change from one to the next. Never found a mob from a different map on my widescan in all of the two weeks since this issue was opened. Anyone have any other ideas? This is my best guess.
https://www.youtube.com/watch?v=pmvsVPfO3YQ&feature=youtu.be



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:51_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Mar 23, 2018 at 01:15 GMT_

----

well I'd say safe bet you ruled out a simple height check. I thought that was the most likely situation. truly baffling. I used to see NMs not on same floor as I was (I wasted many hrs of my life hunting NM on retail)

