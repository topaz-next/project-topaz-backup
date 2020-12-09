**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Monday Sep 07, 2020 at 09:45:01_
_Originally opened as: project-topaz/topaz - Issue 1074_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes https://github.com/project-topaz/topaz/issues/1062

From discussion in Discord and a bunch of reading and clarifying, we have discovered that `static_cast` always succeeds, leading to bad pointers which will explode when used. It looks like that's whats been going on in this section when trusts are being deleted:

```cpp
    auto entity = static_cast<CBattleEntity*>(PEntity);
    entity->StatusEffectContainer->DelStatusEffectsByFlag(EFFECTFLAG_CONFRONTATION, true);
    // ^-- entity will be a bad pointer if PEntity is a trust that's in the middle of being deleted....
```

The cast to `CBattleEntity*` fails, but then the resulting pointer is used.

This PR cleans up that section with a `dynamic_cast`, which will return `nullptr` if it fails, skipping the sections that would rely on it.

**I ASSUME** that the `if in battlefield, remove from battlefield` logic is in `CBaseEntity::~CBaseEntity` is there because NPC's (like treasure chests) need it... so it can't be moved up into BattleEntity.

Please sanity check my logic!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 07, 2020 at 12:28:40_

----

Going into my feature branch, _yeet_
