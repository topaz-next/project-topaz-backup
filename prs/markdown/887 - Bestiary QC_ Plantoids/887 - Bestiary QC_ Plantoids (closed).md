**Labels:**

merge ready



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Jul 25, 2020 at 05:45:50_
_Originally opened as: project-topaz/topaz - Issue 887_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Included in this PR:

* Added missing apostrophes to mob_spawn_points.polutils_name.

* Changed Sauromugue_Skink and Thunderclaw_Thuban family from panopt to raptor.

* Realized that wiki was missing a few mobs from its bestiary category lists, so I revisited the categories from my previous PR (beasts, lizards, vermin), cross-checked each by family, found the missing mobs, and QCed them as well.  Going forward I'll use both wiki and family-crosscheck to find as many mobs as possible.

* QCed against retail members of the "Plantoids" category.  Put each species in its own commit for easier reviewing.



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Jul 26, 2020 at 04:24:57_

----

Do 16933057 and 16933058 need the same change?


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Sunday Jul 26, 2020 at 04:32:57_

----

So, in each of Barometz and Borametz, there is one mob with different flags (noted here by pool 98 and 99) than the others (noted here with pools 38 and 39).  In the retail capture I have from Nyu, the ID of the different mob is 16933055 for Barometz, and 16933056 for Borametz.

It might be that the "special" mob is chosen at random, each time you start a NE Apollyon run.  But unless that's the case, these values are what match the most recent retail cap.

Per wiki,
```
Note that there is one large black Barometz and one large white Borametz. Combined with Goobbue Harvester, one will open the Vortex, one will drop the item chest and one will do nothing.
```

The ones with the different flags are probably these "large" versions, which I'm guessing are static rather than randomly selected.  Code for opening the portal doesn't yet exist; Goobbue Harvester script isn't created yet, and none of the Bora/Baro-metz scripts open the portal.  But that change is outside the scope of this PR.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Jul 26, 2020 at 05:08:40_

----

@cocosolos , @59blargedy ^ (we'll have to look into how the "special" mob works; random or static; re: flags)

Wren: Scripts work in Limbus branch, but nailing down the exact behavior to correct mob ID is indeed outside of scope of this PR.




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jul 26, 2020 at 05:30:25_

----

The large mobs are probably supposed to be random, but at the time I couldn't figure out a clean way to adjust flags on spawn, so just went with static for now since their functions are still random. 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Jul 26, 2020 at 04:24:57_

----

Do 16933057 and 16933058 need the same change?


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Sunday Jul 26, 2020 at 04:32:57_

----

So, in each of Barometz and Borametz, there is one mob with different flags (noted here by pool 98 and 99) than the others (noted here with pools 38 and 39).  In the retail capture I have from Nyu, the ID of the different mob is 16933055 for Barometz, and 16933056 for Borametz.

It might be that the "special" mob is chosen at random, each time you start a NE Apollyon run.  But unless that's the case, these values are what match the most recent retail cap.

Per wiki,
```
Note that there is one large black Barometz and one large white Borametz. Combined with Goobbue Harvester, one will open the Vortex, one will drop the item chest and one will do nothing.
```

The ones with the different flags are probably these "large" versions, which I'm guessing are static rather than randomly selected.  Code for opening the portal doesn't yet exist; Goobbue Harvester script isn't created yet, and none of the Bora/Baro-metz scripts open the portal.  But that change is outside the scope of this PR.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Jul 26, 2020 at 05:08:40_

----

@cocosolos , @59blargedy ^ (we'll have to look into how the "special" mob works; random or static; re: flags)

Wren: Scripts work in Limbus branch, but nailing down the exact behavior to correct mob ID is indeed outside of scope of this PR.




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jul 26, 2020 at 05:30:25_

----

The large mobs are probably supposed to be random, but at the time I couldn't figure out a clean way to adjust flags on spawn, so just went with static for now since their functions are still random. 
