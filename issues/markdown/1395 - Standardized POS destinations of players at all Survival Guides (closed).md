**Labels:**



<a href="https://github.com/EpicTaru"><img src="https://avatars3.githubusercontent.com/u/26195580?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [EpicTaru](https://github.com/EpicTaru)**
_Monday Oct 19, 2020 at 23:58:20_
_Originally opened as: project-topaz/topaz - Issue 1395_

----

This is to ensure that when a Survival Guide teleport is used, the player is placed directly next to a Guide (or ON the guide in navmesh limitations prohibit the placing next to the Guide).

Multiple times were noticed when using a Survival Guide the player was placed at a position near the Survival Guide but not directly next or ON the Guide.

This all began because of the below issue with the placement of the player at the Survival Guide in Romaeve.  In my post-code fix of that placement, I audited all of the other Survival Guide placements (to make sure that they were all working) and the oddity and non-standardness of player placement. At some, players were placed near, at some, players were placed far away, at some, players were placed directly ON the survival guide. This all /triggered me so I decided to standardize the player placement at all Survival Guides.

Biggest change: Position of Survival Guide in Romaeve was a full 36 points different on the X-axis from where the Survival Guide book actually is (most likely an accidental inverse of numbers (51 instead of 15)).

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/EpicTaru"><img src="https://avatars3.githubusercontent.com/u/26195580?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [EpicTaru](https://github.com/EpicTaru)**
_Wednesday Oct 21, 2020 at 03:54:55_

----

~~I've decided to convert this to draft and work on rotation of player when placed at the target guide.~~

Edit: DONE!!!

By default, I'll set it so they are placed in front of the guide, facing it. If navmesh issues prevent this, you'll be placed on the left or right side, facing the guide. If neither of these are able to be used, I'll place you on the guide, facing out from it (as if you were the open guide book, but you had eyes, looking out at people that are standing in front of the guide).....but don't think I'll need this last option at all. 

Any thoughts/objections? 
