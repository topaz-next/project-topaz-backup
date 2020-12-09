**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:43_
_Originally opened as: project-topaz/topaz - Issue 297_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday May 28, 2019 at 18:47 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6036_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
n/a

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Type `!where` in game, which relies on `showPosition()`

Observe values always `-1`

Some folks mention this is "still" broken, despite never having reported it in the first place. So I'm reporting it myself now.

![image](https://user-images.githubusercontent.com/6871475/58503981-b2001b00-8157-11e9-8dae-93ef82ca6121.png)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:44_

----

<a href="https://github.com/zynjec"><img src="https://avatars3.githubusercontent.com/u/17911103?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zynjec](https://github.com/zynjec)**
_Tuesday May 28, 2019 at 19:48 GMT_

----

I can't actually reproduce on master, despite the fact it definitely should be wrong/failing. 

![image](https://user-images.githubusercontent.com/17911103/58507583-0c04de80-8160-11e9-826e-dc750d9d23fc.png)

The positions of the player (which are floats) are being cast to an unsigned integer rather than signed.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:46_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday May 28, 2019 at 22:17 GMT_

----

possibly related to where I was at when I reproduced it?




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday May 15, 2020 at 00:24:58_

----

This was fixed in 96f6ca16cb6d557cd257a684de1340ce7aadda9b and can be closed


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Jul 14, 2020 at 02:22:05_

----

Yep, looks signed.
