**Labels:**

merge ready



<a href="https://github.com/brianmask"><img src="https://avatars2.githubusercontent.com/u/33399423?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [brianmask](https://github.com/brianmask)**
_Monday May 04, 2020 at 02:40:07_
_Originally opened as: project-topaz/topaz - Issue 581_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- x[] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Purpose of this pull request is to ensure Trust Spells are both level appropriate and pass required checks in order to cast.

In the current implementation gambits registered with the SELECT_SPECIFIC reaction modifier will be cast regardless of level, recast timer and current MP.

This pull request adds one method to mob_spell_container (GetAvailable) in the same style as (GetBestAvailable) in order to check the trust has the spell in a spell container, has the appropriate mp to cast the spell, and the spell is currently not on cooldown.

This will still allow the trust lua files to register any needed gambits without regard to the trust level or other conditions and keep the flow as simple and straight forward as possible.

If a more appropriate method already exists rather than the new method added, I'm happy to modify the PR accordingly.



----
<a href="https://github.com/brianmask"><img src="https://avatars2.githubusercontent.com/u/33399423?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [brianmask](https://github.com/brianmask)**
_Monday May 04, 2020 at 23:09:58_

----

going to make a few more enhancements to not load the gambit in the first place if not applicable instead of checking every time if is applicable


----
<a href="https://github.com/brianmask"><img src="https://avatars2.githubusercontent.com/u/33399423?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [brianmask](https://github.com/brianmask)**
_Tuesday May 05, 2020 at 02:11:22_

----

modified logic slightly to check if spell is level appropriate during call to AddGambit
modified spell::CanUseSpell slightly to take in account for trust level during check
added GetAvailable to mob_spell_container to return SpellID if passed id is available and null if spell is on cooldown or trust does not have appropriate MP to cast
