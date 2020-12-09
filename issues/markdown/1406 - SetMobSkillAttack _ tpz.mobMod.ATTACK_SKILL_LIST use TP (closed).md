**Labels:**

good first issue



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Thursday Oct 22, 2020 at 02:46:55_
_Originally opened as: project-topaz/topaz - Issue 1406_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

I observed and discussed this issue in https://github.com/project-topaz/topaz/pull/1388#issuecomment-712293072 and even made a [debug video](https://streamable.com/ojrve0) of this behavior.
`SetMobSkillAttack(list_id)` and `setMobMod(tpz.mobMod.ATTACK_SKILL_LIST, list_id)` are supposed to replace the default attack of a mob with the skill list ID passed to them and are currently mainly used for flying wyrms during their flight phase. The latter is actually not used at all but it serves the same purpose, and has the same flaw.

It can be observed however that **both of these** actually **use up all TP of the mob** on every regular hit as if it still was a mobskill instead of a regular attack. This is extremely bad, as the mob now does not generate any TP at all and does not use any mobskills.

This affects all flying wyrms like Jormungand, Tiamat, Ouryu and Wyrm and makes their flying phase extremely boring and well,...simply bugged.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 23, 2020 at 11:42:21_

----

This is easily fixable:

When a mob has an ATTACK_SKILL_LIST set, every time they're due to make a regular attack, they will instead fire off a MobSkill.

That trickle's down into `CMobSkillState`, which will eventually try and `SpendCost()`.
https://github.com/project-topaz/topaz/blob/bc0834018961a177f754185537a7f644d66ab2b9/src/map/ai/states/mobskill_state.cpp#L76

It'll only spend TP if the skill's `isTpSkill()` is true:
https://github.com/project-topaz/topaz/blob/bc0834018961a177f754185537a7f644d66ab2b9/src/map/ai/states/mobskill_state.cpp#L86-L90

```
bool CMobSkill::isTpSkill() const
{
    return !isSpecial();
}

bool CMobSkill::isSpecial() const
{
  // means it is a ranged attack or call beast, etc..
  return m_Flag & SKILLFLAG_SPECIAL;
}
```

Add this flag to moves you don't want to consume TP:
```
    // Special skill (ranged attack / call beast)
    SKILLFLAG_SPECIAL        = 0x004,
```

(This was a useful dig for me, I'll need to use this info for Trusts later on)

**EDIT**

My suggestion would be to add this to MobSkill:
```cpp
bool CMobSkill::isAttackReplacement() const
{
  return m_Flag & SKILLFLAG_REPLACE_ATTACK;
}
```

and change `isTpSkill`
```cpp
bool CMobSkill::isTpSkill() const
{
    return !isSpecial() && !isAttackReplacement();
}
```

**EDIT2**
To double clarify, target this fix at `release` whoever does it. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 23, 2020 at 19:08:42_

----

Fixed in #1415 
