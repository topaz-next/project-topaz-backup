**Labels:**

bug

focus



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:16_
_Originally opened as: project-topaz/topaz - Issue 314_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Sunday Sep 22, 2019 at 21:34 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6225_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** n/a


**_Source Branch_** (master/stable) **:** master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Before I forget to publicly note this (again): Damage-dealing Blue Magic that goes through `BlueFinalAdjustments` is always treated as `attackType.PHYSICAL`, even if the damage type should be Magical.

Some examples of Blue Spells that should be treated as Magical - but aren't due to `BlueFinalAdjustments` - are:

Death Ray
> github/DarkstarProject/darkstar/blob/master/scripts/globals/spells/bluemagic/death_ray.luaDarkstar Issue L42

Ice Break
> github/DarkstarProject/darkstar/blob/master/scripts/globals/spells/bluemagic/ice_break.luaDarkstar Issue L50

Mind Blast
> github/DarkstarProject/darkstar/blob/master/scripts/globals/spells/bluemagic/mind_blast.luaDarkstar Issue L44

When they get into `BlueFinalAdjustments`, after calculating reductions due to Phalanx and Stoneskin, `takeDamage` is always called with `attackType.PHYSICAL`:

> github/DarkstarProject/darkstar/blob/master/scripts/globals/bluemagic.luaDarkstar Issue L232-L247



----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 16:03:42_

----

This mirrors https://github.com/DarkstarProject/darkstar/issues/6225
I already have some work on this locally, so I can apply the same changeset to Topaz.
