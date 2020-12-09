**Labels:**

merge ready



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Friday Jul 24, 2020 at 09:25:54_
_Originally opened as: project-topaz/topaz - Issue 885_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Seems like our original retail capture of these banners got them out of order.  Our base/offsets were correct, and the banners were correctly placed in the gaps between the NPCs, but the actual banner data wasn't in the right order.  I updated them from Nyu's more recent retail captures.

I tested ownership of region under all three cities, and beastmen, and the correct banners and NPCs now show up in each case.

I also scanned through npc_list, and it looks like this was the only zone with out-of-order banners.

Fixes #866
