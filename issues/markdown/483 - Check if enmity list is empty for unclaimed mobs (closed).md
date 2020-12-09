**Labels:**

merge ready



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Thursday Apr 09, 2020 at 20:36:21_
_Originally opened as: project-topaz/topaz - Issue 483_

----

Prior to the recent changes the attack round would simply set the owner instead of checking enmity since without unclaiming mechanics it didn't really matter. Attack enmity is set in takePhysicalDamage, so missed attacks and 0 damage attacks didn't generate any enmity, BUT since the owner was getting set either way, during the mob roam tick it checks if it has anyone on their enmity list, and if it doesn't but it does have an owner, it adds base enmity there. This fixes an oversight in the claim code for when claim is attempted with an empty enmity list.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


