**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:03:21_
_Originally opened as: project-topaz/topaz - Issue 279_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [isotor](https://github.com/isotor)**
_Thursday Apr 18, 2019 at 13:23 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5865_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30190328_2


**_Source Branch_** (master/stable) **:** master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Weird one since it's a magical AOE move, right?

I vaguely tried to take a crack at submitting this directly as a PR but I'm not quite sure how to update. Earthbreaker is currently defined as a [MobMagicalMove](github/DarkstarProject/darkstar/blob/230ab12088d288122c3414757ff74e0f25a3d61b/scripts/globals/mobskills/earthbreaker.luaDarkstar Issue L24) with param `WIPE_SHADOWS` when it should be work like a multihit AOE using something like `numhits`.

I found a video showing Earthbreaker being absorbed by shadows twice, timestamped here:
https://youtu.be/hy3GPJc3kEw?t=128 *(turn your volume down)*
https://youtu.be/hy3GPJc3kEw?t=407

Not sure how many the max numhits should be, though if I had to bet I'd go with 3 or 5. Any help on how to slide this parameter into a MagicalMove would be appreciated.

Oh, and you can chalk up the inaccuracy to [Darkstar Issue wikifails](https://ffxiclopedia.fandom.com/wiki/Earthbreaker) TeoTwawki 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:03:22_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [isotor](https://github.com/isotor)**
_Thursday Apr 18, 2019 at 13:24 GMT_

----

**Related:** unsure if this same issue should apply to it's little brother Earth Pounder but I rather strongly suspect it does.

