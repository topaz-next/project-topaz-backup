**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Sunday Sep 06, 2020 at 01:42:06_
_Originally opened as: project-topaz/topaz - Issue 1070_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes #1069 

Thanks to Teo and especially Wren for his urganite mixin work which I used as the skeleton for this mixin.

The regain portion was actually untested because I didn't fancy waiting around for firesday.  The regain amount is a complete guess too.  This might vary from crawler to crawler and the mixin might need another variable for it.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Sunday Sep 06, 2020 at 03:19:55_

----

Also had to add the NO_LINK mob mod to this PR to disable linking temporarily for the crawlers while asleep.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Sunday Sep 06, 2020 at 03:42:37_

----

Last order of business to make this behavior 100% is to determine what the eruca crawlers do when it's sleepy time and they have been pulled to the zone or something.  Right now, they will just fall asleep immediately wherever it was they disengaged and stay there until sun up or re-engage, but they should likely head to their respawn point before sleepy time.

If someone wants to recommend a fix for that I'll include it, otherwise it's good to go as is imo.


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Monday Sep 07, 2020 at 22:05:57_

----

From Discord (thanks to Apo for checking on retail!):
> if you move them even a couple yalms outside of their spawn point, they despawn and respawn already asleep
if you leave them at their spawn point, logout, come back in without aggroing them, they go back to sleep after exactly 2 mins
until that 2 mins is reached, they wander around their spawn like normal


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Tuesday Sep 08, 2020 at 04:37:07_

----

Waiting on teo's distance function PR so that we can get easy distance from home determination for the crawlers.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Sep 10, 2020 at 03:38:56_

----

It's finished!  Tested with teo's checkDistance fixes as well.

Eruca crawlers will now behave in a retail-like manner when a player disengages them during sleep hours:  

- For servers that allow mobs to roam home if disengaged, the crawlers will roam like normal mobs until they are within 25y of their spawn, at which point a 2 minute timer will put them to sleep again if they remain undisturbed, and it's still night time.
- For servers that despawn mobs that roam too far from spawn, they will depop like normal, and spawn asleep if it's still night.
- For either server, if the crawler is disengaged within 25y of its spawn position, it will idle for 2 minutes and then sleep, if it's still night.

Thanks for testing this on retail ^.^
