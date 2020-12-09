**Labels:**



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Sep 05, 2020 at 09:35:09_
_Originally opened as: project-topaz/topaz - Issue 1065_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Compared our data against retail captures for mob species within the "Dragons" category of the bestiary. Used both the wiki, and also cross-referencing the database by familyId, to find as many mobs within each species as I could. Did one species per commit for easier reviewing.

According to retails caps, Hydra's AnimationSub varies between 4 and 6, rather than 0 and 2.  The animations look the same, e.g. animation 0 and 4 are both three-headed.

Fixed Feldrautte_I_Rouhent's groupid.


----
<a href="https://github.com/Arklus"><img src="https://avatars1.githubusercontent.com/u/61334622?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Arklus](https://github.com/Arklus)**
_Saturday Sep 05, 2020 at 13:35:58_

----

only the linking table was changed?



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Sep 07, 2020 at 12:03:36_

----

> According to retails caps, Hydra's AnimationSub varies between 4 and 6, rather than 0 and 2. The animations look the same, e.g. animation 0 and 4 are both three-headed.

That makes me wonder what SE is using the extra bits on the mask for. Most models have 2 states, witha  few having 3. rarely you'll see more like that flying snake in abyssea that does wind wall animation. Especially weird that there are more values being used that it has visuals for.
