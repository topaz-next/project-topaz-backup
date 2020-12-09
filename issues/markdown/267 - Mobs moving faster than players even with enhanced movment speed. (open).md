**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:55_
_Originally opened as: project-topaz/topaz - Issue 267_

----

<a href="https://github.com/Snugglesffxi"><img src="https://avatars0.githubusercontent.com/u/19786824?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Snugglesffxi](https://github.com/Snugglesffxi)**
_Thursday Mar 21, 2019 at 13:30 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5802_

----

We thought this was a problem with the gravity spell but it turns out after a bunch of testing, both on the base master branch and another private server(SuperNova for reference), mobs are actually running a lot faster than players and when they appear to slow down behind you its just them capping their speed to match yours. This is both with enhanced player movement speed and without. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:56_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Mar 21, 2019 at 14:08 GMT_

----

Saw pretty much same thing in my own testing yesterday. One thing I know we have in common is we both used the move speed settings for both players and mobs. I think mob speed setting isn't functioning as originally intended. Retail saw a boost to the speed of all things by +10 (so our base of 40 is the old school speed, and 50 is the new retail).  At the time this happened DSP made the setting apply to mobs. This made people complain, so I went and split it into two settings. Looked to be working fine at the time. Doesn't seem to be working now.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:58_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Mar 21, 2019 at 14:08 GMT_

----

p.s. Snugglesffxi you missed using template



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:59_

----

<a href="https://github.com/zynjec"><img src="https://avatars3.githubusercontent.com/u/17911103?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zynjec](https://github.com/zynjec)**
_Thursday Mar 21, 2019 at 17:56 GMT_

----

There might be a couple things at play here.

- Every family has a speed column, it could be a family with an inaccurate value, or interacting poorly with custom mob speeds.

- For pathfinding (chasing players), `mob_speed_mod` is added to the final speed after all speed reductions are made, making speed reductions feel a whole lot less powerful.

eg: the video robber crab in the gravity issue has a family base of 40, with no speed modifiers a capped gravity reduces it to a movement speed of 29.6 (truncated to 29), then if you have `mob_speed_mod` set to a value of 20, that crab is now running at 49 instead of the probably expected 44, about 12% faster.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:00_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Mar 21, 2019 at 19:20 GMT_

----

so there is an order of things happening in play after all.

