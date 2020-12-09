**Labels:**

good first issue



<a href="https://github.com/ffxisf"><img src="https://avatars3.githubusercontent.com/u/2270559?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ffxisf](https://github.com/ffxisf)**
_Wednesday Sep 02, 2020 at 10:44:40_
_Originally opened as: project-topaz/topaz - Issue 1055_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 02, 2020 at 13:10:37_

----

Welcome to Project Topaz! I'm going to post instructions on how to fix this issue (if you need to apply a hot-fix to your local server), and tag this so that someone else might be able to come along and fix this in our repo, thanks for reporting!

https://github.com/project-topaz/topaz/blob/release/scripts/zones/Northern_San_dOria/npcs/Madaline.lua#L13
https://github.com/project-topaz/topaz/blob/release/scripts/zones/Northern_San_dOria/npcs/Telmoda.lua#L14

These are in the form:
```lua
player:setCharVar(player, "Telmoda_Madaline_Event", 1)
```

but should be:
```lua
player:setCharVar("Telmoda_Madaline_Event", 1)
```

I imagine these will trigger a `TPZ_DEBUG_BREAK` when they hit core and the server will die :(


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 18:16:08_

----

Fixed in `release` with https://github.com/project-topaz/topaz/pull/1056, will get merged into `canary` in a few days. Thanks for reporting @ffxisf  👍 
