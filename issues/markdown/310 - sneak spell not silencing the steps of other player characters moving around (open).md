**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:08_
_Originally opened as: project-topaz/topaz - Issue 310_

----

<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Aug 08, 2019 at 06:34 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6178_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
30190702_0

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
You cast sneak on someone else and they move around, you can hear their steps. It works for own player character.




----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Mar 19, 2020 at 20:32:33_

----

Just wanted to confirm this as it still being a valid issue


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Mar 20, 2020 at 03:35:13_

----

sneak bit needs set. its a flag but I think its not mapped to any of the enums, not sure.
`WBUFB(data,(0x38)-4) |= 0x04` should set it by directly modifying the data in the char entity packet.
(edit clarification: it should _already be happening there_, so I dunno why its not workin exactly, but somethin fubar'd it)

that _might_ be equivalent to nameflag 0x00000004 on retail but I'd need to look at the nameflags captured to check, just setting them on a private server doesn't mean it'll work.
