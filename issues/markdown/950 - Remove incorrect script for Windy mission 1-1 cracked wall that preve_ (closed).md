**Labels:**

approved



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Friday Aug 14, 2020 at 21:23:09_
_Originally opened as: project-topaz/topaz - Issue 950_

----

…nts it from opening

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

A couple of weeks ago, the name of this file was corrected to match its counterpart in our database.  Unfortunately, when that happened, it broke the cracked wall that opens to windurst mission 1-1.  Since no standard door on topaz has a script, this needs to be deleted to allow players access to the magical gizmo that lies within.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 14, 2020 at 21:50:38_

----

It looks like that script was used by somebody for testing so that they did not have to walk all the way to the correct door for a quest they were working on. then they commented it out and left it in place.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Friday Aug 14, 2020 at 21:56:00_

----

> 
> 
> It looks like that script was used by somebody for testing so that they did not have to walk all the way to the correct door for a quest they were working on. then they commented it out and left it in place.

I had assumed that maybe it WAS the correct script for this name 2 years ago, but SE changed it and the script was never updated.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 14, 2020 at 23:10:48_

----

> I had assumed that maybe it WAS the correct script for this name 2 years ago, but SE changed it and the script was never updated.

possibly if someone made a 2nd script instead of renaming the original. Sometimes the special named object due name change - in some cases the "name" we capture amounts to what offset the npc is, so any shift renamed it. `@05A` or `_5A` being shorthand for 90th object in zone for instance (0x05A). In most cases, our name doesn't even have to match but some object need their special name to function right, like the bcnm entrances up in sky. Or airships. if you rename an airship client go boom.
