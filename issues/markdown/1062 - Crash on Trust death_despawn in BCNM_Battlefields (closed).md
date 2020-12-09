**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Sep 05, 2020 at 07:07:46_
_Originally opened as: project-topaz/topaz - Issue 1062_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

from Canaria players, it happens when releasing trusts in BCNM. Tagging @jarmengaud  for more info
```
[02/Sep] [08:51:12][Debug] CZone:: Monastic_Cavern IncreaseZoneCounter <1> Brain 
[02/Sep] [08:51:12][Info] parse: 00D | 0143 0141 04 from user: Yinnyboy
[02/Sep] [08:51:12][Debug] CZone:: Bastok_Markets DecreaseZoneCounter <0> Yinnyboy
[02/Sep] [08:51:12][Info] parse: 011 | 0002 0001 04 from user: Brain
```
```
Thread 1 "topaz_game" received signal SIGSEGV, Segmentation fault.
CStatusEffect::GetFlag (this=0x7573656b01043780)
    at src/map/status_effect.cpp:94
94              return m_Flag;
89          return m_Tier;
90      }
91
92      uint32 CStatusEffect::GetFlag()
---Type <return> to continue, or q <return> to quit---
93      {
94              return m_Flag;
95      }
96
97      uint32 CStatusEffect::GetTickTime()
98      {
#0  CStatusEffect::GetFlag (this=0x7573656b01043780) at src/map/status_effect.cpp:94
#1  0x000055555566abab in CStatusEffectContainer::DelStatusEffectsByFlag (this=0x555586903770, flag=flag@entry=524288,
    silent=silent@entry=true) at src/map/status_effect_container.cpp:648
#2  0x00005555555dce4c in CBattlefield::RemoveEntity (this=0x5555867284f0, PEntity=PEntity@entry=0x555586906d50,
    leavecode=leavecode@entry=3 '\003') at src/map/battlefield.cpp:488
#3  0x00005555555c6010 in CBaseEntity::~CBaseEntity (this=0x555586906d50, __in_chrg=<optimized out>)
    at src/map/entities/baseentity.cpp:55
#4  0x00005555555dbbf3 in CTrustEntity::~CTrustEntity (this=0x555586906d50, __in_chrg=<optimized out>)
    at src/map/entities/trustentity.h:33
#5  CTrustEntity::~CTrustEntity (this=0x555586906d50, __in_chrg=<optimized out>) at src/map/entities/trustentity.h:33
#6  0x00005555556c1330 in CZoneEntities::ZoneServer (this=0x55555a092bf0, tick=..., check_regions=false)
    at src/map/zone_entities.cpp:1116
#7  0x00005555556ba4ab in CZone::ZoneServer (this=0x555559c588d0, tick=..., check_regions=<optimized out>)
    at src/map/zone.cpp:806
#8  0x00005555556bb283 in zone_server (tick=..., PTask=<optimized out>) at src/map/zone.cpp:83
#9  0x0000555555591f99 in CTaskMgr::DoTimer (this=0x555555ac0b10, tick=...) at src/common/taskmgr.cpp:78
#10 0x0000555555571920 in main (argc=1, argv=0x7fffffffdf98) at src/common/kernel.cpp:267
   0x555555667a8a:      test   %al,(%rax)
   0x555555667a8c:      add    %al,(%rax)
   0x555555667a8e:      add    %al,(%rax)
=> 0x555555667a90 <CStatusEffect::GetFlag()>:   mov    0x38(%rdi),%eax
   0x555555667a93 <CStatusEffect::GetFlag()+3>: retq
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 07, 2020 at 06:11:18_

----

So, the _previous crash_ was because Trusts were being let in here:
https://github.com/project-topaz/topaz/blob/canary/src/map/battlefield.cpp#L459

_This crash_ is because they've made it past that point and land in here:
https://github.com/project-topaz/topaz/blob/canary/src/map/battlefield.cpp#L488

I've **never** been able to reproduce this, so it's extremely hard for me to debug it properly without risking destroying things. For instance, we could set trusts to skip this entire section - but then they would remain on the enmity lists of monsters.

**EDIT:** After a little chat in Discord, this might fix the issue (CBattleEntity being called after it's already gone). The idea is that it'll try to cast PEntity down into a CBattleEntity and only continue if that succeeds. If that fails, it won't try to do the things:

**Replace this section:** 
https://github.com/project-topaz/topaz/blob/canary/src/map/battlefield.cpp#L485-L491

```cpp
// Remove enmity from valid battle entities
if (auto PBattleEntity = dynamic_cast<CBattleEntity*>(PEntity))
{
    PBattleEntity->StatusEffectContainer->DelStatusEffectsByFlag(EFFECTFLAG_CONFRONTATION, true);
    PBattleEntity->StatusEffectContainer->DelStatusEffect(EFFECT_LEVEL_RESTRICTION);
    ClearEnmityForEntity(PBattleEntity);
}
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Sep 08, 2020 at 07:17:03_

----

Original crash seems to be fixed, replaced with this one:
https://github.com/project-topaz/topaz/blob/canary/src/map/zone_entities.cpp#L570

Looks like released Trusts aren't being removed from the zone's trustList, so when the pointer to them is eventually de-referenced in `CTrustSyncPacket`, it's all screwed up.
 
```
[07/Sep] [17:17:40][Debug] CZone:: The_Shrine_of_RuAvitau IncreaseZoneCounter <2> Macncheese 
[07/Sep] [17:17:41][Info] parse: 011 | 0002 0001 04 from user: Macncheese
[07/Sep] [17:17:42][Info] parse: 016 | 0822 0821 04 from user: Macvean
[07/Sep] [17:17:42][Info] parse: 00C | 0003 0002 06 from user: Macncheese
[07/Sep] [17:17:42][Info] parse: 061 | 0003 0002 04 from user: Macncheese
[07/Sep] [17:17:42][Info] parse: 118 | 0003 0002 04 from user: Macncheese
[07/Sep] [17:17:42][Warning] parse: Unhandled game packet 118 from user: Macncheese
[07/Sep] [17:17:42][Info] parse: 11B | 0003 0002 04 from user: Macncheese
[07/Sep] [17:17:42][Warning] parse: Unhandled game packet 11B from user: Macncheese
[07/Sep] [17:17:42][Info] parse: 053 | 0003 0002 44 from user: Macncheese
[07/Sep] [17:17:42][Info] parse: 01A | 0003 0002 0E from user: Macncheese

Thread 1 "topaz_game" received signal SIGSEGV, Segmentation fault.
CTrustSyncPacket::CTrustSyncPacket (this=0x5555870fbad0, PChar=0x0, PTrust=0x5555870c3f50) at src/map/packets/trust_sync.cpp:45
45          ref<uint16>(0x0C) = PChar->targid;
40          ref<uint8>(0x04) = 0x03;
41          ref<uint8>(0x05) = 0x05;
42
43          ref<uint16>(0x06) = PTrust->targid;
44          ref<uint32>(0x08) = PTrust->id;
45          ref<uint16>(0x0C) = PChar->targid;
46
47          packBitsBE(data + (0x04), (0x18) + PTrust->packetName.size(), 0, 6, 10); // Message Size
48          memcpy(data + (0x18), PTrust->packetName.c_str(), PTrust->packetName.size());
49
#0  CTrustSyncPacket::CTrustSyncPacket (this=0x5555870fbad0, PChar=0x0, PTrust=0x5555870c3f50) at src/map/packets/trust_sync.cpp:45
#1  0x00005555556c2f5f in CZoneEntities::SpawnTRUSTs (this=<optimized out>, PChar=0x555587154260) at src/map/zone_entities.cpp:570
#2  0x000055555565567b in SmallPacket0x01A (session=<optimized out>, PChar=0x555587154260, data=...) at src/map/packet_system.cpp:826
#3  0x000055555562f77e in parse (buff=0x555586e28400 "\003", buffsize=buffsize@entry=0x7fffffffdd28, from=from@entry=0x7fffffffdd40,
    map_session_data=map_session_data@entry=0x5555870fe8f0) at src/map/map.cpp:605
#4  0x000055555562fe18 in do_sockets (rfd=<optimized out>, next=...) at src/map/map.cpp:386
#5  0x000055555557192b in main (argc=1, argv=0x7fffffffdf98) at src/common/kernel.cpp:268
   0x5555556436f9 <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+153>:        lea    0x4(%rax),%edi
   0x5555556436fc <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+156>:        mov    %edx,0x8(%rax)
---Type <return> to continue, or q <return> to quit---
=> 0x5555556436ff <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+159>:        movzwl 0xc(%r13),%edx
   0x555555643704 <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+164>:        mov    %dx,0xc(%rax)
   0x555555643708 <CTrustSyncPacket::CTrustSyncPacket(CCharEntity*, CTrustEntity*)+168>:        xor    %edx,%edx
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
```


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Sep 08, 2020 at 15:44:03_

----

another crash log, looks different Zach

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

^ Canaria player was doing Bastok mission fight again Zeid in Throne Room. 
After 2nd form died he healed Volker (Trust), then it R0 (unsure if the trigger for crash was the healing the trust, or the Mob dying)




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Oct 28, 2020 at 07:44:20_

----

Both of these have been merged for ages and haven't shown up again for a while.

The check with PMaster being null in the packet is fixed, but resulted in Trusts not showing their despawn animation.
That is fixed in this upcoming PR:
https://github.com/project-topaz/topaz/pull/1424
https://github.com/project-topaz/topaz/pull/1424/commits/f3799bf76944bb102e737bbccce7dc27c6c6d66a
