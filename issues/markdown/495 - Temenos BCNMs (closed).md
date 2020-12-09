**Labels:**

focus



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 15, 2020 at 00:10:57_
_Originally opened as: project-topaz/topaz - Issue 495_

----

All 8 level 75 Temenos zones.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Apr 21, 2020 at 23:29:14_

----

> Regarding Carbuncle's decreasing resistances:
> 
> > [Note: Carbuncle has exceptionally high damage taken resistance upon first entering the zone; this is progressively weakened by defeating the six elementals/avatars scattered around the zone.](https://www.bg-wiki.com/bg/Central_Temenos_-_2nd_Floor)
> 
> Is this elemental resistances as coded, or flat physical/magical resistances?

This was already being done with elemental resistance in the Mystic Avatar script, so I just moved it to the elementals. It sounds like it should be damage taken though not elemental resist.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 22, 2020 at 04:39:01_

----

> > Regarding Carbuncle's decreasing resistances:
> > > [Note: Carbuncle has exceptionally high damage taken resistance upon first entering the zone; this is progressively weakened by defeating the six elementals/avatars scattered around the zone.](https://www.bg-wiki.com/bg/Central_Temenos_-_2nd_Floor)
> > 
> > 
> > Is this elemental resistances as coded, or flat physical/magical resistances?
> 
> This was already being done with elemental resistance in the Mystic Avatar script, so I just moved it to the elementals. It sounds like it should be damage taken though not elemental resist.

Probably the element defense mods, which act like damage taken mods of 1 specified element each - the early revisions often mixed these up with resistance rate mods
