**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:53_
_Originally opened as: project-topaz/topaz - Issue 299_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 02, 2019 at 15:28 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6051_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
n/a

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Some uses of infinite duration effects are broken by a stupidly enforced minimum duration, which was a piss poor way to handle a bug it was done to fix. To test that with disease effect I had to set a huge duration instead of using zero duration for infinite. We should have a better way to do this that 

A) forcing a minimum on a bunch of things and calling that a fix for glitches rolling the timer over into huge numbers (no, that is stupid) 

and B) we should have alternate methods for at least some if not all these things instead of using hidden status effects to accomplish them in the first place.


