**Labels:**

bug

focus



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 03:55:13_
_Originally opened as: project-topaz/topaz - Issue 377_

----

There's an `ATTACK_BREATH` enum value (and similar one in Lua). But it's not used anywhere.

It's possible this may not be needed, since most breath spells are listed as "magical" by most FFXI websites. e.g. "heat breath" is labeled as "fire" + "magical". (https://ffxiclopedia.fandom.com/wiki/Heat_Breath)

Although if it was intended to be used for something, it's not.

https://github.com/DarkstarProject/darkstar/blob/master/src/map/entities/battleentity.h#L244

https://github.com/DarkstarProject/darkstar/blob/master/scripts/globals/status.lua#L2123


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 03:57:01_

----

I'm in the process of updating the `attackType` for all blu spells. I'm going to follow the convention of labeling them as MAGICAL for now.

If we decide this is something we want used, I can go through and change the breath spells to BREATH.

(For context: https://github.com/project-topaz/topaz/issues/314)


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 19:18:29_

----

Per discussion with the appropriate stakeholders, Breath spells will be fixed in the future to have proper damage calculations. I'll update my outstanding PR to label the breath spells as such in preparation for that.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 19:29:45_

----

Issue to fix breath damage calculation appears to be here: https://github.com/project-topaz/topaz/issues/239
