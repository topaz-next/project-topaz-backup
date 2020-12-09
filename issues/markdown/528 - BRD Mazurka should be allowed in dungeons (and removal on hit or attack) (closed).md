**Labels:**

bug



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Apr 25, 2020 at 20:38:28_
_Originally opened as: project-topaz/topaz - Issue 528_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Bard Mazurka currently is not removed when taking an action against an enemy or when getting hit (https://ffxiclopedia.fandom.com/wiki/Mazurka)

Also it should work in dungeons (https://www.bg-wiki.com/bg/Category:Mazurka) Currently if tried to cast on a dungeon shows "you cannot use raptor mazurka in this area)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Apr 25, 2020 at 21:05:00_

----

the casting should be an easy fix, took a look at the zone.cpp and it looks like its received from the zone db under misc. (just need to be patient whomever gets to work on it)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 26, 2020 at 17:23:19_

----

I dunno if SE kept it (as it was always stupid tbh) but that used to be a legit retail restriction on it. I never understood why.

Edit: it was updated out, took forever to find the patch it happened in.


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Saturday May 02, 2020 at 20:45:28_

----

Fixed by https://github.com/project-topaz/topaz/pull/539.
