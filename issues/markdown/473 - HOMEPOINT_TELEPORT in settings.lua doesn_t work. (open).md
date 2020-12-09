**Labels:**

bug



<a href="https://github.com/gweivyth"><img src="https://avatars2.githubusercontent.com/u/37130689?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [gweivyth](https://github.com/gweivyth)**
_Tuesday Apr 07, 2020 at 23:13:53_
_Originally opened as: project-topaz/topaz - Issue 473_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Also looked on DSP and it looks like at some point back in December, someone broke it.  Home Point Warps are available whether you set 0 or 1. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Apr 07, 2020 at 23:21:35_

----

From discord, for anyone that wants to take care of this:
https://discordapp.com/channels/639659267003252746/678732530169544714/697223128312709193
```lua
    if not HOMEPOINT_TELEPORT == 1 then -- Settings.lua Homepoints disabled
        player:startEvent(csid, 0, 0, 0, 0, 0, player:getGil(), 4095, index)
        return
    end
```
Original authors intent was for it to return out there but its starting event 1st which defeats the point. .And options can be injected and onEvent Finish will let it pass, so that section has to change to not accept the options as well. 


----
<a href="https://github.com/gweivyth"><img src="https://avatars2.githubusercontent.com/u/37130689?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [gweivyth](https://github.com/gweivyth)**
_Wednesday Apr 08, 2020 at 16:27:17_

----

Tried this fix out last night but it didn't actually change the ability to Homepoint Warp.  After the adjustments, the homepoints still freely offered warps and worked the same as before.  I started rewriting my homepoints already (since I just need them to set homepoints, nothing fancy.) but it would be awesome to fix this for others who come along.  :D  I know some other servers were looking for something like this but were just waiting for a fix for the settings.lua function to work.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 08, 2020 at 18:19:42_

----

I think you misunderstood the post then, that wasn't code for you to copy and paste it was showing the mistake.


----
<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Tuesday Sep 08, 2020 at 19:42:01_

----

In my testing, the homepoints still offer to teleport, but the list of destinations is always empty. This does prevent using the homepoint teleport, but it may be confusing.
