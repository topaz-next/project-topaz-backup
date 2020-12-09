**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Saturday Nov 28, 2020 at 18:38:56_
_Originally opened as: project-topaz/topaz - Issue 1537_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
From @Omnione 

Everything in core works as expected, upon looking in the scripts:
https://github.com/project-topaz/topaz/blob/59597822cc386ae8022d07df104408f8d15d87d2/scripts/globals/abilities/hasso.lua#L26

This call will fail, as trusts are mobs behind the scenes - and don't have equipment. 

This call requires equipment:
```cpp
inline int32 CLuaBaseEntity::isWeaponTwoHanded(lua_State *L)
{
    TPZ_DEBUG_BREAK_IF(m_PBaseEntity == nullptr);
    TPZ_DEBUG_BREAK_IF(m_PBaseEntity->objtype == TYPE_NPC);

    auto weapon = dynamic_cast<CItemWeapon*>(((CBattleEntity*)m_PBaseEntity)->m_Weapons[SLOT_MAIN]);

    if (weapon == nullptr)
    {
        ShowDebug(CL_CYAN"lua::getWeaponDmg weapon in main slot is NULL!\n" CL_RESET);
        return 0;
    }
    lua_pushboolean(L, weapon->isTwoHanded());
    return 1;
}
```
```cpp
bool CItemWeapon::isTwoHanded()
{
    return m_twoHanded;
}
```

**Possible ways to handle this:** 
The `mob_pool` entries for Trusts have correct cmbSkill, but it isn't assigned to anything. If it was looked at on load and then used to set the `m_twoHanded` flag - Hasso might start working.

Probably worth looking through all the other abilities that Trusts use and see if there are other gotchas like this



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Dec 01, 2020 at 16:55:35_

----

cmbSkill should be deprecated phased out and unused by even regular mobs, let alone trusts as its correct and accurate that they do not actually have weapons equipped, and the if check condition should be adjusted to check for 2 handed equipped OR isn't a player.

`if target:isWeaponTwoHanded() or not target:isPC() then -- If we're not a PC, we don't care about weapons`

Additional note: there will be other things like this and you will run into quotes of SE saying such and such trust "counts as using a 2 handed weapon" - this ONLY means that they get the benefits of traits that in players hands would depend on 2 handed weapons, and not that they are coded to use a 2 handed weapon. Like other things player shave to put effort into (such as certain merit bonuses), mobs (and by extension trusts) just get the perks for free.
