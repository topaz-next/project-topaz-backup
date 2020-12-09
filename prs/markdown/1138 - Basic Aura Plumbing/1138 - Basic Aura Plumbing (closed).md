**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Monday Sep 14, 2020 at 14:18:34_
_Originally opened as: project-topaz/topaz - Issue 1138_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Way back when I wrote some messy core code to allow the use of GEO Auras. I handed this off to MrSent who then wrote _all_ of GEO. Super impressive stuff, but functionally impossible to review. 

**So I'd like to:**
- Get the core plumbing into `release`, where it will sit unused by anything. 
- Use it in my `feature/trust` branch for Sakura - the passive regen trust.
- Ship those two off into canary for general testing.
- Once we see that the aura code doesn't ruin servers, and maybe iterate on it a bit, we can start dripping in geo content.

**TODO:**
- ~~Make effects fall off silently~~
- ~~Address that TODO about using spawnlists, or something that isn't _everyone in the zone_~~

**Testing**
Make a gm command:
```lua
cmdprops =
{
    permission = 1,
    parameters = ""
}

function onTrigger(player)
    local bubbleEffect = 14
    local tick_effect = tpz.effect.GEO_REGEN
    local potency = 10
    local target_type = tpz.allegiance.PLAYER

    player:addStatusEffectEx(tpz.effect.COLURE_ACTIVE, tpz.effect.COLURE_ACTIVE, bubbleEffect, 3, 15, tick_effect,
        potency, target_type, tpz.effectFlag.AURA + tpz.effectFlag.NO_LOSS_MESSAGE)
end
```




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Sep 14, 2020 at 22:52:14_

----

allegiance.PLAYER is the wrong approach to the problem. Bubble types should be tagged as targeting aliies or enemies, and allegiance checks against potential targets done based on that.

If this paradigm isn't corrected early, it _will_ bite people in the ass the _second_ they start trying to implement NMs with auras.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 15, 2020 at 02:01:37_

----

Oops. Good catch tho, don’t want to repeat the player/mob paradigm that is a problem with skill/ability use atm. 
