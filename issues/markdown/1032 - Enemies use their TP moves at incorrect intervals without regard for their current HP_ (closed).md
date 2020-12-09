**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Saturday Aug 29, 2020 at 03:38:52_
_Originally opened as: project-topaz/topaz - Issue 1032_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

https://ffxiclopedia.fandom.com/wiki/Tactical_Points
"Monsters will use their TP semi-randomly when at 25% HP or above, until reaching 3000 TP at which point they will use it on one of their special attacks. Once monsters fall below 25% HP, they will no longer save their TP and will attempt to use their special attacks immediately upon reaching 1000 TP."

This is supposedly part of issue #184 as discussed in the last 1/3 of it, but that issue is very unclear and can likely be closed.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Monday Aug 31, 2020 at 04:04:18_

----

I found the offending code; in the function CMobController::DoCombatTick:
```else if (m_Tick >= m_LastMobSkillTime && tpzrand::GetRandomNumber(100) < PMob->TPUseChance() && MobSkill())```
which leads us to ``TPUseChance()``
```
uint8 CMobEntity::TPUseChance()
{
    auto& MobSkillList = battleutils::GetMobSkillList(getMobMod(MOBMOD_SKILL_LIST));

    if (health.tp < 1000 || MobSkillList.empty() == true || !static_cast<CMobController*>(PAI->GetController())->IsWeaponSkillEnabled())
    {
        return 0;
    }

    if (health.tp == 3000 || (GetHPP() <= 25 && health.tp >= 1000))
    {
        return 100;
    }

    return (uint8)getMobMod(MOBMOD_TP_USE_CHANCE);
}
```
MOBMOD_TP_USE_CHANCE defaults to 30 in mobutils.cpp if it's not normally set... but obviously this isn't working as intended.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 31, 2020 at 11:44:23_

----

so it looks like what happened is back when the tickrate was made a shorter time interval that caused the use chance check to fire more often, leading to more frequent tp use at the same hp/tp amounts.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 05, 2020 at 09:24:02_

----

Fixed by https://github.com/project-topaz/topaz/pull/1046



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Sep 05, 2020 at 21:44:00_

----

note: there *may* still be an issue in that its unconfirmed if we should have an on tick random check *at all* but that PR put the rate of fire back where it used to be before the tick rate was changed.

