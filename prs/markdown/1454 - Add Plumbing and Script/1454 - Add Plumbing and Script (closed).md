**Labels:**



<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [neuromancerxi](https://github.com/neuromancerxi)**
_Thursday Oct 29, 2020 at 21:47:40_
_Originally opened as: project-topaz/topaz - Issue 1454_

----

Modifies/Reorders magic_shield and physical_shield effects and adds new tiers.
Moves Rampart IronWill check to rampart effect.
Modifies the MAGIC_SHIELD check to check which power tier is active before flooring magic.
Adds scripts for Fanatics/Fools Drink/Tonics.
Adds scripts for Carnal/Spiritual Incense.
Adjusts timers to 1s where applicable.
Adjusts scripts to new values where applicable.

**SPECIAL NOTE TO SERVER OPERATORS**: Make sure you check your custom scripts when merging this change. This adjusts the scripts that existed in Topaz at the time of submission, but due to the change in how power is now applied, please make sure any scripts that use apply (and possibly remove) MAGIC_SHIELD and/or PHYSICAL_SHIELD effects use the new values in the effects.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2020 at 23:00:03_

----

Just tossing you some info/possibilities here:

We do have additional field sin the effect we could be using, which could make this simpler.

`hasStatusEffect(effectID, subid)` is also a thing. one of the lines you replaced was using that to tell apart 2 versions of magic shield. We could also use subpower and tiers. Frankly what we're doing with power even before your PR should have been tiers but way back when somebody used power so we stuck with it. We could use subpower to decide if we're blocking status effects or not as an example instead of using an invalid dmg reduction of -101.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2020 at 23:02:26_

----

We have 2 versions of this overloaded function:
 - https://github.com/project-topaz/topaz/blob/45c97efb1fdb128570a223b3bea8cb40ed281182/src/map/status_effect_container.cpp#L1110
```cpp
bool CStatusEffectContainer::HasStatusEffect(EFFECT StatusID, uint16 SubID)
{
    for (CStatusEffect* PStatusEffect : m_StatusEffectSet)
    {
        if (PStatusEffect->GetStatusID() == StatusID &&
            PStatusEffect->GetSubID() == SubID &&
            !PStatusEffect->deleted)
        {
            return true;
        }
    }
    return false;
}
```

- https://github.com/project-topaz/topaz/blob/45c97efb1fdb128570a223b3bea8cb40ed281182/src/map/status_effect_container.cpp#L835
```cpp
bool CStatusEffectContainer::HasStatusEffect(EFFECT StatusID)
{
    for (CStatusEffect* PStatusEffect : m_StatusEffectSet)
    {
        if (PStatusEffect->GetStatusID() == StatusID &&
            !PStatusEffect->deleted)
        {
            return true;
        }
    }
    return false;
}
```

I believe the original intent was to have this only apply to versions that did not have a subid, and use subid to tell apart differing versions. An unfinished implementation looked like to me (or they mistook subid for power?)


----
<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Friday Oct 30, 2020 at 11:40:32_

----

Ah, that makes much more sense now, I think I'm following your line of reasoning. I'll take a look at applying a "isfakemagicshield" sub for Fanatic's Tonic and Spiritual Incense since these offer the MDT UMDT adjustments, but not the actual magic immunity.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2020 at 23:00:03_

----

Just tossing you some info/possibilities here:

We do have additional field sin the effect we could be using, which could make this simpler.

`hasStatusEffect(effectID, subid)` is also a thing. one of the lines you replaced was using that to tell apart 2 versions of magic shield. We could also use subpower and tiers. Frankly what we're doing with power even before your PR should have been tiers but way back when somebody used power so we stuck with it. We could use subpower to decide if we're blocking status effects or not as an example instead of using an invalid dmg reduction of -101.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2020 at 23:02:26_

----

We have 2 versions of this overloaded function:
 - https://github.com/project-topaz/topaz/blob/45c97efb1fdb128570a223b3bea8cb40ed281182/src/map/status_effect_container.cpp#L1110
```cpp
bool CStatusEffectContainer::HasStatusEffect(EFFECT StatusID, uint16 SubID)
{
    for (CStatusEffect* PStatusEffect : m_StatusEffectSet)
    {
        if (PStatusEffect->GetStatusID() == StatusID &&
            PStatusEffect->GetSubID() == SubID &&
            !PStatusEffect->deleted)
        {
            return true;
        }
    }
    return false;
}
```

- https://github.com/project-topaz/topaz/blob/45c97efb1fdb128570a223b3bea8cb40ed281182/src/map/status_effect_container.cpp#L835
```cpp
bool CStatusEffectContainer::HasStatusEffect(EFFECT StatusID)
{
    for (CStatusEffect* PStatusEffect : m_StatusEffectSet)
    {
        if (PStatusEffect->GetStatusID() == StatusID &&
            !PStatusEffect->deleted)
        {
            return true;
        }
    }
    return false;
}
```

I believe the original intent was to have this only apply to versions that did not have a subid, and use subid to tell apart differing versions. An unfinished implementation looked like to me (or they mistook subid for power?)


----
<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Friday Oct 30, 2020 at 11:40:32_

----

Ah, that makes much more sense now, I think I'm following your line of reasoning. I'll take a look at applying a "isfakemagicshield" sub for Fanatic's Tonic and Spiritual Incense since these offer the MDT UMDT adjustments, but not the actual magic immunity.
