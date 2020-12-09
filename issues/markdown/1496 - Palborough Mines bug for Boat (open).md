**Labels:**



<a href="https://github.com/Reaper76"><img src="https://avatars2.githubusercontent.com/u/74263470?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Reaper76](https://github.com/Reaper76)**
_Tuesday Nov 10, 2020 at 18:14:11_
_Originally opened as: project-topaz/topaz - Issue 1496_

----

Palborough Mines  Start From Crystal  (job thf32/war6) with DRK flag quest run to boat with quadav train following you 
run to where the boat to Zeruhn Mines
once you click the boat switch it goes to black screen ( just like a Cut Screen (cant spell) while all the monsters attacking you cant do anything but die
 I just did this on Redqueen 
it was to click lever then boat and go into CS without any monster following you but instead it cuts to black screen and you get Gang Killed by Quadav without being kicked from the boat to fight back 



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Nov 10, 2020 at 18:21:24_

----

This is **very likely** because we do not (yet) have a method for de-aggro'ing mobs at cs fadeout the way retail does, nor have we implemented "event skipped" that retail has for being attacked before the fadeout. Instead cs plays to the fadeout but you still keep getting clobbered in the dark.

* **Additional** things that can get one stuck in a black screen include but may not be limited to: 
  * missing cs npc due to ID shifts
  * bad cs parameters
  * client issues such as damaged files or misbehaving plugins 


Protip: bring a source of sneak


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Nov 11, 2020 at 05:55:43_

----

Related:
https://github.com/project-topaz/topaz/issues/1375
https://github.com/project-topaz/topaz/pull/1328
https://github.com/project-topaz/topaz/issues/1180


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Nov 11, 2020 at 05:56:50_

----

I think I saw in the Eden patch notes that they added a system of "you're invincible/untargettable for this CS" or "If you get hit this CS is skipped and cancelled", might be worth reaching out to see if they would give us the assist or some clues.
