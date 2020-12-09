**Labels:**

merge ready



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday Jun 26, 2020 at 08:44:29_
_Originally opened as: project-topaz/topaz - Issue 774_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Tested a bunch, I'm getting pretty good at the minigame...

**New:**
Added tracking via Quest Log
Fixed missing Item and NPC IDs in completion CS
Changed motivation/pep relationship
Added clamping to motivation and pep to fix any weirdness with the bar rendering
Added failure CS when you dismount or run out of motivation, which lets you enable easy mode (or not)
Added easy mode: tracked through the effect's power (acts as a modifier for motivation decay and pep growth)
Fixed bug where the final Raptor Food region was acting like it was Syrillia's region
Added MEET_SYRILLIA text when you've eaten 5 foods

**Not doing in this PR:**
Additional Raptor animations
Varying pep and speed depending on terrain slope etc.
Best time tracking

**Once this PR goes in, I think it would be fair to open two new issues:**
**- [Good First Issue] Quest: Full Speed Ahead! doesn't track server best time**
Using `Get/SetServerVariable`

**- [Good First Issue][Core] Quest: Full Speed Ahead! raptor doesn't slow down as it runs out of pep**
Mount speed is hard-coded, and needs to be modifiable (through mods or otherwise) for Full Speed Ahead!

`battleentity.cpp`
```
uint8 CBattleEntity::GetSpeed()
{
    return (isMounted() ? 50 + map_config.speed_mod : std::clamp<uint16>(speed * (100 + getMod(Mod::MOVE)) / 100, std::numeric_limits<uint8>::min(), std::numeric_limits<uint8>::max()));
}
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 13:51:46_

----

This gap worries me; we'll have to check dats later and add whatever is missing from Jeuno's quest log


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 13:57:29_

----

How are we handling the quest mounted status again? Did it get a special effect, or are we using regular mounted?

In other words: what if a player fails, quits, rides a chocobo in Batalia, then dismounts?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 14:00:05_

----

Could be wrong, but I think you bumped up your quest vars, so talking to Mapitoto after trying once will result in completion. 😉 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 11, 2020 at 17:04:01_

----

~~he dat index stops at 158 and shows this quest as 157 so I dunno wtf we did to get these values...~~
_our packet is fubar and we're gonna wind up with migrations again later, awesome_


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 17:16:55_

----

More fuel for the dumpster fire that this one PR line has illuminated: every quest area is messed up at each interval of 32!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Jul 12, 2020 at 14:05:59_

----

It has its own special effect which is a wrapper for regular mount and all the functions in `quests/full_speed_ahead.lua`. This handles the loss of the underlying mounted effect, it's own loss, ticks, power for difficulty etc.

I tested your scenario: nothing extra happens :+1:




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 13:51:46_

----

This gap worries me; we'll have to check dats later and add whatever is missing from Jeuno's quest log


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 13:57:29_

----

How are we handling the quest mounted status again? Did it get a special effect, or are we using regular mounted?

In other words: what if a player fails, quits, rides a chocobo in Batalia, then dismounts?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 14:00:05_

----

Could be wrong, but I think you bumped up your quest vars, so talking to Mapitoto after trying once will result in completion. 😉 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 11, 2020 at 17:04:01_

----

~~he dat index stops at 158 and shows this quest as 157 so I dunno wtf we did to get these values...~~
_our packet is fubar and we're gonna wind up with migrations again later, awesome_


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 17:16:55_

----

More fuel for the dumpster fire that this one PR line has illuminated: every quest area is messed up at each interval of 32!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Jul 12, 2020 at 14:05:59_

----

It has its own special effect which is a wrapper for regular mount and all the functions in `quests/full_speed_ahead.lua`. This handles the loss of the underlying mounted effect, it's own loss, ticks, power for difficulty etc.

I tested your scenario: nothing extra happens :+1:


