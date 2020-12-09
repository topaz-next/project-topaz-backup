**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:20:55_
_Originally opened as: project-topaz/topaz - Issue 73_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Dec 25, 2015 at 22:40 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2524_

----

Despite currently scripted and in progress scripts for these I've been thinking maybe individually scripting every additional effect weapon in the game wasn't the best approach we could have taken to this. I know previously there were additional effect weapons hard coded in the core and am **not** advocating a return to that. But perhaps a method closer to spike effects via modifiers would be better for setting the effect type and potency / base dmg of the effect. Note that the spikes still allow scripting, and so far we've done monster spikes scripted and item spikes by modifier.
Also:
http://ffxiclopedia.wikia.com/wiki/Dweomer_Scythe
There are additional effects granted via augments, which in our current system of full on scripting we could do as an extra modifier to check for in the scripts of the individual items. However, as mentioned in Darkstar Issue 2522 scripted additional effects presently ignore sync as well (I believe they shouldn't fire off at all if you are below the level of your weapon, and not a thing that scales down). That too, could be checked for in scripts. But maybe it'd be better to just have modifiers for the effect type and power that could then be directly set to the item via the augments. In the spikes code in core for items you can see the modifiers get set to the item, not the player, and checks per item. We could check for the player being below the weapons level right there one time to stop the proc, rather then repeatedly check for being sync'd below the weapons level in every onAdditionalEffect script.

**So my long winded wall-o-text boils down to the question:
Better to implement workarounds in scripts, or to change the underlying method?**




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:20:57_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Dec 25, 2015 at 23:02 GMT_

----

Additional thought: if SE ever allows those add effect augments to be applied to more than a handful of weapons, we'd need a generic (onAdditionalEffectEX? nothx) or individual scripts for all weapon (lolno) under the current system.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:20:58_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 21, 2018 at 20:46 GMT_

----

Its not current atm and I rebase it a lot but am working on it here:
github/TeoTwawki/darkstar/tree/addEffectsRework

