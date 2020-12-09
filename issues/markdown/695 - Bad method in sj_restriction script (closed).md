**Labels:**



<a href="https://github.com/whasf"><img src="https://avatars3.githubusercontent.com/u/6373706?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [whasf](https://github.com/whasf)**
_Saturday Jun 06, 2020 at 23:29:30_
_Originally opened as: project-topaz/topaz - Issue 695_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

luautils::onEffectLose: scripts/globals/effects/sj_restriction.lua:24: attempt to call method 'sjRestriction' (a nil value)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jun 06, 2020 at 23:39:43_

----

Looking like this method doesn't exist; and [the effect script itself](https://github.com/project-topaz/topaz/blob/release/scripts/globals/effects/sj_restriction.lua) feels off.

Looking at the history, kj did implement it as part of the bcnm branch:
<https://github.com/project-topaz/topaz/commit/22d6a6208de337bb126019ff4a9b6addb1b2d776#diff-69a67ebc82338a85694844fa4e41584b>

But then removed the redundant function, updating the effect script to account for it:
<https://github.com/project-topaz/topaz/commit/76aad6d23d05a966010df7f2b14ee788b254a861#diff-69a67ebc82338a85694844fa4e41584b>

Then master was merged into bcnm, and the older script which calls the now-removed sjRestriction function was accidentally picked during merge conflicts:
<https://github.com/project-topaz/topaz/commit/78ce0d363258739d6899579088412ef6cb97190a#diff-69a67ebc82338a85694844fa4e41584b>


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 06, 2020 at 23:40:41_

----

iirc that got removed from core during the bcnm rewrite so the binding ceased to exist.

```cpp
/************************************************************************
*  Function: sjRestriction()
*  Purpose : Places a sub-job restriction on the PC and recalculates stats
*  Example : target:sjRestriction(power,false);
*  Notes   : If true is provided, removes SJ completely; else - sets level
************************************************************************/

inline int32 CLuaBaseEntity::sjRestriction(lua_State* L)
{
    DSP_DEBUG_BREAK_IF(m_PBaseEntity == nullptr);
    DSP_DEBUG_BREAK_IF(m_PBaseEntity->objtype != TYPE_PC);

    CCharEntity* PChar = (CCharEntity*)m_PBaseEntity;

    uint8 job = (uint8)lua_tonumber(L, 1);
    bool state = lua_toboolean(L, 2);

    if (state)
        PChar->SetSJob(JOB_NON);
    else if (!state && job != JOB_NON)
    {
        PChar->SetSJob(job);
        PChar->SetSLevel(PChar->jobs.job[PChar->GetSJob()]);
    }

    charutils::BuildingCharSkillsTable(PChar);
    charutils::CalculateStats(PChar);
    charutils::BuildingCharAbilityTable(PChar);
    charutils::BuildingCharTraitsTable(PChar);
    charutils::CheckValidEquipment(PChar);

    PChar->UpdateHealth();
    PChar->health.hp = PChar->GetMaxHP();
    PChar->health.mp = PChar->GetMaxMP();

    PChar->pushPacket(new CCharJobsPacket(PChar));
    PChar->pushPacket(new CCharUpdatePacket(PChar));
    PChar->pushPacket(new CCharHealthPacket(PChar));
    PChar->pushPacket(new CCharStatsPacket(PChar));
    PChar->pushPacket(new CCharSkillsPacket(PChar));
    PChar->pushPacket(new CCharRecastPacket(PChar));
    PChar->pushPacket(new CCharAbilitiesPacket(PChar));
    PChar->pushPacket(new CCharJobExtraPacket(PChar, true));
    PChar->pushPacket(new CCharJobExtraPacket(PChar, false));
    PChar->pushPacket(new CMenuMeritPacket(PChar));
    PChar->pushPacket(new CCharSyncPacket(PChar));
    return 0;
}
```

was its content


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 06, 2020 at 23:40:56_

----

ibm beat me to finding the exact commits


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 06, 2020 at 23:43:06_

----

So it just needs replaced by `target:recalculateStats()` then from the looks of those commits
