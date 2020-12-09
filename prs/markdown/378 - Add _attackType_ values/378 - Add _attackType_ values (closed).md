**Labels:**

merge ready



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 04:26:31_
_Originally opened as: project-topaz/topaz - Issue 378_

----

Also updated bluemagic.lua to properly default to NONE for
any non-damage dealing spells.

This commit follows updates breath spells to use the BREATH enum value, per:
https://github.com/project-topaz/topaz/issues/377

Fixes https://github.com/project-topaz/topaz/issues/314

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Feb 24, 2020 at 19:37:45_

----

Do we want a different identifier for ranged physical spells?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Feb 24, 2020 at 19:43:22_

----

Not necessarily a question directed at you, mrhappyasthma (unless you _want_ to take a guess):

Bgwiki has two different classifications for spells whose damage type _I_ would normally consider "blunt" - they have identifiers for both "Blunt" and "Hand-to-hand". In this instance, they identify Asuran Claws as "hand to hand".

Are there theories on why they might do this, and is it something we should be mindful of?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Feb 24, 2020 at 19:44:35_

----

Because down here, we _are_ using the "hth" damage type, when for all the "hand-to-hand" (as identified on bgwiki) before this were simply "blunt".


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Feb 24, 2020 at 19:48:17_

----

Marking queasyshroom here as another "ranged" spell.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Feb 24, 2020 at 19:52:04_

----

And for example, here we have it as "hand-to-hand" when bgwiki lists it as "blunt"

(I know you weren't responsible for this, mrhappyasthma)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Feb 24, 2020 at 21:44:04_

----

@ibm2431 there actually are different dmg resistances between the 2 on mobs. there are only a few mobs where that difference matters however, and I don't know that anyone confirmed it before tossing it onto the wiki.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Feb 25, 2020 at 04:40:29_

----

Would we prefer to update this to H2H then?




----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Feb 25, 2020 at 04:41:14_

----

I grabbed the H2H classification from here: https://ffxiclopedia.fandom.com/wiki/Hysteric_Barrage


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Feb 25, 2020 at 04:42:28_

----

This should be blunt, it seems. From the various websites that have it documented as such.

I can't find any reference to H2H


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Feb 25, 2020 at 04:42:32_

----

These aren't labeled as range in a very noticeable spot. But seems like the following 3 are classified as ranged:

Queasyshroom
Feather Storm
Pinecone Bomb


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Feb 25, 2020 at 04:43:18_

----

Interestingly this is `Blunt` here: https://ffxiclopedia.fandom.com/wiki/Asuran_Claws

But in the comments they say:

> Hand-to-Hand-based damage.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Wednesday Feb 26, 2020 at 04:04:14_

----

should be changed to ranged yes


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 03:56:33_

----

Seems to be H2H here also: https://www.bg-wiki.com/bg/Hysteric_Barrage


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 03:57:39_

----

It is marked H2H here: https://www.bg-wiki.com/bg/Asuran_Claws

So I'll go with that since it seems to be the correct one.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 03:59:59_

----

Done.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 04:00:05_

----

Done.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 04:00:12_

----

Done.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 04:00:19_

----

Done.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Feb 24, 2020 at 19:37:45_

----

Do we want a different identifier for ranged physical spells?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Feb 24, 2020 at 19:43:22_

----

Not necessarily a question directed at you, mrhappyasthma (unless you _want_ to take a guess):

Bgwiki has two different classifications for spells whose damage type _I_ would normally consider "blunt" - they have identifiers for both "Blunt" and "Hand-to-hand". In this instance, they identify Asuran Claws as "hand to hand".

Are there theories on why they might do this, and is it something we should be mindful of?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Feb 24, 2020 at 19:44:35_

----

Because down here, we _are_ using the "hth" damage type, when for all the "hand-to-hand" (as identified on bgwiki) before this were simply "blunt".


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Feb 24, 2020 at 19:48:17_

----

Marking queasyshroom here as another "ranged" spell.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Feb 24, 2020 at 19:52:04_

----

And for example, here we have it as "hand-to-hand" when bgwiki lists it as "blunt"

(I know you weren't responsible for this, mrhappyasthma)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Feb 24, 2020 at 21:44:04_

----

@ibm2431 there actually are different dmg resistances between the 2 on mobs. there are only a few mobs where that difference matters however, and I don't know that anyone confirmed it before tossing it onto the wiki.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Feb 25, 2020 at 04:40:29_

----

Would we prefer to update this to H2H then?




----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Feb 25, 2020 at 04:41:14_

----

I grabbed the H2H classification from here: https://ffxiclopedia.fandom.com/wiki/Hysteric_Barrage


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Feb 25, 2020 at 04:42:28_

----

This should be blunt, it seems. From the various websites that have it documented as such.

I can't find any reference to H2H


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Feb 25, 2020 at 04:42:32_

----

These aren't labeled as range in a very noticeable spot. But seems like the following 3 are classified as ranged:

Queasyshroom
Feather Storm
Pinecone Bomb


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Feb 25, 2020 at 04:43:18_

----

Interestingly this is `Blunt` here: https://ffxiclopedia.fandom.com/wiki/Asuran_Claws

But in the comments they say:

> Hand-to-Hand-based damage.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Wednesday Feb 26, 2020 at 04:04:14_

----

should be changed to ranged yes


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 03:56:33_

----

Seems to be H2H here also: https://www.bg-wiki.com/bg/Hysteric_Barrage


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 03:57:39_

----

It is marked H2H here: https://www.bg-wiki.com/bg/Asuran_Claws

So I'll go with that since it seems to be the correct one.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 03:59:59_

----

Done.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 04:00:05_

----

Done.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 04:00:12_

----

Done.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 04:00:19_

----

Done.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Sunday Feb 23, 2020 at 13:27:16_

----

In the future the breath spells will need the breath enum or another call to bluemagic lua to get its correct formula as it doesnt follow the magical formula at all, not even its magic burst formula


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 23, 2020 at 14:08:55_

----

If we're going to redo BLU soon-ish, I'd say keep breath spells labeled as breath spells, because whether a spell is a breath attack _will_ be accounted for.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 19:17:20_

----

Sounds good. I'll update the breath spells after a rebase. Will also add context to the issue.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 19:38:35_

----

Rebased and updated breath spells to use `attachType.BREATH`.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 04:02:55_

----

Consensus seemed to be that the 3 RANGED spells should be annotated as such. I applied those as well as fixed the two mistakes in the attackTypes.
