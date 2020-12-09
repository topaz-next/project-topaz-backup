**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Monday Oct 12, 2020 at 03:46:59_
_Originally opened as: project-topaz/topaz - Issue 1336_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Unsure if this was due to the bit stuff move to lua

[11/Oct] [20:41:24][Error] luautils::onTrigger: ./scripts/globals/gobbiemysterybox.lua:113: attempt to call method 'getMaskBit' (a nil value)



----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Oct 12, 2020 at 04:07:26_

----

i didn't test any of the CS that rely on writing and reading bits (like mandragoras) but i will try in a bit (get it lol puns!)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Oct 12, 2020 at 08:20:44_

----

Player mask functions in [mystery box global](https://github.com/project-topaz/topaz/blob/feature/mystery/scripts/globals/gobbiemysterybox.lua#L113-L116) got [updated in release](https://github.com/project-topaz/topaz/pull/1261). `Mystery` branch isn't in release, so the uses in `mystery` are leftover stragglers.

Should be easy fix - just update references to the new functions that Wren added. Maybe check core-side mystery files too.


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Friday Oct 16, 2020 at 12:53:02_

----

This can be closed now.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Oct 16, 2020 at 13:30:55_

----

#1366 
