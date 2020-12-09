**Labels:**

merge ready



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Monday May 04, 2020 at 09:07:20_
_Originally opened as: project-topaz/topaz - Issue 583_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes the issue where an active exp chain always applies the current chain bonus exp to Decent Challenge and below mobs without giving a message.  Also eliminates several unnecessary conditional checks if the mob isn't EM+.  Thanks to cocosolos and aether for their help diagnosing and fixing this issue.
