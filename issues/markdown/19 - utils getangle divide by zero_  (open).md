**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:23_
_Originally opened as: project-topaz/topaz - Issue 19_

----

<a href="https://github.com/Jupiter065"><img src="https://avatars3.githubusercontent.com/u/7451641?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Jupiter065](https://github.com/Jupiter065)**
_Monday May 25, 2015 at 22:51 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 1477_

----

github/DarkstarProject/darkstar/blob/ad5385f30df4e8cc903b756c8ade392fd2b5e850/src/common/utils.cppDarkstar Issue L139
When I was working on Closed Position I considered using the IsFaceing function, but ended up just comparing the attacker and defender rotation. But I did notice that the getAngle function it uses seems like it would cause divide-by-zero exceptions whenever the two entities have the same x-coordinates. Is there some check for that that I'm missing somewhere? That function gets called a lot.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:23_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday May 27, 2015 at 05:55 GMT_

----

seems likely, though i've never heard or seen of it happening anywhere before.  put a test case together to make sure




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:24_

----

<a href="https://github.com/z16"><img src="https://avatars2.githubusercontent.com/u/1635608?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [z16](https://github.com/z16)**
_Wednesday May 27, 2015 at 06:38 GMT_

----

There is no "divide by zero" exception for floating point numbers. if the y and x axes are the same, the final value would result in 0 (since `0.0f/0.0f` is `Not a number`), if only the x axes are the same it would result in 192 (since `x/0.0f` is `Infinity` if `x` is not `0.0f`). Whether or not those numbers make sense is debatable, but it won't crash at least.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:26_

----

<a href="https://github.com/Jupiter065"><img src="https://avatars3.githubusercontent.com/u/7451641?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Jupiter065](https://github.com/Jupiter065)**
_Wednesday May 27, 2015 at 15:30 GMT_

----

Ah, right, I forgot about +INF and -INF. I think atanf returns NaN if NaN is the parameter (http://en.cppreference.com/w/c/numeric/math/atan). I'll see if I can test how the game would react to that.


