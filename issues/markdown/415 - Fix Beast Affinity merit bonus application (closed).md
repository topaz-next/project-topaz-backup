**Labels:**

merge ready



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Thursday Mar 12, 2020 at 19:41:38_
_Originally opened as: project-topaz/topaz - Issue 415_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This closes https://github.com/project-topaz/topaz/issues/322

The issue seemed very well documented, so I just went ahead and did the change.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 22:44:53_

----

I was about to hit approve, but [double-checked bgwiki](https://www.bg-wiki.com/bg/Beast_Affinity):
> A pet's level cannot exceed the calling Beastmaster's level or main hand weapon item level (whichever is highest), but it can exceed the pet's normal cap.
This means a Jug Pet that caps at level 90 may reach 105 with 5/5 merits and Monster +2/Ankusa gloves and a main hand weapon that is ilvl 105+.

I'm guessing that the original GitHub issue was based off of a reading of [ffxiclopedia's page](https://ffxiclopedia.fandom.com/wiki/Beast_Affinity), but looking at the [update notes for the referenced update](https://www.bg-wiki.com/bg/Version_Update_(07/08/2013)):
> If the main weapon is switched out when a pet is active, the increased stats will change based on the new main weapon

Which makes me think the level cap is capped by BST level or ilvl, whichever is higher. But absent an ilvl mainhand, the pet is still capped by the BST's level.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Mar 17, 2020 at 09:37:22_

----

In that case, reverting this change and adding this:
```
// Increase the pet's level cal by the bonus given by BEAST AFFINITY merits.
            CCharEntity* PChar = (CCharEntity*)PMaster;
            highestLvl += PChar->PMeritPoints->GetMeritValue(MERIT_BEAST_AFFINITY, PChar);

            // And cap it to the master's level or weapon ilvl, whichever is greater
            auto iLvlMaster = std::max(PMaster->GetMLevel(), PMaster->m_Weapons[SLOT_MAIN]->getILvl());
            if (highestLvl > iLvlMaster)
            {
                highestLvl = iLvlMaster;
            }

            // Randomize: 0-2 lvls lower, less Monster Gloves(+1/+2) bonus
            highestLvl -= tpzrand::GetRandomNumber(3 - std::clamp<int16>(PChar->getMod(Mod::JUG_LEVEL_RANGE), 0, 2));
```

?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 18, 2020 at 01:09:20_

----

Maybe `capLevel` instead of `iLvlMaster` for more clarity (since ilvl will be 0 for most servers), but yeah, looks fine.
