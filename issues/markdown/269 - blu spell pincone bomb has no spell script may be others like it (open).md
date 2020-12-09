**Labels:**

feature

focus



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:05_
_Originally opened as: project-topaz/topaz - Issue 269_

----

<a href="https://github.com/ziaxe427"><img src="https://avatars1.githubusercontent.com/u/48656526?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [ziaxe427](https://github.com/ziaxe427)**
_Tuesday Mar 26, 2019 at 17:34 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5810_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**


- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
version 30190305_8

**_Source Branch_** (master/stable) **:** 
dont know what this is first time posting an issue lol

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
i did this on the dsp oldschool server where i am currently lvling blu wheneveri go to cast pinecone bomb at an enemy it cause ziaxe cannot cast or something like that.

also on a side note i cant confirm if this is a bug or an issue or not but sometimes blu spells do 0 dmg for no reason on  eenemys of any lvl and other times will do dmg. i cant confirm if this is an issue or an intended fature lol im new to this game so yea lol.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:06_

----

<a href="https://github.com/whasf"><img src="https://avatars3.githubusercontent.com/u/6373706?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [whasf](https://github.com/whasf)**
_Tuesday Mar 26, 2019 at 18:02 GMT_

----

A missing script isn't a bug, it's just not implemented.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:07_

----

<a href="https://github.com/zynjec"><img src="https://avatars3.githubusercontent.com/u/17911103?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zynjec](https://github.com/zynjec)**
_Thursday Mar 28, 2019 at 00:13 GMT_

----

Just because it's not implemented doesn't mean there can't be an issue, it's not exclusively for bugs.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:09_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Mar 28, 2019 at 00:30 GMT_

----

if I recall correctly nobody has tackled the prob of it trying to apply its damage after it applies the sleep effect without giving up partway into the attempt yet.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:10_

----

<a href="https://github.com/helixhamin"><img src="https://avatars1.githubusercontent.com/u/2202779?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [helixhamin](https://github.com/helixhamin)**
_Saturday Mar 30, 2019 at 16:06 GMT_

----

Can you just apply the damage then apply sleep after to get around that issue? 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:11_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Mar 30, 2019 at 20:24 GMT_

----

The issue of effects getting removed by the damage exists precisely because you don’t have that ability in scripts - the damage happens at the end. We need to refactor how these work to let you do that.

We had this is ws's too. Even if you have the dmg call then the effect call, the core processed the 2nd last.

