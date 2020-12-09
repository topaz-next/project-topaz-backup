**Labels:**

approved



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday May 10, 2020 at 08:32:42_
_Originally opened as: project-topaz/topaz - Issue 607_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

**Rewritten Ticket 2: Electric Boogaloo:**
I've bounced around a bunch from this being a single timer packet, to the full quest, to just two packets, to the whole quest. Now it's the whole quest, a bunch of bindings and 3 new packets. Oops.

Everything is kept inside the `full_speed_ahead.lua` helper. It is ticked by a `FULL_SPEED_AHEAD` status, which wraps `MOUNTED` status and the other logic. 

There is a binding for `onPlayerEmote`. 

Everything is tracked with localVars and a single charVar for status between zones. It doesn't look like this appears in the quest log and I can't see any caps or packets to confirm otherwise.

Fixes #603

