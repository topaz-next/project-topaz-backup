**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:42_
_Originally opened as: project-topaz/topaz - Issue 302_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Wiggo32](https://github.com/Wiggo32)**
_Tuesday Jun 11, 2019 at 22:58 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6079_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 


**_Source Branch_** (master/stable) **:**  master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

github/DarkstarProject/darkstar/blob/746b0aeb8a54452eeaf62d754268a5e7be0730f0/src/map/utils/mobutils.cppDarkstar Issue L807

current retail as it stands now does not make all dynamis mobs have true detection. so this line would be set to false for that. though, dynamis D may? idk anything about dynamis D. So, whatever the best way to handle that is.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:43_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jun 13, 2019 at 05:41 GMT_

----

For record, Dynamis D mobs are true detection.

(This feels like something that should be handled by scripts or DB anyway.)



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:45_

----

<a href="https://github.com/helixhamin"><img src="https://avatars1.githubusercontent.com/u/2202779?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [helixhamin](https://github.com/helixhamin)**
_Thursday Jun 13, 2019 at 09:40 GMT_

----

I thought mobs true detect was handled already?
Maybe I am wrong. In the mobs family system table, it has detects type. 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:46_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 13, 2019 at 14:15 GMT_

----

old style dyna all mobs were true detect so somebody hard-coded it instead of setting them the normal way. mob families has the detection type (sight/sound/blood/magic) and I think pools has the true-detect flag (on/off) and agro/linking (also both on/off). I think it all should have been one combined mask in the group or pool table personally.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:47_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday Jun 13, 2019 at 18:13 GMT_

----

I believe the reason it was hardcoded for all Dynamis spawns is because some mobs are shared outside of it - specifically the Kindred (jobs) in the Uleguerand Range. Those would need to be properly separated from the Dynamis versions.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:49_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jun 14, 2019 at 16:12 GMT_

----

they share families I dunno if they share pools (they should not share pools since they are completely diff mobs, but would not surprise me to find they DO). a long while back true detect and the detection type were combined and moved around, but the hardcoding of this predates all of that - it was just a quick way out to hit the entire zone without having to set them individually



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:50_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Saturday Jun 15, 2019 at 04:05 GMT_

----

can update the hardcoding to check for dynamis d zones only and not touch the regular dynamis... ?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:51_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jun 15, 2019 at 08:24 GMT_

----

Just remove the hardcoding altogether. No need to add additional hardcode for content that isn't currently implemented (and for an incorrect solution at that).

Whenever someone adds Dynamis D mobs they can just set true detection in pool or w/e it is by then.

edit: Maybe check the current NMs' pools for those that should still be true detection and update DB if necessary. I think this is only applicable to the Mega Bosses, as I don't recall the timed spawn NMs being true detection (in Neo Dynamis).



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:52_

----

<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Friday Sep 13, 2019 at 07:33 GMT_

----

I removed the "Dynamis true detection" default from core in Darkstar Issue 6181.  It's possible (likely) that some of the NMs need some true-detection fixing in their specific pool data, but that can go in the general Dynamis TODO issue (added it).  I think this issue can close.

Currently, Dynamis mobs don't share pools with non-dynamis mobs.



----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Feb 27, 2020 at 21:05:36_

----

I believe this issue can be closed.  See above comment.
