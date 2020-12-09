**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:38_
_Originally opened as: project-topaz/topaz - Issue 321_

----

<a href="https://github.com/tourmaline3333"><img src="https://avatars1.githubusercontent.com/u/55633564?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [tourmaline3333](https://github.com/tourmaline3333)**
_Sunday Oct 27, 2019 at 12:05 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6263_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
30190731

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Desperate Blows has haste "15%".
Desperate Blows Merits has "-2% per 1 point"
Desperate Blows with Merits 5 -> haste 25%
So, addMod(dsp.mod.HASTE_ABILITY, ***2500***)

but "effect/last_resort.lua" coded
---
target:addMod(dsp.mod.HASTE_ABILITY, target:getMod(dsp.mod.DESPERATE_BLOWS) + 
target:getMerit(dsp.merit.DESPERATE_BLOWS))
---
its addMod(dsp.mod.HASTE_ABILITY, ***1532***).
because "target:getMerit(dsp.merit.DESPERATE_BLOWS)" was only 32, not 1000.


