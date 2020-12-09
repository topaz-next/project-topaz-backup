**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:29_
_Originally opened as: project-topaz/topaz - Issue 65_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Hozu](https://github.com/Hozu)**
_Tuesday Nov 17, 2015 at 21:35 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2426_

----

Normally I'd say nothing about something that's not implemented, but it's allowing access to home points that you don't have saved, including access to areas that require mission access such as sky and sea.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:30_

----

<a href="https://github.com/OtianNgocnion"><img src="https://avatars2.githubusercontent.com/u/14980726?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [OtianNgocnion](https://github.com/OtianNgocnion)**
_Friday Nov 20, 2015 at 16:01 GMT_

----

To add: the server I play on doesn't grant access to Adoulin (i.e. there are no methods at the moment to gain access through sanctioned means) and yet, I HPed there from my favorites. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:19:31_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 23, 2015 at 03:58 GMT_

----

similar/related issue: Darkstar Issue 1589
something about the values are off, list entries for point people have never unlocked seem to be available before unlocking _any_ (I'm told new char can go to strange places, like sky or west adoulin and a player showed me his lv 1 mule in sky) and thats on top of the values getting shifted and scrambling saved homepoint data when new ones get added.

Opinion: need to get these the heck out of playerVars and into a table sooner rather than later. Its messy to work with in its current form.




----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Monday Mar 09, 2020 at 18:06:20_

----

Hello. I'm unable to reproduce any issue regarding Homepoint teleports on master as of 03/09/2020. Feel free to reopen an issue if you come across something new regarding this. Thank you.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 08:06:39_

----

Confirming that Homepoint favorites were addressed in a PR to DSP. SQL storage was as well; they were taken out of playerVars.
