**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:44_
_Originally opened as: project-topaz/topaz - Issue 21_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 04, 2015 at 04:05 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 1510_

----

I believe this is because the server message length calc is wrong. At least I recall discussions where that was said to be the reason.

As a result, you get garbage at your line ends like `test` being displayed in game as `testg` or the occasional Japanese yen symbol in place of whatever your last character was.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:45_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 16, 2015 at 21:20 GMT_

----

Related: if your servermessage conf file is empty, the server will crash here github/DarkstarProject/darkstar/blob/a567cf469f7bbf1f34b4327228da582e9c4b45e4/src/map/lua/luautils.cppDarkstar Issue L4236 trying to read the non-message.


