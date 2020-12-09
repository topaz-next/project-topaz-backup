**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday Aug 07, 2020 at 08:48:55_
_Originally opened as: project-topaz/topaz - Issue 929_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

My original comment still holds true:
```
// TODO: All of this is very ugly, but is fairly fragile, be careful refactoring!
```

`trust_stability_2` cleaned up a lot of things, but the samba handling is still exploding with trusts. 

Crash report from Canaria:
```
Thread 1 "topaz_game" received signal SIGSEGV, Segmentation fault.
battleutils::HandleEnspell (PAttacker=0x55558663a9b0, PDefender=0x5555710c4a10, Action=0x5555865ab420, isFirstSwing=<optimized out>, weapon=0x5555865d2ae0,
    finaldamage=1) at src/map/utils/battleutils.cpp:1027
1027                    else if (PAttacker->objtype == TYPE_TRUST && PAttacker->PMaster->PParty)
1022                                power = PDefender->StatusEffectContainer->GetStatusEffect(EFFECT_ASPIR_DAZE, PAttacker->PParty->members[i]->id)->GetPower();
1023                                break;
1024                            }
1025                        }
1026                    }
1027                    else if (PAttacker->objtype == TYPE_TRUST && PAttacker->PMaster->PParty)
1028                    {
1029                        for (uint8 i = 0; i < PAttacker->PMaster->PParty->members.size(); i++)
1030                        {
1031                            if (PDefender->StatusEffectContainer->HasStatusEffect(EFFECT_DRAIN_DAZE, PAttacker->PMaster->PParty->members[i]->id))
#0  battleutils::HandleEnspell (PAttacker=0x55558663a9b0, PDefender=0x5555710c4a10, Action=0x5555865ab420, isFirstSwing=<optimized out>, weapon=0x5555865d2ae0, 
    finaldamage=1) at src/map/utils/battleutils.cpp:1027
#1  0x00005555555cade5 in CBattleEntity::OnAttack (this=this@entry=0x55558663a9b0, state=..., action=...) at src/map/entities/battleentity.cpp:1684
#2  0x00005555555d821c in CMobEntity::OnAttack (this=0x55558663a9b0, state=..., action=...) at src/map/entities/mobentity.cpp:1132
#3  0x00005555555af8d7 in CAttackState::Update (this=0x5555865cb060, tick=...) at src/map/ai/states/attack_state.cpp:65
#4  0x0000555555597b0e in CAIContainer::Tick (this=0x555586632380, _tick=..., _tick@entry=...) at src/map/ai/ai_container.cpp:361
#5  0x00005555556bcc74 in CZoneEntities::ZoneServer (this=0x55555de29fd0, tick=..., check_regions=false) at src/map/zone_entities.cpp:1097
#6  0x00005555556b604b in CZone::ZoneServer (this=0x55555d677b40, tick=..., check_regions=<optimized out>) at src/map/zone.cpp:806
#7  0x00005555556b6e23 in zone_server (tick=..., PTask=<optimized out>) at src/map/zone.cpp:83
#8  0x0000555555591c99 in CTaskMgr::DoTimer (this=0x555555abab10, tick=...) at src/common/taskmgr.cpp:78
#9  0x0000555555571620 in main (argc=1, argv=0x7fffffffdf98) at src/common/kernel.cpp:267
   0x55555567db1a <battleutils::HandleEnspell(CBattleEntity*, CBattleEntity*, actionTarget_t*, bool, CItemWeapon*, int)+2170>:  test   %al,(%rax)
   0x55555567db1c <battleutils::HandleEnspell(CBattleEntity*, CBattleEntity*, actionTarget_t*, bool, CItemWeapon*, int)+2172>:  add    %al,(%rax)
   0x55555567db1e <battleutils::HandleEnspell(CBattleEntity*, CBattleEntity*, actionTarget_t*, bool, CItemWeapon*, int)+2174>:  add    %al,(%rax)
=> 0x55555567db20 <battleutils::HandleEnspell(CBattleEntity*, CBattleEntity*, actionTarget_t*, bool, CItemWeapon*, int)+2176>:  mov    0x240(%rax),%rax
   0x55555567db27 <battleutils::HandleEnspell(CBattleEntity*, CBattleEntity*, actionTarget_t*, bool, CItemWeapon*, int)+2183>:  test   %rax,%rax
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
```

I've never been able to reproduce this crash reliably on my machine, so another round of refactoring might help.

**Work:**
- Doesn't automatically fall into the Samba/Daze handling with `else`. This should at least only go into the crash-prone code if there is actually a Daze on a mob.
- PMaster or PParty might be getting wiped out while iterating the party members, so swap out for `ForPartyWithTrusts`, which handles a shrinking party (or one disappearing), maybe.
- Remove some dead comments while I'm here.

**Tested with:**
- Regular battle with only Char
- Regular battle with Char + Trusts
- Regular battle with Char (as DNC w/ Sambas) + Trusts
- All of the above, randomly killing trusts
- All of the above, randomly killing main char
- All of the above, randomly killing main char + warping to homepoint immediately
- All of the above, force-zoning with !zone in the middle of battle

**If this goes in, this will at least mean that you can tell your players (or yourself) not to use DNC Sambas and Trusts at the same time.**

**You can apply this as a patch by downloading:**
https://patch-diff.githubusercontent.com/raw/project-topaz/topaz/pull/929.patch
and running `git apply <patch name>`

If it's STILL unstable after this, I would recommend reverting this section all the way back to before it allowed trusts in (like in release), and then open an ongoing bug that trusts don't benefit from sambas.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Aug 07, 2020 at 19:43:14_

----

It goes against Canaria's server to run non approved PRs. But given how critical this fix is, i'm going to go ahead and make an exception for testing.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Aug 09, 2020 at 05:33:03_

----

working well thus far in Canaria. No longer crashing, really stable.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Aug 17, 2020 at 16:36:40_

----

this fix has been working great in Canaria. There was a time that the server crashed but it mighta not been related to what's being fixed in here.
