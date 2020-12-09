**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:01_
_Originally opened as: project-topaz/topaz - Issue 115_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Hozu](https://github.com/Hozu)**
_Sunday Apr 10, 2016 at 17:22 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3019_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [X] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [X] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30160203_0

**_Server Version_** (type `revision` in game) **:**
github/DarkstarProject/darkstar/commit/ec30b55f7457dbfbbe190ed181c4b83e7e07871d

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
It should use the mobskill when the target is in range of the mobskill. This matters more for mobs that are forced to use multiple mobskills in a row, like Tinnin does on regrowing heads.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:02_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Wednesday May 04, 2016 at 16:41 GMT_

----

is it supposed to keep the skill queued and fire off once in range or just fail altogether?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:03_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday May 04, 2016 at 16:42 GMT_

----

I am pretty sure that depends on the mob




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:05_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Wednesday May 04, 2016 at 16:49 GMT_

----

IIRC before on DSP it would not force the move if the target is out of range (not until it gets back in range), but if the target runs out of range during the prepare time, then it doesn't get used again. Not sure if that was correct or not, but it sounds reasonable.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:06_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday May 04, 2016 at 16:50 GMT_

----

Reasonable enough


