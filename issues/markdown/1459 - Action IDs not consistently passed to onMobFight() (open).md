**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Saturday Oct 31, 2020 at 18:39:00_
_Originally opened as: project-topaz/topaz - Issue 1459_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

I have stumbled across mob scripts that use `mob:getCurrentAction()` to check for certain `ACTION IDs`, mostly to prevent overlapping/interference of actions. Some of these deliberately check for `MOBABILITY_START`, `MAGIC_START`, `JOBABILITY_START` (10) and the like.
All of these are mapped to verbose states in https://github.com/project-topaz/topaz/blob/71059dea38bd9230e23f2c69cecd547665f6b9d1/scripts/globals/status.lua#L2513
While debugging different things I have noticed that most of these states actually aren't ever recognized inside of `onMobFight()`. **May this be because `onMobFight()` doesn't catch it, or that `getCurrentAction()` never passes them, I would not know**.

The only states that are returned are the actual "using" states like `MOBABILITY_USING` (34), or `MAGIC_CASTING` (30) and `ATTACK` (1). Interestingly enough `JOBABILITY_X` and `RANGED_X` are also erroneously recognized as (34) throughout their whole animation and `MAGIC_INTERRUPT` is also simply (30).
**It would seem** that 1, 30 and 34 are the only states ever passed to `getCurrentAction()`. [I made a short video](https://streamable.com/1kdsv7) where this only shows for casting and mobskill though. (I tested several others today)

For the current state of the project **this results in scripts with erroneously false checks** (false negatives) and new scripts might be written with these in mind, not knowing that they don't get passed at all. It's not particularly breaking bad, but it does lead to false negatives and it simply provokes unnecessary checks in the code base.

Some pointers:
ACTION_MAGIC_INTERRUPT & ACTION_MAGIC_FINISH:
https://github.com/project-topaz/topaz/blob/71059dea38bd9230e23f2c69cecd547665f6b9d1/src/map/entities/battleentity.cpp#L1465
ACTION_MOBABILITY_START & ACTION_MOBABILITY_INTERRUPT:
https://github.com/project-topaz/topaz/blob/71059dea38bd9230e23f2c69cecd547665f6b9d1/src/map/ai/states/mobskill_state.cpp#L61
ACTION_RANGED_START & ACTION_RANGED_INTERRUPT:
https://github.com/project-topaz/topaz/blob/71059dea38bd9230e23f2c69cecd547665f6b9d1/src/map/ai/states/range_state.cpp#L65
  
  
**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
Print the currentAction to console on any mob and watch the output:
```LUA
function onMobFight(mob, target)
    print(mob:getCurrentAction())
end
```
One would expect to print states like 2, 4, 6, 8, 31, 32, 33 etc. etc.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Oct 31, 2020 at 20:48:46_

----

> JOBABILITY_X and RANGED_X are also erroneously recognized as (34)

There are multiple types of action categories; among others: ["True" Ranged](https://github.com/Windower/Lua/wiki/Action-Category-02), [WS + Damaging JAs](https://github.com/Windower/Lua/wiki/Action-Category-03), [(Most) Non-damaging JAs](https://github.com/Windower/Lua/wiki/Action-Category-06), and Mobskills ([Start](https://github.com/Windower/Lua/wiki/Action-Category-07), ([Finish](https://github.com/Windower/Lua/wiki/Action-Category-11))

Mobs will use RA (Cat 2), WS (Cat 3), and true mobskill (Cat 11) under different circumstances. For example, what "looks" like a ranged attack from a mob may actually be a Category 11 impersonating a "true" Ranged Attack (category 2).

Our current handling of WS for mobs can complicate matters too, because [while mobs are capable of using WS+JA (Category 3) on retail, we currently "fake it" with Mobskills (Category 11)](https://github.com/project-topaz/topaz/issues/663).

This can get even more confusing because on both retail and Topaz, mobs are capable of using messageless Category 11s to "fake" a "regular melee attack" which _isn't_ a true melee attack ([Category 1](https://github.com/Windower/Lua/wiki/Action-Category-01)) - they typically do this for "AoE melee" attacks (no such thing, any physical AoE is _always_ a Category 11) or any "attack" that has knockback.

I dunno about any timing things for getCurrentAction, or if the thing I'm working on might help. Just explaining that sometimes things with mobs can get wonky because they fake a lot of stuff - and not _all_ of it is on us.
