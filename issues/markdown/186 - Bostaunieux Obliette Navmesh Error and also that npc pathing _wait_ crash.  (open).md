**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:45_
_Originally opened as: project-topaz/topaz - Issue 186_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Wiggo32](https://github.com/Wiggo32)**
_Friday Aug 25, 2017 at 01:40 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4017_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**30170728_2


**_Server Version_** (type `!revision` in game) **:**unknown


**_Source Branch_** (master/stable) **:**master


**_Additional Information_** (Steps to reproduce/Expected behavior) **:**When zoning into Bostaunieux Obliette the Server throws a seemingly endless loop of errors: 

CNavMesh::findPath Couldn't find path <0.000000, 0.000000, 0.000000>-><101.293579, -0.118097, -37.808445> <167>
CPathFind::FindPath Entity <17461410> could not find path

![bostaunieux - navmesh error](https://user-images.githubusercontent.com/30469395/29696003-8f2dc348-890b-11e7-9d4d-f24b9e3d29a6.jpg)

After about 5 min of running around and clicking on NPCs the server crashed. I don't know if it's related. The errors stop when zoning out of Bostaunieux Obliette.






----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:46_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 25, 2017 at 03:42 GMT_

----

Wait awhile and you'll see those errors in ***all*** zones. This is a longstanding annoyance that isn't getting fixed anytime soon, which was why I went and created a filter for those:
github/DarkstarProject/darkstar/blob/master/conf/map_darkstar.confDarkstar Issue L33

Add 1024 to your `console_silent` setting and no more spam from mob that can't find its next path node.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:48_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Friday Aug 25, 2017 at 04:01 GMT_

----

Oh, and I think I might have figured out what the crash was from. Because it happened after disabling navmesh for that area. I clicked on Novalmauge too many times too quickly. I'm suspecting an issue with the wait function? I'm not sure yet though.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:49_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 25, 2017 at 04:09 GMT_

----

That's not really a navmesh problem, but yes its the wait function. The code for his pathing doesn't use mesh to fidn his next pos, its just scripted "you go here! then here! Oh wait a player clicked on you so stop"

Except that last part is kinda splodey. Happens with those 2 dudes in west Ronfuare too. And the kid in south sandy.

