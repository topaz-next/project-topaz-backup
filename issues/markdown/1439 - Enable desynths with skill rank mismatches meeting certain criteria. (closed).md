**Labels:**

crafting



<a href="https://github.com/Dirk-Dieters"><img src="https://avatars3.githubusercontent.com/u/35855037?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Dirk-Dieters](https://github.com/Dirk-Dieters)**
_Tuesday Oct 27, 2020 at 16:43:08_
_Originally opened as: project-topaz/topaz - Issue 1439_

----

Continuing the work of #1306, This is the first step of verifying excluded recipes following the synthesis database rewrite. Per [IBM2431's comment](https://github.com/project-topaz/topaz/pull/1306#issuecomment-717001439), I have activated and assigned levels to recepies with the following criteria:

1. Desynth with FFXIAH listing the skill level as 255
2. BGWiki lists a specific level (no approximations or verification needed flags)
3. Recipe and results match

No assumptions were made based on similar recipes (various gem rings and earrings for example), and no other data was considered.

Recipes with a specific BGWiki skill level but a mismatch in yield or recipe had their skill level set, but remained commented out and had comment added at the end of the line.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


