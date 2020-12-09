**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:41_
_Originally opened as: project-topaz/topaz - Issue 111_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Deadwing888](https://github.com/Deadwing888)**
_Monday Apr 04, 2016 at 10:22 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2989_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **30160203_0**

**_Server Version_** (type `revision` in game) **Unknown** 5 day old build.

**_Source Branch_** (master/stable) **Master**

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**

Example: Black mage casts burn on a high HP target. Corsair(s) proceed to use 20 fire shots on it ---> Hp starts dropping very quickly (thousands per tick).




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:42_

----

<a href="https://github.com/Kubisnaxx"><img src="https://avatars0.githubusercontent.com/u/15025127?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Kubisnaxx](https://github.com/Kubisnaxx)**
_Tuesday Apr 05, 2016 at 02:27 GMT_

----

So that's how you killed Tiamat in 10 minutes!




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:43_

----

<a href="https://github.com/sgtgunso"><img src="https://avatars0.githubusercontent.com/u/18276099?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [sgtgunso](https://github.com/sgtgunso)**
_Tuesday Apr 05, 2016 at 02:39 GMT_

----

so. . .you exploited, abused, and made this post as an escape goat. . . GG sir




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:44_

----

<a href="https://github.com/metalfiiish"><img src="https://avatars1.githubusercontent.com/u/6957288?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [metalfiiish](https://github.com/metalfiiish)**
_Thursday Dec 14, 2017 at 18:40 GMT_

----

Seems to be because the lua script for Fire shot (and all other elemental shots) is simply getting the existing power of effects like burn, etc. and then multiplying them by 1.2 so it could exponentially build up per use. Not sure on a fix yet but we need a way to identify if the burn, etc. was already modified by an elemental shot before allowing it to do that power change.

My suggestion would be to use subPower to track the amount of modified power so we can check if it's already powered up, but would require updating the BRD's trenody effect to track resistance_type in subId instead of subPower, would make more sense anyway.

