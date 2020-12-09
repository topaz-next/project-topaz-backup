**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Jun 27, 2020 at 06:08:14_
_Originally opened as: project-topaz/topaz - Issue 776_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

This was experienced on current Canaria.

This is for the Zilart Mission in Den of Rancor.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 27, 2020 at 14:44:39_

----

bcnm superlink got broken/removed sounds like


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Jun 27, 2020 at 14:51:45_

----

> bcnm superlink got broken/removed sounds like

totally, its a good first issue for someone =)


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Oct 10, 2020 at 03:08:02_

----

Apocalypse Nigh is another example where mobs don't superlink


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 11, 2020 at 05:44:36_

----

We used to have all battelfields automatically set superlink on all mobs within them somewhere in the core.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 11, 2020 at 15:18:13_

----

https://discord.com/channels/639659267003252746/639670779386134548/699662862557249566

Superlinking MOBMODs [should still be handled by the BCNM mob loading](https://github.com/project-topaz/topaz/blob/release/src/map/utils/mobutils.cpp#L812-L817)


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Monday Oct 12, 2020 at 03:38:57_

----

I briefly looked into this a while back, but didn't come to a resolution at this time.  But IIRC, the problem has something to do with when the mob is given the SUPERLINK mobmod, versus when it's used to actually create the party of mobs that will link together when one is pulled.

I believe that at the time when the party is created, not all mobs have yet been given the MOBMOD that's used in the party-building code.  So like, the code's there to do everything, but it's not running in the correct order or something.

