**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Wednesday Aug 26, 2020 at 18:07:14_
_Originally opened as: project-topaz/topaz - Issue 1008_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Reported by Canaria:
```
#0  std::__find_if<__gnu_cxx::__normal_iterator<CMobEntity**, std::vector<CMobEntity*> >, __gnu_cxx::__ops::_Iter_pred<CBattlefield::RemoveEntity(CBaseEntity*, uint8)::<lambda(auto:1)> > > (__pred=..., __last=<error reading variable: Cannot access memory at address 0x2f73746365666665>,
    __first=<error reading variable: Cannot access memory at address 0x2f736c61626f6c67>) at /usr/include/c++/7/bits/stl_algo.h:120
#1  std::__find_if<__gnu_cxx::__normal_iterator<CMobEntity**, std::vector<CMobEntity*> >, __gnu_cxx::__ops::_Iter_pred<CBattlefield::RemoveEntity(CBaseEntity*, uint8)::<lambda(auto:1)> > > (__pred=..., __last=..., __first=...) at /usr/include/c++/7/bits/stl_algo.h:162
#2  std::__remove_if<__gnu_cxx::__normal_iterator<CMobEntity**, std::vector<CMobEntity*> >, __gnu_cxx::__ops::_Iter_pred<CBattlefield::RemoveEntity(CBaseEntity*, uint8)::<lambda(auto:1)> > > (__pred=..., __last=<error reading variable: Cannot access memory at address 0x2f73746365666665>,
    __first=<error reading variable: Cannot access memory at address 0x2f736c61626f6c67>) at /usr/include/c++/7/bits/stl_algo.h:863
#3  std::remove_if<__gnu_cxx::__normal_iterator<CMobEntity**, std::vector<CMobEntity*> >, CBattlefield::RemoveEntity(CBaseEntity*, uint8)::<lambda(auto:1)> > (__pred=..., __last=..., __first=...) at /usr/include/c++/7/bits/stl_algo.h:940
#4  CBattlefield::RemoveEntity (this=0x555588cb7b20, PEntity=PEntity@entry=0x555588cb1d30, leavecode=leavecode@entry=3 '\003')
    at src/map/battlefield.cpp:470
#5  0x00005555555c57d0 in CBaseEntity::~CBaseEntity (this=0x555588cb1d30, __in_chrg=<optimized out>) at src/map/entities/baseentity.cpp:55
#6  0x00005555555db3b3 in CTrustEntity::~CTrustEntity (this=0x555588cb1d30, __in_chrg=<optimized out>) at src/map/entities/trustentity.h:33
#7  CTrustEntity::~CTrustEntity (this=0x555588cb1d30, __in_chrg=<optimized out>) at src/map/entities/trustentity.h:33
---Type <return> to continue, or q <return> to quit---
#8  0x00005555556bf920 in CZoneEntities::ZoneServer (this=0x555556ec0010, tick=..., check_regions=false) at src/map/zone_entities.cpp:1116
#9  0x00005555556b8a9b in CZone::ZoneServer (this=0x555555cf4570, tick=..., check_regions=<optimized out>) at src/map/zone.cpp:806
#10 0x00005555556b9873 in zone_server (tick=..., PTask=<optimized out>) at src/map/zone.cpp:83
#11 0x0000555555592009 in CTaskMgr::DoTimer (this=0x555555abeb10, tick=...) at src/common/taskmgr.cpp:78
#12 0x0000555555571990 in main (argc=1, argv=0x7fffffffdf98) at src/common/kernel.cpp:267
   0x5555555dc605 <CBattlefield::RemoveEntity(CBaseEntity*, unsigned char)+165>:        jle    0x5555555dcbc4 <CBattlefield::RemoveEntity(CBaseEntity*, unsigned char)+1636>
=> 0x5555555dc60b <CBattlefield::RemoveEntity(CBaseEntity*, unsigned char)+171>:        cmp    (%rdx),%rbx
   0x5555555dc60e <CBattlefield::RemoveEntity(CBaseEntity*, unsigned char)+174>:        je     0x5555555dca8a <CBattlefield::RemoveEntity(CBaseEntity*, unsigned char)+1322>
   0x5555555dc614 <CBattlefield::RemoveEntity(CBaseEntity*, unsigned char)+180>:        cmp    0x8(%rdx),%rbx
   0x5555555dc618 <CBattlefield::RemoveEntity(CBaseEntity*, unsigned char)+184>:        je     0x5555555dcbbb <CBattlefield::RemoveEntity(CBaseEntity*, unsigned char)+1627>
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

```

The area in question is this:
```cpp
                if (m_AllyList.size() > 0)
                {
                    m_AllyList.erase(std::remove_if(m_AllyList.begin(), m_AllyList.end(), check), m_AllyList.end());
                }
```

So, it looks like Trusts are being removed from the AllyList... but they're never added to it as far as I can see, nor should they be. They'll clean themselves up as soon as their master zones, so no need to handle them. 

Also, since `CTrustEntity` inherits from `CMobEntity` it's destructor should be virtual.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Aug 27, 2020 at 07:57:12_

----

Confirmed that summoning trusts in a BCNM _doesn't_ add them to the ally list, so the logic that tried to remove them was always going to fail. This should sort everything else out, the rest of `RemoveEntity` looks pretty harmless.
