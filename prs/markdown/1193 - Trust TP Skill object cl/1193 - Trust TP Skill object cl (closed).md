**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Saturday Sep 26, 2020 at 09:17:13_
_Originally opened as: project-topaz/topaz - Issue 1193_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Remove this horrible broken object:
```lua
mob:setTPSkills({
        ['skills'] = {
            { ai.r.WS, tpz.ws.BURNING_BLADE, 0 },
            { ai.r.WS, tpz.ws.RED_LOTUS_BLADE, 0 },
            { ai.r.WS, tpz.ws.VORPAL_BLADE, 60 },
        },
        ['mode'] = ai.tp.ASAP,
        ['skill_select'] = ai.s.RANDOM,
    })
```

Replace with a db-based mob skill list and this simple binding:
```sql
INSERT INTO `mob_skill_lists` VALUES ('TRUST_Naji',1012,33); -- Burning Blade
INSERT INTO `mob_skill_lists` VALUES ('TRUST_Naji',1012,34); -- Red Lotus Blade
INSERT INTO `mob_skill_lists` VALUES ('TRUST_Naji',1012,40); -- Vorpal Blade
```
```lua
mob:setTrustTPSkillSettings(ai.tp.ASAP, ai.s.RANDOM)
```
The binding will default to `ai.tp.ASAP, ai.s.RANDOM` behaviour if not provided, so it isn't present in simple trusts.

Added bonus: All the trust skill list numbers are reserved in `release`, so no conflicts!

Also removes a good amount of wacky Lua stack and table shenanigans, so if the stack overflows were from me... this should fix it. But we still don't know the cause for sure 🤷 

This update sponsored by Maat - who has his own animations, so can't have all of his WSs yet.



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 26, 2020 at 10:24:24_

----

Since this is targetting `feature/trust`, I'm going to merge it in right away - because `feature/trust` is getting a bit far behind and I still have to merge `release` into it :(

EDIT: Also, it removes _horror_ and adds some potential stability fixes, so there's no reason no to!
