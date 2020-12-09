**Labels:**

reviewed



<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [neuromancerxi](https://github.com/neuromancerxi)**
_Friday Oct 02, 2020 at 01:44:16_
_Originally opened as: project-topaz/topaz - Issue 1229_

----

Adds MOD and Math to implement Subtle Blow II.
Per BGWiki SB_II caps at 50%, however SB + SB_II cannot exceed (cap at) 75%.
https://www.bg-wiki.com/bg/Subtle_Blow_II

Added clamps for each individual pool and a clamp for combined pool.

Adds Subtle Blow II to Moonbow Belt/+1
Corrects Subtle Blow -> Subtle Blow II on Sherida and Niqmaddu

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 02, 2020 at 06:37:21_

----

Would this be more what you're after?
```cpp
float sBlow1 = std::clamp((float)PAttacker->getMod(Mod::SUBTLE_BLOW), 0.0f, 50.0f); // 20
float sBlow2 = std::clamp((float)PAttacker->getMod(Mod::SUBTLE_BLOW_II), 0.0f, 50.0f); // 10
float sBlowMult = ((100.0f - std::clamp((float)(sBlow1 + sBlow2), 0.0f, 75.0f)) / 100.0f); // (100 - 30) / 100 = 0.7
```

Meaning the range for the multiplier is `1.00 to 0.25`

After looking at that wiki page, there are items that give `Suble Blow - X`, so using those:
```cpp
float sBlow1 = std::clamp((float)PAttacker->getMod(Mod::SUBTLE_BLOW), 0.0f, 50.0f); // -20
float sBlow2 = std::clamp((float)PAttacker->getMod(Mod::SUBTLE_BLOW_II), 0.0f, 50.0f); // -10
float sBlowMult = ((100.0f - std::clamp((float)(sBlow1 + sBlow2), 0.0f, 75.0f)) / 100.0f); // (100 - (-30) / 100 = 1.3 (if you don't clamp it)
```

I went through all the comments for all the items that have negative subtle blow on all the wikis, and there are no definitive answers of if you can wear a single negative piece and feed TP to a mob. 
I'm inclined to clamp between -75.0f and 75.0f and then if someone complains later we can turn down the "difficulty". When things are left a little too easy, people aren't as likely to complain and fix them.
