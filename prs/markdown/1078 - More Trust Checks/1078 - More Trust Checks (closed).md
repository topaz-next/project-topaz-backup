**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Tuesday Sep 08, 2020 at 15:37:54_
_Originally opened as: project-topaz/topaz - Issue 1078_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes https://github.com/project-topaz/topaz/issues/1062
Hah, I wish. The crashes never end.

Death to C-style casts and static casts. Long live dynamic_cast, so we know if all or part of the target pointer's pointee has been deleted, so it'll be unsafe to dereference.

Honestly, I _still_ can't reproduce any of these crashes, on Windows, on Linux, taking off trust limits and zoning, killing, warping, refa-all-ing etc.

Like all the previous "fixes" this doesn't introduce any new crashes for me, but it might move the crash to somewhere else 🤷 



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 09, 2020 at 06:13:52_

----

Gonna target this new crash in this PR also:

For my notes: Bastok Mission 9-2 - Throne Room - Heal Volker (trust) after phase 2.

```
[08/Sep] [08:21:43][Info] parse: 01A | 0243 0242 0E from user: Brain
[08/Sep] [08:21:43][Action Info] CLIENT Brain PERFORMING ACTION 03

Thread 1 "topaz_game" received signal SIGSEGV, Segmentation fault.
battleutils::ClaimMob (PDefender=0x5555875f9860, PAttacker=0x55558721e4e0, passing=<optimized out>) at src/map/utils/battleutils.cpp:4116
4116                                if (highestClaim->objtype == TYPE_TRUST)
4111                                    mob->m_OwnerID.id = PAttacker->id;
4112                                    mob->m_OwnerID.targid = PAttacker->targid;
4113                                    return;
4114                                }
4115                                CBattleEntity* highestClaim = mob->PEnmityContainer->GetHighestEnmity();
4116                                if (highestClaim->objtype == TYPE_TRUST)
4117                                {
4118                                    highestClaim = static_cast<CTrustEntity*>(highestClaim)->PMaster;
4119                                }
4120                                PAttacker->ForAlliance([&](CBattleEntity* PMember){
#0  battleutils::ClaimMob (PDefender=0x5555875f9860, PAttacker=0x55558721e4e0, passing=<optimized out>) at src/map/utils/battleutils.cpp:4116
#1  0x00005555555c7d94 in CBattleEntity::OnCastFinished (this=this@entry=0x55558721e4e0, state=..., action=...) at src/map/entities/battleentity.cpp:1389
#2  0x00005555555d47cc in CCharEntity::OnCastFinished (this=0x55558721e4e0, state=..., action=...) at src/map/entities/charentity.cpp:714
#3  0x00005555555b4415 in CMagicState::Update (this=0x5555875c3270, tick=...) at src/map/ai/states/magic_state.cpp:121
#4  0x0000555555597e0e in CAIContainer::Tick (this=0x555586ea0bb0, _tick=..., _tick@entry=...) at src/map/ai/ai_container.cpp:361
---Type <return> to continue, or q <return> to quit---
#5  0x00005555556c1d28 in CZoneEntities::ZoneServer (this=0x5555647f7d00, tick=..., check_regions=false) at src/map/zone_entities.cpp:1138
#6  0x00005555556bb0bb in CZone::ZoneServer (this=0x555564792e40, tick=..., check_regions=<optimized out>) at src/map/zone.cpp:806
#7  0x00005555556bbe93 in zone_server (tick=..., PTask=<optimized out>) at src/map/zone.cpp:83
#8  0x0000555555591f99 in CTaskMgr::DoTimer (this=0x555555ac1b10, tick=...) at src/common/taskmgr.cpp:78
#9  0x0000555555571920 in main (argc=1, argv=0x7fffffffdf98) at src/common/kernel.cpp:267
   0x55555567a79b <battleutils::ClaimMob(CBattleEntity*, CBattleEntity*, bool)+555>:    add    %ch,%al
   0x55555567a79d <battleutils::ClaimMob(CBattleEntity*, CBattleEntity*, bool)+557>:    lahf   
   0x55555567a79e <battleutils::ClaimMob(CBattleEntity*, CBattleEntity*, bool)+558>:    cltd   
   0x55555567a79f <battleutils::ClaimMob(CBattleEntity*, CBattleEntity*, bool)+559>:    hlt    
   0x55555567a7a0 <battleutils::ClaimMob(CBattleEntity*, CBattleEntity*, bool)+560>:    incl   0x49201078(%rbx)
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
```

Paging Dr. @cocosolos, who might know some things about claims and BCNMs. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 09, 2020 at 06:15:42_

----

I assume `highestClaim` is invalid after being made on 4115, so when it's checked on 4116 it explodes


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Sep 09, 2020 at 06:20:56_

----

> I assume `highestClaim` is invalid after being made on 4115, so when it's checked on 4116 it explodes

Think you're right, needs to check for null.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 09, 2020 at 06:26:28_

----

At some point before _the journey into release_ I'm going to have to do a deep dive into the management of Trust lifetimes, wrapping every corner of the code that trusts touch with checks is no bueno. Fine for now though.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Sep 09, 2020 at 06:28:11_

----

This function in particular is weird because it's the central spot for claiming so needs special treatment for pets.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 09, 2020 at 11:00:39_

----

My reminder for later:
```cpp
    CBattleEntity* highestClaim = mob->PEnmityContainer->GetHighestEnmity();
    if (highestClaim && highestClaim->objtype == TYPE_TRUST)
    {
        highestClaim = static_cast<CTrustEntity*>(highestClaim)->PMaster;
    }
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 09, 2020 at 11:06:09_

----

Ninja'd in the tiny change from github web, what a time to be alive...

EDIT: I'll do a before and after test with this and see if I can trigger anything, this one looks much more likely than all the previous trust-related crashes

EDIT2: Tested, no more crash when healing Volker (The NPC) or Volker (as a Trust). 

The rest of that BCNM and BCNM allies are all messed up, but at least there's no crash

