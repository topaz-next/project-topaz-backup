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
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Nov 06, 2020 at 01:34:34_

----

~~This will fix the display but it's still not ticking on JST midnight like it should. Instead of changing this I think `playerAgeDays` needs to account for JST midnight since it currently uses `os.time()`. I think you can just switch it to `JstMidnight()`.~~


----
<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Friday Nov 06, 2020 at 01:49:02_

----

Based on the data from Nyu, it's not based on JP midnight, but character creation time stamp.

How this was tested:

1. Character created same day and spoke with Gobbie at ~23:14 JST
2. Character spoke with gobbie, "You must wait another 45 days to..."
3. Waited until after JST midnight (12:01 JST)
4. Character spoke with gobbie, "You must wait another 45 days to..."

This debunked my theory that it was based on JST Midnight, seems to confirm that it's based on character creation time stamp, and lends credence to the fix as submitted. (Screenshots below are taken in Time Zone UTC+1)

![image](https://user-images.githubusercontent.com/3996176/98316163-b9ebfd80-1f8e-11eb-8546-dfdbf2d8a13f.png)

![image](https://user-images.githubusercontent.com/3996176/98316099-9923a800-1f8e-11eb-96fa-2488d442c693.png)



----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Nov 06, 2020 at 01:52:08_

----

Oh I misunderstood or misread your first post, my bad! 😫


----
<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Friday Nov 06, 2020 at 01:56:31_

----

All good, I can see how my last sentence in the PR could be ambiguous. Hopefully this does a better job of painting the picture. :+1: 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Nov 06, 2020 at 01:34:34_

----

~~This will fix the display but it's still not ticking on JST midnight like it should. Instead of changing this I think `playerAgeDays` needs to account for JST midnight since it currently uses `os.time()`. I think you can just switch it to `JstMidnight()`.~~


----
<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Friday Nov 06, 2020 at 01:49:02_

----

Based on the data from Nyu, it's not based on JP midnight, but character creation time stamp.

How this was tested:

1. Character created same day and spoke with Gobbie at ~23:14 JST
2. Character spoke with gobbie, "You must wait another 45 days to..."
3. Waited until after JST midnight (12:01 JST)
4. Character spoke with gobbie, "You must wait another 45 days to..."

This debunked my theory that it was based on JST Midnight, seems to confirm that it's based on character creation time stamp, and lends credence to the fix as submitted. (Screenshots below are taken in Time Zone UTC+1)

![image](https://user-images.githubusercontent.com/3996176/98316163-b9ebfd80-1f8e-11eb-8546-dfdbf2d8a13f.png)

![image](https://user-images.githubusercontent.com/3996176/98316099-9923a800-1f8e-11eb-96fa-2488d442c693.png)



----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Nov 06, 2020 at 01:52:08_

----

Oh I misunderstood or misread your first post, my bad! 😫


----
<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Friday Nov 06, 2020 at 01:56:31_

----

All good, I can see how my last sentence in the PR could be ambiguous. Hopefully this does a better job of painting the picture. :+1: 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Nov 06, 2020 at 06:53:06_

----

I was about to try and argue that there might be some rounding shenanigans going on here, but we're already dealing with days, so the rounding has already happened. I'm fine with the `+1`, rather than trying to dig in and find the epoch  times and `ceil` them to the next day so the maths sorts itself out 👍 
