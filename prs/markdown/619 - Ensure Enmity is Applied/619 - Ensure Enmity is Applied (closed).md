**Labels:**



<a href="https://github.com/brianmask"><img src="https://avatars2.githubusercontent.com/u/33399423?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [brianmask](https://github.com/brianmask)**
_Thursday May 14, 2020 at 01:02:32_
_Originally opened as: project-topaz/topaz - Issue 619_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Easy one liner...

Enmity generating trust skills currently are not generating enmity towards the user.  This is due to a missing call to state.ApplyEnmity().  Added the missing line to trustentity.cpp -> OnAbility.

A page of old commented out BST logic buried this call in charentity.cpp OnAbility which is what trustentify OnAbility seems to be based on.
