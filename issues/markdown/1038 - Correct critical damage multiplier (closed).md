**Labels:**

reviewed



<a href="https://github.com/Nireya"><img src="https://avatars2.githubusercontent.com/u/17558211?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Nireya](https://github.com/Nireya)**
_Sunday Aug 30, 2020 at 04:17:58_
_Originally opened as: project-topaz/topaz - Issue 1038_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Currently critical damage caps at 2.25 which is incorrect as it should cap at a multiplier of 3. Right now it has the same cap as a maximum pDIF hit, so you can run into weird scenarios where your critical hits will do the same damage or less than a non-critical hit when fighting mobs much lower level than you because of this.

Sources:
https://ffxiclopedia.fandom.com/wiki/Level_Correction_Function_and_pDIF
"For both one- and two-handed melee weapons, a Critical Hit adds 1.0 to intermediate pDIFa value and capped at 3.0 before the x1.00-1.05 randomization is applied."

![89826797-c8a84d00-db24-11ea-998d-34c9545b4ddf](https://user-images.githubusercontent.com/17558211/91650931-0cbbad00-ea54-11ea-8c59-d9021cc75a0d.gif)
(the only thing incorrect on this chart is that the pDIF high should be capping at 2.25 as per the updated information in the top link)

Taken from:
http://ffxiclopedia.wikia.com/wiki/Level_Correction_Function_and_pDIF?oldid=85991


