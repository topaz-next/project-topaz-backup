**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Friday Sep 18, 2020 at 05:55:12_
_Originally opened as: project-topaz/topaz - Issue 1152_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

debug log below, first stack overflow was onSpellCast. Related to luautils?

```[17/Sep] [22:40:28][Info] parse: 01A | 1715 1714 0E from user: Macvean
[17/Sep] [22:40:28][Action Info] CLIENT Macvean PERFORMING ACTION 07
[17/Sep] [22:40:28][Error] luautils::onSpellCast: stack overflow
[17/Sep] [22:40:28][Error] luautils::onUseWeaponSkill: ./scripts/globals/weaponskills.lua:218: stack overflow
[17/Sep] [22:40:28][Navmesh Error] CNavMesh::findPath Couldn't find path (179.000000, -19.000000, 127.000000)->(244.465912, -15.461306, 142.510529) (52)
[17/Sep] [22:40:28][Navmesh Error] CNavMesh::findPath Couldn't find path (0.000000, 0.000000, 0.000000)->(-471.527954, -21.469034, -91.409157) (52)
[17/Sep] [22:40:28][Navmesh Error] CPathFind::FindPath Entity (16990443) could not find path
[17/Sep] [22:40:29][Navmesh Error] CNavMesh::findRandomPath startRef is invalid (150.000000, -18.000000, -496.000000) (52)
[17/Sep] [22:40:29][Navmesh Error] CNavMesh::findPath Couldn't find path (0.000000, 0.000000, 0.000000)->(-471.812500, -21.469034, -90.968765) (52)
[17/Sep] [22:40:29][Navmesh Error] CPathFind::FindPath Entity (16990443) could not find path
[17/Sep] [22:40:29][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:29][Navmesh Error] CNavMesh::findPath Couldn't find path (0.000000, 0.000000, 0.000000)->(-473.061920, -20.188343, -90.034248) (52)
[17/Sep] [22:40:29][Navmesh Error] CPathFind::FindPath Entity (16990443) could not find path
[17/Sep] [22:40:29][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:29][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:29][Navmesh Error] CNavMesh::findPath Couldn't find path (0.000000, 0.000000, 0.000000)->(-472.656677, -20.188343, -89.120041) (52)
[17/Sep] [22:40:29][Navmesh Error] CPathFind::FindPath Entity (16990443) could not find path
[17/Sep] [22:40:29][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:29][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:30][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:30][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:30][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:30][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:30][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:30][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:30][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:30][Navmesh Error] CNavMesh::findPath Couldn't find path (0.000000, 0.000000, 0.000000)->(-472.251434, -20.188343, -88.205833) (52)
[17/Sep] [22:40:30][Navmesh Error] CPathFind::FindPath Entity (16990443) could not find path
[17/Sep] [22:40:30][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:30][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:30][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:30][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:30][Navmesh Error] CNavMesh::findPath Couldn't find path (0.000000, 0.000000, 0.000000)->(-471.846191, -20.188343, -87.291626) (52)
[17/Sep] [22:40:30][Navmesh Error] CPathFind::FindPath Entity (16990443) could not find path
[17/Sep] [22:40:30][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:30][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:30][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:30][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:31][Error] luautils::onSpellCast: stack overflow
[17/Sep] [22:40:31][Navmesh Error] CNavMesh::findPath Couldn't find path (0.000000, 0.000000, 0.000000)->(-471.440948, -20.188343, -86.377419) (52)
[17/Sep] [22:40:31][Navmesh Error] CPathFind::FindPath Entity (16990443) could not find path
[17/Sep] [22:40:31][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:31][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:31][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:31][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:31][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:31][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:31][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:31][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:31][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:31][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:31][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:31][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:31][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:31][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:31][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:31][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:31][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:31][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:31][Error] luautils::onSpellCast: stack overflow
[17/Sep] [22:40:31][Navmesh Error] CNavMesh::findPath Couldn't find path (0.000000, 0.000000, 0.000000)->(-471.035706, -20.188343, -85.463211) (52)
[17/Sep] [22:40:31][Navmesh Error] CPathFind::FindPath Entity (16990443) could not find path
[17/Sep] [22:40:31][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:31][Error] luautils::onMobFight: stack overflow
[17/Sep] [22:40:31][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:31][Error] luautils::onMobFight: stack overflow
[17/Sep] [22:40:31][Error] luautils::onSpellCast: stack overflow
[17/Sep] [22:40:31][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:31][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:31][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:31][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:31][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:31][Info] parse: 016 | 07CD 07C8 04 from user: Kong
[17/Sep] [22:40:31][Error] luautils::onZoneWeatherChange: stack overflow
[17/Sep] [22:40:31][Navmesh Error] CNavMesh::findPath Couldn't find path (0.000000, 0.000000, 0.000000)->(-470.630463, -20.188343, -84.549004) (52)
[17/Sep] [22:40:31][Navmesh Error] CPathFind::FindPath Entity (16990443) could not find path
[17/Sep] [22:40:31][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:31][Error] luautils::onMobFight: stack overflow
[17/Sep] [22:40:31][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:31][Error] luautils::onMobFight: stack overflow
[17/Sep] [22:40:32][Error] luautils::onZoneWeatherChange: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Info] parse: 117 | 07CE 07C9 04 from user: Kong
[17/Sep] [22:40:32][Info] parse: 01A | 12CD 12C8 0E from user: Wendy
[17/Sep] [22:40:32][Action Info] CLIENT Wendy PERFORMING ACTION 09
[17/Sep] [22:40:32][Navmesh Error] CNavMesh::findPath Couldn't find path (0.000000, 0.000000, 0.000000)->(-470.200409, -20.188343, -83.645432) (52)
[17/Sep] [22:40:32][Navmesh Error] CPathFind::FindPath Entity (16990443) could not find path
[17/Sep] [22:40:32][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:32][Error] luautils::onMobFight: stack overflow
[17/Sep] [22:40:32][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:32][Error] luautils::onMobFight: stack overflow
[17/Sep] [22:40:32][Error] luautils::onAbilityCheck: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Navmesh Error] CNavMesh::findPath Couldn't find path (0.000000, 0.000000, 0.000000)->(-469.832764, -20.188343, -82.747726) (52)
[17/Sep] [22:40:32][Navmesh Error] CPathFind::FindPath Entity (16990443) could not find path
[17/Sep] [22:40:32][Error] [Lua] Anonymous function: stack overflow
17/Sep] [22:40:32][Error] luautils::onMobFight: stack overflow
[17/Sep] [22:40:32][Error] luautils::onAbilityCheck: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Navmesh Error] CNavMesh::findPath Couldn't find path (0.000000, 0.000000, 0.000000)->(-469.832764, -20.188343, -82.747726) (52)
[17/Sep] [22:40:32][Navmesh Error] CPathFind::FindPath Entity (16990443) could not find path
[17/Sep] [22:40:32][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:32][Error] luautils::onMobFight: stack overflow
[17/Sep] [22:40:32][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:32][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:32][Error] luautils::onMobFight: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:32][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:33][Error] roeutils::onRecordTrigger: ./scripts/globals/roe.lua:44: stack overflow
[17/Sep] [22:40:33][Error] roeutils::onRecordTrigger: ./scripts/globals/roe.lua:44: stack overflow
[17/Sep] [22:40:33][Error] roeutils::onRecordTrigger: ./scripts/globals/roe.lua:44: stack overflow
[17/Sep] [22:40:33][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:33][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:33][Error] luautils::onMobFight: stack overflow
[17/Sep] [22:40:33][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:33][Error] [Lua] Anonymous function: stack overflow
[17/Sep] [22:40:33][Error] luautils::onMobFight: stack overflow
[17/Sep] [22:40:33][Error] luautils::onSpellCast: stack overflow
[17/Sep] [22:40:33][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:33][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:33][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:33][Error] luautils::onPath: stack overflow
[17/Sep] [22:40:33][Info] parse: 01A | 12D0 12CB 0E from user: Wendy
[17/Sep] [22:40:33][Action Info] CLIENT Wendy PERFORMING ACTION 09
[17/Sep] [22:40:33][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:33][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:33][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:33][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:33][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:33][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:33][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:33][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:33][Error] luautils::onMobRoam: stack overflow
```
......
```
[17/Sep] [22:40:36][Error] [Lua] Anonymous function: ./scripts/mixins/families/colibri_mimic.lua:36: stack overflow
[17/Sep] [22:40:36][Error] luautils::onMobFight: stack overflow
[17/Sep] [22:40:36][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:36][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:36][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:36][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:36][Error] luautils::onMobRoam: stack overflow
[17/Sep] [22:40:36][Error] luautils::onMagicCastingCheck: stack overflow
PANIC: unprotected error in call to Lua API (stack overflow)
terminate called without an active exception

Thread 1 "topaz_game" received signal SIGABRT, Aborted.
__GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:51
51      ../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
46      in ../sysdeps/unix/sysv/linux/raise.c
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:51
#1  0x00007ffff61f38b1 in __GI_abort () at abort.c:79 
#2  0x00007ffff6848957 in ?? () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#3  0x00007ffff684eae6 in ?? () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#4  0x00007ffff684eb21 in std::terminate() () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#5  0x0000555555630dc1 in std::thread::~thread (this=<optimized out>, __in_chrg=<optimized out>)
    at /usr/include/c++/7/thread:135
#6  0x00007ffff61f60f1 in __run_exit_handlers (status=1, listp=0x7ffff659e718 <__exit_funcs>,
    run_list_atexit=run_list_atexit@entry=true, run_dtors=run_dtors@entry=true) at exit.c:108
#7  0x00007ffff61f61ea in __GI_exit (status=<optimized out>) at exit.c:139
#8  0x00007ffff7b71cb9 in ?? () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#9  0x00007ffff7b865af in ?? () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#10 0x00007ffff7b756e1 in ?? () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#11 0x00007ffff7b756fb in ?? () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#12 0x00007ffff7b75022 in ?? () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#13 0x0000555555605ee3 in Lunar<CLuaAbility>::push (L=0x40000378, obj=0x7fffffffd980, gc=<optimized out>)
    at src/map/lua/../../common/lua/lunar.h:137
#14 0x00005555555fe381 in luautils::OnUseAbility (PUser=PUser@entry=0x5555873836c0,
    PTarget=PTarget@entry=0x55556e4c4040, PAbility=PAbility@entry=0x55557f2cdd80, action=action@entry=0x7fffffffdb90)
    at src/map/lua/luautils.cpp:3703
#15 0x00005555555dbeab in CTrustEntity::OnAbility (this=0x5555873836c0, state=..., action=...)
    at src/map/entities/trustentity.cpp:125
#16 0x00005555555afaed in CAbilityState::Update (this=0x5555866f73b0, tick=...)
    at src/map/ai/states/ability_state.cpp:108
#17 0x0000555555597f6e in CAIContainer::Tick (this=0x555586b6c250, _tick=..., _tick@entry=...)
    at src/map/ai/ai_container.cpp:361
#18 0x00005555556c3fd1 in CZoneEntities::ZoneServer (this=0x555557fed440, tick=..., check_regions=false)
    at src/map/zone_entities.cpp:1099
#19 0x00005555556bd2db in CZone::ZoneServer (this=0x555558b8fb50, tick=..., check_regions=<optimized out>)
    at src/map/zone.cpp:806
#20 0x00005555556be0b3 in zone_server (tick=..., PTask=<optimized out>) at src/map/zone.cpp:83
#21 0x00005555555920f9 in CTaskMgr::DoTimer (this=0x555555ac6b10, tick=...) at src/common/taskmgr.cpp:78
#22 0x0000555555571a80 in main (argc=1, argv=0x7fffffffdf98) at src/common/kernel.cpp:267
   0x7ffff61f1f41 <__GI_raise+193>:     (bad)
   0x7ffff61f1f42 <__GI_raise+194>:     add    %al,(%rax)
   0x7ffff61f1f44 <__GI_raise+196>:     add    %cl,(%rdi)
   0x7ffff61f1f46 <__GI_raise+198>:     add    $0x248c8b48,%eax
   0x7ffff61f1f4b <__GI_raise+203>:     or     %al,(%rcx)
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Sep 18, 2020 at 12:45:08_

----

stack corruption on the lua side can cayse that error to constantly trip on any/all/random/unrelated lua things after the point at which it went "bad". need to audit the lua bindings and see where we introduced a stack problem. something shoved the wrong amount of stuff into the stack.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Sep 19, 2020 at 17:09:22_

----

another one just 30 minutes ago, looks about the same so posting it here as a same bug

```
46	in ../sysdeps/unix/sysv/linux/raise.c
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:51
#1  0x00007ffff61f38b1 in __GI_abort () at abort.c:79
#2  0x00007ffff6848957 in ?? () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#3  0x00007ffff684eae6 in ?? () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#4  0x00007ffff684eb21 in std::terminate() () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#5  0x0000555555630dc1 in std::thread::~thread (this=<optimized out>, __in_chrg=<optimized out>) at /usr/include/c++/7/thread:135
#6  0x00007ffff61f60f1 in __run_exit_handlers (status=1, listp=0x7ffff659e718 <__exit_funcs>, run_list_atexit=run_list_atexit@entry=true, run_dtors=run_dtors@entry=true)
    at exit.c:108
#7  0x00007ffff61f61ea in __GI_exit (status=<optimized out>) at exit.c:139
#8  0x00007ffff7b71cb9 in ?? () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#9  0x00007ffff7b71d51 in ?? () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#10 0x00007ffff7b90f36 in ?? () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#11 0x00007ffff7b91663 in ?? () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#12 0x00007ffff7b91b2c in ?? () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#13 0x00007ffff7bb3378 in lua_loadx () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#14 0x00007ffff7bb340a in luaL_loadfilex () from /usr/lib/x86_64-linux-gnu/libluajit-5.1.so.2
#15 0x00005555555f6c7d in luautils::prepFile (File=File@entry=0x7fffffffda70 "scripts/zones/Crawlers_Nest/mobs/Vespo.lua", function=function@entry=0x5555556e5c85 "onMobRoam")
    at src/map/lua/luautils.cpp:257
#16 0x00005555555fd2f8 in luautils::OnMobRoam (PMob=<optimized out>) at src/map/lua/luautils.cpp:3171
#17 0x00005555555a4288 in CMobController::DoRoamTick (this=0x555578fa5e90, tick=...) at src/map/ai/controllers/mob_controller.cpp:835
#18 0x0000555555598073 in CAIContainer::Tick (this=0x555578fa5f90, _tick=_tick@entry=...) at src/map/ai/ai_container.cpp:358
#19 0x00005555556c3e20 in CZoneEntities::ZoneServer (this=0x5555656f6310, tick=..., check_regions=false) at src/map/zone_entities.cpp:1047
#20 0x00005555556bd2db in CZone::ZoneServer (this=0x555565688790, tick=..., check_regions=<optimized out>) at src/map/zone.cpp:806
#21 0x00005555556be0b3 in zone_server (tick=..., PTask=<optimized out>) at src/map/zone.cpp:83
#22 0x00005555555920f9 in CTaskMgr::DoTimer (this=0x555555ac6b10, tick=...) at src/common/taskmgr.cpp:78
#23 0x0000555555571a80 in main (argc=1, argv=0x7fffffffdf98) at src/common/kernel.cpp:267
   0x7ffff61f1f41 <__GI_raise+193>:	(bad)  
   0x7ffff61f1f42 <__GI_raise+194>:	add    %al,(%rax)
   0x7ffff61f1f44 <__GI_raise+196>:	add    %cl,(%rdi)
   0x7ffff61f1f46 <__GI_raise+198>:	add    $0x248c8b48,%eax
   0x7ffff61f1f4b <__GI_raise+203>:	or     %al,(%rcx)
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 21, 2020 at 11:07:07_

----

@kaincenteno When did these start happening?
https://github.com/project-topaz/topaz/releases/tag/C202009-02
or 
https://github.com/project-topaz/topaz/releases/tag/C202009-03?

If we can narrow down which release they started after then we can go through each PR and inspect how they play with the stack


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Sep 21, 2020 at 19:44:22_

----

@zach2good  it started happening with https://github.com/project-topaz/topaz/releases/tag/C202009-02

I'm going to keep an eye on it if it still occurs with https://github.com/project-topaz/topaz/releases/tag/C202009-03, server was update 26 hours ago and it's still up and running. Our population at a single time doesnt go above 12 users concurrently online, but hopefully it increases to be able to notice these sort of issues.
