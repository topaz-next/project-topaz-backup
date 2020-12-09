**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:15_
_Originally opened as: project-topaz/topaz - Issue 118_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Hozu](https://github.com/Hozu)**
_Thursday Apr 14, 2016 at 20:09 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3042_

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
It should do both, except supposedly 2hr abilities don't have their timer consumed for paralysis.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:16_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Thursday Apr 14, 2016 at 21:57 GMT_

----

On retail paralysis no longer consumes items it paralyzes, although it did for the first ~8 years of game-play.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:17_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday Apr 14, 2016 at 22:34 GMT_

----

Wait WHAT??? That's interesting. Does it still consume recast timer?

Also, whenever I get a paralysis proc on a JA, battlemod addon throws an error, but idk if it's from the addon itself or DSP not sending the packet out correctly.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:18_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Friday Apr 15, 2016 at 02:02 GMT_

----

I believe recast timer is still consumed.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:20_

----

<a href="https://github.com/gedads"><img src="https://avatars1.githubusercontent.com/u/5845173?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [gedads](https://github.com/gedads)**
_Friday Apr 15, 2016 at 06:55 GMT_

----

yes JA is still consumed, same for spells recast etc 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:21_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Friday Apr 15, 2016 at 18:02 GMT_

----

Ok yeah battlemod only throws errors on JAs being para'd, not items.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:22_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Friday Apr 15, 2016 at 18:20 GMT_

----

Battlemod throwing an error is likely due to DSP displaying the paralysis message with a different packet than retail does (there are probably 3 or 4 ways to have the client display the same thing, and one was likely just picked at random)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:23_

----

<a href="https://github.com/xipies"><img src="https://avatars3.githubusercontent.com/u/7948457?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [xipies](https://github.com/xipies)**
_Tuesday Jul 12, 2016 at 14:55 GMT_

----

A few months ago, (on DSP), I had an xp ring charge get eaten by para. I haven't retested recently to see if it still can. Sounds like that's handled by recast timer rather than item consumption code. Not sure what the behavior is actually supposed to be, though. :)


