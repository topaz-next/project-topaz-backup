**Labels:**

bug



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Apr 09, 2020 at 05:30:28_
_Originally opened as: project-topaz/topaz - Issue 480_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Two weird things are happening with the bridges:
* the highest bridge (the one right next to the fountain), dissapears entirely if you walk away from it by at least 50 meters.
* they raise a bit too much when night time on a full moon. Unsure if its retail accurate or if pos needs to decrease a bit.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 09, 2020 at 20:18:02_

----

> the highest bridge (the one right next to the fountain), dissapears entirely if you walk away from it by at least 50 meters.

Entity packets not currently sent when farther than that. For most objects that should be retail accurate but then when you come in range they should "repop" on your screen. may need a way to make exceptions to that. Not sure what retail does in this case for these specific objects.

> hey raise a bit too much when night time on a full moon. Unsure if its retail accurate or if pos needs to decrease a bit.

Are you able to step onto them?


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Apr 09, 2020 at 20:35:32_

----

@TeoTwawki 
yeah once u get back to it the whole bridge is gone lol. it only reappears once the moon gate doors close

Yes you are able to step on them but it's raise too high it makes the taru feet dissapear lol


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Apr 10, 2020 at 01:38:36_

----

Its eating taru feet? clearly a secret mimic, and a racial hate crime.  We can't let that stand. To war! [We'll show those packets!](https://github.com/project-topaz/topaz/blob/4d09173b57dd5867dd3997436fa3ee66eeea0fbb/src/map/zone_entities.cpp#L787)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Apr 10, 2020 at 19:09:26_

----

@TeoTwawki  hopefully someone takes a look at this =) funny thing is that it only happens to the top bridge but not the bottom.

This should help also with the gates in the desert (those high towers) for opening that door that u need to hit on 4 switches in the map. cause if u are far away the look as if they are off, but if u get close they look as if the switch is on
