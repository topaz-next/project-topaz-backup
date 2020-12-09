**Labels:**



<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [KnowOne134](https://github.com/KnowOne134)**
_Sunday Feb 16, 2020 at 00:47:55_
_Originally opened as: project-topaz/topaz - Issue 343_

----

…vage global file i will add to for future use on entering, exit, ect

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

the global file will also play a big part for entering exiting and many other functions to come that are already planned


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Feb 17, 2020 at 03:05:44_

----

it might be worth a helper function to perform this task. do the pets have to be resummoned to update their status in salvage?  know there is a potentially similar situation down the road in voidwatch and also abyssea with buffs getting copied to pets.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Monday Feb 17, 2020 at 03:16:30_

----

You start salvage with the debuffs when entering. So you summon after the effect is already in place. And when so the pet will gain what ever effect and power you have. Also using a cell will remove the effect from the player amd the pet at same time. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Feb 17, 2020 at 03:28:38_

----

I mean synchronizing pets with masters in general though. it might be worthwhile to just have a reusable something we can call to sync their effects up in these situations rather than copying same block code to each pet script. A global func you feed which effects are being copied to and it do the work all in one spot.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Feb 17, 2020 at 03:29:24_

----

I'm probably not describing it well. think mixin like.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Feb 17, 2020 at 03:05:44_

----

it might be worth a helper function to perform this task. do the pets have to be resummoned to update their status in salvage?  know there is a potentially similar situation down the road in voidwatch and also abyssea with buffs getting copied to pets.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Monday Feb 17, 2020 at 03:16:30_

----

You start salvage with the debuffs when entering. So you summon after the effect is already in place. And when so the pet will gain what ever effect and power you have. Also using a cell will remove the effect from the player amd the pet at same time. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Feb 17, 2020 at 03:28:38_

----

I mean synchronizing pets with masters in general though. it might be worthwhile to just have a reusable something we can call to sync their effects up in these situations rather than copying same block code to each pet script. A global func you feed which effects are being copied to and it do the work all in one spot.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Feb 17, 2020 at 03:29:24_

----

I'm probably not describing it well. think mixin like.
