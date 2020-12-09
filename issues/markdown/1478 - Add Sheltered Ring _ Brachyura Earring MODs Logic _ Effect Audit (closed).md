**Labels:**



<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [neuromancerxi](https://github.com/neuromancerxi)**
_Wednesday Nov 04, 2020 at 23:00:56_
_Originally opened as: project-topaz/topaz - Issue 1478_

----

Adds MOD ENHANCES_PROT_SHELL_RCVD (977) to the following:
Sheltered Ring 10764
Brachyura Earring 11039

Adds Tier of Spell x 2 DEF to Protect Spells/Effects
Adds Tier of Spell / 256 to Shell Spells/Effects

Effect Detail and confirmation items do not stack:

https://www.ffxiah.com/item/10764/sheltered-ring
https://www.ffxiah.com/item/11039/brachyura-earring

Current BG Values:

https://www.bg-wiki.com/bg/Protect (and _II -> _V)
https://www.bg-wiki.com/bg/Protectra (and _II -> _V)
https://www.bg-wiki.com/bg/Shell (and _II -> _V)
https://www.bg-wiki.com/bg/Shellra (and _II -> _V)

```
Protect/ra  DEF            DEF
                           With MOD
       I -   20             22
      II -   50             54
     III -   90             96
      IV -  140            148
       V -  220            230

Shell/ra    MDT  as /256   MDT  as /256
                           With MOD
       I -  -11 (-27/256)  -11 (-28/256)
      II -  -16 (-42/256)  -17 (-44/256)
     III -  -22 (-56/256)  -23 (-59/256)
      IV -  -26 (-67/256)  -28 (-71/256)
       V -  -29 (-75/256)  -31 (-80/256)
```

Script Adjustments:

Added checks on individual Spells/Item Scripts
Logic will check for MOD Value > 0
Updated Protect Values in scripts to match BG.
Updated regimes to include Tier V and apply buff bonus with MOD present.
Tested gaining and losing buffs with and without MOD items:
Shell -> Shell V
Protect -> Protect V
Shellra -> Shellra V
Protectra -> Protectra V
Coated Shield
Protect Earring
Protect Ring
Regime Protect/Shell

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


