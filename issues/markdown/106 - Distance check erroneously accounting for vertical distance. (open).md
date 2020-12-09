**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:00_
_Originally opened as: project-topaz/topaz - Issue 106_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Hozu](https://github.com/Hozu)**
_Sunday Mar 13, 2016 at 05:18 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2904_

----

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

Client Version (type /ver in game) :
30160203_0

Server Version (type revision in game) :
2643851

Source Branch (master/stable) :
master

Additional Information (Steps to reproduce/Expected behavior) :
The client-side distance check for using a spell/ability can show as you bring in range but the server doesn't allow it. On level ground, the client-side check works exactly, but when you take vertical distance into account, you end up having a shorter range than the client says.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:02_

----

<a href="https://github.com/dazusu"><img src="https://avatars0.githubusercontent.com/u/7009763?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dazusu](https://github.com/dazusu)**
_Sunday Mar 13, 2016 at 09:07 GMT_

----

Pretty sure this is a Navmesh issue that still exists, unless you're getting the out of range message specifically?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:03_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Sunday Mar 13, 2016 at 16:46 GMT_

----

This has been a problem since before navmeshes were even a thing, actually. But since server-side range checks weren't a thing until recently, it was going by the 21.4 distance thing instead of the proper range. It still used a vertical check because we'd have to go closer to be able to cast.

Also, the distance plugin for both Windower and Ashita only track horizontal distance - I'm fairly certain it would account for vertical distance too if it was required.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:04_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Sunday Mar 13, 2016 at 21:27 GMT_

----

I believe vertical distance is supposed to factor in.

I've always wanted a version of distance that accounted for the vertical, but no one has ever made one.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:05_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Sunday Mar 13, 2016 at 22:21 GMT_

----

Well if the client outright tells you that vertical distance does not count, then it most likely doesn't count. Would be nice to get retail verification though. Check sloped areas to see.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:06_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Mar 20, 2016 at 00:27 GMT_

----

On the retail game my vertical reach is crazy but does eventually stop, though I am uncertain of the exact thing stopping me.Like a dragoon on that cliff near spiny spipi in saruta and jump a mob at the bottom, where if the same distance were laid out between it and the target horizontally the client would say its out of reach. (you will prolly need 2 chars to recreate this because of mob positioning)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:07_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Sunday Mar 20, 2016 at 03:04 GMT_

----

I'm guessing vertical distance caps at 30 yalms or something stupid.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:09_

----

<a href="https://github.com/xipies"><img src="https://avatars3.githubusercontent.com/u/7948457?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [xipies](https://github.com/xipies)**
_Tuesday Jul 12, 2016 at 15:12 GMT_

----

30 yalms would make sense. IIRC, when there was the (DSP) bug of spell ranges not checking correctly, spells were still getting hard capped by client at 30. I wouldn't be surprised if vertical range had the same hard cap.


