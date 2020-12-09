**Labels:**

bug



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jan 08, 2020 at 15:51:53_
_Originally opened as: project-topaz/topaz - Issue 326_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened or fixed
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Basically, on retail, [pdiff min and max are supposed to have different caps depending on the weapon type](https://www.bg-wiki.com/bg/PDIF#Attack.2FDefense_Ratio). This behavior is [currently not accounted for at all](https://github.com/project-topaz/topaz/blob/3eb1c1570f276c8510300a2993fc225fc50d4ba7/scripts/globals/weaponskills.lua#L692-L717) (at least in WS scripts, I haven't checked melee white hits). This results in weapons like Great Katana having the same pdiff ratios as Daggers.

This, naturally, results in some unhappy Samurai~!

Copy-pasted from [my gist when I first found this](https://gist.github.com/ibm2431/a4de145c74c571c2fc264d6bb9e17e0a):

---

Let's look at only non-crit caps.

cratio is initially calculated as Attacker Atk / Defender Def:
https://github.com/DarkstarProject/darkstar/blob/3edcc7b6c22bcf16227a2d3b3cc47da7baa046f2/scripts/globals/weaponskills.lua#L500
Let's assume some scenario of 1000 atk and 20 def. This would put our initial cratio at 50.

According to bgwiki, it's supposed to have varying non-crit caps between 3.25 and 4.75, DEPENDING ON WEAPON TYPE:
https://www.bg-wiki.com/bg/PDIF#Attack.2FDefense_Ratio

DSP however pre-emptively clamps it to 2.25, always:
https://github.com/DarkstarProject/darkstar/blob/3edcc7b6c22bcf16227a2d3b3cc47da7baa046f2/scripts/globals/weaponskills.lua#L501

Ignoring level correction for the sake of simplicity...
DSP then adjusts pdifmin (LL on bgwiki) and pdifmax (UL on bgwiki) based off the initial cratio.

Since our 1000atk/20def scenario got clamped to 2.25:
https://github.com/DarkstarProject/darkstar/blob/3edcc7b6c22bcf16227a2d3b3cc47da7baa046f2/scripts/globals/weaponskills.lua#L528-L529
Our pdif max (UL) becomes cratio + 0.375 = 2.625.

When by the current retail formula on bg, our cratio (or, "wratio", since we didn't crit):
https://www.bg-wiki.com/bg/PDIF#2._qRatio
1000 atk / 20 def = starting cratio of 50 -> h2h/GK cap of 3.5 -> cratio of 3.5 + 0.375 = pdifmax (UL) of 3.875



