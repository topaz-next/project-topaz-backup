**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Oct 04, 2020 at 02:04:23_
_Originally opened as: project-topaz/topaz - Issue 1248_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This commit adds a check for whether the player already obtained the key item of the quest's current step. Without this, and the former code, the key item could be obtained an infinite number of times by clicking the fountain again and again after killing the Mantas.

Also reduces the conditions path, applies style guide and adds locals for re-use.
