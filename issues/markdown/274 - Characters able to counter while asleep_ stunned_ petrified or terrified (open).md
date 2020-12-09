**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:26_
_Originally opened as: project-topaz/topaz - Issue 274_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [isotor](https://github.com/isotor)**
_Tuesday Apr 16, 2019 at 06:15 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5848_

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

Characters (and mobs) should be unable to block, parry, or counter while under any of these four status effects.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:28_

----

<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Apr 16, 2019 at 10:42 GMT_

----

Possible relevant area:
github/DarkstarProject/darkstar/blob/master/src/map/entities/battleentity.cppDarkstar Issue L1563



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:29_

----

<a href="https://github.com/maxtherabbit"><img src="https://avatars3.githubusercontent.com/u/6538577?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [maxtherabbit](https://github.com/maxtherabbit)**
_Tuesday Apr 16, 2019 at 13:16 GMT_

----

do you have a source to verify how retail handles this?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:31_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Apr 16, 2019 at 13:24 GMT_

----

I'm like 80% sure I have parried in my sleep on retail. The rest, no idea. Terror I think should stop everything. But we need some verification on retail both both. https://discord.gg/AVQRwv3



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:32_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [isotor](https://github.com/isotor)**
_Tuesday Apr 16, 2019 at 15:51 GMT_

----

If this helps, check the section on Counterstance: https://www.ffxiah.com/forum/topic/36705/iipunch-monk-guide/Darkstar Issue traits

> Keep in mind that you cannot counter while asleep, petrified, terrorized, or stunned. You also cannot counter mob area attacks, such as those from Ironclads and Mantis mobs, nor can you counter TP moves.

Thanks Nyu!



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:33_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [isotor](https://github.com/isotor)**
_Tuesday Apr 16, 2019 at 16:09 GMT_

----

Not in this issue list but [this video](https://youtu.be/s6orP8M_nG8?t=72) confirms you can still proc guard while under any of the above effects *(not sure about terror but reasonably safe bet)*. Again props to Nyu for flagging.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:34_

----

<a href="https://github.com/maxtherabbit"><img src="https://avatars3.githubusercontent.com/u/6538577?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [maxtherabbit](https://github.com/maxtherabbit)**
_Thursday Apr 18, 2019 at 01:30 GMT_

----

my assumption would be that if guard works, then all the other strictly defensive abilities will as well - which is how we have it currently



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:35_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [isotor](https://github.com/isotor)**
_Thursday Apr 18, 2019 at 13:15 GMT_

----

If you say, I provided a text guide from a fansite explicitly stating counter at the very least can't proc under these effects - it's going to be very difficult to arrange video proof of an effect *not* occurring under certain conditions.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:37_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 18, 2019 at 13:37 GMT_

----

1 important distinction here: guard parry etc have a skill, counter does not. this may be the thing that SE used to decide which things happen at which step causing some to be prevented and others not. Still conjecture on my part.

Instead of looking for proof of a negative, we'd just need one instance of something showing it does happen. that shouldn't be to terrible to pull off. grab a sleep pot and fight a chigoe, see if you can parry it. If you can thats a strong indication that all defensive skills (with a skill value) work in like fashion to guard, and we'll need to see whats up with just counter. 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:38_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [isotor](https://github.com/isotor)**
_Thursday Apr 18, 2019 at 14:18 GMT_

----

That's a fair point on the three having associated skills, willing to concede on those until I can prove otherwise.

As to capturing an instance of procs occurring that doesn't help as proc can already occur on DSP - max (I think) is asking me to submit proof of procs not occurring, and I have no idea how I'm supposed to satisfy that outside of community knowledge such as countering in the MNK guide linked above.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:39_

----

<a href="https://github.com/maxtherabbit"><img src="https://avatars3.githubusercontent.com/u/6538577?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [maxtherabbit](https://github.com/maxtherabbit)**
_Thursday Apr 18, 2019 at 14:56 GMT_

----

you are the one who opened the issue, so it's not unreasonable to ask you to substantiate the premise of your issue.

you provided evidence that counter is wrong, so we can fix that but counter is an offensive ability - it requires the player to be able to hit the monster

i.e. if guard is working correctly on DSP, what reason do you have to suggest that block and parry are different?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:40_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [isotor](https://github.com/isotor)**
_Tuesday Apr 23, 2019 at 05:19 GMT_

----

Fair enough, updated the issue to specifically target countering for now - if I come across similar for the others I'll open a separate issue.

