**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Sep 12, 2020 at 16:33:16_
_Originally opened as: project-topaz/topaz - Issue 1108_

----

Alternate title: Satisfy Teo OCD

Todo: helper/utils function? The other times we check this we're also modifying the number right in the ability check, which we probably shouldn't be doing.. see Violent Flourish for an example.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Sep 12, 2020 at 16:35:47_

----

on one hand, there is probably a tiny performance saving on returning out before hitting another hasStatsusEffect call. On the other hand..Just look at it. It looks like a sin doesn't it? I'm just saying..


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 15:07:45_

----

I'm having a small argument with myself about this. On one hand - it is optimised and does no additional work than it has to.

On the other hand, it isn't being called _that much_, and we do much more horrifying things per-tick that make this look insignificant (looking at enmity distribution when someone cures... good lord.)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 15:08:32_

----

That being said, if you just ramble a couple of lines at me about performance impact (or lack thereof) I'll just merge it 👍 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Sep 14, 2020 at 00:21:23_

----

I wasn’t 100% on this myself figured I’d ross noodle and see if it sticks. I thing the way it was is technically more performant by an possibly immeasurably small amount. I just hate if/else towers.
