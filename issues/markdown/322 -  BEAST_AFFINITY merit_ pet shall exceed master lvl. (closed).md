**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:40_
_Originally opened as: project-topaz/topaz - Issue 322_

----

<a href="https://github.com/benfolka"><img src="https://avatars0.githubusercontent.com/u/17715043?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [benfolka](https://github.com/benfolka)**
_Monday Oct 28, 2019 at 04:48 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6266_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30191004_0


**_Source Branch_** (master/stable) **:** master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** Since pet not reciving any exp fix has been implemented, This wont cause any problems. This behaviour is retail and shall be same in DSP servers. Pets shall exceed master level with beast affinity merits.





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:41_

----

<a href="https://github.com/zynjec"><img src="https://avatars3.githubusercontent.com/u/17911103?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zynjec](https://github.com/zynjec)**
_Friday Nov 08, 2019 at 17:33 GMT_

----

I'm not sure I follow the issue, BEAST_AFFINITY already allows the pet to go above the masters level unless you've experienced it not working?

github/DarkstarProject/darkstar/blob/43698546fcb01ef1eae1adb2ceac1f57c5f043b0/src/map/utils/petutils.cppDarkstar Issue L1652



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:42_

----

<a href="https://github.com/gori123"><img src="https://avatars3.githubusercontent.com/u/18142814?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [gori123](https://github.com/gori123)**
_Friday Nov 08, 2019 at 17:42 GMT_

----

// And cap it to the master's level.
            if (highestLvl > PMaster->GetMLevel())
            {
                highestLvl = PMaster->GetMLevel();
            }



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:43_

----

<a href="https://github.com/gori123"><img src="https://avatars3.githubusercontent.com/u/18142814?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [gori123](https://github.com/gori123)**
_Friday Nov 08, 2019 at 17:45 GMT_

----

merit works but then there are lines that drops pet level again to masters level,
which is not retail default



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:44_

----

<a href="https://github.com/zynjec"><img src="https://avatars3.githubusercontent.com/u/17911103?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zynjec](https://github.com/zynjec)**
_Friday Nov 08, 2019 at 17:52 GMT_

----

Fair enough, just grepped for BEAST_AFFINITY and didn't see the code under it. Seems easy enough to fix.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:45_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Nov 09, 2019 at 15:43 GMT_

----

there is supposed to be some capping, but its need to be done before merit and other mods apply, not after.

got stuffed in wrong place.

