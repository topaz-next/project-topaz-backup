**Labels:**



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Oct 10, 2020 at 22:15:01_
_Originally opened as: project-topaz/topaz - Issue 1313_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes for some of the quest issues recently opened by eyes-and-brain:

* Add dialog to Nonterene for quest "Exit the Gambler" [Fixes #1220]
* Add dialog to NPCs in West Ronfaure for quest "The Pickpocket" [Fixes #1222]
* Add post-quest dialog to Fontoumant for quest "The Brugaire Consortium" [Fixes #1228]
* Add arguments to event during tutorial quest [Fixes #1265]
* Add dialog to Drangord during quest "Stardust" [Fixes #1269]
* Add argument to event during quest "A Pose by Any Other Name" [Fixes #1275]
* Reposition QM and Gerwitz's Axe during quest "Dark Puppet" [Fixes #1308]
* Add csnpc to Middle Delkfutt's Tower [Fixes #1310]




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 10, 2020 at 22:48:23_

----

Anytime you have to use showtext instead of messageSpecial, and the npc is -not- a shop, it is all but guaranteed to be the incorrect way to display the dialog. This is likely to be an event that our extractor tool was unable to handle.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 04:41:23_

----

100 - Thank you for your help.
101 - Ow! Ouch! Gah... If only I'd remembered that ointment!
106 - What's this? I can't accept gifts from strangers.
118 - Thank you for your help.
126 - My wounds are healed, thanks to you!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 04:41:54_

----

No event dumps :(


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 04:42:42_

----

Yeah, no extracts for this one :(


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 04:43:00_

----

Nor this


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 10, 2020 at 22:48:23_

----

Anytime you have to use showtext instead of messageSpecial, and the npc is -not- a shop, it is all but guaranteed to be the incorrect way to display the dialog. This is likely to be an event that our extractor tool was unable to handle.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 04:41:23_

----

100 - Thank you for your help.
101 - Ow! Ouch! Gah... If only I'd remembered that ointment!
106 - What's this? I can't accept gifts from strangers.
118 - Thank you for your help.
126 - My wounds are healed, thanks to you!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 04:41:54_

----

No event dumps :(


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 04:42:42_

----

Yeah, no extracts for this one :(


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 04:43:00_

----

Nor this


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 04:40:00_

----

Based on what Teo said, I think it might be worth trying to replace these show-texts with their CS counterparts (if they're quickly accessible in event extractor)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 11, 2020 at 04:44:27_

----

I maybe jumped the gun when I went and got the ID's for Aaveleon's CSs, he's the only one that's got anything listed in the events repo. You could put replacing their text's with CSs at the very very back of your TODO list, but it isn't major at all :)
