**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:51_
_Originally opened as: project-topaz/topaz - Issue 114_

----

<a href="https://github.com/helixhamin"><img src="https://avatars1.githubusercontent.com/u/2202779?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [helixhamin](https://github.com/helixhamin)**
_Sunday Apr 10, 2016 at 12:00 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3018_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30160329_0

**_Server Version_** (type `revision` in game) **:**
github/DarkstarProject/darkstar/commit/aa2124945c3b872e0888d5296ba783f1b58e4f3b

**_Source Branch_** (master/stable) **:**
Master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
Mission 6-1, after accepting from gate guard, Halver is not setting the MissionStatus variable to 1, which means the mission will not progress.

The current code links are:
`
elseif (currentMission == LEAUTE_S_LAST_WISHES and MissionStatus == 0) then
            player:startEvent(25);
`

Then event 25 is:
`elseif (csid == 25) then
        player:setVar("MissionStatus",1);`

The odd part is, I get the proper dialog, but the MissionStatus variable is not being set. At first I thought it was because it was looking for the MissionStatus variable to be set to 0, but...I am not sure.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:52_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Apr 18, 2016 at 00:09 GMT_

----

I see this happen to people randomly if they have multiple characters connected from the same external IP.

Keyitems too. They get whatever cs/dialog they were supposed to and there are no errors in log, but they are missing a variable change or a keyitem they were supposed to receive that the onEventFinish should have applied.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:53_

----

<a href="https://github.com/helixhamin"><img src="https://avatars1.githubusercontent.com/u/2202779?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [helixhamin](https://github.com/helixhamin)**
_Monday Apr 18, 2016 at 02:09 GMT_

----

Yeah, I had to just gm in the variable, and I was x3 boxing, so...
Still, what happens if you have two people playing from the same internal network? Would this still happen? I mean, dual/trio boxing is one thing, but what about those that may just be on the same network but different computers?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:55_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Apr 18, 2016 at 02:23 GMT_

----

Yes, still happens. My nephew plays from same connection as me, we get this all the time.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:56_

----

<a href="https://github.com/abriasffxi"><img src="https://avatars1.githubusercontent.com/u/20671885?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [abriasffxi](https://github.com/abriasffxi)**
_Friday Aug 12, 2016 at 06:11 GMT_

----

I have had it happen about 15 times on various missions in the last 3 weeks.  Theres 6 of us that went from rank 1-6 so maybe 60 cutscenes each?   Nobody is dual boxing or on the same external IP.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:57_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 12, 2016 at 13:43 GMT_

----

I will do some digging either late tonight or tomorrow morning, gotta be some optional bit or some sequence breaking to cause it since most players have gotten by this without getting that error.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:58_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 12, 2016 at 13:43 GMT_

----

> various missions

gotta be more specific for me to look into though...




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:59_

----

<a href="https://github.com/abriasffxi"><img src="https://avatars1.githubusercontent.com/u/20671885?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [abriasffxi](https://github.com/abriasffxi)**
_Monday Aug 15, 2016 at 04:28 GMT_

----

Sorry was away for the weekend.  One was Sandy 3-1, Infiltrate Davoi.  Zoning in to Davoi, the cutscene showed for two people, but the NPC near the bridge wouldn't talk to them.  I had to delmission them, and start over.  On the second time, one of them had the same issue in the same spot, but he logged out all the way to desktop, logged back in, and the NPC talked to him and everything worked from there.

It also happened a few times during 3-3 when we tried to talk to the King someone had a problem, and when returning to the ambassador in Re'Lude a different person didn't get the cutscene.  We fixed both by logging out to desktop since we kinda figured out that solved it the first time.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:00_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 15, 2016 at 20:02 GMT_

----

Theres about zero chance that there was a script bug if it suddenly worked without us changing the script.


