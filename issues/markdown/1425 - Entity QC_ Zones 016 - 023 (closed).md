**Labels:**



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Oct 24, 2020 at 13:48:15_
_Originally opened as: project-topaz/topaz - Issue 1425_

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

* Each Promyvion zone has a QM that players can trade an item to receive a map of the zone.  This QM moves every 20-30min, or on a successful trade.  In Topaz, this QM currently does not move.  I've noted the known-so-far locations in the QM script.  Implementing this movement requires retail caps of all locations, and is outside the scope of these QC PRs.

