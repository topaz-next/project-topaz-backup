**Labels:**



<a href="https://github.com/ffxijuggalo"><img src="https://avatars3.githubusercontent.com/u/22580624?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ffxijuggalo](https://github.com/ffxijuggalo)**
_Thursday Jun 25, 2020 at 04:38:28_
_Originally opened as: project-topaz/topaz - Issue 769_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

[24/Jun] [18:00:48] [1;31m[Error] luautils::onSpellCast: scripts/globals/spells/bluemagic/battle_dance.lua:29: attempt to index global 'parrams' (a nil value)

Removed the extra "r" in parrams on line 29, no more errors.


----
<a href="https://github.com/ffxijuggalo"><img src="https://avatars3.githubusercontent.com/u/22580624?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ffxijuggalo](https://github.com/ffxijuggalo)**
_Thursday Jun 25, 2020 at 22:29:59_

----

I would have targeted release, but the line in question doesn't exist in release. Figured it was a canary only fix from a different PR that hasn't yet been merged into release.
