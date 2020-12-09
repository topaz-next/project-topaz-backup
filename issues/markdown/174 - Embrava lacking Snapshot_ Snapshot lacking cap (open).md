**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:42:25_
_Originally opened as: project-topaz/topaz - Issue 174_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Hozu](https://github.com/Hozu)**
_Tuesday Apr 18, 2017 at 21:09 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3853_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
current

**_Server Version_** (type `revision` in game) **:**
current

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**

- [ ] Embrava adds Snapshot effect equal to the amount of Haste it gives. - https://www.bluegartr.com/threads/112776-Dev-Tracker-Findings-Posts-(NO-DISCUSSION)?p=6482749&viewfull=1Darkstar Issue post6482749

Since Snapshot mod is out of 100 while Haste is out of 1024, in the Embrava effect script, it should be easy enough to do something like...

`target:addMod(MOD_SNAPSHOT, math.floor(haste/1024*100));`

That, along with the associated modifier removal for onEffectLoss. That way you don't have to figure out how to pass in another parameter that's going to be the same as the one for the Haste modifier.

- [ ] However, with adding this, it may be possible to bypass the Snapshot effect cap. The total ranged delay reduction cap from all sources is 70% - https://www.bluegartr.com/threads/112776-Dev-Tracker-Findings-Posts-(NO-DISCUSSION)?p=6370091&viewfull=1Darkstar Issue post6370091 That cap would probably go above the return here? github/DarkstarProject/darkstar/blob/8f6bf13014f1903fb632456828f1c8821e757690/src/map/utils/battleutils.cppDarkstar Issue L4832

