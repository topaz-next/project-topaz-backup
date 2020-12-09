**Labels:**



<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Monday Sep 21, 2020 at 13:54:37_
_Originally opened as: project-topaz/topaz - Issue 1174_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

It appears as if the end of the trade process, all detectable effects are removed from the character:
https://github.com/project-topaz/topaz/blob/release/src/map/packet_system.cpp#L1362
https://github.com/project-topaz/topaz/blob/release/src/map/status_effect.h#L56

This was most likely done while thinking of trading keys to chests and coffers, which is the correct behavior for them. However, it results in Sneak breaking when trading a Pickaxe to Mine, something it shouldn't.

https://ffxiclopedia.fandom.com/wiki/Sneak_Mining

We can't simply change the flag to the existing EFFECTFLAG_INVISIBLE, because it would ruin the proper behavior for chests.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 21, 2020 at 14:15:43_

----

We could check for
```
if (targetOfTrade == a HELM point) { don't remove the stuff}
or
if (targetOfTrade == a HELM point && trade.contains(OnePickaxe)) { don't remove the stuff}
```


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Monday Sep 21, 2020 at 14:30:34_

----

I think we have the same issue when trading an item for a quest
For instance for the THF AF in Dangruf, i traded an item to a ??? and it removed sneak and i got instantly killed by a high level worm nearby :-)



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Sep 22, 2020 at 11:33:11_

----

Another way to do this would be to change:
```
        PChar->StatusEffectContainer->DelStatusEffectsByFlag(EFFECTFLAG_DETECTABLE);
        luautils::OnTrade(PChar, PNpc);
```
to 
```
    auto result = luautils::OnTrade(PChar, PNpc);
    if (result == don't take away sneak)
    {
        PChar->StatusEffectContainer->DelStatusEffectsByFlag(EFFECTFLAG_DETECTABLE);
    }

```
Then you could just change the `helm.lua` onTrade helper to return a value for "don't take away sneak"


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Sep 22, 2020 at 11:34:30_

----

Or like we have helpers that change the message type of an action from Lua, we could modify aspects of the trade while in onTrade



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Sep 23, 2020 at 14:03:05_

----

Seems to me like chests and coffers should not have removed everything detectable via the trade itself core side and instead just had a delStatusEffect() in its global lua so as to spare us this issue of its specific thing firing on other trade events like this.¯\\\_(ツ)\_/¯ 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Sep 23, 2020 at 14:03:17_

----

1) On retail, isn't it impossible to trade while invisible?

2) If so, can remove flag deletion in 0x036 altogether, and have chests/coffers do it in their scripts

Edit: Teo won by _seconds_


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Sep 23, 2020 at 14:05:08_

----

Actually I think you do have to drop invis (manually yourself) but only invis, not sneak or deo. 


----
<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Thursday Sep 24, 2020 at 05:30:58_

----

> Actually I think you do have to drop invis (manually yourself) but only invis, not sneak or deo.

That is what I recall and backed up with everything I've seen related to it while looking at this initially.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Sep 24, 2020 at 12:13:04_

----

Got retail confirmation that the client at least universally blocks any ability to attempt trades while invis, so we shoudl disallow trying it rather than stripping it. And chests/coffers are the only thing to remove sneak.
