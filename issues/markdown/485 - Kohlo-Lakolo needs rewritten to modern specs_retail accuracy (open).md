**Labels:**

bug



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Apr 10, 2020 at 23:50:29_
_Originally opened as: project-topaz/topaz - Issue 485_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
https://github.com/project-topaz/topaz/blob/c52431e2c48516954aa2f5ebbb331238f43cc3d8/scripts/zones/Port_Windurst/npcs/Kohlo-Lakolo.lua

This script for Kohlo-Lakolo (in bad need of reformatting) for the "know one's onions" quest. The flow of the quest isn't even correct because ffxiclopedia is wrong - bg wiki has it right.

It presently does not check if you have already completed the trade and been sent to the house of heroes before accepting the same trade again. if you have the onions for it, you can keep generating scrolls of blaze spikes. 

The conflict with the summon quest cs is wrong as well - you should get the opening cs for the job quest if you have not already, but the reminder event should not be repeated locking you out of this quest. 

`needToZone()` also needs replaced, and the KnowOnesOnionsTime variable is ..I don't know what to say here. It makes no sense from either wiki's description. Supposedly the timer on retail had to do with a KI from Windurst Mission 3-1 due to a plot point if you were recently on that mission and not to do with the time you traded the onions. 

Per  https://www.bg-wiki.com/bg/Know_One%27s_Onions
- Before you begin, you are required to zone if you just completed Truth, Justice, and the Onion  Way!. (use `player:setLocalVar()`)
- Speak to Kohlo-Lakolo Port Windurst behind the warehouse at (G-5).
- Retrieve 4 Wild Onions and trade them to him. (don't award blaze spikes here)
- Head to House of the Hero in Windurst Walls (G-3) and try to enter to see a cutscene. (**may possibly** be delayed or skipped if you just got the "old ring" KI from WM 3-1 but I cannot confirm this at present)
- **Return to** Kohlo-Lakolo and speak with him to complete the quest and receive your reward. (award blaze spikes here)

I recently did this quest on retail, and it went exactly how BG described it. I was not recording however, had no reason to think I would need to as I thought this was working accurately already.

tl;dr
Halver's disease got'em, poor Kohlo needs surgery to rewrite all the things.


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 15, 2020 at 03:15:18_

----

I can start working on this... will be a nice starter project. Would it be best just to redo the entire series or specifically just Know Ones Onions?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 11:59:21_

----

I only looked into know one's onions specifically but from the age of his code and the bad formatting I would guess a full rewrite would be a great idea. This guys script is a fossil.


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Thursday Apr 16, 2020 at 04:03:22_

----

So I have most of it done as of right now. One of the issues that kind of threw me for a loop was the difference between the wikipedia and BG. For example, in Wild Card BG has the mission ending on talking to House of Hero, wikipedia has it talking to Honoi, which makes sense. Doing the best I can without have pcaps.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 16, 2020 at 13:24:27_

----

if need be we can request caps/video in the captures discord for any that don't already exist https://discord.gg/v6cv2t2


----
<a href="https://github.com/svarsstad"><img src="https://avatars3.githubusercontent.com/u/28391488?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [svarsstad](https://github.com/svarsstad)**
_Sunday Jul 05, 2020 at 22:51:29_

----

port windurst event 584 doesn't play when you have the dark mana orb. i just feel like it should.
