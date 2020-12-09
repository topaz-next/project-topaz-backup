**Labels:**

approved



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Wednesday May 27, 2020 at 23:49:11_
_Originally opened as: project-topaz/topaz - Issue 662_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Adds functionality for multiple crystal drops from a mob while in a party.  Also re-orders drops to make seals occur before crystals as is retail.  The code was tested on my server in a party of 1 to 3 people and works well.  The code was styled a tiny bit differently for topaz, so this exact code wasn't built or tested.

Closes issue #551 

Co-contribution credit to Teotwawki and cocosolos for working on this with me.


----
<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Friday May 29, 2020 at 01:32:08_

----

Let's simplify this block as each case is checking:

- if the member is in zone
- if the member is within distance

```cpp

PChar->ForParty([this, &crystalRolls, &effect](CBattleEntity* PMember)
{
    If (PMember->getZone() == getZone() && distance(PMember->loc.p, loc.p) < 100)
    {
        switch (effect)
        {
            case 1:
                if (PMember->StatusEffectContainer->HasStatusEffect(EFFECT_SIGNET)
                {
                    crystalRolls++;
                }
                break;
            // other cases similar..
        }
    }
});
```


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jun 03, 2020 at 03:28:46_

----

Each case except the default case, and then for each member we don't even bother checking zone and distance unless they also have the status.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jun 03, 2020 at 04:39:15_

----

I would maybe change this to:
```cpp
        if (m_Element > 0)
        {
            uint8 regionID = PChar->loc.zone->GetRegionID();
            switch (regionID)
            {
                // Sanction Regions
                case 28:
                case 29:
                case 30:
                case 31:
                    effect = 2;
                    break;
                // Sigil Regions
                case 33:
                case 34:
                case 35:
                case 36:
                case 37:
                case 38:
                case 39:
                case 40:
                    effect = 3;
                    break;
                // Signet Regions
                default:
                    effect = (conquest::GetRegionOwner(PChar->loc.zone->GetRegionID()) <= 2) ? 1 : 0;
                    break;
            }
        }
```
This would avoid a lot of unnecessary comparisons being done in the if/else stack.


----
<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Friday May 29, 2020 at 01:32:08_

----

Let's simplify this block as each case is checking:

- if the member is in zone
- if the member is within distance

```cpp

PChar->ForParty([this, &crystalRolls, &effect](CBattleEntity* PMember)
{
    If (PMember->getZone() == getZone() && distance(PMember->loc.p, loc.p) < 100)
    {
        switch (effect)
        {
            case 1:
                if (PMember->StatusEffectContainer->HasStatusEffect(EFFECT_SIGNET)
                {
                    crystalRolls++;
                }
                break;
            // other cases similar..
        }
    }
});
```


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jun 03, 2020 at 03:28:46_

----

Each case except the default case, and then for each member we don't even bother checking zone and distance unless they also have the status.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jun 03, 2020 at 04:39:15_

----

I would maybe change this to:
```cpp
        if (m_Element > 0)
        {
            uint8 regionID = PChar->loc.zone->GetRegionID();
            switch (regionID)
            {
                // Sanction Regions
                case 28:
                case 29:
                case 30:
                case 31:
                    effect = 2;
                    break;
                // Sigil Regions
                case 33:
                case 34:
                case 35:
                case 36:
                case 37:
                case 38:
                case 39:
                case 40:
                    effect = 3;
                    break;
                // Signet Regions
                default:
                    effect = (conquest::GetRegionOwner(PChar->loc.zone->GetRegionID()) <= 2) ? 1 : 0;
                    break;
            }
        }
```
This would avoid a lot of unnecessary comparisons being done in the if/else stack.
