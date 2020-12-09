**Labels:**



<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 02:48:29_
_Originally opened as: project-topaz/topaz - Issue 341_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

found that temp items were only removing from zoning out of an instance in retail captures. logging out and in from or crashing in an instance retained items


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 16, 2020 at 00:45:37_

----

temp items clear out in normal zones to. the only place they retain is in abyssea to my knowledge. I am not sure they even have retail reloading behavior yet (didn't look) but I suspect they should just always clear out on leaving(entering?) a zone and for the other places (abyssea, besieged) they get loaded in based on a condition of some sort - be it a variable or what have you saying.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Sunday Feb 16, 2020 at 03:27:28_

----

My intention here and has been tested that any assault where you dc or logout and back into an instance where you havent changed zone you do retain every temp item you have, in abyssea it reloads a new set of temp items. And I believe anywhere else in the game they just clear out. Test in nyzul buying items and ones loaded from box. Force dc and logout and in and all temp items retained. In assault you always keep your fireflies. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Feb 16, 2020 at 03:42:06_

----

I think I misread this
```
 if (m_zoneType != ZONETYPE_DUNGEON_INSTANCED)
```
as == actually

for some derpy reason I was thinking of nyzul's temp items, and those teleports probably don't "zone" you.
