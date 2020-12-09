**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:28_
_Originally opened as: project-topaz/topaz - Issue 262_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Feb 11, 2019 at 20:40 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5729_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
n/a

**_Source Branch_** (master/stable) **:** 
I AM THE **MASTER** /kungfumusic

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

"UpdateNMSpawnPoint: SQL error: No entries for mobid \<number here\> found."

~~17219886, Rampaging Ram~~
~~17211702, Maighdean Uaine~~
~~17220001, Bendigeit Vran~~
~~17309954, Despot~~
_thanks Wren._

~~All trigger that log error.~~ I'm sure there are more as well. These actually _should_  have multiple spawn pos, but  I also feel we could be handling this better than just assuming every NM has multiple pos entries in that sql table / auto calling this function in the global on every NM. These log messages aren't making anyone go capture retail pos and we can see which NM need pos data using a very simple SQL query.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:29_

----

<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Monday Feb 11, 2019 at 20:42 GMT_

----

There are alot that are coded with the original spawnpoint and have 1 nm spawn point. Both being the same pos



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:31_

----

<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Feb 12, 2019 at 20:17 GMT_

----

those are in there pretty much to avoid this exact message.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 15, 2020 at 18:27:06_

----

Thank you @wrenffxi 
