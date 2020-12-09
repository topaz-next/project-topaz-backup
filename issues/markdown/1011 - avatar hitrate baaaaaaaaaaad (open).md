**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 27, 2020 at 15:28:26_
_Originally opened as: project-topaz/topaz - Issue 1011_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
https://github.com/project-topaz/topaz/blob/release/scripts/globals/summon.lua#L55

`if math.random() < hitrate then`

that check as is will pretty much always pass because its rolling a floating point form 0 to 1, which is always less than what the hitrate will be.

But if we fix it you go from always hitting to always missing [because](https://github.com/project-topaz/topaz/blob/release/scripts/globals/summon.lua#L24):
`local hitrate = utils.clamp(acc - eva, 20, 95)` is always returning around 20. Avatar acc is garbage while mob eva is not. It would probably help if avatars weren't statted like taru\([\*1](https://github.com/project-topaz/topaz/blob/release/src/map/utils/petutils.cpp#L840)) blm\([\*2](https://github.com/project-topaz/topaz/blob/release/sql/mob_pools.sql#)), a combination not known for its amazing acc stat.



----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Aug 27, 2020 at 16:28:04_

----

adding some more information here
avatar accuracy = (first hit bonus acc if first hit(100) + accuracy from combat skill (A-) + master summoning skill over cap (1:1 mapping skill to acc) + master pet accuracy gear + avatar job acc traits + ((avatar dex *.5 + summoner merits (3 acc per))
avatars get a first hit bonus of 100 acc
so need to factor that in as well

hitrate would be:
75 + (acc-eva)/2
if mob is higher than avatar, then
75 + (acc-eva)/2 - 2*(target level - attacker level)



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 27, 2020 at 18:26:29_

----

so looking over avatar's tp skills scripts and the 2 globals (it goes into the monstertpmoves global as well)..there are multiple other issues to, like hard coded pet ID ranges instead of exposing petType to lua and effectively checking for things like stoneskin twice.

the entire flow(pun not intended) could use an overhaul.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Aug 27, 2020 at 20:47:37_

----

yeah for sure, it is in a bit of a mess. baby steps?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 27, 2020 at 20:53:55_

----

> 
> 
> yeah for sure, it is in a bit of a mess. baby steps?

and lots of them. I have a few minor ones incoming.
