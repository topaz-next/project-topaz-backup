**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Sep 29, 2020 at 19:42:14_
_Originally opened as: project-topaz/topaz - Issue 1216_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Filing this as new crash, dont think it's related to old trust issues (stack overflows)

```
[29/Sep] [12:08:50][Info] parse: 01A | 1948 193C 0E from user: Remode
[29/Sep] [12:08:50][Action Info] CLIENT Remode PERFORMING ACTION 03
[29/Sep] [12:08:51][Info] parse: 03A | 194A 193E 04 from user: Remode

Thread 1 "topaz_game" received signal SIGSEGV, Segmentation fault.
battleutils::GenerateCureEnmity (PSource=0x55558777da10, PTarget=0x5555876c0070, amount=254) at src/map/utils/battleutils.cpp:3418
3418                CMobEntity* PCurrentMob = static_cast<CMobEntity*>(it->second);
3413            auto PMasterSource = PSource->PMaster ? PSource->PMaster : PSource;
3414            auto PMasterSourceChar = static_cast<CCharEntity*>(PMasterSource);
3415
3416            for (SpawnIDList_t::const_iterator it = PMasterSourceChar->SpawnMOBList.begin(); it != PMasterSourceChar->SpawnMOBList.end(); ++it)
3417            {
3418                CMobEntity* PCurrentMob = static_cast<CMobEntity*>(it->second);
3419
3420                if (PCurrentMob->m_HiPCLvl > 0 && PCurrentMob->PEnmityContainer->HasID(PTarget->id))
3421                {
3422                    PCurrentMob->PEnmityContainer->UpdateEnmityFromCure(PSource, PTarget->GetMLevel(), amount, (amount == 65535)); //true for "cure v"
#0  battleutils::GenerateCureEnmity (PSource=0x55558777da10, PTarget=0x5555876c0070, amount=254) at src/map/utils/battleutils.cpp:3418
#1  0x0000555555616b23 in CLuaBaseEntity::updateEnmityFromCure (this=0x7fffffffd968, L=<optimized out>) at src/map/lua/lua_baseentity.cpp:10894
#2  0x00007ffff7b64e37 in ?? () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#3  0x00007ffff7bb227c in lua_pcall () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#4  0x00005555555fbe6b in luautils::OnSpellCast (PCaster=PCaster@entry=0x55558777da10, PTarget=PTarget@entry=0x5555876c0070, PSpell=PSpell@entry=0x555581d063f0)
    at src/map/lua/luautils.cpp:2261
#5  0x00005555555c8988 in CBattleEntity::OnCastFinished (this=this@entry=0x55558777da10, state=..., action=...) at src/map/entities/battleentity.cpp:1391
#6  0x00005555555dd0f2 in CTrustEntity::OnCastFinished (this=0x55558777da10, state=..., action=...) at src/map/entities/trustentity.cpp:176
#7  0x00005555555b51f5 in CMagicState::Update (this=0x555583afcd30, tick=...) at src/map/ai/states/magic_state.cpp:121
#8  0x00005555555982ee in CAIContainer::Tick (this=0x555583661ff0, _tick=..., _tick@entry=...) at src/map/ai/ai_container.cpp:361
#9  0x00005555556c77e1 in CZoneEntities::ZoneServer (this=0x5555657d86a0, tick=..., check_regions=false) at src/map/zone_entities.cpp:1099
#10 0x00005555556c0aeb in CZone::ZoneServer (this=0x555565723220, tick=..., check_regions=<optimized out>) at src/map/zone.cpp:806
#11 0x00005555556c18c3 in zone_server (tick=..., PTask=<optimized out>) at src/map/zone.cpp:83
---Type <return> to continue, or q <return> to quit---
#12 0x0000555555592479 in CTaskMgr::DoTimer (this=0x555555ad0b10, tick=...) at src/common/taskmgr.cpp:78
#13 0x0000555555571d60 in main (argc=1, argv=0x7fffffffdf98) at src/common/kernel.cpp:267
   0x55555567c32a <battleutils::GenerateCureEnmity(CBattleEntity*, CBattleEntity*, int)+74>:
    loopne 0x55555567c374 <battleutils::GenerateCureEnmity(CBattleEntity*, CBattleEntity*, int)+148>
   0x55555567c32c <battleutils::GenerateCureEnmity(CBattleEntity*, CBattleEntity*, int)+76>:    mov    %eax,%ebx
   0x55555567c32e <battleutils::GenerateCureEnmity(CBattleEntity*, CBattleEntity*, int)+78>:
    je     0x55555567c390 <battleutils::GenerateCureEnmity(CBattleEntity*, CBattleEntity*, int)+176>
=> 0x55555567c330 <battleutils::GenerateCureEnmity(CBattleEntity*, CBattleEntity*, int)+80>:    mov    0x28(%rbx),%rbp
   0x55555567c334 <battleutils::GenerateCureEnmity(CBattleEntity*, CBattleEntity*, int)+84>:    cmpb   $0x0,0x395(%rbp)
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 29, 2020 at 21:20:43_

----

emani..emaninimi..enmimity.. The code couldn't pronounce it right either and had an aneurysm trying!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 30, 2020 at 05:13:02_

----

> battleutils::GenerateCureEnmity 
https://github.com/project-topaz/topaz/blob/canary/src/map/utils/battleutils.cpp#L3413-L3423

Note to self: This whole function call needs just a little love.
Also,:
```cpp
if (CMobEntity* PCurrentMob = dynamic_cast<CMobEntity*>(it->second))
{
    ...
}
```

Most of the time, static_casting is fine, but there are places where we should be checking before we do. When that happens: dynamic_cast. dynamic_cast isn't free though, so _some_ caution is required. In something that's fired after a spell, rather than on tick: probably fine.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 30, 2020 at 05:49:20_

----

It would be nice to say: "Yeah well, invalid entities should never make it to this point"
.. but they do ..
We should be coding defensively wherever possible


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Oct 03, 2020 at 04:47:15_

----

Server crashed again, it looks about the same kind of crash, unsure 100% if its related but it looks like it on enmity cure

```
[02/Oct] [21:28:14][Action Info] CLIENT Remode PERFORMING ACTION 00
[02/Oct] [21:28:15][Info] parse: 01A | 0147 0144 0E from user: Remode
[02/Oct] [21:28:15][Action Info] CLIENT Remode PERFORMING ACTION 03
[02/Oct] [21:28:16][Info] parse: 029 | 10C7 10C3 06 from user: Kong
[02/Oct] [21:28:16][Info] parse: 03A | 10C8 10C4 04 from user: Kong

Thread 1 "topaz_game" received signal SIGSEGV, Segmentation fault.
0x00007ffff6865fa3 in std::_Rb_tree_increment(std::_Rb_tree_node_base*) () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
230     }
231
232     /************************************************************************
233     *                                                                                                                   ----------------Type <return> to continue, or q <return> to quit---
*
234     *  CORE : MAINROUTINE                                                                                                   *
235     *                                                                                                                               *
236     ************************************************************************/
237
238     int main (int argc, char **argv)
239     {
#0  0x00007ffff6865fa3 in std::_Rb_tree_increment(std::_Rb_tree_node_base*) () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#1  0x000055555567c328 in std::_Rb_tree_const_iterator<std::pair<unsigned int const, CBaseEntity*> >::operator++ (
    this=<synthetic pointer>) at /usr/include/c++/7/bits/stl_tree.h:366
#2  battleutils::GenerateCureEnmity (PSource=0x555588cdcd40, PTarget=0x555588b16930, amount=0) at src/map/utils/battleutils.cpp:3416
#3  0x0000555555616b23 in CLuaBaseEntity::updateEnmityFromCure (this=0x7fffffffd968, L=<optimized out>)
    at src/map/lua/lua_baseentity.cpp:10894
#4  0x00007ffff7b64e37 in ?? () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#5  0x00007ffff7bb227c in lua_pcall () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#6  0x00005555555fbe6b in luautils::OnSpellCast (PCaster=PCaster@entry=0x555588cdcd40, PTarget=PTarget@entry=0x555588b16930,
    PSpell=PSpell@entry=0x555588d56c70) at src/map/lua/luautils.cpp:2261
#7  0x00005555555c8988 in CBattleEntity::OnCastFinished (this=this@entry=0x555588cdcd40, state=..., action=...)
    at src/map/entities/battleentity.cpp:1391
#8  0x00005555555dd0f2 in CTrustEntity::OnCastFinished (this=0x555588cdcd40, state=..., action=...)
    at src/map/entities/trustentity.cpp:176
#9  0x00005555555b51f5 in CMagicState::Update (this=0x5555867fa660, tick=...) at src/map/ai/states/magic_state.cpp:121
#10 0x00005555555982ee in CAIContainer::Tick (this=0x555588c42de0, _tick=..., _tick@entry=...) at src/map/ai/ai_container.cpp:361
#11 0x00005555556c77e1 in CZoneEntities::ZoneServer (this=0x55555e5dedd0, tick=..., check_regions=false)
    at src/map/zone_entities.cpp:1099
#12 0x00005555556c0aeb in CZone::ZoneServer (this=0x55555df477a0, tick=..., check_regions=<optimized out>) at src/map/zone.cpp:806
#13 0x00005555556c18c3 in zone_server (tick=..., PTask=<optimized out>) at src/map/zone.cpp:83
#14 0x0000555555592479 in CTaskMgr::DoTimer (this=0x555555ad0b10, tick=...) at src/common/taskmgr.cpp:78
#15 0x0000555555571d60 in main (argc=1, argv=0x7fffffffdf98) at src/common/kernel.cpp:267
   0x7ffff6865f9d <_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base+13>: add    %r8b,(%rax)
   0x7ffff6865fa0 <_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base+16>: mov    %rdx,%rax
---Type <return> to continue, or q <return> to quit---
=> 0x7ffff6865fa3 <_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base+19>: mov    0x10(%rax),%rdx
   0x7ffff6865fa7 <_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base+23>: test   %rdx,%rdx
   0x7ffff6865faa <_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base+26>: 
    jne    0x7ffff6865fa0 <_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base+16>
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
```




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 03, 2020 at 09:10:29_

----

#1239 was merged by force, not as a PR, so if there isn't a similar crash over the next week or so this issue can be closed 👍 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Oct 04, 2020 at 06:52:10_

----

rebuilt canaria with the fix, hopefully it's stable for the next 7 days =)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Nov 02, 2020 at 06:07:05_

----

Crashed again on Canary C202010-04

```
[01/Nov] [15:42:52][Action Info] CLIENT Myguri PERFORMING ACTION 00
[01/Nov] [15:42:52][Info] parse: 01A | 0E2A 0E29 0E from user: Myguri
[01/Nov] [15:42:52][Action Info] CLIENT Myguri PERFORMING ACTION 00
[01/Nov] [15:42:52][Info] parse: 01A | 0E2A 0E29 0E from user: Myguri
[01/Nov] [15:42:52][Action Info] CLIENT Myguri PERFORMING ACTION 00
[01/Nov] [15:42:52][Info] parse: 01A | 0E2A 0E29 0E from user: Myguri
[01/Nov] [15:42:52][Action Info] CLIENT Myguri PERFORMING ACTION 00
[01/Nov] [15:42:53][Info] parse: 01A | A09A A096 0E from user: Bronard
[01/Nov] [15:42:53][Action Info] CLIENT Bronard PERFORMING ACTION 07
[01/Nov] [15:42:54][Info] parse: 01A | 0E2D 0E2C 0E from user: Myguri
[01/Nov] [15:42:54][Action Info] CLIENT Myguri PERFORMING ACTION 03
[01/Nov] [15:42:54][Info] parse: 03A | 0E2E 0E2D 04 from user: Myguri

Thread 1 "topaz_game" received signal SIGSEGV, Segmentation fault.
0x00007ffff6fa1fa3 in std::_Rb_tree_increment(std::_Rb_tree_node_base*) () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
230     }
231
232     /************************************************************************
233     *                                                                                                                                               *
234     *  CORE : MAINROUTINE                                                                                                   *
235     *                                                                                                                                               *
236     ************************************************************************/
237     #ifndef DEFINE_OWN_MAIN
238     int main (int argc, char **argv)
239     {
#0  0x00007ffff6fa1fa3 in std::_Rb_tree_increment(std::_Rb_tree_node_base*) () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#1  0x00005555555f11e8 in std::_Rb_tree_const_iterator<std::pair<unsigned int const, CBaseEntity*> >::operator++() () at /usr/include/c++/7/bits/stl_tree.h:366
#2  GenerateCureEnmity (amount=65535, PTarget=0x5555a5edddb0, PSource=0x5555a5dd56f0) at /opt/topaz/src/map/utils/battleutils.cpp:3416
#3  CLuaBaseEntity::updateEnmityFromCure(lua_State*) (this=<optimized out>, L=<optimized out>) at /opt/topaz/src/map/lua/lua_baseentity.cpp:10882
#4  0x00007ffff7289e37 in ?? () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#5  0x00007ffff72d727c in lua_pcall () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#6  0x000055555557e720 in luautils::OnSpellCast(CBattleEntity*, CBattleEntity*, CSpell*) (PCaster=PCaster@entry=0x5555a5dd56f0, PTarget=PTarget@entry=0x5555a5edddb0, PSpell=PSpell@entry=0x5555a5f0b780)
    at /opt/topaz/src/map/lua/luautils.cpp:2295
#7  0x000055555560f446 in CBattleEntity::OnCastFinished (this=this@entry=0x5555a5dd56f0, state=..., action=...) at /opt/topaz/src/map/entities/battleentity.cpp:1393
#8  0x000055555564c7b2 in CTrustEntity::OnCastFinished(CMagicState&, action_t&) (this=0x5555a5dd56f0, state=..., action=...) at /opt/topaz/src/map/entities/trustentity.cpp:176
#9  0x000055555558646f in CMagicState::Update(std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<long, std::ratio<1l, 1000000000l> > >) (this=0x5555a5eb5ab0, tick=...)
    at /opt/topaz/src/map/ai/states/magic_state.cpp:121
#10 0x00005555555b71bd in CState::DoUpdate (tick=..., this=0x5555a5eb5ab0) at /opt/topaz/src/map/ai/states/state.cpp:86
#11 CAIContainer::Tick (this=0x5555a5e8aea0, _tick=_tick@entry=...) at /opt/topaz/src/map/ai/ai_container.cpp:361
#12 0x0000555555630d5a in ZoneServer (this=0x5555799ec850, tick=..., check_regions=false) at /opt/topaz/src/map/zone_entities.cpp:1094
#13 0x000055555563123b in ZoneServer (this=0x5555799443c0, tick=..., check_regions=<optimized out>) at /opt/topaz/src/map/zone.cpp:807
#14 0x000055555562ba93 in zone_server (tick=..., PTask=<optimized out>) at /opt/topaz/src/map/zone.cpp:84
#15 0x0000555555571dbb in CTaskMgr::DoTimer (tick=..., this=0x555555a22ff0) at /opt/topaz/src/common/taskmgr.cpp:78
#16 main (argc=<optimized out>, argv=<optimized out>) at /opt/topaz/src/common/kernel.cpp:267
   0x7ffff6fa1f9d <_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base+13>: add    %r8b,(%rax)
   0x7ffff6fa1fa0 <_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base+16>: mov    %rdx,%rax
=> 0x7ffff6fa1fa3 <_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base+19>: mov    0x10(%rax),%rdx
---Type <return> to continue, or q <return> to quit---
   0x7ffff6fa1fa7 <_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base+23>: test   %rdx,%rdx
   0x7ffff6fa1faa <_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base+26>: jne    0x7ffff6fa1fa0 <_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base+16>
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[Info] Topaz[Status] do_init: begin server initialization...             - [OK]
[01/Nov] [15:47:58][Status] do_init: map_config is reading               - [OK]
[01/Nov] [15:47:58][Status] luautils::init:lua initializing...           - [OK]
[01/Nov] [15:47:58][Status] do_init: sqlhandle is allocating             - [OK]
[01/Nov] [15:47:59][Status] do_init: zlib is reading                     - [OK]
[New Thread 0x7ffff4fc2700 (LWP 395)]
[01/Nov] [15:47:59][Status] do_init: loading items[New Thread 0x7fffeffff700 (LWP 396)]
[New Thread 0x7fffef7fe700 (LWP 397)]
```



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Nov 02, 2020 at 07:16:15_

----

Note to self:

https://github.com/project-topaz/topaz/blob/canary/src/map/utils/battleutils.cpp#L3413-L3419

Is something being removed from the iterator while it's iterating? We should wrap `PMasterSourceChar` in a sanity check:
```cpp
        if (auto PMasterSourceChar = dynamic_cast<CCharEntity*>(PSource->PMaster ? PSource->PMaster : PSource))
        {
            for (auto entry : PMasterSourceChar->SpawnMOBList)
            {
                if (CMobEntity* PCurrentMob = dynamic_cast<CMobEntity*>(entry->second))
                {
                    if (PCurrentMob->m_HiPCLvl > 0 && PCurrentMob->PEnmityContainer->HasID(PTarget->id))
                    {
                        PCurrentMob->PEnmityContainer->UpdateEnmityFromCure(PSource, PTarget->GetMLevel(), amount, (amount == 65535)); //true for "cure v"
                    }
                }
            }
        }
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Nov 02, 2020 at 17:11:42_

----

https://github.com/project-topaz/topaz/pull/1424/commits/49b96f7322a49450f57ae72fa10ca923db24fe3f
