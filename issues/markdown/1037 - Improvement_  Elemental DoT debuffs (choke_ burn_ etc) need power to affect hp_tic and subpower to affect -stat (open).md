**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Saturday Aug 29, 2020 at 21:00:50_
_Originally opened as: project-topaz/topaz - Issue 1037_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Currently all 6 ele DoT spells use a singular ratio to determine both their hp/tic loss and -stat loss from the effect's power variable.  We need the -stat loss to be taken from the subpower so it is configurable independently of the -hp/tic.  The ratio we have currently should ONLY be used if the subpower is not provided, it would default to the ratio.

@TeoTwawki  has input on this too from talking to him several times about it.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Aug 29, 2020 at 21:17:48_

----

Like tank said, I think we should be able to simply specify what we want, power for dot subpower for stat down, and fall back to [the current behavior](https://github.com/project-topaz/topaz/blob/release/scripts/globals/effects/drown.lua#L12) when we do not:
```lua
target:addMod(tpz.mod.REGEN_DOWN, effect:getPower())
target:addMod(tpz.mod.STR, -getElementalDebuffStatDownFromDOT(effect:getPower()))
```
```lua
function getElementalDebuffStatDownFromDOT(dot)
    local stat_down = 0
    stat_down = (dot-1)*2 +5
    return stat_down
end
```
