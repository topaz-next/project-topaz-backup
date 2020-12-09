**Labels:**



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Friday Oct 23, 2020 at 02:13:44_
_Originally opened as: project-topaz/topaz - Issue 1409_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Same operations as previous entity PRs, including ...

* Update NPCs in our database from Nyu's retail caps.

* Rename qm1, qm2, etc. to something more meaningful.

* Update mob coords from Nyu's retail caps.  Note that many of these adjustments are insignificant, but this also infills coords for some mobs that have none.  If it makes reviewing easier, I could add an adjustment minimum.  For example, "don't touch rows where the mob has 'moved' fewer than 20 yalms from its previous position."  Let me know!

* When we have coords for one arena mob, infill coords for other arenas using known arena offsets.

Additional note for this PR:

The QM_POPS table in Abyssea zone IDs.luas could use some love.  They include unused string value describing each NPC as qm1, qm2, etc.  This string isn't used by functions in Abyssea global that consume QM_POPS.  And QM_POPS could have better formatting, removing that first value, adding keys, and so on.

Once I reach the last of the Abyssea zones with these entity QC PRs, I plan to reformat those tables and adjust the Abyssea global to match.  I added some TODOs for this work.

