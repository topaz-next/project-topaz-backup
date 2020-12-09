**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Oct 29, 2020 at 22:57:35_
_Originally opened as: project-topaz/topaz - Issue 1455_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

```
[29/Oct] [15:52:36][Info] parse: 03A | 55E5 55E3 04 from user: Bronard
[29/Oct] [15:52:36][Info] parse: 01A | 55E5 55E3 0E from user: Bronard
[29/Oct] [15:52:36][Action Info] CLIENT Bronard PERFORMING ACTION 04
[29/Oct] [15:52:36][Navmesh Error] CPathFind::FindPath Entity (17309942) could not find path
[29/Oct] [15:52:36][Navmesh Error] CPathFind::FindPath Entity (17309943) could not find path
[29/Oct] [15:52:37][Navmesh Error] CPathFind::FindPath Entity (17309942) could not find path
[29/Oct] [15:52:37][Navmesh Error] CPathFind::FindPath Entity (17309943) could not find path
[29/Oct] [15:52:37][Navmesh Error] CPathFind::FindPath Entity (17309942) could not find path
[29/Oct] [15:52:37][Navmesh Error] CPathFind::FindPath Entity (17309943) could not find path
[29/Oct] [15:52:38][Navmesh Error] CPathFind::FindPath Entity (17309942) could not find path
[29/Oct] [15:52:38][Navmesh Error] CPathFind::FindPath Entity (17309943) could not find path
[29/Oct] [15:52:38][Navmesh Error] CPathFind::FindPath Entity (17309942) could not find path
[29/Oct] [15:52:38][Navmesh Error] CPathFind::FindPath Entity (17309943) could not find path

Thread 1 "topaz_game" received signal SIGSEGV, Segmentation fault.
std::_Hashtable::_M_find_before_node (__code=4, __k=@0x7fffffffd6dc: Mod::CONVMPTOHP, __n=4, this=0x55558fcc61b8) at /usr/include/c++/7/bits/hashtable.h:1548
1548          for (__node_type* __p = static_cast<__node_type*>(__prev_p->_M_nxt);;
1543        {
1544          __node_base* __prev_p = _M_buckets[__n];
1545          if (!__prev_p)
1546            return nullptr;
1547
1548          for (__node_type* __p = static_cast<__node_type*>(__prev_p->_M_nxt);;
1549               __p = __p->_M_next())
1550            {
1551              if (this->_M_equals(__k, __code, __p))
1552                return __prev_p;
#0  std::_Hashtable::_M_find_before_node (__code=4, __k=@0x7fffffffd6dc: Mod::CONVMPTOHP, __n=4, this=0x55558fcc61b8) at /usr/include/c++/7/bits/hashtable.h:1548
#1  std::_Hashtable<Mod, std::pair<Mod const, short>, std::allocator<std::pair<Mod const, short> >, std::__detail::_Select1st, std::equal_to<Mod>, EnumClassHash, std::__detail::_Mod_range_hashing, std::__detail::_Default_ranged_hash, std::__detail::_Prime_rehash_policy, std::__detail::_Hashtable_traits<true, false, true> >::_M_find_node ()
    at /usr/include/c++/7/bits/hashtable.h:642
#2  std::__detail::_Map_base<Mod, std::pair<Mod const, short>, std::allocator<std::pair<Mod const, short> >, std::__detail::_Select1st, std::equal_to<Mod>, EnumClassHash, std::__detail::_Mod_range_hashing, std::__detail::_Default_ranged_hash, std::__detail::_Prime_rehash_policy, std::__detail::_Hashtable_traits<true, false, true>, true>::operator[] (
    this=this@entry=0x55558fcc61b8, __k=@0x7fffffffd6dc: Mod::CONVMPTOHP, __k@entry=@0x7fffffffd6dc: Mod::NONE) at /usr/include/c++/7/bits/hashtable_policy.h:746
#3  0x000055555560e6a9 in std::unordered_map<Mod, short, EnumClassHash, std::equal_to<Mod>, std::allocator<std::pair<Mod const, short> > >::operator[] ()
    at /usr/include/c++/7/bits/unordered_map.h:973
#4  CBattleEntity::getMod (this=this@entry=0x55558fcc5f20, modID=<optimized out>, modID@entry=Mod::CONVMPTOHP) at /opt/topaz/src/map/entities/battleentity.cpp:1093
#5  0x0000555555611822 in CBattleEntity::UpdateHealth (this=0x55558fcc5f20) at /opt/topaz/src/map/entities/battleentity.cpp:157
#6  0x00005555556436b3 in CStatusEffectContainer::KillAllStatusEffect() (this=<optimized out>) at /opt/topaz/src/map/status_effect_container.cpp:657
#7  0x00005555555c8ef3 in mobutils::CalculateStats(CMobEntity*) (PMob=0x55558fcc5f20) at /opt/topaz/src/map/utils/mobutils.cpp:212
#8  0x000055555564e4d2 in CMobEntity::Spawn() (this=0x55558fcc5f20) at /opt/topaz/src/map/entities/mobentity.cpp:541
---Type <return> to continue, or q <return> to quit---
#9  0x000055555562f922 in WeatherChange (weather=WEATHER_FOG, this=0x55556b01ed50) at /opt/topaz/src/map/zone_entities.cpp:317
#10 CZone::SetWeather(WEATHER) (this=this@entry=0x55556a959530, weather=WEATHER_FOG) at /opt/topaz/src/map/zone.cpp:516
#11 0x000055555562fb92 in CZone::UpdateWeather() (this=0x55556a959530) at /opt/topaz/src/map/zone.cpp:586
#12 0x000055555562ffb5 in zone_update_weather (tick=..., PTask=<optimized out>) at /opt/topaz/src/map/zone.cpp:123
#13 0x0000555555571dbb in CTaskMgr::DoTimer (tick=..., this=0x555555a22ff0) at /opt/topaz/src/common/taskmgr.cpp:78
#14 main (argc=<optimized out>, argv=<optimized out>) at /opt/topaz/src/common/kernel.cpp:267
   0x5555555ede2b <std::__detail::_Map_base<Mod, std::pair<Mod const, short>, std::allocator<std::pair<Mod const, short> >, std::__detail::_Select1st, std::equal_to<Mod>, EnumClassHash, std::__detail::_Mod_range_hashing, std::__detail::_Default_ranged_hash, std::__detail::_Prime_rehash_policy, std::__detail::_Hashtable_traits<true, false, true>, true>::operator[](Mod&&)+43>:  add    %cl,-0x7b(%rbp)
   0x5555555ede2e <std::__detail::_Map_base<Mod, std::pair<Mod const, short>, std::allocator<std::pair<Mod const, short> >, std::__detail::_Select1st, std::equal_to<Mod>, EnumClassHash, std::__detail::_Mod_range_hashing, std::__detail::_Default_ranged_hash, std::__detail::_Prime_rehash_policy, std::__detail::_Hashtable_traits<true, false, true>, true>::operator[](Mod&&)+46>:  
    shlb   %cl,0x4d(%rdi,%rbx,2)
   0x5555555ede32 <std::__detail::_Map_base<Mod, std::pair<Mod const, short>, std::allocator<std::pair<Mod const, short> >, std::__detail::_Select1st, std::equal_to<Mod>, EnumClassHash, std::__detail::_Mod_range_hashing, std::__detail::_Default_ranged_hash, std::__detail::_Prime_rehash_policy, std::__detail::_Hashtable_traits<true, false, true>, true>::operator[](Mod&&)+50>:  mov    (%rdx),%eax
   0x5555555ede34 <std::__detail::_Map_base<Mod, std::pair<Mod const, short>, std::allocator<std::pair<Mod const, short> >, std::__detail::_Select1st, std::equal_to<Mod>, EnumClassHash, std::__detail::_Mod_range_hashing, std::__detail::_Default_ranged_hash, std::__detail::_Prime_rehash_policy, std::__detail::_Hashtable_traits<true, false, true>, true>::operator[](Mod&&)+52>:  mov    %rbx,%r12
   0x5555555ede37 <std::__detail::_Map_base<Mod, std::pair<Mod const, short>, std::allocator<std::pair<Mod const, short> >, std::__detail::_Select1st, std::equal_to<Mod>, EnumClassHash, std::__detail::_Mod_range_hashing, std::__detail::_Default_ranged_hash, std::__detail::_Prime_rehash_policy, std::__detail::_Hashtable_traits<true, false, true>, true>::operator[](Mod&&)+55>:  mov    %rdx,%r11
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
```
