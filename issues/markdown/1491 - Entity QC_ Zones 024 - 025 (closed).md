**Labels:**



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Nov 10, 2020 at 05:22:35_
_Originally opened as: project-topaz/topaz - Issue 1491_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Same operations as previous entity PRs, including ...

* Update NPCs in our database from Nyu's retail caps.
* Rename qm1, qm2, etc. to something more meaningful.
* Update mob coords from Nyu's retail caps.
* When we have coords for one arena mob, infill coords for other arenas using known arena offsets.

Notes for this PR:

* Interestingly, the [Amaltheia](https://ffxiclopedia.fandom.com/wiki/Amaltheia) QM (16875894) was at 0, 0, 0 with status DISAPPEAR in retail capture.  I could not find any indication that this NM's location had been moved from the cave at K-6, and no other QM had coordinates in that area.  So in this case I ignored the retail caps and kept this QM at its current location.

