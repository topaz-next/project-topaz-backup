**Labels:**

merge ready



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Jul 01, 2020 at 10:59:50_
_Originally opened as: project-topaz/topaz - Issue 789_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes #667 
Relates to #682 

This PR fixes the remaining issues with quest "Flyers for Regine" and neatens the code.

* When approaching tradable NPCs, you now receive a message "So-and-so looks over curiously for a moment."
* The "looks over curiously" messages are now found by offsets from a base message.
* The after-trading dialog from each NPC is now prefixed with their name.
* Trade progress is now tracked with a single bitmask rather than 15 vars.
* Code for defining approach regions and trading flyers is now contained in scripts/quests/flyers_for_regine

