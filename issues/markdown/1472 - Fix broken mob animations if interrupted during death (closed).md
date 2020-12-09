**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Tuesday Nov 03, 2020 at 06:16:57_
_Originally opened as: project-topaz/topaz - Issue 1472_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

If `ActionType` isn't set, there is an area of empty space left behind. The bitpacking at the end of this packet sees that empty space and thinks "Ohh, free real estate" and puts information in there - resulting in a shift of the rest of the packet - which leads to broken animations.

Thanks to Setzor for the explanation!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Nov 03, 2020 at 06:41:09_

----

>  when action are rewritten.
😱 
