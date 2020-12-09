**Labels:**

merge ready



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Jul 16, 2020 at 08:04:34_
_Originally opened as: project-topaz/topaz - Issue 854_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

As always, big thanks to Nyu for capturing this data from retail zones.

This fixes (or creates new, where needed) mob pool data for mobs belonging to following categories of the [bestiary](https://ffxiclopedia.fandom.com/wiki/Category:Bestiary).  I've broken the commits into families for easier reviewing.

Completed Categories:
* Beasts
* Lizards
* Vermin

Going to stop adding to this PR now, to allow for review before it starts conflicting with other PRs.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 25, 2020 at 00:10:52_

----

Others: If you see a name change in this diff, it's because there's currently two groups with the same group name in a zone. Wren is updating the name of the duplicate group to match the mobs that are already in that group.

GitHub might refuse to properly expand surrounding lines, but in zone 272, there were two batches of Tarichuk: group 14 and group 32. The tarichuks in the zone are already divided into these separate groups, Group 32 in mob_spawn_points are already named Irascible Tarichuk. So Wren's updating the name in mob_groups to match the mobs belonging to it, and giving them a new mob_pool.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 25, 2020 at 00:17:05_

----

I'm intrigued how the previous model fields for these twitherym had random junk model data, when as "simple mobs" they should have all been "simple model" types.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Jul 25, 2020 at 00:26:41_

----

The reason this happened, btw, is because when the name column was added to the groups table, it was infilled from the pools table for whatever poolid was currently in the row, rather than from the mob_spawn_points table.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 25, 2020 at 14:13:22_

----

SE doesn't zero the unused bytes, so junk data gets caught in caps sometimes depending on capture methods (if you wireshark it you will get all sorts of nonsense)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 25, 2020 at 15:26:47_

----

Huh, TIL.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 25, 2020 at 00:10:52_

----

Others: If you see a name change in this diff, it's because there's currently two groups with the same group name in a zone. Wren is updating the name of the duplicate group to match the mobs that are already in that group.

GitHub might refuse to properly expand surrounding lines, but in zone 272, there were two batches of Tarichuk: group 14 and group 32. The tarichuks in the zone are already divided into these separate groups, Group 32 in mob_spawn_points are already named Irascible Tarichuk. So Wren's updating the name in mob_groups to match the mobs belonging to it, and giving them a new mob_pool.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 25, 2020 at 00:17:05_

----

I'm intrigued how the previous model fields for these twitherym had random junk model data, when as "simple mobs" they should have all been "simple model" types.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Jul 25, 2020 at 00:26:41_

----

The reason this happened, btw, is because when the name column was added to the groups table, it was infilled from the pools table for whatever poolid was currently in the row, rather than from the mob_spawn_points table.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 25, 2020 at 14:13:22_

----

SE doesn't zero the unused bytes, so junk data gets caught in caps sometimes depending on capture methods (if you wireshark it you will get all sorts of nonsense)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 25, 2020 at 15:26:47_

----

Huh, TIL.
