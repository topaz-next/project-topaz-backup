**Labels:**

bug



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Thursday Apr 30, 2020 at 05:19:54_
_Originally opened as: project-topaz/topaz - Issue 551_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

With current code, when a player has signet, there is a base 20% chance for an enemy that *can* drop a crystal to drop it.  Regardless of how many players are in the party and have attacked the enemy, only one crystal can drop, with the % rate being unaffected.  In retail, the # of players with signet that have attacked the mob should increase the amount of crystals that can/will drop.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 30, 2020 at 11:49:15_

----

What I and @KnowOne134 found out is that retail will  load its "global drops" (like crystals) onlyin any unused drop slots that nothing already filled, up to the party size that killed the mob. This is quite different from what happens now at a static rate with a cooldown.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 30, 2020 at 13:17:35_

----

> only in any unused drop slots that nothing already filled, up to the party size that killed the mob

For clarification, if a mob is killed by a party with two members, and the mob drops 1 rabbit hide, is it:

1) One crystal is added, bringing the total drops to 2 (the max party size);
or
2) Two crystals are added, bringing the total drops to 3 (hide + size, so long as total is kept to less than 8)

?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 30, 2020 at 13:24:00_

----

its crystals added to existing pool as long as there are free spaces to do so. Party size doesn't limit the pool size, just determine show many xtal -can try- to fill in the empty slots of the pool. similar situations happen for seals geodes etc.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Apr 30, 2020 at 13:35:16_

----

I think it has diminishing returns. A party of 6 can have 6 Crystal's drop. But is super rare. Cap is 6


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 30, 2020 at 13:37:18_

----

I believe they simply roll per party member. so to get 6 all 6 members rolls would would need to succeed in addition to have 6 unused loot pool slots after the mob dies.
