**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Nov 26, 2020 at 01:08:11_
_Originally opened as: project-topaz/topaz - Issue 1530_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

```
[25/Nov] [16:08:04][Info] parse: 0B5 | 0175 0174 0A from user: Lara
[25/Nov] [16:08:09][Info] parse: 061 | 0181 0180 04 from user: Lara

Thread 1 "topaz_game" received signal SIGSEGV, Segmentation fault.
gambits::CGambitsContainer::TryTrustSkill() (this=this@entry=0x5555a3a355b0) at /opt/topaz/src/map/ai/helpers/gambits_container.cpp:613
613                             resonanceProperties.push_back((SKILLCHAIN_ELEMENT)PMasterLastWeaponSkill->getPrimarySkillchain());
608                     if (PMasterLastWeaponSkill)
609                     {
610                         for (auto& skill : tp_skills)
611                         {
612                             std::list<SKILLCHAIN_ELEMENT> resonanceProperties;
613                             resonanceProperties.push_back((SKILLCHAIN_ELEMENT)PMasterLastWeaponSkill->getPrimarySkillchain());
614                             resonanceProperties.push_back((SKILLCHAIN_ELEMENT)PMasterLastWeaponSkill->getSecondarySkillchain());
615                             resonanceProperties.push_back((SKILLCHAIN_ELEMENT)PMasterLastWeaponSkill->getTertiarySkillchain());
616
617                             std::list<SKILLCHAIN_ELEMENT> skillProperties;
#0  gambits::CGambitsContainer::TryTrustSkill() (this=this@entry=0x5555a3a355b0) at /opt/topaz/src/map/ai/helpers/gambits_container.cpp:613
#1  0x0000555555676742 in Tick (this=0x5555a3a355b0, tick=tick@entry=...) at /opt/topaz/src/map/ai/helpers/gambits_container.cpp:72
#2  0x00005555556791b7 in DoCombatTick (this=0x5555a3ce5310, tick=...) at /opt/topaz/src/map/ai/controllers/trust_controller.cpp:183
#3  0x00005555555c3e49 in CAIContainer::Tick(std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<long, std::ratio<1l, 1000000000l> > >) (
    this=0x5555a3c10810, _tick=_tick@entry=...) at /opt/topaz/src/map/ai/ai_container.cpp:359
#4  0x000055555566e1ca in CZoneEntities::ZoneServer(std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<long, std::ratio<1l, 1000000000l> > >, bool) (this=0x55557aeb14c0, tick=..., check_regions=false) at /opt/topaz/src/map/zone_entities.cpp:1114
#5  0x000055555559d82b in CZone::ZoneServer (this=0x55557aeb12d0, tick=..., check_regions=<optimized out>) at /opt/topaz/src/map/zone.cpp:808
#6  0x000055555559dfda in zone_server_region (tick=..., PTask=<optimized out>) at /opt/topaz/src/map/zone.cpp:101
#7  0x000055555557299b in CTaskMgr::DoTimer (tick=..., this=0x555555a26ff0) at /opt/topaz/src/common/taskmgr.cpp:78
#8  main (argc=<optimized out>, argv=<optimized out>) at /opt/topaz/src/common/kernel.cpp:267
---Type <return> to continue, or q <return> to quit---
   0x555555571da3 <gambits::CGambitsContainer::TryTrustSkill()+1053>:   mov    %rbp,%rsi
   0x555555571da6 <gambits::CGambitsContainer::TryTrustSkill()+1056>:   mov    %rbp,%rdi
=> 0x555555571da9 <gambits::CGambitsContainer::TryTrustSkill()+1059>:   movzbl 0x29(%rax),%eax
   0x555555571dad <gambits::CGambitsContainer::TryTrustSkill()+1063>:   mov    %eax,0x3c(%rsp)
   0x555555571db1 <gambits::CGambitsContainer::TryTrustSkill()+1067>:   callq  0x5555555a75e0
     <std::__cxx11::list<SKILLCHAIN_ELEMENT, std::allocator<SKILLCHAIN_ELEMENT> >::_M_insert<SKILLCHAIN_ELEMENT>(std::_List_iterator<SKILLCHAIN_ELEMENT>, SKILLCHAIN_ELEMENT&&)>
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
```
