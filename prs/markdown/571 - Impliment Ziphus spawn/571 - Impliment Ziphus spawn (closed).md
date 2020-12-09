**Labels:**

merge ready



<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [hooksta4](https://github.com/hooksta4)**
_Saturday May 02, 2020 at 20:06:47_
_Originally opened as: project-topaz/topaz - Issue 571_

----

Updated to Topaz from @Wiggo DSP contribution a few years ago.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday May 02, 2020 at 21:06:21_

----

If using npcUtil.tradeHas(), which flags matched items to be removed, then use player:confirmTrade() rather than player:tradeComplete().  confirmTrade consumes only the marked items, and returns excess items in the trade window to the player.  tradeComplete removes from player all items put into the trade window.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Sunday May 03, 2020 at 18:58:53_

----

This line is unneeded since its defined in the I'd page. 
ID.npc.ZIPHIUS_QM_BASE


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Sunday May 03, 2020 at 19:01:13_

----

Hours check should maybe have >= and <= times so if the sever is restarted they will still work for the current day


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Sunday May 03, 2020 at 19:02:10_

----

Both these locals can be pulled from ID page


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Sunday May 03, 2020 at 19:02:40_

----

Can delete the prints if not needed


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Sunday May 03, 2020 at 19:04:10_

----

If all the qms are the same code can make a global for the zone and just have each script pull the data from it. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday May 04, 2020 at 00:57:10_

----

you've accidentally included solution changes


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Monday May 04, 2020 at 01:43:27_

----

ah shoot... how would I remove that? or block it from going forward?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 09:40:26_

----

Do players "share" traps? In that, if Player A baits the trap, if Player B checks later, Player B can get the spawn?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 09:42:50_

----

A random number between 1 and 1000 will always be less than 1000~!

(This is why global scripts help when testing 😉 )


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 09:44:45_

----

General excess parens statement~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 09:54:11_

----

I believe in this case you can push an amend commit that changes it back to the exact original value. These files can be edited manually, but you may need to use an external text editor since Visual Studio is reluctant to let you open/edit project files by hand.

If you're going to retarget the solution, I don't think there's a way to prevent changes to your project file from being potentially included in git changes - it can't be added to `.gitignore` because sometimes the solution _does_ need to change. You can check the file changes before you commit and "revert" any changes that Visual Studio made after a retarget. (Alternatively: update your toolset so you don't need to retarget 😉)


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Thursday May 07, 2020 at 12:47:11_

----

It seems that way. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday May 08, 2020 at 22:44:48_

----

Teo :point_left:  _wants a cap showing this_


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Friday May 08, 2020 at 23:26:43_

----

me too! 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday May 11, 2020 at 15:19:54_

----

Fortunately we have a free week :)


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday May 02, 2020 at 21:06:21_

----

If using npcUtil.tradeHas(), which flags matched items to be removed, then use player:confirmTrade() rather than player:tradeComplete().  confirmTrade consumes only the marked items, and returns excess items in the trade window to the player.  tradeComplete removes from player all items put into the trade window.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Sunday May 03, 2020 at 18:58:53_

----

This line is unneeded since its defined in the I'd page. 
ID.npc.ZIPHIUS_QM_BASE


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Sunday May 03, 2020 at 19:01:13_

----

Hours check should maybe have >= and <= times so if the sever is restarted they will still work for the current day


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Sunday May 03, 2020 at 19:02:10_

----

Both these locals can be pulled from ID page


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Sunday May 03, 2020 at 19:02:40_

----

Can delete the prints if not needed


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Sunday May 03, 2020 at 19:04:10_

----

If all the qms are the same code can make a global for the zone and just have each script pull the data from it. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday May 04, 2020 at 00:57:10_

----

you've accidentally included solution changes


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Monday May 04, 2020 at 01:43:27_

----

ah shoot... how would I remove that? or block it from going forward?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 09:40:26_

----

Do players "share" traps? In that, if Player A baits the trap, if Player B checks later, Player B can get the spawn?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 09:42:50_

----

A random number between 1 and 1000 will always be less than 1000~!

(This is why global scripts help when testing 😉 )


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 09:44:45_

----

General excess parens statement~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 09:54:11_

----

I believe in this case you can push an amend commit that changes it back to the exact original value. These files can be edited manually, but you may need to use an external text editor since Visual Studio is reluctant to let you open/edit project files by hand.

If you're going to retarget the solution, I don't think there's a way to prevent changes to your project file from being potentially included in git changes - it can't be added to `.gitignore` because sometimes the solution _does_ need to change. You can check the file changes before you commit and "revert" any changes that Visual Studio made after a retarget. (Alternatively: update your toolset so you don't need to retarget 😉)


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Thursday May 07, 2020 at 12:47:11_

----

It seems that way. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday May 08, 2020 at 22:44:48_

----

Teo :point_left:  _wants a cap showing this_


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Friday May 08, 2020 at 23:26:43_

----

me too! 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday May 11, 2020 at 15:19:54_

----

Fortunately we have a free week :)


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Sunday May 03, 2020 at 20:20:33_

----

KO thanks! I have been working with coco on the side learning how to convert the server variables to local vars. I am testing it out now and should update the commit soon. 

Thanks! 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday May 14, 2020 at 20:07:55_

----

I went ahead and globalized these functions and cleaned up some style stuff. I also did some retail testing and found that only 1 player can trade to each QM, and only that player can check the trap, so I updated to reflect that as well. I'm pretty sure that Ziphius will always spawn from 1 random trap given that it's been baited, so I changed that as well.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday May 14, 2020 at 20:33:27_

----

> I went ahead and globalized these functions and cleaned up some style stuff. I also did some retail testing and found that only 1 player can trade to each QM, and only that player can check the trap, so I updated to reflect that as well. I'm pretty sure that Ziphius will always spawn from 1 random trap given that it's been baited, so I changed that as well.

I can confirm Hercules Beetle in Carpenter’s Landing works identically. 


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Thursday May 14, 2020 at 21:09:59_

----

Thanks for squaring all that away. Didnt know what was meant by globalize the functions. Glad someone with a lot more knowledge was able to get it sorted and implemented! 
