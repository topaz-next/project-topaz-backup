**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:01_
_Originally opened as: project-topaz/topaz - Issue 235_

----

<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Jul 21, 2018 at 21:02 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5129_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** n/a


**_Source Branch_** (master/stable) **:** master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Some of the values in augments table have incorrectly.  For example

augmentId = 320 and modId = 357 (Blood Pact Delay) has value -1, when it should be 1
augmentId = 322 and modId = 455 (Song Casting Time) has value -1, when it should be 1.

This is because we are inconsistent with how many mods are implemented.  In these two cases, positive values mean "good" (delay is reduced), which to me is counterintuitive.

I'm sure there are many more augments that are doing the reverse of what we want.

Maybe we fix this problem in augments table.  Or maybe the QC should start by standardizing sign on the mods themselves.

