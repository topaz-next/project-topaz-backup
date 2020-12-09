**Labels:**

exploit



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Saturday Oct 31, 2020 at 12:40:06_
_Originally opened as: project-topaz/topaz - Issue 1458_

----

**NOTE:** There is a patch that must be applied to this PR if you're taking it in isolation, otherwise you get strange behaviour (see comments below).
**PATCH:** https://github.com/project-topaz/topaz/commit/26263447def756aead19281e19cd5f3757cd467b

Stop players being able to hide off-navmesh close to walls.

This is a further cleaned up and tested version of the code changes in here: https://github.com/project-topaz/topaz/pull/1423
I'm going to dedicate that PR solely to actual navmesh changes.

EDIT: Thanks again to @xenonsmurf for digging into recast/detour and figuring out all of this stuff, and for teaching the community how to deal with navigation and navmeshes 🙏 

EDIT2: Added exploit tag, while this isn't directly harmful to a server, it does allow abusers to avoid dangers and 'cheese' certain zones. No bueno.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Nov 01, 2020 at 04:52:54_

----

I have gotten a report that this has created "wallhacking death machines", looking into it right away!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Nov 01, 2020 at 06:12:59_

----

Fixed: https://github.com/project-topaz/topaz/commit/26263447def756aead19281e19cd5f3757cd467b
