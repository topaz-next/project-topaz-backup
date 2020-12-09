**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:02_
_Originally opened as: project-topaz/topaz - Issue 136_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Deadwing888](https://github.com/Deadwing888)**
_Wednesday Sep 14, 2016 at 16:53 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3367_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **not a client issue**

**_Server Version_** (type `revision` in game) **f8175463415d4964d3deb2492d73a1bd03b548c6**

**_Source Branch_** (master/stable) **master**

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**

On retail souleater will bypass mob's physical damage resistance. The phys- will only be applied to the base damage the strike would have done, with the souleater damage getting added on top.

Currently on darkstar MOD_DMGPHYS will cut the damage of the melee hit after souleater is factored in, sending a souleater hit from 200 to 100.

I believe this also applies to MOD_UDMGPHYS although I do not understand the difference between the two mods.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:03_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Wednesday Sep 14, 2016 at 19:35 GMT_

----

`MOD_UDMGPHYS` is uncapped, `MOD_DMGPHYS` is capped at 50%.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:04_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Wednesday Sep 14, 2016 at 21:08 GMT_

----

Thank you bendangelo 

Any chance you could pop on IRC and chat with me a bit on how to address this issue in core?
I've been all through battleutils and attack.cpp and just can't figure out what's going on.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:05_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Wednesday Sep 14, 2016 at 21:42 GMT_

----

Okay so I was able to solve this issue on my core by removing the souleater function in attack.cpp then adding a function call of doSoulEaterEffect underneath the shield block section of TakePhysicalDamage in battleutils.cpp

Curious if this is the legit way to handle this issue. teschnei? 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:07_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Sep 14, 2016 at 21:44 GMT_

----

I think there are more things than just attacks that go through
TakePhysicalDamage.  So it would probably need to have TakePhysicalDamage
split into two functions, one for reductions and one for actually taking
the damage.


