**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:06_
_Originally opened as: project-topaz/topaz - Issue 146_

----

<a href="https://github.com/dwn134"><img src="https://avatars3.githubusercontent.com/u/17234748?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [dwn134](https://github.com/dwn134)**
_Sunday Nov 27, 2016 at 03:05 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3561_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30161103_1

**_Server Version_** (type `revision` in game) **:**
github/DarkstarProject/darkstar/commit/dec03e7567fe7d37016c44a9b5c2867ced2f8ffa

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
if you retreat a spirit and assualt it will begin again to cast another spell over and over again. Just seems to restart the timer to 0.
also I'm not sure if it should be casting immediately after being summoned I thought it had a cool down from 1st cast also.
and last thing is the Light Spirit doesnt cure, which would probably need some type of AI or HP checks to function correctly. I have had it cast haste on me once other than that it does banish dia and flash.

my server is currently down and i can get the ver and misc when its back up in an edit




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:07_

----

<a href="https://github.com/dwn134"><img src="https://avatars3.githubusercontent.com/u/17234748?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dwn134](https://github.com/dwn134)**
_Sunday Nov 27, 2016 at 14:53 GMT_

----

ver 30161103_1

revision dec03e7567fe7d37016c44a9b5c2867ced2f8ffa



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:08_

----

<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Monday Jan 28, 2019 at 23:53 GMT_

----

re: "I'm not sure if it should be casting immediately after being summoned I thought it had a cool down from 1st cast also."

There should be a forced delay before a spirit will start casting spells.  It is calculated by [this formula](https://ffxiclopedia.fandom.com/wiki/Thunder_Spirit):
```
Casting Time (in seconds) = 48 + (max Summoning Skill - current Summoning Skill) / 3
If Spirit is cast on corresponding day: -3 seconds
If Spirit is cast on weak day: +3 seconds
If Spirit is cast during corresponding weather: -2 seconds
If Spirit is cast during weak weather: +2 seconds
If using Summoner's Spats: -5 seconds
If using Astral Flow: -5 seconds
Light Spirit in healing mode or buffing mode: 1/2 Casting Time
```



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:10_

----

<a href="https://github.com/hargrave81"><img src="https://avatars1.githubusercontent.com/u/4106934?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [hargrave81](https://github.com/hargrave81)**
_Thursday Apr 18, 2019 at 11:17 GMT_

----

I'm rather new, but this is super OP.  Everyone just kills everything 15+ levels above them with spirits.  They cast spells on spawn/assault and appear to cast very often regardless of skill.  Something I did notice is when using spirits in certain zones, their rate of casting isn't so high.  I have not dug through the code on how this is performed yet, but just what I had noticed.  Fire spirit also I had noticed the highest spell cast rate.



----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Friday Mar 20, 2020 at 22:34:57_

----

to update, was using spirits on my test server and they currently do not cast any spells whatsoever, just attack. behavior should allow buffs at idle (if light spirit) and attacks as appropriate, while not at a constant rate. unsure if this should be a new issue entirely since functionality seemed to be available at one point. validated on another test server as broken.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Mar 21, 2020 at 03:43:20_

----

@59blargedy I've been seeing them function normally for a time, and then suddenly they stop casting even after being dismissed and re-summoned. They just seem to get stuck till the map server is restarted. Unsure what the trigger is. One of my players uses them rather heavily due to their tendency to open up right away with elemental nukes.
