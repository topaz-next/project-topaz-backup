**Labels:**



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Friday Sep 18, 2020 at 18:38:45_
_Originally opened as: project-topaz/topaz - Issue 1158_

----

Just a small clean-up PR of 0x106 that was noticed. #1157 is just as effective - this PR isn't for security or anything.

- Moved quantity validation nearer the top, so it's clearer sooner that we're validating it
- Removed duplicate price check
- Removed duplicate null item check
- Move down the item creation a little so we're more consistent of when it's generated (ie: _after_ our checks)

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


