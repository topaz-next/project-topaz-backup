**Labels:**

merge ready



<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Lynnea1320](https://github.com/Lynnea1320)**
_Thursday Jun 25, 2020 at 18:43:23_
_Originally opened as: project-topaz/topaz - Issue 771_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 25, 2020 at 19:10:46_

----

Where did you get 4-5 hours? I'm only seeing as low as 15-30 mins on wikia, and again I don't think lottery mobs should have an upper bound on their spawn time.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 25, 2020 at 19:34:01_

----

It seems that none of these NM IDs exist. Also the only placeholder seems to be 16814330 and is supposed to spawn in a few different locations (there's only 1 room with 3 Diremites, the 3rd one in that room is 16814330 and is supposed to spawn in a few different places.)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 25, 2020 at 19:37:31_

----

Sorry I might actually be wrong about this, they're there they just don't have any spawn points so they're not being loaded at all. Same with the other PHs, looks like there are multiples (assuming only 1 is supposed to be up at a time) but none of the other ones have spawn points set.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 25, 2020 at 19:39:12_

----

PHs should be:
```lua
[16814319] = 16814320,
[16814330] = 16814331,
[16814343] = 16814344,
```


----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Thursday Jun 25, 2020 at 20:59:17_

----

Oh sorry, I thought I pasted the clean version not the Dawnbreak version.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 25, 2020 at 19:10:46_

----

Where did you get 4-5 hours? I'm only seeing as low as 15-30 mins on wikia, and again I don't think lottery mobs should have an upper bound on their spawn time.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 25, 2020 at 19:34:01_

----

It seems that none of these NM IDs exist. Also the only placeholder seems to be 16814330 and is supposed to spawn in a few different locations (there's only 1 room with 3 Diremites, the 3rd one in that room is 16814330 and is supposed to spawn in a few different places.)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 25, 2020 at 19:37:31_

----

Sorry I might actually be wrong about this, they're there they just don't have any spawn points so they're not being loaded at all. Same with the other PHs, looks like there are multiples (assuming only 1 is supposed to be up at a time) but none of the other ones have spawn points set.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 25, 2020 at 19:39:12_

----

PHs should be:
```lua
[16814319] = 16814320,
[16814330] = 16814331,
[16814343] = 16814344,
```


----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Thursday Jun 25, 2020 at 20:59:17_

----

Oh sorry, I thought I pasted the clean version not the Dawnbreak version.
