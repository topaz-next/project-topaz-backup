**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:03_
_Originally opened as: project-topaz/topaz - Issue 33_

----

<a href="https://github.com/xipies"><img src="https://avatars3.githubusercontent.com/u/7948457?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [xipies](https://github.com/xipies)**
_Thursday Jul 23, 2015 at 03:18 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 1782_

----

At least for An Empty Vessel.

Revision: e9658f2
Server: Classic




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:04_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday Jul 23, 2015 at 05:00 GMT_

----

IIRC this is the case in retail. It's the case for the Bibiki Seashell quest at least. http://ffxiclopedia.wikia.com/wiki/Got_It_All




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:05_

----

<a href="https://github.com/xipies"><img src="https://avatars3.githubusercontent.com/u/7948457?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [xipies](https://github.com/xipies)**
_Thursday Jul 23, 2015 at 05:17 GMT_

----

Ah, OK. I wonder if it was different at one point in time (not necessarily this quest, but zoning behavior for quests in general). Still a question about zoning into MH, though.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:06_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 23, 2015 at 05:58 GMT_

----

Its quest dependent, some will make you actually zone and a logout isn't enough, and others just logout will do the deed. In DSP there is a specific function intended to check if its a real zone change. `needToZone()`




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:07_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday Jul 23, 2015 at 17:33 GMT_

----

I believe zoning into a mog house on retail doesn't count. They seem to be considered the same zone, ie. zoning from Whitegate to Whitegate when you enter your Mog House.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:08_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 23, 2015 at 20:09 GMT_

----

I was mainly looking at the shutting down part, without noticing the mog house part. My bad.

But yeah mog house in retail doesn't have a real zone to itself and people in mog will even show on search as being in the zone they entered from

**I think** it **may** count as an "area change" for a few things (usually NOT for cs's that requires a zone change, those will snub the mog pretty much very time). Its fairly safe to assume that going in/out of mog house will not trip whatever thing you need tripped, because that is the majority situation.

As for shutdown vs actually zoning for non mog house areas I think SE used 2 diff checks in yet another example of "new programmer didn't know how last programmer already handled this".




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:10_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Jul 23, 2015 at 20:27 GMT_

----

and we do already have support for both of these situations: needToZone() (doesn't count logging in/out nor mog house) and the use of a localVar on the player character (will include logging out/mog house)


