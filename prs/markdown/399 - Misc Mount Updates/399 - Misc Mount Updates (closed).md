**Labels:**

merge ready



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday Feb 28, 2020 at 22:52:55_
_Originally opened as: project-topaz/topaz - Issue 399_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

**NOTE:** Doll only works after a version update

**Added:**
GM Command: addallmounts
- Gives all mount summoning KIs

GM Command: mount
- Puts current player or target on a chocobo, or other specific mount

Missing key items 3092-3098 (new mounts)
Updates tpz.mount and MOUNTTYPE with new mounts
SQL and scripts for the two mount npcs in upper jeuno

![image](https://user-images.githubusercontent.com/1389729/75592981-7ac6ed80-5a8c-11ea-9291-a8841194dd60.png)

Testing:
```lua
-- Correct
!mount -- Summons Chocobo
!mount 22
!mount GOOBBUE
!mount GOOBBUE Raguza

!addallmounts
!addallmounts Raguza

-- Incorrect (Handled)
!mount -1
!mount 100
!mount Raguza
!mount ULTIMA

!addallmounts SomeoneElse
```

Tested in {South Gustaberg}, {Upper Jeuno}, 210 (GM HOME). 
Since this is a GM command, I guess it's fine to be able to use mounts in non-mount areas.

Tested all the item trades to Mapitoto


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Feb 29, 2020 at 22:59:53_

----

```lua
if trade:getSlotCount() == 1 then
    local item = trade:getItemId(0)
    local mount = item - 10050
    if mount >= 0 and mount <= 24 then
        player:setLocalVar("FullSpeedAheadReward", tpz.ki.TIGER_COMPANION + mount)
        player:startEvent(10227, item, tpz.ki.TRAINERS_WHISTLE, tpz.mount.TIGER + mount - 1)
    end
end


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Feb 29, 2020 at 23:00:57_

----

```lua
local rewardKI = player:getLocalVar("FullSpeedAheadReward")
player:setLocalVar("FullSpeedAheadReward", 0)
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Mar 01, 2020 at 07:42:38_

----

I didn't think to inspect the details of the trade object without npcUtil, many thanks 🙏 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Mar 01, 2020 at 07:43:04_

----

I need to go read the difference between LocalVar and CharVar, thanks!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Mar 01, 2020 at 20:35:44_

----

`not` is a thing in lua. Instead of having an empty conditional, just add "not these things" to whatever else is being done and proceed as normal.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 06:19:10_

----

Should probably have this default to permission 1


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 06:20:34_

----

~~`mount` needs a `local` definition~!~~ I am blind.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Feb 29, 2020 at 22:59:53_

----

```lua
if trade:getSlotCount() == 1 then
    local item = trade:getItemId(0)
    local mount = item - 10050
    if mount >= 0 and mount <= 24 then
        player:setLocalVar("FullSpeedAheadReward", tpz.ki.TIGER_COMPANION + mount)
        player:startEvent(10227, item, tpz.ki.TRAINERS_WHISTLE, tpz.mount.TIGER + mount - 1)
    end
end


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Feb 29, 2020 at 23:00:57_

----

```lua
local rewardKI = player:getLocalVar("FullSpeedAheadReward")
player:setLocalVar("FullSpeedAheadReward", 0)
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Mar 01, 2020 at 07:42:38_

----

I didn't think to inspect the details of the trade object without npcUtil, many thanks 🙏 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Mar 01, 2020 at 07:43:04_

----

I need to go read the difference between LocalVar and CharVar, thanks!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Mar 01, 2020 at 20:35:44_

----

`not` is a thing in lua. Instead of having an empty conditional, just add "not these things" to whatever else is being done and proceed as normal.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 06:19:10_

----

Should probably have this default to permission 1


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 06:20:34_

----

~~`mount` needs a `local` definition~!~~ I am blind.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Feb 29, 2020 at 05:10:06_

----

2 thoughts: 
 - could default to chocobo if no mount ID is specified 
 - since its invoked by GM command, may as well use inf duration (0 = inf)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Mar 01, 2020 at 20:17:58_

----

Re: Fenrir crash - on retail, Fenrir mount _key item_ is rewarded directly by choosing it as a reward for completing Moonlit Path. The astral notebook is technically unattainable.
