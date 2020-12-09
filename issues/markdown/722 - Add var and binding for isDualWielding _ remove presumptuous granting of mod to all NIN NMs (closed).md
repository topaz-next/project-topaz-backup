**Labels:**

approved



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Sunday Jun 14, 2020 at 00:25:30_
_Originally opened as: project-topaz/topaz - Issue 722_

----

As previously discussed, without adding dual wield mobs to the NIN NMs which _should_ have them, this will result in some NIN NMs becoming easier than they should be.

Here is a list of NMs which are currently automatically being given Dual Wield mobmod (note: _not trait_) which will make them _always_ have a second hit:
![github](https://user-images.githubusercontent.com/13112942/84581797-825c9900-add4-11ea-9ff9-69f2029df960.png)

Some of these mobs should always be attacking twice; others should not. Unfortunately, _the mob's model **can not** be used to distinguish which is which_. Some NIN NMs with the _same_ model will always attack twice per round, and others only once. Determining which are "dual wielding" (ie: which will always attack twice per combat round) would require video captures from retail.

**Future selves: The dual wield mobmod is bad, and we need to make it go away.** Mobs don't wield weapons, and the assumption that they do leads to mistakes like the one currently being fixed in this PR (NIN NMs with a great sword model being given "dual wield"). We will need to add some sort of numHits column to the DB which dictates how many hits a mob has per attack round. This is _not_ the same as Double Attack, which procs on weaponskill/TP moves.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 18, 2020 at 03:48:52_

----

Regarding the dual wield mobmod, would `tpz.mobMod.MULTI_HIT` work instead?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jun 18, 2020 at 16:38:57_

----

I think that's similar to the idea that we were going to go with, but with a db column in mob_pool instead, as an alternative to defining a mobmod for individual mobs or more entries in pool_mobmods. Teo and I have gone in circles over how to handle multi-hit mobs... multiple... times, and at this point I'm not 100% positive what if anything was decided on.
