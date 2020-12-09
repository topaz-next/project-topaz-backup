**Labels:**

reviewed



<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [InoUno](https://github.com/InoUno)**
_Tuesday Jun 16, 2020 at 16:37:26_
_Originally opened as: project-topaz/topaz - Issue 734_

----

This PR adds a static ordering to status effects just like retail has. This is achieved by changing the `vector` of status effects in the `StatusEffectContainer` to a `multiset` with a specific ordering.

The ordering is generally done via the new `sort_key` column in the `status_effects` table. Certain special effects are grouped together and then ordered in various ways internally, such as songs/rolls and maneuvers.

I have not set a `sort_key` for all status effects with this PR, since I am not able to test it for all status effects in retail by myself. I've added the most basic ones I could test with the jobs/levels I had.
However, the way it's currently set up, `sort_key`s can be added in later PRs when the correct placement for any given status effect is figured out. The `sort_key`s I've added in this PR are spaced quite far from each other, to allow for insertions of other status effects in-between them, if it is found out that other status effects should fit in that place.

Status effects without a `sort_key` will be grouped together towards the end of the effects (defaults to a sort key with value `10000`), and then ordered internally by their status effect ID such that the ordering of them is also static. Ideally, all status effects should have a sort key, but I think this is a decent fall-back ordering until the correct ordering is figured out.

**Maneuver ordering**
Maneuvers are all grouped together, and then internally ordered by their start time, having the newest on the left, and oldest on the right.
See https://github.com/EdenServer/community/issues/2507

**Song/roll ordering**
From my testing on retail, the following is what I've found and implemented. Here's a [video showing it in action on retail](https://www.youtube.com/watch?v=TkGdnLPxGjI).

All songs and rolls are grouped with the same sort key, and then internally ordered based on which "slot" they occupy. The "slot" here is just an internal ordering key, mostly based on when the effect was added.

The slot a new song/roll will take, is determined in this order:
* If the song/roll overwrites an existing song/roll of the same type/tier, it will occupy the same slot as the one it overwrites. 
* If the song/roll replaces the "oldest" song/roll (because there's more than the allowed songs/rolls from that character), then the new song/roll will take the slot of the "oldest" song/roll which it replaces.
* Otherwise, the new song/roll will occupy the lowest free slot number.


<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jul 13, 2020 at 14:36:38_

----

I believe wards are similar.

Would it be more prudent add these as a status flag? I'm seeing similar hard-coded comparison functions down below relating to bust effects (I realize these were already there).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jul 13, 2020 at 14:42:19_

----

I may have to go over this again later, but I feel we could store the lowest free slot as effects are added and removed from the container. This would save us having to iterate through all the effects every time we wanted to find the next free slot. But I'm only seeing songs and rolls calling this function, so I may be misunderstanding how the slots function.


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Monday Jul 13, 2020 at 19:26:05_

----

Could definitely add it as a status flag, if it is something that should be generalized.
I wasn't aware of other effects that are ordered by the start time like this, but if there's more then it definitely makes sense.


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Monday Jul 13, 2020 at 21:35:21_

----

Good suggestion. It could probably be changed to store the lowest free slot as a value in the container, but would then need some kind of data structure to make it easy to calculate the smallest free slot.

I didn't test all status effects, but at least songs and rolls are ordered like this. There could definitely be more like this that are grouped with songs and rolls, like maybe DNC buffs, that I haven't researched at this point in time. But this should be easy to add in later, if that's the case.


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Friday Jul 24, 2020 at 13:38:02_

----

After giving it some thought, I don't think it's worth the added complexity of changing this to keep track of lowest free slot, instead of just iterating whenever the lowest free slot is needed (which is not that often).

Besides, the code iterates through the status effects pretty much any time anything happens to some of them (i.e. see all the iterator changes I've made in the PR), so I don't think this is something that would be impacting performance in any noticeable way.


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Friday Jul 24, 2020 at 13:40:41_

----

Since I am not able to research/test/verify that any other effects are ordered like this, I will probably not be changing it in this PR (unless someone else can get confirmation on other status effects behaving like this).
If it is found out at a later date that this is how other certain status effects are ordered, the implementation can be changed at that point.

Thoughts?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jul 13, 2020 at 14:36:38_

----

I believe wards are similar.

Would it be more prudent add these as a status flag? I'm seeing similar hard-coded comparison functions down below relating to bust effects (I realize these were already there).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jul 13, 2020 at 14:42:19_

----

I may have to go over this again later, but I feel we could store the lowest free slot as effects are added and removed from the container. This would save us having to iterate through all the effects every time we wanted to find the next free slot. But I'm only seeing songs and rolls calling this function, so I may be misunderstanding how the slots function.


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Monday Jul 13, 2020 at 19:26:05_

----

Could definitely add it as a status flag, if it is something that should be generalized.
I wasn't aware of other effects that are ordered by the start time like this, but if there's more then it definitely makes sense.


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Monday Jul 13, 2020 at 21:35:21_

----

Good suggestion. It could probably be changed to store the lowest free slot as a value in the container, but would then need some kind of data structure to make it easy to calculate the smallest free slot.

I didn't test all status effects, but at least songs and rolls are ordered like this. There could definitely be more like this that are grouped with songs and rolls, like maybe DNC buffs, that I haven't researched at this point in time. But this should be easy to add in later, if that's the case.


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Friday Jul 24, 2020 at 13:38:02_

----

After giving it some thought, I don't think it's worth the added complexity of changing this to keep track of lowest free slot, instead of just iterating whenever the lowest free slot is needed (which is not that often).

Besides, the code iterates through the status effects pretty much any time anything happens to some of them (i.e. see all the iterator changes I've made in the PR), so I don't think this is something that would be impacting performance in any noticeable way.


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Friday Jul 24, 2020 at 13:40:41_

----

Since I am not able to research/test/verify that any other effects are ordered like this, I will probably not be changing it in this PR (unless someone else can get confirmation on other status effects behaving like this).
If it is found out at a later date that this is how other certain status effects are ordered, the implementation can be changed at that point.

Thoughts?


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Jun 17, 2020 at 06:36:12_

----

awesome :smile: 
does this apply to other effects like white magic?


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Wednesday Jun 17, 2020 at 10:54:07_

----

Yes, this applies to all effects for all battle entities.


----
<a href="https://github.com/zircon-tpl"><img src="https://avatars0.githubusercontent.com/u/60901633?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zircon-tpl](https://github.com/zircon-tpl)**
_Thursday Jul 23, 2020 at 04:20:00_

----

Hello, @InoUno and @ibm2431 !

I am ensuring that this Pull Request has not been forgotten! Will work continue on this Pull Request?


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Saturday Aug 22, 2020 at 17:45:33_

----

@InoUno if you can fix the merge conflicts ill move forward with merging this. i agree with the iterative nature and that this solves a problem and makes ordering more retail accurate, so would like to merge it in. Sorry for all the merge requires.


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Tuesday Sep 08, 2020 at 15:32:31_

----

Current merge conflict resolved.
I noticed this PR is now based on a non-release branch, so just a fair warning that I think there's more merge conflicts once that branch is merged with release.
