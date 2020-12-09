**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday Sep 18, 2020 at 06:11:55_
_Originally opened as: project-topaz/topaz - Issue 1153_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

We mentioned this in the PR and on discord, this will help out @neuromancerxi with https://github.com/project-topaz/topaz/pull/1147

**EDITED TO BE CORRECT**

**Testing Script**
```lua

function onTrigger(player, str)
    local ring = player:getEquippedItem(13)
    printf("sig %s.", ring:getSignature()) -- <-- Note the full stop. Clean string.
end
```

**Steps**
- Craft a bone ring with a _Cyclone Crystal_ (to sign it)
- Run script to get signature

**Results:**
```
[18/Sep] [09:35:54][LUA Script] sig Test.
```



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Sep 18, 2020 at 06:14:43_

----

Now I see that signature is it's own field in the db, so it isn't held in m_extra at all?
EDIT:
I forgot what coco said yesterday:
```
if anyone is wondering about signatures, we store them as strings in the db, then when we load them into memory, we copy that string into the items ex data, since the client uses the ex data to display to the client
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Sep 18, 2020 at 12:38:56_

----

> getEquippedItem(13)

WRY U NO USE ENUM IN EXAMPLE

:stuck_out_tongue: 
