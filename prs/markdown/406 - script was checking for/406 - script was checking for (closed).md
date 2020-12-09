**Labels:**



<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [59blargedy](https://github.com/59blargedy)**
_Saturday Mar 07, 2020 at 15:29:21_
_Originally opened as: project-topaz/topaz - Issue 406_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Did not test, but minor fix so felt safe.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Mar 07, 2020 at 15:32:06_

----

it doesn't even need to check - defense down naturally doesn't reapply unless the new effects power is greater than the existing effect.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Mar 10, 2020 at 23:30:53_

----

Thank you - I'm ridiculously new at this so forgive the question - does that mean i should just delete the if not statement entirely as it is checking that elsewhere? REmoving it is of some benefit since it was checking attack_down, right?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 11, 2020 at 01:24:22_

----

yes you want that block to become:
```lua
    if damage > 0 then
        local duration = tp / 1000 * 20 * applyResistanceAddEffect(player, target, tpz.magic.ele.WIND, 0)
        target:addStatusEffect(tpz.effect.DEFENSE_DOWN, 19, 0, duration)

        -- Apply aftermath
        tpz.aftermath.addStatusEffect(player, tp, tpz.slot.MAIN, tpz.aftermath.type.RELIC)
    end
```
note the adjusted indent on the part that was inside the if-then-end pairing


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Mar 11, 2020 at 22:21:41_

----

cool, thanks i changed and committed again so hopefully that is right. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Mar 12, 2020 at 00:22:16_

----

looks good :+1:



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Mar 07, 2020 at 15:32:06_

----

it doesn't even need to check - defense down naturally doesn't reapply unless the new effects power is greater than the existing effect.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Mar 10, 2020 at 23:30:53_

----

Thank you - I'm ridiculously new at this so forgive the question - does that mean i should just delete the if not statement entirely as it is checking that elsewhere? REmoving it is of some benefit since it was checking attack_down, right?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 11, 2020 at 01:24:22_

----

yes you want that block to become:
```lua
    if damage > 0 then
        local duration = tp / 1000 * 20 * applyResistanceAddEffect(player, target, tpz.magic.ele.WIND, 0)
        target:addStatusEffect(tpz.effect.DEFENSE_DOWN, 19, 0, duration)

        -- Apply aftermath
        tpz.aftermath.addStatusEffect(player, tp, tpz.slot.MAIN, tpz.aftermath.type.RELIC)
    end
```
note the adjusted indent on the part that was inside the if-then-end pairing


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Mar 11, 2020 at 22:21:41_

----

cool, thanks i changed and committed again so hopefully that is right. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Mar 12, 2020 at 00:22:16_

----

looks good :+1:

