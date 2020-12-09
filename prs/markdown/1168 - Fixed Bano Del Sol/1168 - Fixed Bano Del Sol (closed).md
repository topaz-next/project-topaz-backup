**Labels:**

hold

reviewed



<a href="https://github.com/gweivyth"><img src="https://avatars2.githubusercontent.com/u/37130689?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [gweivyth](https://github.com/gweivyth)**
_Sunday Sep 20, 2020 at 00:25:31_
_Originally opened as: project-topaz/topaz - Issue 1168_

----

Random item that nobody will ever use but fixed it during a second pass of additional effect items.  Damage might be a little bit too high, sources on the internet said it was a pretty strong effect.  I didn't test this one vs. retail like I did with the rest of the luas I wrote since I couldn't get NM to spawn.  (Sorry I broke everything, I suck at git and tried to post on my phone, bad move!)


```
----------------------------------
-- ID: 17981
-- Item: Bano Del Sol
-- Additional Effect: 100% Proc Rate Light Damage vs. Slimes
-- Gweivyth
----------------------------------
require("scripts/globals/status")
require("scripts/globals/magic")
require("scripts/globals/msg")
-----------------------------------
function onAdditionalEffect(player,target,damage)
    local fam = target:getFamily()
    if not (fam == 228 or fam == 229 or fam == 230) then
        return 0,0,0
    else
        local dmg = math.random(15,30)
        local params = {}
        params.bonusmab = 0
        params.includemab = false
        dmg = addBonusesAbility(player, tpz.magic.ele.LIGHT, target, dmg, params)
        dmg = dmg * applyResistanceAddEffect(player,target,tpz.magic.ele.LIGHT,0)
        dmg = adjustForTarget(target,dmg,tpz.magic.ele.LIGHT)
        dmg = finalMagicNonSpellAdjustments(player,target,tpz.magic.ele.LIGHT,dmg)

        local message = tpz.msg.basic.ADD_EFFECT_DMG
        if (dmg < 0) then
            message = tpz.msg.basic.ADD_EFFECT_HEAL
        end

        return tpz.subEffect.LIGHT_DAMAGE,message,dmg
    end
end
```


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Sep 20, 2020 at 02:07:34_

----

I will add this item in the additional effect branch via latent effect, so that it can serve as an example for others like it.


----
<a href="https://github.com/EpicTaru"><img src="https://avatars3.githubusercontent.com/u/26195580?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [EpicTaru](https://github.com/EpicTaru)**
_Sunday Sep 20, 2020 at 02:18:53_

----

Is your name in the lua file really necessary, @gweivyth? There really isn't any need to state that you created it since anyone can look back at the history of the file to see who did what, lol 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 20, 2020 at 06:21:26_

----

Welcome and thanks for the PR! (I know you're not new, I recognise you from Discord, but it's the first PR from this account :) )

> Teo: I will add this item in the additional effect branch via latent effect, so that it can serve as an example for others like it.

Teo just opened this PR: https://github.com/project-topaz/topaz/pull/1169
That will lead on to the invalidation and removal of scripts like this.

I'd say keep up with him about the status of that and his `effects-rework` PR/branch and in the mean time keep using this script (and others like it) on your server until the big branch is ready.

```lua
-- Additional Effect: 100% Proc Rate Light Damage vs. Slimes
-- Gweivyth
----------------------------------
```

We have git blame/annotations, your name in commits and merge commits, and your name as a shoutout in release notes. No need for additional self-attribution. We _typically_ only include authors names in an actual file if it's accompanying a license header (which none of the scripts have). I'm not sure if we mention that in the contributor agreement, but maybe we should.

Speaking of contributor agreement:
It looks like you've overwritten this section from the PR template~
```
I affirm:

[] that I agree to Project Topaz's Limited Contributor License Agreement, as written on this date
[] that I've tested my code since the last commit in the PR, and will test after any later commits
```
We can't accept PRs unless you agree to the limited contributor agreement. 
https://github.com/project-topaz/topaz/blob/release/CONTRIBUTOR_AGREEMENT.md
Please make sure you tick the box next time :)

Thanks again for the PR, sorry it got trampled by ongoing work 🤒 







----
<a href="https://github.com/gweivyth"><img src="https://avatars2.githubusercontent.com/u/37130689?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [gweivyth](https://github.com/gweivyth)**
_Sunday Sep 20, 2020 at 23:17:14_

----

Thanks! I have like 100+ more of these but I'll refrain for now. Our project is going to be open source and I'll try and take the time to submit them once we open our git. 

@EpicTaru I added this to our live server without a merge, we tag our live fixes so that if they break things we know who to blame :p


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 21, 2020 at 05:24:00_

----

Glad to hear it, looking forward to working alongside you guys 👍 
