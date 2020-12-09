**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Tuesday Nov 10, 2020 at 16:25:06_
_Originally opened as: project-topaz/topaz - Issue 1494_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

**NOT YET SANITY TESTED**

I set up static analysis with Sonar, and started fixing all the things it complained about. Each commit explains what I'm doing.

The biggest thing is in the Packet System:
- `session` was poorly named, and shadowed a global session var -> renamed to `PSession`
- Every packet handler made copies of `CBasicPacket`, which isn't a big deal - `CBasicPacket` is just a bag of pointers, but we still shouldn't be doing that in the hot path 🤷‍♂️ Swapped it for move semantics gubbins


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Nov 10, 2020 at 23:44:41_

----


> `e` is a pretty common variable convention to me, but maybe it's just my Java and Python experience has poisoned me. stuck_out_tongue

knee deep in the venom of experience, the young'uns need time to build up resistance
