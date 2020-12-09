**Labels:**

focus

merge ready



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Apr 29, 2020 at 01:08:02_
_Originally opened as: project-topaz/topaz - Issue 545_

----

Currently a WIP. Only thing ready is Lathuya's logic. I need to verify that the order of the quest is correct, also one thing i am having issues is the zone:registerRegion and onZoneIn for it as i just added a testing print to player to make sure that the area is correct and i do not get any feedback.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Apr 30, 2020 at 18:44:44_

----

I'm done with the quest :cat: 

Only thing missing are:
* 2 mob attacks for the NM that are missing, there were 3 missing attacks before but added one weird one that removes all buffs lol.
* correct location params for onRegionEnter for both optional cutscenes. Since they were options i didn't think it was really a stopped.

Now I'm at the mercy of a review. Please @UynGH @59blargedy remove the WIP tag and change it to ready for review :cat2: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday May 04, 2020 at 17:15:59_

----

You'll have a dedicated skill list ID to use after #584 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday May 07, 2020 at 16:35:43_

----

I'm burnt out after writing this quest. Please make the required changes.
Sorry for my candor.
I'll try to focus on small quests from now on.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 18:14:55_

----

Sure thing! Things like this _can_ be pretty grinding.

You're not in this all by yourself~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday May 11, 2020 at 01:41:26_

----

Pushed a commit to flip the "orientation" of the charVars for AF crafting to start at max and go towards zero, making sure all associated vars are gone when the player has crafted all the AF pieces.

And I tested it too! I have made sure that my changes didn't break kain's code and cause this to happen:
![discord](https://user-images.githubusercontent.com/13112942/81516797-af76e100-9328-11ea-80a5-e394eb7664b3.png)


As it's my own code, I'll tag @cocosolos in case they want to look at the most recent commit.

I intend to push another commit later for the other small things (hopefully tomorrow) .


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday May 12, 2020 at 00:53:40_

----

Pushed a second commit for various fixes and cleanup, including the Undersea regions and CSes. Had to rework Waoud and Whitegate a little after trying them as non-BLU and naked (respectively) caused unexpected behavior.

I set the Soulflayer to use the skill list ID that will be available to it in `release`. This branch is _way_ overdue for a update from `release` (switching to it stills need to deal with non-ignored confs). I'll do that merge after this PR is merged into blue-mage, and I'll uncomment Reprobation then.

I'm okay with merging this without Immortal Shield and Immoral Mind being scripted. We can add those later (after some testing on retail for Immortal Mind). Can potentially hold off on a `blue-mage` -> `canary` merge if those two missing skills are a concern for balance/"earn it" reasons.
