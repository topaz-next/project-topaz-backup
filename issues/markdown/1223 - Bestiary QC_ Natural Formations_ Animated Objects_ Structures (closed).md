**Labels:**



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Sep 30, 2020 at 15:34:52_
_Originally opened as: project-topaz/topaz - Issue 1223_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Compared our data against retail captures for mob species within the "Natural Formations", "Animated Objects", and "Sturctures" categories of the bestiary. Used both the wiki, and also cross-referencing the database by familyIds, to find as many mobs within each species as I could. Did one species per commit for easier reviewing.

* changed [blossoms](https://ffxiclopedia.fandom.com/wiki/Category:Blossoms) and [geysers](https://ffxiclopedia.fandom.com/wiki/Category%3AGeysers) from amorph to unclassified
* added family for [fungi](https://ffxiclopedia.fandom.com/wiki/Category%3AFungi).
* removed droplist 2330 from many mob groups who should not drop these items (steelshell drops)
* Seed Crystal is no longer an amphiptere.
* Crimson Grimoire is no longer a humanoid-hume.
* removed some incorrect skill lists.
* adjusted some aggro / true detection / detection types.

https://www.bg-wiki.com/bg/Category:Bestiary#Miscellaneous_Types
https://ffxiclopedia.fandom.com/wiki/Category:Bestiary
