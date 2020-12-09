**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:36_
_Originally opened as: project-topaz/topaz - Issue 320_

----

<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Oct 23, 2019 at 15:17 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6259_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
30191004_0

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Music for xmas in jeuno area not working, there is nothing wrong in the logic, ChangeMusic is just not working when inside onZoneIn.

Tried placing the ChangeMusic inside afterZoneIn function, but this will make the song repeat itself which is really annoying.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:37_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 23, 2019 at 16:53 GMT_

----

> [12:51 PM] Tēo: changeMusic used to work from onZoneIn just fine I dunno what change broke that. when I have time I'm going to make something that acts on the zone instead of the player to facilitate this.



----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 21:30:01_

----

This bug relates to 

https://github.com/project-topaz/topaz/pull/1517

as explained by @TeoTwawki being a packet timing issue (See https://github.com/project-topaz/topaz/pull/1517#discussion_r523459338)

Can someone that has higher powers change the Title of this bug so it can be better understandable? I submitted the original bug last year but can't change it as it was collected by a bot

thank you :cat: 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Nov 14, 2020 at 22:02:42_

----

on the upside, this will be taken care of after I finish making the functionality to change music of the zone object itself instead if overwriting it with a packet sent to player's client :+1: then we just check the date and zone itself gets changed and any server zoning into it already has correct music. (this is more accurate to what retail actually does too)
