**Labels:**



<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [jarmengaud](https://github.com/jarmengaud)**
_Saturday Oct 10, 2020 at 12:45:16_
_Originally opened as: project-topaz/topaz - Issue 1309_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

I know this has not been coded, so it's not really a bug per-se.
But I am logging this issue to let people know that I am working on this atm.
So we can start discussing before I submit the PR.

So far:
This is about elemental geodes (snow geode, aqua geode, etc) AND the avatar geodes (ifritite, garudite, etc)

I have almost finished writing a log-parser for my retail logs to try to narrow the drop rate of those, for the thousands of mobs I have killed. I am using the Autoexec plugin to track the current weather when the mod dies.

Normal geodes drop from mobs 50+
Avatar geodes drop from mobs 80+
(not 100% sure about those 2 levels, still doing some tests)

When a weather is present, it has precedence and will determine which element the geode will be.
Otherwise its the day element.





----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 11, 2020 at 05:03:47_

----

This is one of the many things I started on and never finished,
https://github.com/TeoTwawki/darkstar/commit/9e8ca8f1b3d65e2c4d4a3d72c78da2c71f1af651

I despise gigantic if/else towers and massive switch statements, and was looking for a better way to code that when I discovered: **we do "global" drops all kinds of wrong.**

On dsp/topaz: 
* crystals/seals/geode/avatarite/etc happen at a fixed rate if you meet the level requirement on an exp mob (with region+status effect for crystals)
* edit - if I am not mistaken there is also a timer to try and prevent seals from dropping "too often".

on retail:
* any unused "drop slot" can contain one of the eligible global drop items, on a per players basis allowing *for example* up to 6 crystals to drop from one mob IF you have a full party of 6 and the mobs drops left 6 open slots for them to fill. If a mob were to drop 10 things in 1 kill, no crystals seals or geodes could drop in the same kill. While killing another mob may push items out of your treasure pool and be "lot" no single mob kill will make an item that mob dropped be lost, it will just not drop any of the globals, and its non-global loot is grouped in a way that will never exceed the max pool size.

The issue I described need to be tackled before we can add these with any retail accuracy. I was tempted to just add them in mobs.lua using `addTreasure()` and if you want to add them to your server as a custom addition I suggest that route rather than using my old code I linked above, as its the shortest/simplest method. be aware however this bypasses the pool cap in the core and can cause treasure loss.


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Sunday Oct 11, 2020 at 07:30:25_

----

I didnt see this coming, i'm glad I did this discussion issue :)
I will see what i can do, if i can attempt to fix both in the same PR.
Thanks for the feedback!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 11, 2020 at 08:40:02_

----

If theres anything you can use from code I already wrote feel free to take and change. I suspect it won’t be useful once the global drop thing is handled proper though.


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Friday Oct 30, 2020 at 12:10:21_

----

I did some research on mobs that drop a lots of things, and it seems that this is incorrect that you cannot drop crystals if all slots are full. Got a ram dropping no less that 12 items, including 2 crystals! (party of 3 players):

[13:04:32] You find a ram skin on the Mosshorn.
[13:04:32] You find a ram skin on the Mosshorn.
[13:04:32] You find a ram horn on the Mosshorn.
[13:04:32] You find a ram skin on the Mosshorn.
[13:04:32] You find a ram skin on the Mosshorn.
[13:04:32] You find a ram skin on the Mosshorn.
[13:04:32] Empathetic obtains a ram skin.
[13:04:32] You find a ram horn on the Mosshorn.
[13:04:32] Coffinnails obtains a ram horn.
[13:04:32] You find a lanolin cube on the Mosshorn.
[13:04:32] Ringzero obtains a ram skin.
[13:04:32] You find a ram skin on the Mosshorn.
[13:04:32] Empathetic obtains a ram skin.
[13:04:32] You find a ram horn on the Mosshorn.
[13:04:32] Empathetic obtains a ram horn.
[13:04:32] You find an earth crystal on the Mosshorn.
[13:04:32] Coffinnails obtains an earth crystal.
[13:04:32] You find an earth crystal on the Mosshorn.
[13:04:32] Koru-Moru casts Haste II.

the only rule is that the rare and ex items are never pushed away from pool by common drops.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Oct 30, 2020 at 13:19:46_

----

Why was the crystal pushed out?


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Friday Oct 30, 2020 at 14:35:07_

----

the pool was not empty when that happenned, so you see some previous items being pushed out


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 30, 2020 at 18:02:13_

----

Your log shows you obtaining the items which frees up room in the pool - have you seen any item "hit dirt" due to the arrival of a crystal? Notice all the crystals arrived last. Notice items were "obtained" prior to crystals arriving, freeing up room in the pool. This is a little different than @KnowOne134 's testing, but supports the possibility of crystals being their own thing as a "global drop" instead of part of the mobs usual loot pool.
