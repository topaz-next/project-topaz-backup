**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday May 22, 2020 at 20:17:50_
_Originally opened as: project-topaz/topaz - Issue 649_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

From Discord:
```
Galieon (wiseowl)
we're testing out the initial trusts over on Dawnbreak and found a bug with kupipi
if the party member is not in range, out of zone, etc, her AI spams rotation of Protectra/Shellra and nothing else
```

Nice catch, all other gambits rely on the fact that a trust cannot exist outside of the same zone as its master. This selector views the whole party, regardless of the zone (or distance).

This should fix that. I'll test this tomorrow, and possibly put a 60-second cooldown on Kupipi's Protectra/Shellra, so if strange conditions happen she's able to do other things.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday May 22, 2020 at 22:36:14_

----

This is also true if one of the party members is in another zone. For some reason when testing this, the hp/mp on the lower right listing all party members would show as if they are not in the same zone, showing only the name. dunno if someone could replicate this, or if its even related.
