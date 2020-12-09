**Labels:**

focus



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Monday Jul 27, 2020 at 07:33:19_
_Originally opened as: project-topaz/topaz - Issue 894_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Last round of stability fixes did a pretty good job and things are looking fairly stable, but they have opened the gates for _other_ bugs to finally start showing themselves.

A lot of these are areas _outside_ of main trust logic areas (which are very well sanity checked). Since PMaster is now cleared out more aggressively, there are likely going to be some more instances of trying to access it after it's gone - which we need to wrap in checks 🤷 

**Bugs fixed:**
- Trusts are now correctly targetted by AOE + Cones, before all trusts would get hit regardless of position 
- Trusts who were the target of an AOE attack were counted and hit twice, not anymore
- If you entered and flee'd a BCNM with trusts out, their "ghosts" would still be in the waiting room. Fixed the packet range that caused this.
- Removed the strange patch in MagicState that kicked off all the trust work, we now model trusts better and don't need it! 
- Interesting goings ons with trust targids (local ids). Will make an issue after this PR to handle them properly properly, but now there is a middle-ground fix that stops crashes when using Windower's Timer plugin and allows Battlemod addon to work with Trusts <3
- Trusts are correctly cleared on death and entry to BCNMs
- You can no longer cast on trusts in another party, or hit your own trusts with SMN skills or offensive spells!
- Trusts now generate enmity when they cure (Curilla & PLD trusts are viable)
- Trust spells are no longer interrupted on melee hit.
- Reverted Samba handling to old layout and added another case to handle trusts. Refactoring it made it explode sometimes...
- Trusts being removed/cleared from your party will no longer destroy the underlying party object.
- ^ This also stops the server exploding if someone DC's or logs out with trusts out
- Despawn Trusts when charmed, if the trust is somehow orphaned, despawn them then too for safety.
- Trust <-> Trust targeting is fixed, and ForParty-style priority is fixed to always go through players first, then trusts.
- Fixed warning-as-error stopping compilation on x86_64

**Notes:**
I've opted to _not_ destroy a player's party when all the trusts are removed because it was causing so many issues. I feel like stability now is worth the cost of people having to dissolve their own party until we can find a good solution (I want to refactor Party lifetimes eventually). 
