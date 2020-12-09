**Labels:**

bug

research needed



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Wednesday May 06, 2020 at 11:30:12_
_Originally opened as: project-topaz/topaz - Issue 588_

----

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Different tiers of elemental threnody are supposed to have caps to the amount of elemental resistance they'll reduce. For example, [tier I caps at 50](https://www.bg-wiki.com/bg/Wind_Threnody), while [tier II caps at 160](https://www.bg-wiki.com/bg/Wind_Threnody_II) (prior to any special cap-breaking gear effects).

Currently, when a [threnody spell is cast, it passes what _should_ be a cap (50) into handleThrenody](https://github.com/project-topaz/topaz/blob/release/scripts/globals/spells/wind_threnody.lua#L13). Unfortunately, the [handleThrenody function erroneously believes this a _base power_](https://github.com/project-topaz/topaz/blob/release/scripts/globals/magic.lua#L1235), and [applies multiplying gear/SP ability mods directly to this "base" before adding an elemental down status of the final value](https://github.com/project-topaz/topaz/blob/release/scripts/globals/magic.lua#L1259-L1273). No checks against player skill are done for the potency effect - only when seeing if the threnody lands. So long as the spell lands (which can happen with sufficient Magic Accuracy), all BRDs will have threnodies of the same potency.

**_I have:_**
- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated






----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 16, 2020 at 03:05:17_

----

Believe it or not, this is retail behavior. A level 30 BRD with just Singing (ie: "half power") reduces elemental resistance by the same amount as a level 99 BRD. After free period I'll upload Ballista captures demonstrating this.
