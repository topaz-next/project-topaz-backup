**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:17_
_Originally opened as: project-topaz/topaz - Issue 148_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Dec 26, 2016 at 00:07 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3600_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30161206_3 (yeah I'm newer than the server...but people on 30161103_1 saw this too)

**_Server Version_** (type `revision` in game) **:**
eb97e4f9b8a53c7a0c6532125c6da0b6a96485a3

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
~~In addition to Darkstar Issue 866 his AI now never engages, doesn't become claimed, and doesn't fight back. But will still counter. And~~ his pathing halts shortly after spawning. I fixed the missing require with eb97e4f9b8a53c7a0c6532125c6da0b6a96485a3 but this still happens. He just freezes solid.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:19_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Dec 26, 2016 at 00:18 GMT_

----

Looks like the pathing probs are just bad positioning smacking him into navmesh, giving him new pos's in his path table fixes that part. ~~His failure to claim or fight back is a separate problem though.~~



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:20_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Monday Dec 26, 2016 at 17:08 GMT_

----

is he set to link with local cactaurs? That is supposed to be the only way to aggro him



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:21_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Dec 26, 2016 at 20:56 GMT_

----

I'm aware of how he works on retail. ~~He runs around so fast he's next to impossible to hit with anything and even if you macro land a provoke he'll fly off and declaim. But he **does** claim and he certainly doesn't stand there letting you beat on him like a Piñata..~~

~~On retail after he links to a sabotender you still have to actually claim him..~~

~~`ROAMFLAG_IGNORE  = 0x200, // ignore all hate, except linking hate`
No such thing as "linking hate". This was implemented all wrong by taking peoples comments on the internet literally instead of someone actually observing it on retail.~~

~~clarification for anyone comes along still confused: he should auto de-claim and disengage himself, not be unclaimable.~~



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:22_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Dec 26, 2016 at 21:44 GMT_

----

Fuggit, I can't get it to happen on camera to prove how it works. If we fix the pathing he's "good enough". _Assuming he starts noticing the sabotender fighting next to him once he's moving again._

