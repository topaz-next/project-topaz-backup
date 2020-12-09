**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Saturday Mar 14, 2020 at 01:30:45_
_Originally opened as: project-topaz/topaz - Issue 420_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

The real padfoot does not drop anything due to a mistake in his scripting:
release/scripts/zones/Lufaise_Meadows/mobs/Padfoot.lua

```lua
function onMobSpawn(mob)
    if mob:getID() == ID.mob.PADFOOT[GetServerVariable("realPadfoot")] then
        mob:setDropID(4478)
    else
        mob:setDropID(2734)
    end
end
```

setDropID(4478); number should be 2911, correlating to padfoot's actual drops from the release mob_droplist table.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Mar 14, 2020 at 02:06:38_

----

[Both drop IDs were wrong.](https://github.com/project-topaz/topaz/pull/421)
