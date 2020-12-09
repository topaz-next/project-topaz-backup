**Labels:**

reviewed



<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [neuromancerxi](https://github.com/neuromancerxi)**
_Thursday Nov 05, 2020 at 23:35:06_
_Originally opened as: project-topaz/topaz - Issue 1480_

----

![unknown](https://user-images.githubusercontent.com/3996176/98307935-cadf4380-1f7b-11eb-8cdb-194e9864ecf0.png)

Adds 1 to final amount printed to the player to prevent "You must wait another 0 days to perform that action." Retail count starts at 45, not 44. 

Thanks again Nyu for the retail confirmation of count starting at 45 days on a new character. Character created just before JST Midnight showed 45 days before JST midnight and after JST midnight.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Nov 06, 2020 at 06:53:06_

----

I was about to try and argue that there might be some rounding shenanigans going on here, but we're already dealing with days, so the rounding has already happened. I'm fine with the `+1`, rather than trying to dig in and find the epoch  times and `ceil` them to the next day so the maths sorts itself out 👍 
