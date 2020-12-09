**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:11_
_Originally opened as: project-topaz/topaz - Issue 98_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Hozu](https://github.com/Hozu)**
_Monday Feb 29, 2016 at 16:46 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2837_

----

Client Version (type /ver in game) :
30160203_0

Server Version (type revision in game) :
14a1e3d

Source Branch (master/stable) :
master

Additional Information (Steps to reproduce/Expected behavior) :
Stairs in various zones (Dynamis - Bastok (AH), Dynamis - Xarcabard (the structures the NMs are on), and The Eldieme Necropolis (the areas next to the plates that toggle the doors). Before line of sight was implemented, mobs had an extremely difficult, if not impossible time pathing up/down the stairs, but with line of sight it's impossible to pull the mobs without going up to them.

Another issue is the bushes that players can traverse through in Caedarva Mire by where Khimaira spawns (and presumably the similar ones in Wajaom Woodlands in the southern part of the main map) - there was an imp that someone managed to get pulled into there and it could not be attacked, nor would it aggro even when I was inside the mob's model.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:12_

----

<a href="https://github.com/Fiocitrine"><img src="https://avatars1.githubusercontent.com/u/7704601?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Fiocitrine](https://github.com/Fiocitrine)**
_Monday Feb 29, 2016 at 17:36 GMT_

----

Also, Castle O where the okote NM spawns. If you aggro a mob and it goes under the bridge it'll just move back and forth underneath the bridge. Doing this, it will not be able to attack you but still be in an aggro state.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:13_

----

<a href="https://github.com/aizenmyou"><img src="https://avatars3.githubusercontent.com/u/4256716?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [aizenmyou](https://github.com/aizenmyou)**
_Monday Feb 29, 2016 at 19:49 GMT_

----

I also experienced similar on the same server Hozu is on. In Ro'Maeve if you stand on the edge of the fountain (Not the part up the stairs but the actual light gray edge as it meets the dark gray of the normal floor) I could not use ranged attack as RNG (Got yellow system message)

I've also see this with the small rocks you can walk over in the same zone when being behind them.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:14_

----

<a href="https://github.com/gedads"><img src="https://avatars1.githubusercontent.com/u/5845173?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [gedads](https://github.com/gedads)**
_Monday Feb 29, 2016 at 23:29 GMT_

----

"but with line of sight it's impossible to pull the mobs without going up to them."
Maybe removing the stairs a add a plane surface instead could help, stairs often have some areas left aside in recast (like that http://imgur.com/4zbounx , but without removing the stairs, just covering them, in the pic the slope isn't matching the stairs) but it would take a lot of time except if anyone know a good way to add those quickly.
same trick could be used to prevent mobs crossing bushes by adding a vertical wall (got that problem with reisenjima and bamboos, i was thinking about adding fake walls)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:16_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Mar 01, 2016 at 00:15 GMT_

----

What do stairs look like now? Small walls for each riser? If so, what would be the implications of ignoring really short walls?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:17_

----

<a href="https://github.com/gedads"><img src="https://avatars1.githubusercontent.com/u/5845173?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [gedads](https://github.com/gedads)**
_Tuesday Mar 01, 2016 at 00:28 GMT_

----

for caedarva mire, the imps went through the bush on my server in the path to khimaira but it can be stuck i think (but i 'm able to attack and be attacked).if needed they 're easy to remove, but i don't remember if the bush was left to prevent mobs going there or if it was just forgotten. (http://imgur.com/3aaSxKe).
actually the stairs are like that: http://imgur.com/NI3p6Vu

there's a way to get all the stairs as walkable area in recast but it would need other settings in recast and probably an increased size




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:18_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Mar 01, 2016 at 01:38 GMT_

----

Yeah I got the imps to go through the bush, but when they were in it after deaggroing, they wouldn't aggro to anyone and they couldn't be acted on (other than by melee).

And yeah, that's how I imagined the stairs looked.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:20_

----

<a href="https://github.com/gedads"><img src="https://avatars1.githubusercontent.com/u/5845173?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [gedads](https://github.com/gedads)**
_Tuesday Mar 01, 2016 at 12:00 GMT_

----

http://imgur.com/UeDXMnI there's something that need testing but after applying general settings, you can undo a tile and change settings and redo that tile only. it might be enough for stairs to be more accurate also it can work for small parts of the map where a mob can be stuck by a small edge etc.
I don't know if those mixed settings can work and also what's the maximum size for a navmesh. I'll try to ask lautan next time he's up.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:22_

----

<a href="https://github.com/dazusu"><img src="https://avatars0.githubusercontent.com/u/7009763?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dazusu](https://github.com/dazusu)**
_Tuesday Mar 01, 2016 at 17:12 GMT_

----

teschnei This seems to be happening in a lot of places; including very minimal inclines - for example, 0.25yalms height difference in La Theine; unable to Provoke a crab less than 5 yalms away. Could be a good thing to temporarily disable the code doing the line of sight checks; or add a toggle to easily enable/disable until there's an opportunity in the future to refine it?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:23_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Mar 01, 2016 at 17:16 GMT_

----

You can turn it off yourself.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:24_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Mar 01, 2016 at 17:22 GMT_

----

There are two main issues that I can think of with line of sight.
One, the raycast is from position_t to position_t, but the position_t represents where your feet are.  Thus if there is a small incline between you and your target, the ray may pass through the floor to get from your feet to your targets feet.  Simple solution, doing a raycast from an offset y position.
Two, the y position for mobs does not change as they move along inclines - the client just auto corrects the placement of their model.  So if a mob moves along an incline, their y position as reported by the server can be pretty different from what the client corrects it to - meaning the raycast can still be going through the floor.  This one's a bit harder to fix, it means clamping their y position to the navmesh plane they are moving along.  It may actually end up being easy to do, but I've never looked into the navmesh code before.

Either way, I can probably look into them this week when I have time.  The first one should be a quick fix




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:27_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Mar 01, 2016 at 17:22 GMT_

----

this is all not including the possibility that the navmeshes are not perfectly in sync with the game world (as Hozu was seeing earlier)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:28_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Mar 01, 2016 at 18:36 GMT_

----

Clamping mob Y pos to the navmesh plane would fix being drawn into the ground as well, as you mentioned before.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:30_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Mar 01, 2016 at 19:11 GMT_

----

Yep, I forgot to mention that (though I was thinking it)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:31_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Mar 02, 2016 at 00:22 GMT_

----

Looks like the y pos clamping is already implemented.  Offset LOS I just implemented, so that's the y-value problems solved.


