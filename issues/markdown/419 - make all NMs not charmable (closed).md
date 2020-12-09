**Labels:**

reviewed



<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [KnowOne134](https://github.com/KnowOne134)**
_Friday Mar 13, 2020 at 13:55:34_
_Originally opened as: project-topaz/topaz - Issue 419_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

not all NMs were being tagged on initialize for being uncharmable. this will correct that.
if you need a NM to be charmable will have to tag it with mobMod Charmable, 1 anywhere in script beside onMobInitialize


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Tuesday Mar 17, 2020 at 15:02:37_

----

Should I delete all this logic and move to instance loader and zone loader?
https://github.com/project-topaz/topaz/blob/8985d2af68876367592222836db1f8e5b15c8175/src/map/utils/mobutils.cpp#L564


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Tuesday Mar 17, 2020 at 15:03:10_

----

As it is I'm just adding to an already in place system


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 18, 2020 at 19:48:20_

----

I think that setting charm mod should never have been in `calculateStats`. The function is used to [recalculate mob stats depending on the level chosen when a mob spawns](https://github.com/project-topaz/topaz/blob/8985d2af68876367592222836db1f8e5b15c8175/src/map/entities/mobentity.cpp#L503-L528). Whether or not a mob is charmable isn't really a "stat" - it never changes from spawn-to-spawn. And as you pointed out, it occurs _after_ mobInitialize, and I feel we shouldn't need to deliberately use a different lua function to overwrite the charm mod simply because core's assignment is in the wrong place.
