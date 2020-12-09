**Labels:**

approved

focus



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday Jun 26, 2020 at 11:25:33_
_Originally opened as: project-topaz/topaz - Issue 775_

----

Ended up completing this feature once I tracked down the required packet and the message offsets.

**Done:**
messageCombat and trust messages

Swapping out hardcoded values for spell table entries.

Swap out hard-coded trust ID values for tabled spellID values in these:

Table the system_messages used in trust.lua

Maybe rename getSeekingParty to isSeekingParty

Add timer for last time a player joined a party or when the party was formed, for the last trust error message

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jun 26, 2020 at 12:16:15_

----

might be worth renaming that packet/message while its still young: 
https://github.com/project-topaz/topaz/search?q=CMessageDebugPacket&unscoped_q=CMessageDebugPacket
