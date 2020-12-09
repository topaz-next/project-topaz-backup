**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:46:00_
_Originally opened as: project-topaz/topaz - Issue 191_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Wiggo32](https://github.com/Wiggo32)**
_Tuesday Oct 10, 2017 at 16:49 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4124_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30170905_5


**_Server Version_** (type `!revision` in game) **:** unknown


**_Source Branch_** (master/stable) **:** master


**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
When values collected from mob_family_system.sql start moving away from 1 in either direction it causes the associated elemental enspell damage to move toward 0. 

Resistance modifier is calculated with the values from the mob_family_system here:
github/DarkstarProject/darkstar/blob/96180dac297db2ec17b1f3f03ebdbecd4a56bd5f/src/map/utils/zoneutils.cppDarkstar Issue L480

And the result from that is pulled to:
github/DarkstarProject/darkstar/blob/96180dac297db2ec17b1f3f03ebdbecd4a56bd5f/src/map/utils/battleutils.cppDarkstar Issue L593

Which is then put through a mess of a formula that deals with negative numbers in a undesireable way. pow(half, 2) / pow(half, 3) --> A negative number in both of those will produce a positive number AND a negative number respectively.

My band aid fix was to get rid of the random (dsprand) as well as the exponent calcs (pow) and just tailor the resistance to be directly reflective of the value calculated from the mob_family_system.sql database info.


