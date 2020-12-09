**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:22_
_Originally opened as: project-topaz/topaz - Issue 140_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 09, 2016 at 06:23 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3425_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30160831-1

**_Server Version_** (type `revision` in game) **:**
ac26b2eac9bea1caee27ee7c7325cdcec2dfef74

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
On retail you can only jam so much into a characters delivery box from stuff mailed to self and returned form AH. You can hit return to sender to stuff more than 8 things from mailing to yourself in there, since that will free up the send box, but there is still eventually a point where the game will cut you off [(at 128 queued items)](http://ffxiclopedia.wikia.com/wiki/Delivery_Box) with an error message and ever prevent you from listing more at the AH until you go reduce your clutter.

Well, on darkstar server I'm not seeing where such a limit is imposed. A character can queue up enough things to break their own delivery box and lose items. Combine this with the still unfixed issue Darkstar Issue 2673 allowing a single player to infinitely list thousands of something (even when not returned, each sale uses its own slot for the gil...lets face it, a lot of players are just massive idiots) and you've a recipe for a lot of annoyance.

On the upside people trying to exploit these 2 bugs on servers where a bot buys the items wind up punishing themselves! 😈 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:23_

----

<a href="https://github.com/Djcocha"><img src="https://avatars3.githubusercontent.com/u/7566917?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Djcocha](https://github.com/Djcocha)**
_Thursday Oct 13, 2016 at 17:10 GMT_

----

idk if helpful or related but issue Darkstar Issue 3350 is effected by this on Oldschool. With the same duplication method applying to things sent to deliv box from AH, like if I have 100 wind xtals posted for 100gil each, and someone buys them, but then buys just one Vulcan's Staff for lets say 50k, my DBox will them have 50k in one single slot, and I will then be able to go back into 100 more times(for the amount of crystal cash sent) for 50k each time (referencing Darkstar Issue 3350 to see why)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:24_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 13, 2016 at 21:51 GMT_

----

Sounds like the overloaded mailbox system may be the cause of Darkstar Issue 3350




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:25_

----

<a href="https://github.com/maxtherabbit"><img src="https://avatars3.githubusercontent.com/u/6538577?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [maxtherabbit](https://github.com/maxtherabbit)**
_Friday Feb 03, 2017 at 04:03 GMT_

----

the way it's written currently, the dbox should support up to 65535-7 pending items

do you really have people getting up that high? or is there a smaller limit somewhere I'm missing?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:26_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Feb 03, 2017 at 04:10 GMT_

----

I'm not sure exactly, I was helping someone figure out why they were seeing errors when I noticed there seems to be no limit in place and figured that there *should be*.

I have seen players break the AH listings, I think it might have been fixed (or might not, i dunno) where the AH would say its in stock but nobody can buy nor list more because it was overflowed. And people listing thousands of an item have seen items not arrive - maybe AH bug is eating it when overflowed. 

Retail limits both the deliverbox and the Ah slots, and neither of those are retail in DSP right now. I don't see why on the AH slot one, it looks like the code limits to 7..but in game its not unless you happen to check history to trip the client side limit.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 31, 2020 at 05:36:28_

----

![image](https://user-images.githubusercontent.com/6871475/97771754-8b959a80-1b16-11eb-85ff-4f4347740d49.png)

Finally got around to nabbing the retail message+behavior of a full delivery box. I had 130 "slots" in my delivery box, and 7 items on AH (which may possibly factor in because when your AH sales end the money or returned item is sent to your dbox queue). When I tried to mail the 131st item I got the above message. Its unclear if it counts total items or just the slots,, but I believe it goes by slots since I has multiple stacks of 99 items among these (I just tossed wtf ever I had on hand till it stopped me - mostly synth mats on that mule) which would have been a rather insane number that I am certain would not be legit. :+1: 

I thought it was at 128 (wiki says..) /shrug but I hit 130
