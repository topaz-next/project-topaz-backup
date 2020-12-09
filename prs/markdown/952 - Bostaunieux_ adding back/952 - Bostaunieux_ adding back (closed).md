**Labels:**



<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [jarmengaud](https://github.com/jarmengaud)**
_Saturday Aug 15, 2020 at 09:26:31_
_Originally opened as: project-topaz/topaz - Issue 952_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Adding missing mobs "Mousse" (so that Sewer sirups can be poped)
Aligning respawn timers to retail (5 min)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Aug 15, 2020 at 17:13:33_

----

this isn't needed. we normally do not comment out rows. Mobs w3ith a position of 0,0,0 normally will not spawn. To fix them, the correct position must be given.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Aug 15, 2020 at 17:15:50_

----

```sql

INSERT INTO `mob_spawn_points` VALUES (17461300,'Funnel_Bats','Funnel Bats',4,-24.162,0.012,-102.723,29);
INSERT INTO `mob_spawn_points` VALUES (17461301,'Mousse','Mousse',3,-21.231,0.968,-123.463,187);
INSERT INTO `mob_spawn_points` VALUES (17461302,'Mousse','Mousse',3,-32.273,1.000,-99.785,150);
INSERT INTO `mob_spawn_points` VALUES (17461303,'Mousse','Mousse',3,-19.582,0.954,-125.114,31);
INSERT INTO `mob_spawn_points` VALUES (17461304,'Mousse','Mousse',3,-19.178,0.964,-147.278,7);
INSERT INTO `mob_spawn_points` VALUES (17461305,'Mousse','Mousse',3,-20.786,1.047,-147.246,137);
INSERT INTO `mob_spawn_points` VALUES (17461306,'Mousse','Mousse',3,-20.579,0.998,-160.756,172);
INSERT INTO `mob_spawn_points` VALUES (17461307,'Sewer_Syrup','Sewer Syrup',10,-20.321,0.500,-160.689,59);
```
id 17461306 is the retail placeholder, currently using group id 3

looks like the real problem was the ph was set to a scripted pop in one the group rows you changed instead of timed


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Saturday Aug 15, 2020 at 19:22:36_

----

idk why these mobs were changed to group 3 and group 15 was changed/deleted. Group 3 are the Mousse that are fished up, and are supposed to have a scripted spawn. Group 15 was being used for roaming Mousse, but looks like it was adjusted instead for the higher level Panna Cotta.


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Monday Aug 17, 2020 at 16:46:10_

----

Ok I removed the unnecessary comments.

Other than that, it's not very clear what I should do...
What is sure is that Mousse were missing, and with my PR they are back, and I tested that the NM can be poped by killing them.



----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Aug 17, 2020 at 18:38:49_

----

Mousse needs a new group for IDs 17461301-17461306. IDs 17461252 and 17461253 are fished up and have different stats/drops/spawntype. [See the first two entries on this page.](https://ffxiclopedia.fandom.com/wiki/Mousse)


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Friday Aug 21, 2020 at 19:37:46_

----

Ok added new group for non-fished up Mousses (level 58-62)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Sep 08, 2020 at 00:22:20_

----

Generally, conflicts should be resolved with rebases, not merges. If a Pull Request has a merge commit in its history, the PR should be held until it has a clean commit history, because it is likely community members who try to resolve conflicts with merges will botch the process.

This is what happened here - @wrenffxi [specifically created a new pool for the Garms in Bostaunieux - and other groups in Bostaunieux - as part of their Undead QC PR](https://github.com/project-topaz/topaz/commit/c1b010a4dc57c4bb9a03b7a1561832ee7e850dc3#diff-2c6729e449bb65fc41e44ba3d47356ec). This, along with other work on the mob groups in the zone, has been undone.

[The outdated version of the branch did not have the new group values](https://github.com/project-topaz/topaz/pull/952/commits/cbcba185ccd95a97fabf36ae4de3bd1356d6cfcc). The conflicting line in the "updated" file was taken in its entirety. This is _not_ how merges should be done. **Merge conflicts happen for a reason**. Two people touched the same line - it is vital to determine _what_ caused the conflict so that the merged line incorporates _both_ changes.


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Tuesday Sep 08, 2020 at 17:51:37_

----

You didnt look at the entire PR, as I did resolve the conflict


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Tuesday Sep 08, 2020 at 18:15:13_

----

OK i had a discussion in discord, and I think i understand why rebase is prefered.
The way we work with git at work is that we merge all changes from a PR into a single commit, so there would be no difference


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Sep 08, 2020 at 18:25:50_

----

You selected your line change in its entirety to be the final line in the resulting file. This makes git stop complaining about the conflict - it does not actually resolve it.


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Tuesday Sep 08, 2020 at 19:07:33_

----

Ok i understand the confusion. I thought we were discussing mob_droplist because thats where the merge conflict was.
Not sure why but I had no merge conflict on mob_groups. But I see that I need to fix what I have undone...


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Aug 15, 2020 at 17:13:33_

----

this isn't needed. we normally do not comment out rows. Mobs w3ith a position of 0,0,0 normally will not spawn. To fix them, the correct position must be given.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Aug 15, 2020 at 17:15:50_

----

```sql

INSERT INTO `mob_spawn_points` VALUES (17461300,'Funnel_Bats','Funnel Bats',4,-24.162,0.012,-102.723,29);
INSERT INTO `mob_spawn_points` VALUES (17461301,'Mousse','Mousse',3,-21.231,0.968,-123.463,187);
INSERT INTO `mob_spawn_points` VALUES (17461302,'Mousse','Mousse',3,-32.273,1.000,-99.785,150);
INSERT INTO `mob_spawn_points` VALUES (17461303,'Mousse','Mousse',3,-19.582,0.954,-125.114,31);
INSERT INTO `mob_spawn_points` VALUES (17461304,'Mousse','Mousse',3,-19.178,0.964,-147.278,7);
INSERT INTO `mob_spawn_points` VALUES (17461305,'Mousse','Mousse',3,-20.786,1.047,-147.246,137);
INSERT INTO `mob_spawn_points` VALUES (17461306,'Mousse','Mousse',3,-20.579,0.998,-160.756,172);
INSERT INTO `mob_spawn_points` VALUES (17461307,'Sewer_Syrup','Sewer Syrup',10,-20.321,0.500,-160.689,59);
```
id 17461306 is the retail placeholder, currently using group id 3

looks like the real problem was the ph was set to a scripted pop in one the group rows you changed instead of timed


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Saturday Aug 15, 2020 at 19:22:36_

----

idk why these mobs were changed to group 3 and group 15 was changed/deleted. Group 3 are the Mousse that are fished up, and are supposed to have a scripted spawn. Group 15 was being used for roaming Mousse, but looks like it was adjusted instead for the higher level Panna Cotta.


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Monday Aug 17, 2020 at 16:46:10_

----

Ok I removed the unnecessary comments.

Other than that, it's not very clear what I should do...
What is sure is that Mousse were missing, and with my PR they are back, and I tested that the NM can be poped by killing them.



----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Aug 17, 2020 at 18:38:49_

----

Mousse needs a new group for IDs 17461301-17461306. IDs 17461252 and 17461253 are fished up and have different stats/drops/spawntype. [See the first two entries on this page.](https://ffxiclopedia.fandom.com/wiki/Mousse)


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Friday Aug 21, 2020 at 19:37:46_

----

Ok added new group for non-fished up Mousses (level 58-62)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Sep 08, 2020 at 00:22:20_

----

Generally, conflicts should be resolved with rebases, not merges. If a Pull Request has a merge commit in its history, the PR should be held until it has a clean commit history, because it is likely community members who try to resolve conflicts with merges will botch the process.

This is what happened here - @wrenffxi [specifically created a new pool for the Garms in Bostaunieux - and other groups in Bostaunieux - as part of their Undead QC PR](https://github.com/project-topaz/topaz/commit/c1b010a4dc57c4bb9a03b7a1561832ee7e850dc3#diff-2c6729e449bb65fc41e44ba3d47356ec). This, along with other work on the mob groups in the zone, has been undone.

[The outdated version of the branch did not have the new group values](https://github.com/project-topaz/topaz/pull/952/commits/cbcba185ccd95a97fabf36ae4de3bd1356d6cfcc). The conflicting line in the "updated" file was taken in its entirety. This is _not_ how merges should be done. **Merge conflicts happen for a reason**. Two people touched the same line - it is vital to determine _what_ caused the conflict so that the merged line incorporates _both_ changes.


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Tuesday Sep 08, 2020 at 17:51:37_

----

You didnt look at the entire PR, as I did resolve the conflict


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Tuesday Sep 08, 2020 at 18:15:13_

----

OK i had a discussion in discord, and I think i understand why rebase is prefered.
The way we work with git at work is that we merge all changes from a PR into a single commit, so there would be no difference


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Sep 08, 2020 at 18:25:50_

----

You selected your line change in its entirety to be the final line in the resulting file. This makes git stop complaining about the conflict - it does not actually resolve it.


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Tuesday Sep 08, 2020 at 19:07:33_

----

Ok i understand the confusion. I thought we were discussing mob_droplist because thats where the merge conflict was.
Not sure why but I had no merge conflict on mob_groups. But I see that I need to fix what I have undone...


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Aug 15, 2020 at 18:27:20_

----

From the title of the PR, this seems to do two different things but it has one commit only. I would recommend breaking these two changes into two different commits. One for fixing the respawn timers and another for adding back the mousses. This way it is easier to see in steps "okay, this part is just the respawns, and this part is adding the mouses back." Instead of it all being mixed in together, I hope that makes sense. 


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Sunday Sep 06, 2020 at 13:09:34_

----

apologies, got lost as to what was going on here. looks like drop list id just needs to be changed as something else was merged in prior. if you can update the id and change the mob group assignment, i'll merge this in asap @jarmengaud 
