**Labels:**

merge ready



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 03, 2020 at 08:11:01_
_Originally opened as: project-topaz/topaz - Issue 464_

----

A few things are still needed:

1. Add enmity when cast.
2. Update the status_effect to also protect against status effect
spells that cause debuffs.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Apr 03, 2020 at 11:42:45_

----

>spell castable

*ability usable

:)


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Apr 09, 2020 at 20:37:26_

----

Whoops. Force of habit. Will update the spacing.

Is it sufficient to just add the CE/VE to the sql file? Or do I need to apply those enmity values somewhere in code?

It seems like they will get picked up in the core and added to the `spell`. But I couldn't seem to find where it's applied to the player (if that's done automatically).

Any pointers would be helpful :) thanks!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Apr 10, 2020 at 01:34:10_

----

> Is it sufficient to just add the CE/VE to the sql file? Or do I need to apply those enmity values somewhere in code?

Yep just plug into the table, core does the rest on [ability ](https://github.com/project-topaz/topaz/blob/8985d2af68876367592222836db1f8e5b15c8175/src/map/ai/states/ability_state.cpp#L76)use.




----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Friday Apr 10, 2020 at 06:02:01_

----

Updated indentation and added the CE/VE values.

Thanks for the code pointers.
