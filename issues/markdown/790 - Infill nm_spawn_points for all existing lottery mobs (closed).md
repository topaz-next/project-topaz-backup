**Labels:**

merge ready



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Jul 01, 2020 at 12:10:20_
_Originally opened as: project-topaz/topaz - Issue 790_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes #262 

This PR contains two commits.

* The first orders nm_spawn_points.sql by mobid (fixing just a few entries that aren't in order)
* The second infills from mob_spawn_points missing coordinates for all lottery-type mobs.  The lottery code calls UpdateNMSpawnPoint, which causes those logged errors in #262, so these entries will prevent errors for all existing mobs.

I understand that we may eventually move to a different/better spawn point system, but this at least fixes the immediate problem.
