**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Jul 18, 2020 at 18:01:39_
_Originally opened as: project-topaz/topaz - Issue 866_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

bastok has the region but banner is showing on same spot as I.M.

![bastok has power](https://user-images.githubusercontent.com/26943220/87858875-e1d32a80-c8e5-11ea-91cb-f537b178317b.png)

![takemoto](https://user-images.githubusercontent.com/26943220/87858893-029b8000-c8e6-11ea-9656-0f83727da90f.png)




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 18, 2020 at 19:36:03_

----

usually caused by client and server having different versions of the npc list - one is newer than the other

the other possibility is an id is wrong so the wrong one gets activated/spawned.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Jul 18, 2020 at 19:40:31_

----

i updated the server on Wednesday, and my client on that same day, this is odd indeed.

Just checked !ver: 30200702_2
Server Version: C202007-02


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 18, 2020 at 19:43:45_

----

we can compare the id against polutils on the latest client to see if/how far off it is


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Jul 18, 2020 at 19:45:24_

----

we? not it :cat: 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 18, 2020 at 20:16:38_

----

its a royal we "anyone contributing to the project" = we

I have not updated for July yet, so can't help you yet.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Jul 23, 2020 at 23:31:15_

----

Can verify that npc_list.sql in current release branch matches current POL extract for these NPCs, and also that OVERSEER_BASE in Jugner Forests's IDs.lua is correctly set.  So are the offsets from this base, for the Norvallen region, that are defined in scripts/globals/conquest.lua.  So issue is not desync of IDs between retail and Topaz.

~~@kaincenteno can you verify that in your DB, npc_list, npcid 17203848 is Chaplion_RK?  Let's make absolutely sure it's not a sync issue before digging deeper.~~ never mind, I'm able to replicate the issue.  Will get to bottom of it.  We may have incorrect models on the banners.

edit: all fixed


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 24, 2020 at 00:11:02_

----

Thanks for the checkup Wren


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 24, 2020 at 00:12:36_

----

next guess: maybe the beastman banner npc has wrong status somehow, it is supposed to be there but hidden/unpopped till beastman gain control after tally
