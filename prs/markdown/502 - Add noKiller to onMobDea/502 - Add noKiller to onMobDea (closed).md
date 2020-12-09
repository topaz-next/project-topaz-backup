**Labels:**



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Friday Apr 17, 2020 at 01:54:18_
_Originally opened as: project-topaz/topaz - Issue 502_

----

Usage of noKiller is similar to isKiller, but is only true when a mob dies
unclaimed. Useful for executing lua on mob death when something needs to
happen only once and a player object isn't required.

Example usage:
```lua
function onMobDeath(mob, player, isKiller, noKiller)
    if isKiller or noKiller then
        -- open a door, spawn a chest, show some death dialogue, etc
        -- do not use player with noKiller
    end
end
```
<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Apr 17, 2020 at 04:29:57_

----

I think this is more intuitive than checking for nil player/killer - isKiller pushes nil instead of bool when there isn't one, but someone is bound to be confused if they see us check for it being true or being nil on the same line.
