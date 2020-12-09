**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:10_
_Originally opened as: project-topaz/topaz - Issue 130_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Deadwing888](https://github.com/Deadwing888)**
_Monday Aug 29, 2016 at 01:21 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3336_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **30160728_0**

**_Server Version_** (type `revision` in game) **f8175463415d4964d3deb2492d73a1bd03b548c6**

**_Source Branch_** (master/stable) **master**

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**

Issue 1) The spell meteor is not currently reducing damage for multiple targets hit as it would in retail. This functions correctly for most other AOE spells.

Issue 2) Currently the spell's 30' damage radius is being considered as a sphere. It needs to in fact be considered as a ~8' cylinder with radius 30'. Important because certain fight tactics change dramatically when vertical height can be used to block meteor. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:11_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Monday Aug 29, 2016 at 04:06 GMT_

----

I'm 99% sure that issue 2 is a thing for literally every AoE on Darkstar, unfortunately.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:12_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Monday Aug 29, 2016 at 04:08 GMT_

----

See: github/DarkstarProject/darkstar - Issue 2904




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:14_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Monday Aug 29, 2016 at 04:35 GMT_

----

I believe the issues are similar but not exactly the same. For a normal instance of a mob casting on a player the AOE range is so tight it would be difficult to discern the distance between sphere and cylinder.

For a wide aoe such as Meteor the issue becomes much more noticeable.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:15_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Wednesday Oct 12, 2016 at 05:54 GMT_

----

I believe the following line:
github/DarkstarProject/darkstar/blob/master/src/map/ai/helpers/targetfind.cppDarkstar Issue L411

Should read:
    return distance(*m_PRadiusAround, *pos) <= m_radius && abs(m_PRadiusAround->y - pos->y) < 6;

to fix the AOE height check problem


