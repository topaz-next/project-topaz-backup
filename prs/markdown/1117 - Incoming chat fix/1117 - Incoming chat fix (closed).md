**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:00:02_
_Originally opened as: project-topaz/topaz - Issue 1117_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Entirely thanks to the work of Windower devs.
https://github.com/Windower/Lua/pull/1936/files

Adjust data locations and sizes after the version update

@wrenffxi if you're working on a version update PR, feel free to nab this

**Testing**
- I wasn't getting correct system messages with additem after the update
- Now I am


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Sep 13, 2020 at 06:01:44_

----

looks right to me.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Sep 13, 2020 at 06:02:27_

----

Nice work :+1: 

There was word on the Discord that character creation was also broken because of this (presumably same reason and fix). If this is true, any chance of getting that tested and rolled in as well? It would be nice to have one commit to fix it all up in one fell swoop. :smiley: 

Edit: disclaimer I haven't tested whether this was true. :detective: 


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Sunday Sep 13, 2020 at 12:28:02_

----

~~Confirming that I get an "Error code: POL-0001" when creating a new character (without and with the fix). Message pops up right before logging in (after chosing a nation). Character will still be present in the list but the same error pops up if you try to log in with it afterwards. I don't know if it's clearly related but here it is. Logging with characters created before that is fine.~~

Chat is working again with it tho! Thank you, zach.

[edit]

Thank you, EpicTaru, and sorry, zach!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 12:46:07_

----

I'm not sure what packets are doing in login, but I don't think they'll use the packet I changed here. The fix will be the same, just in the packets in login. I'll take a look later 


----
<a href="https://github.com/EpicTaru"><img src="https://avatars3.githubusercontent.com/u/26195580?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [EpicTaru](https://github.com/EpicTaru)**
_Sunday Sep 13, 2020 at 14:28:30_

----

That issue with getting the POL-0001 error is because the connection between the lobby server and the game server timing out or something. If you speed thru the character creation process you won't run into that issue. I haven't created enough characters to know exactly how long it takes to not have the connection time out, but I have created enough to know that that error is due to that. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 15:23:47_

----

Can anyone with an older version test this and make sure it doesn't destroy the server for you? Don't want to merge this and _force_ an update


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 20:11:25_

----

I forced an update, I think it's better to have a slightly wonky game than a game that doesn't work at all (depending on what version you have / or are stuck with). Will be working hard the next few days to sort out the login issues now that we've figured out chat 


----
<a href="https://github.com/waterlgndx"><img src="https://avatars0.githubusercontent.com/u/1085232?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [waterlgndx](https://github.com/waterlgndx)**
_Tuesday Sep 15, 2020 at 16:01:54_

----

Maybe this is a stupid question but just for clarification: is this related to issue #1096  ?


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Tuesday Sep 15, 2020 at 16:06:32_

----

This is not a stupid question and yes it's related to said issue!
