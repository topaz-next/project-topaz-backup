**Labels:**

approved

merge ready



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Tuesday Jul 28, 2020 at 22:32:02_
_Originally opened as: project-topaz/topaz - Issue 905_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Don't see anywhere that these are supposed to link: https://ffxiclopedia.fandom.com/wiki/Steelshell


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Jul 28, 2020 at 23:25:29_

----

Good catch.

For everyone's clarity: my recent bestiary PRs are only checking against retail captures, so they may contain incorrect data in fields not captured, such as mob jobs, immunities, aggro, or linking.

When I find mobs sharing a pool, I use the existing pool to create one for the "new" mob, then edit the retail-captured fields on both.  For example, Fortalice Bats were using Funnel Bats pool.  I made a new pool for Fortalice Bats, that inherited all the non-capturable fields from Funnel Bats.

All this to say, that once I finish checking all bestiary families again retail, we'll still need to do another sweep through all the mobs, to QC against wikis all the non-captured fields.  I expect we'll find a lot of mistakes similar to this one that Tankfest is fixing.

