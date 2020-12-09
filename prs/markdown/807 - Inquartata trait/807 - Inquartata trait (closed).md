**Labels:**

merge ready



<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Apocarypse](https://github.com/Apocarypse)**
_Saturday Jul 04, 2020 at 19:55:45_
_Originally opened as: project-topaz/topaz - Issue 807_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Added mod enum for Inquartata in modifier.h
Added entries for Inquartata in traits.sql
Applied Inquartata bonus logic to GetParryRate()


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jul 06, 2020 at 00:16:43_

----

Sverdheid and Zurko-Bazurko are RUN mobs that players need to fight.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Jul 06, 2020 at 18:30:33_

----

I think based on what was said on the discord, that ibm's idea was that if you aren't needing the trait check, then there's no need to cast to CCharEntity*. You can just use PDefender directly as CBattleEntity has the getMod method. :)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jul 06, 2020 at 00:16:43_

----

Sverdheid and Zurko-Bazurko are RUN mobs that players need to fight.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Jul 06, 2020 at 18:30:33_

----

I think based on what was said on the discord, that ibm's idea was that if you aren't needing the trait check, then there's no need to cast to CCharEntity*. You can just use PDefender directly as CBattleEntity has the getMod method. :)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 23, 2020 at 22:40:59_

----

@Apocarypse @cocosolos @ibm2431 modifiers in modifier.h and statsu.lua should mirror each other until such time as lua can automagically use the core enums, even if the mod is never used in script so that future editor don't mistakenly use the same ID - this has happened multiple times in the older project history until I became its watchdog in dsp.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 24, 2020 at 00:50:29_

----

_sees this merged PR in notifications_
_sees Teo as a participant_

"I _did_ miss one, didn't I?"

_clicks_

"Yeeeep. Whoops."
