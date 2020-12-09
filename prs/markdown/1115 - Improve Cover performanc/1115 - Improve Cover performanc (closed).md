**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 05:48:53_
_Originally opened as: project-topaz/topaz - Issue 1115_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Cover partners are being re-calculated and checked on every attack round, for every entity in a battle - including mobs. 
Mobs can exist in giant parties, so if they're checking for cover all the time things are gonna get bad.

This is a quick fix to limit that re-calculation to just PCs, but there is plenty of room for improvement here.

**Ideally**
- Only recalculate when: the party changes, someone's cover status changes

If anyone sees any more **quick wins** for performance here, let me know so we can ninja this into `release` and `canary`


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Sep 13, 2020 at 06:33:29_

----

I don't care what clang-format says, I still think it looks good. :laughing: 

Simple enough remediation for now. I mentioned on the Discord that this may be causing the server hangs reported on Canaria; due to the cover code using uint8's for its loop counters, and some areas having more than 255 mobs in a party. Understandably, `i` would loop infinitely in such a case. Presumably this fix should obviate that issue, can't have that many players in a party from what I understand.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:38:15_

----

```
Simple enough remediation for now. I mentioned on the Discord that this may be causing the server hangs reported on Canaria; due to the cover code using uint8's for its loop counters, and some areas having more than 255 mobs in a party. Understandably, i would loop infinitely in such a case. Presumably this fix should obviate that issue, can't have that many players in a party from what I understand.
```
That is a very interesting bug!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:45:34_

----

Gonna merge and start proliferating things around, if more fixes come up we can deal with them normally
