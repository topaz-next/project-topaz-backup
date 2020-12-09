**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Oct 08, 2020 at 18:14:07_
_Originally opened as: project-topaz/topaz - Issue 1287_

----

onZoneIn passing params is not implemented, so I commented it out

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Oct 08, 2020 at 18:25:21_

----

These params aren't passed as part of the cs start.
They're passed as a response to an EventUpdate the client sends with option 1. That response and option needs to be coded in onEventUpdate below.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Oct 08, 2020 at 19:31:51_

----

:penguin:  ty


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 08, 2020 at 23:36:29_

----

we actually didn't exceed the width there, it was ok.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 08, 2020 at 23:37:02_

----

short enough to be one line here


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 08, 2020 at 23:39:29_

----

so uh... I guess ya just did that to all the if/thens? [we normally only break the wide ones](https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md#general-code-guidlines-all-languages)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Oct 08, 2020 at 18:25:21_

----

These params aren't passed as part of the cs start.
They're passed as a response to an EventUpdate the client sends with option 1. That response and option needs to be coded in onEventUpdate below.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Oct 08, 2020 at 19:31:51_

----

:penguin:  ty


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 08, 2020 at 23:36:29_

----

we actually didn't exceed the width there, it was ok.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 08, 2020 at 23:37:02_

----

short enough to be one line here


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 08, 2020 at 23:39:29_

----

so uh... I guess ya just did that to all the if/thens? [we normally only break the wide ones](https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md#general-code-guidlines-all-languages)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Oct 09, 2020 at 01:00:59_

----

@TeoTwawki  dunno if im doing something wrong but after the styleguide talk on discord i understood that if there's several and or then it can be done one per line. Under "Lua"

@staff would love some clarification :bow: i would hate to be doing something wrong


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Oct 09, 2020 at 05:48:41_

----

Closing as it needs more research for retail accuracy, but it should help with CSID and some of the params that are being passed.
