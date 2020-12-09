**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:58_
_Originally opened as: project-topaz/topaz - Issue 307_

----

<a href="https://github.com/xipies"><img src="https://avatars3.githubusercontent.com/u/7948457?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [xipies](https://github.com/xipies)**
_Thursday Jun 27, 2019 at 03:30 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6115_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
30190605_0

**_Source Branch_** (master/stable) **:** 
Old School server (updated 2019-06-26)

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Entered Shattering Stars/SMN as 75smn.
Ate rolanberry pie.
Drank melon juice.
Summoned Garuda.
Used Aerial Armor.
Used Release.
Server crashed.





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:00_

----

<a href="https://github.com/whasf"><img src="https://avatars3.githubusercontent.com/u/6373706?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [whasf](https://github.com/whasf)**
_Thursday Jun 27, 2019 at 14:53 GMT_

----

Here is the crash dump: https://1drv.ms/u/s!AvyTIXTmkiRwpXz8Bt6u6F7NMqXm



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:01_

----

<a href="https://github.com/xipies"><img src="https://avatars3.githubusercontent.com/u/7948457?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [xipies](https://github.com/xipies)**
_Thursday Jul 04, 2019 at 20:45 GMT_

----

Reproduced locally.

Exception:
Unhandled exception at 0x01614D07 in DSGame-server.exe: 0xC00000FD: Stack overflow (parameters: 0x00000001, 0x00132FD8). occurred

Stack trace:

```
 	DSGame-server.exe!std::_Iterator_base12::_Orphan_me() Line 214	C++	Symbols loaded.
 	DSGame-server.exe!std::_Iterator_base12::_Adopt(const std::_Container_base12 * _Parent) Line 187	C++	Symbols loaded.
 	DSGame-server.exe!std::_Tree_unchecked_const_iterator<std::_Tree_val<std::_Tree_simple_types<std::pair<unsigned short const ,CBaseEntity *> > >,std::_Iterator_base12>::_Tree_unchecked_const_iterator<std::_Tree_val<std::_Tree_simple_types<std::pair<unsigned short const ,CBaseEntity *> > >,std::_Iterator_base12>(std::_Tree_node<std::pair<unsigned short const ,CBaseEntity *>,void *> * _Pnode, const std::_Tree_val<std::_Tree_simple_types<std::pair<unsigned short const ,CBaseEntity *> > > * _Plist) Line 40	C++	Symbols loaded.
 	DSGame-server.exe!std::_Tree_const_iterator<std::_Tree_val<std::_Tree_simple_types<std::pair<unsigned short const ,CBaseEntity *> > > >::_Tree_const_iterator<std::_Tree_val<std::_Tree_simple_types<std::pair<unsigned short const ,CBaseEntity *> > > >(std::_Tree_node<std::pair<unsigned short const ,CBaseEntity *>,void *> * _Pnode, const std::_Tree_val<std::_Tree_simple_types<std::pair<unsigned short const ,CBaseEntity *> > > * _Plist) Line 203	C++	Symbols loaded.
 	DSGame-server.exe!std::_Tree<std::_Tmap_traits<unsigned short,CBaseEntity *,std::less<unsigned short>,std::allocator<std::pair<unsigned short const ,CBaseEntity *> >,0> >::_Eqrange<unsigned short>(const unsigned short & _Keyval) Line 1976	C++	Symbols loaded.
 	DSGame-server.exe!std::_Tree<std::_Tmap_traits<unsigned short,CBaseEntity *,std::less<unsigned short>,std::allocator<std::pair<unsigned short const ,CBaseEntity *> >,0> >::_Eqrange<unsigned short>(const unsigned short & _Keyval) Line 1984	C++	Symbols loaded.
 	DSGame-server.exe!std::_Tree<std::_Tmap_traits<unsigned short,CBaseEntity *,std::less<unsigned short>,std::allocator<std::pair<unsigned short const ,CBaseEntity *> >,0> >::equal_range(const unsigned short & _Keyval) Line 1509	C++	Symbols loaded.
 	DSGame-server.exe!std::_Tree<std::_Tmap_traits<unsigned short,CBaseEntity *,std::less<unsigned short>,std::allocator<std::pair<unsigned short const ,CBaseEntity *> >,0> >::erase(const unsigned short & _Keyval) Line 1379	C++	Symbols loaded.
 	DSGame-server.exe!CZoneEntities::DeletePET(CBaseEntity * PPet) Line 126	C++	Symbols loaded.
 	DSGame-server.exe!CZone::DeletePET(CBaseEntity * PPet) Line 431	C++	Symbols loaded.
 	DSGame-server.exe!CBattlefield::RemoveEntity(CBaseEntity * PEntity, unsigned char leavecode) Line 467	C++	Symbols loaded.
 	DSGame-server.exe!CBaseEntity::~CBaseEntity() Line 58	C++	Symbols loaded.
<<<<
(repeated 650 times)
 	[External Code]		Annotated Frame
 	DSGame-server.exe!CBattlefield::RemoveEntity(CBaseEntity * PEntity, unsigned char leavecode) Line 468	C++	Symbols loaded.
 	DSGame-server.exe!CBaseEntity::~CBaseEntity() Line 58	C++	Symbols loaded.
>>>>
 	DSGame-server.exe!CBattleEntity::~CBattleEntity() Line 92	C++	Symbols loaded.
 	DSGame-server.exe!CMobEntity::~CMobEntity() Line 142	C++	Symbols loaded.
 	DSGame-server.exe!CPetEntity::~CPetEntity() Line 55	C++	Symbols loaded.
 	[External Code]		Annotated Frame
 	DSGame-server.exe!CZoneEntities::ZoneServer(std::chrono::time_point<std::chrono::system_clock,std::chrono::duration<__int64,std::ratio<1,10000000> > > tick, bool check_regions) Line 974	C++	Symbols loaded.
 	DSGame-server.exe!CZone::ZoneServer(std::chrono::time_point<std::chrono::system_clock,std::chrono::duration<__int64,std::ratio<1,10000000> > > tick, bool check_regions) Line 782	C++	Symbols loaded.
 	DSGame-server.exe!zone_server(std::chrono::time_point<std::chrono::system_clock,std::chrono::duration<__int64,std::ratio<1,10000000> > > tick, CTaskMgr::CTask * PTask) Line 85	C++	Symbols loaded.
 	DSGame-server.exe!CTaskMgr::DoTimer(std::chrono::time_point<std::chrono::system_clock,std::chrono::duration<__int64,std::ratio<1,10000000> > > tick) Line 71	C++	Symbols loaded.
 	DSGame-server.exe!main(int argc, char * * argv) Line 269	C++	Symbols loaded.
 	[External Code]		Annotated Frame
 	[Frames below may be incorrect and/or missing, no symbols loaded for kernel32.dll]		Annotated Frame
```




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:02_

----

<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Sep 01, 2019 at 21:24 GMT_

----

Not only happening to Shattering Stars/SMN, but confirmed also happening with BST both on release of pet and BST and on different BCNM like Creeping Doom, and Trial by Lightning.

`[01/Sep] [14:16:23][Fatal Error] --- gdb backtrace ---
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
0x00007efbfea4023a in __waitpid (pid=2656, stat_loc=0x0, options=0) at ../sysdeps/unix/sysv/linux/waitpid.c:30
Saved corefile core.2561
Darkstar Issue 0  0x00007efbfea4023a in __waitpid (pid=2656, stat_loc=0x0, options=0) at ../sysdeps/unix/sysv/linux/waitpid.c:30
Darkstar Issue 1  0x0000565555580383 in dump_backtrace () at src/common/kernel.cpp:128
Darkstar Issue 2  0x0000565555580725 in sig_proc (sn=6) at src/common/kernel.cpp:162
Darkstar Issue 3  <signal handler called>
Darkstar Issue 4  __GI_raise (sig=sigentry=6) at ../sysdeps/unix/sysv/linux/raise.c:51
Darkstar Issue 5  0x00007efbfd89c801 in __GI_abort () at abort.c:79
Darkstar Issue 6  0x00007efbfd88c39a in __assert_fail_base (fmt=0x7efbfda137d8 "%s%s%s:%u: %s%sAssertion `%s' failed.\n%n", assertion=assertionentry=0x5655556bea47 "rc == 0", file=fileentry=0x5655556bea32 "/usr/include/zmq.hpp", line=lineentry=406, function=functionentry=0x5655556beea0 <zmq::context_t::~context_t()::__PRETTY_FUNCTION__> "zmq::context_t::~context_t()") at assert.c:92
Darkstar Issue 7  0x00007efbfd88c412 in __GI___assert_fail (assertion=assertionentry=0x5655556bea47 "rc == 0", file=fileentry=0x5655556bea32 "/usr/include/zmq.hpp", line=lineentry=406, function=functionentry=0x5655556beea0 <zmq::context_t::~context_t()::__PRETTY_FUNCTION__> "zmq::context_t::~context_t()") at assert.c:101
Darkstar Issue 8  0x00005655555ba0e4 in zmq::context_t::~context_t (this=<optimized out>, __in_chrg=<optimized out>) at /usr/include/zmq.hpp:406
Darkstar Issue 9  0x00007efbfd89f041 in __run_exit_handlers (status=statusentry=1, listp=0x7efbfdc47718 <__exit_funcs>, run_list_atexit=run_list_atexitentry=true, run_dtors=run_dtorsentry=true) at exit.c:108
Darkstar Issue 10 0x00007efbfd89f13a in __GI_exit (status=statusentry=1) at exit.c:139
Darkstar Issue 11 0x000056555561d959 in do_final (code=codeentry=1) at src/map/map.cpp:284
Darkstar Issue 12 0x000056555561d97e in do_abort () at src/map/map.cpp:295
Darkstar Issue 13 0x000056555558072a in sig_proc (sn=11) at src/common/kernel.cpp:163
Darkstar Issue 14 <signal handler called>
Darkstar Issue 15 0x0000000000000000 in ?? ()
Darkstar Issue 16 0x00005655555d5b7d in CBattlefield::RemoveEntity (this=0x565587311b50, PEntity=PEntityentry=0x56558731e3c0, leavecode=leavecodeentry=3 '\003') at src/map/battlefield.cpp:468
Darkstar Issue 17 0x00005655555c04d0 in CBaseEntity::~CBaseEntity (this=0x56558731e3c0, __in_chrg=<optimized out>) at src/map/entities/baseentity.cpp:57
Darkstar Issue 18 0x00005655555d3413 in CPetEntity::~CPetEntity (this=0x56558731e3c0, __in_chrg=<optimized out>) at src/map/entities/petentity.cpp:53
Darkstar Issue 19 CPetEntity::~CPetEntity (this=0x56558731e3c0, __in_chrg=<optimized out>) at src/map/entities/petentity.cpp:55
Darkstar Issue 20 0x00005655556ac5cd in CZoneEntities::ZoneServer (this=0x565565914c50, tick=..., check_regions=false) at src/map/zone_entities.cpp:974
Darkstar Issue 21 0x00005655556a657b in CZone::ZoneServer (this=0x565565914b60, tick=..., check_regions=<optimized out>) at src/map/zone.cpp:780
Darkstar Issue 22 0x00005655556a6956 in zone_server (tick=..., PTask=<optimized out>) at src/map/zone.cpp:85
Darkstar Issue 23 0x000056555558fd89 in CTaskMgr::DoTimer (this=0x565557a65ed0, tick=...) at src/common/taskmgr.cpp:71
Darkstar Issue 24 0x000056555556f8b0 in main (argc=1, argv=0x7ffbffffb0d8) at src/common/kernel.cpp:269
double free or corruption (!prev)
`
tagging UynGH as he was also able to reproduce locally



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:03_

----

<a href="https://github.com/Safhaven"><img src="https://avatars1.githubusercontent.com/u/22181123?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Safhaven](https://github.com/Safhaven)**
_Tuesday Sep 03, 2019 at 04:11 GMT_

----

Found the issue with this.
its seems that it is trying to delete the same pet multiple times

This issue is fixed and will do a PR soon



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 28, 2020 at 15:40:21_

----

Fixed in https://github.com/DarkstarProject/darkstar/pull/6212.

Original issue https://github.com/DarkstarProject/darkstar/issues/6115 just wasn't closed.
