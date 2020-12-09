**Labels:**

bug



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Apr 08, 2020 at 06:29:57_
_Originally opened as: project-topaz/topaz - Issue 476_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- []x checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Romaeve will have the mob bellow always showing navmesh errors on topaz_game:
[07/Apr] [02:36:55][Navmesh Error] CPathFind::FindPath Entity (17276998) could not find path



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 08, 2020 at 11:42:20_

----

mob: _"I stubbed my toe on this bump in the floor of this navmesh! Gonna fill your log with useless messages now. kthx bai"_


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 12:31:02_

----

Did the poor mob get locked inside one of the moongate chambers?


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Apr 08, 2020 at 15:37:17_

----

@TeoTwawki  @ibm2431  lol u guys are funny.
It's an Apocalypse Weapon that gets stuck to a wall (i can see its little hand going beyond the wall when using !wallhack).

It's the only mob in the entire zone that does this, and it's pretty consistent with every time i reboot the server.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Apr 08, 2020 at 15:38:53_

----

If i get emmity from it, it will set itself free and go for me, and then once i lose it out of sight, it will go back to its area, then eventually getting stuck again lol


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 08, 2020 at 15:45:34_

----

sounds like his intial pos has him stuck in the wall or too close to it to navigate, and when you aggro it (correctly) wallhacks itself to reach you. then goes home and again can't roam again.

RE: stubbed toe joke
quite often navigation does get tripped up by the smallest of bumps that the player can go right through by the navmesh presents as a pillar of iron to the mobs pathing. Their vertical axis doesn't handle well. its funny.

These errors will also spam the log even while mobs appear to be moving just fine, so I keep them just filtered out as they are 90% useless garbage in my log.
