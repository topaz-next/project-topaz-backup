**Labels:**

crafting

reviewed



<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [jarmengaud](https://github.com/jarmengaud)**
_Sunday Sep 13, 2020 at 17:17:24_
_Originally opened as: project-topaz/topaz - Issue 1129_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes #201

Remove guild holidays as per retail
Uncomment guild shops items that were removed because an old 30-item limit

There is still work to try to find exact prices from retail (wiki data are very approximative!)
However note that the Mhaura/Selbina/Al zhabi guilds already had most of the restocked items, not commented out



----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Sep 14, 2020 at 18:13:10_

----

Can this be instead a setting that can be handled as a global in settings.lua?

I ask cuz oldschool servers might not want to have this current QoL change, right @TeoTwawki ?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Sep 14, 2020 at 18:15:19_

----

Old school servers would have already had to customize this coz it was never retail accurate even for the old system


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Sep 15, 2020 at 06:28:51_

----

I know _nothing_ about guilds and crafting, so I can only comment on code and style etc. All looks pretty sane, this is one of the rare cases where I'm in favor of leaving the old code around with a comment saying "this was removed in 2014" in case people want to revert it.

We can make _some_ allowances and settings to help people that want to run era servers, but we can't be expected to do that for every possible thing that's changed between 2006 and now. If _yet another person_ wants to spin up a TOAU-era server, then they can expect to do at least a little bit of work.

Happy to sign off on this if it gets a couple of "yes" votes.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Sep 15, 2020 at 07:08:14_

----

Yes


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Tuesday Sep 15, 2020 at 08:55:11_

----

Let me clear some confusion: this is not at all a QoL...!
The understanding of what happened, as I understand it:
Before the big crafting change from SE (2014?), there were 2 guild shops per guild in main cities. Selling the same thing.

DSP had an issue with more than 30 items per shop, so they split the big list between those 2 NPCs.

When SE changed the crafting, the left hand side NPC turned into a normal shop, selling the kits + materials depending on your rank.
But for DSP/Topaz it meant there were only 1 guild NPC left. And all the restocked items were missing as they usually were on the left hand side NPC! (thats why we have empty shops at the moment).

The PR consists of putting back the complete original list on the remaining NPC.

If you would like an era-like system, you would have to revert also the left hand side NPC.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 19, 2020 at 12:30:22_

----

It seems like this is fixes something that wasn't era - so it doesn't serve era servers, and isn't retail - so it doesn't serve the goal of matching retail. Seems like a win to me 🤷 
