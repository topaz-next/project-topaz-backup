**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:16_
_Originally opened as: project-topaz/topaz - Issue 139_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Sep 26, 2016 at 01:22 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3393_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30160831-1

**_Server Version_** (type `revision` in game) **:**
58fb230362ebdc9b6836bfa84ad9e00cf80e517a

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
If you stun a mob in time to prevent its mobskill, it still attempts to animate. And does the wrong animation. May possibly crash the client if it also dies during this small time frame of screwed up animation. Replicated on Exorays, Doom scorpions, and Crawler Hunters in Crawler's Nest. Only tested it with Black magic stun, was told by others that any stun will do it quite possibly sleep/terror/etc as well.

Edit: this was mentioned in Darkstar Issue 1618 and I didn't notice till after posting. Different effect than that issue describes but a comment by Ben inside it says the packet is broken.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:17_

----

<a href="https://github.com/abriasffxi"><img src="https://avatars1.githubusercontent.com/u/20671885?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [abriasffxi](https://github.com/abriasffxi)**
_Monday Sep 26, 2016 at 23:47 GMT_

----

Something worth noting is that sometimes the animation of the mob will stop correctly, but the animation of the stun does not go off.  Seems to be about 20% of the time in my estimate, with the rest of the time behavior as TT describes.

Also, the client can crash when you are doing an animation on a mob (weaponskill or cast or anything) and the mob dies.  Not sure if it's related.  Seems to be about 1%.

And I can confirm that any stun does that I've tested so far, and sleep.

AND, when they die it can also sometimes happen (not to be mistake with rabbits, which seem to do it 100% of the time).




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:18_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 27, 2016 at 01:11 GMT_

----

The exact results are timing related, which makes it looks kind of random at first to people trying to reproduce it.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:20_

----

<a href="https://github.com/ZariusCane"><img src="https://avatars2.githubusercontent.com/u/16099481?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ZariusCane](https://github.com/ZariusCane)**
_Wednesday Oct 05, 2016 at 11:35 GMT_

----

if you're too far out of range while mob is trying to use a tp move will also cause it to happen on fights you would kite something.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:21_

----

<a href="https://github.com/abriasffxi"><img src="https://avatars1.githubusercontent.com/u/20671885?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [abriasffxi](https://github.com/abriasffxi)**
_Thursday Oct 13, 2016 at 19:14 GMT_

----

Suggest using summoner pets (interrupted physical attack by mob death) when testing/replicating.  Happens nearly 100%.




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Nov 03, 2020 at 12:36:05_

----

#1472
