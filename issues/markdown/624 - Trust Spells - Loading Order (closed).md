**Labels:**



<a href="https://github.com/brianmask"><img src="https://avatars2.githubusercontent.com/u/33399423?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [brianmask](https://github.com/brianmask)**
_Friday May 15, 2020 at 00:20:13_
_Originally opened as: project-topaz/topaz - Issue 624_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Currently Trust spells are loaded into the spell container by order of appearance in the mob_spell_lists.sql.  This presents logic issues for get_highest_available due to not all spells being ordered by absolute highest available order.

This pull basically places an order by clause in the sql upon spell load which will order by minimum level required and will naturally place spells in order so highest available and lowest available are in natural order based on availability.

This should not affect mob casting since all functions were random in nature to begin with, but will resolve trust casting for cases such as Shantotto.

