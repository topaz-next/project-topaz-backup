**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:03:16_
_Originally opened as: project-topaz/topaz - Issue 278_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [isotor](https://github.com/isotor)**
_Tuesday Apr 16, 2019 at 12:35 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5855_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30190328_2


**_Source Branch_** (master/stable) **:** master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Excerpt from the relevant [wiki page](https://ffxiclopedia.fandom.com/wiki/Mazurka):

> - Mazurka effect immediately wears off if the player performs any sort of offensive action on an enemy, or if an enemy performs any sort of offensive action on the player. This is designed to inhibit the effectiveness of kiting tactics. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:03:17_

----

<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Tuesday Apr 16, 2019 at 12:44 GMT_

----

Does this also effect all mivement spells and abilities? Cor and dnc have thier own version



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:03:19_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [isotor](https://github.com/isotor)**
_Tuesday Apr 16, 2019 at 12:55 GMT_

----

Good point - yes this should also be the case also for [Chocobo Jig](https://ffxiclopedia.fandom.com/wiki/Chocobo_Jig) and [Bolter's Roll](https://ffxiclopedia.fandom.com/wiki/Bolter%27s_Roll). Unfortunately I built the server with the setting toggled off for anything post-Abby so can't check those right now - if nobody else can give this a quick look I'll rebuild and test in the next few days.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:03:20_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Apr 16, 2019 at 13:09 GMT_

----

its the diff between Flee-type effects and Quickening-type effects.
one stays, one doesn't.

Jig is quickening.

