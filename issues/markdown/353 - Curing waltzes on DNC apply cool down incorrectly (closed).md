**Labels:**

bug

good first issue



<a href="https://github.com/SirGouki"><img src="https://avatars3.githubusercontent.com/u/11664236?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [SirGouki](https://github.com/SirGouki)**
_Wednesday Feb 19, 2020 at 03:03:21_
_Originally opened as: project-topaz/topaz - Issue 353_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

server branch: master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Steps:  Be DNC or /DNC
use any tier Curing Waltz other than the first one.  The cool down will apply to Curing Waltz instead of the correct ability.  The cool down applied appears to be correct, however.  This is exploitable in that it would allow a DNC to spam higher level Curing Waltzes as long as the have the TP.

Expected Behavior:  The cooldown should be applied to the skill used in this case.  For example, If I use Curing Waltz III, that should go on CD, not Curing Waltz.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Feb 19, 2020 at 12:44:55_

----

This may have happened because they used to be in a shared timer and SE changed them (I think I remember reading update notes about it), or possibly whoever added the tier 3 one typo'd or copy pasted the recast id not realizing the result.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 19, 2020 at 12:45:01_

----

It appears that all the waltzes are using the same recast ID of 217 in `abilities.sql`

It did use to be the case that waltzes were supposed to be linked, but SE delinked their recast timers in the [January 2019 version update](http://forum.square-enix.com/ffxi/threads/54901-January.-10-2019-%28JST%29-Version-Update).

I want to say the fix should be as simple as updating the recastIDs to use the [new, separated ones](https://github.com/Windower/Resources/blob/master/resources_data/ability_recasts.lua).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Feb 19, 2020 at 12:46:58_

----

oh hey look at that, I did remember right


----
<a href="https://github.com/SirGouki"><img src="https://avatars3.githubusercontent.com/u/11664236?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [SirGouki](https://github.com/SirGouki)**
_Wednesday Feb 19, 2020 at 16:43:48_

----

It happens with all tiers not just III.  (just to clarify)


----
<a href="https://github.com/SirGouki"><img src="https://avatars3.githubusercontent.com/u/11664236?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [SirGouki](https://github.com/SirGouki)**
_Wednesday Feb 19, 2020 at 18:27:34_

----

https://github.com/project-topaz/topaz/pull/356
