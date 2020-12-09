**Labels:**



<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [KnowOne134](https://github.com/KnowOne134)**
_Friday Feb 14, 2020 at 01:46:09_
_Originally opened as: project-topaz/topaz - Issue 339_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

mobs should pop unclaimed, A bst can charm the 2 other mobs and use them in aid of fight, should despawn after some time if you cant beat the fight


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Friday Feb 14, 2020 at 02:24:50_

----

unfortunately looks like mobMod CHARMABLE isnt working


----
<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Friday Feb 14, 2020 at 02:39:01_

----

```lua
UPDATE `mob_pools` SET `mobType`='16' WHERE `poolid`='3834';  -- Taifun
UPDATE `mob_pools` SET `mobType`='16' WHERE `poolid`='4038';  -- Trombe
```
This worked for me... see if it helps


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Friday Feb 14, 2020 at 11:57:52_

----

The reason that works is it removes its NM tag where the mob mod should make it so a mob is charmable when it's set to not be in database


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 14, 2020 at 13:15:07_

----

It's hitting the `MOBTYPE_NOTORIOUS` check for bind and returning before doing anything else.

https://github.com/project-topaz/topaz/blob/master/src/map/utils/battleutils.cpp#L3855-L3860

Might need to rework it to be an `AND NOT` `mobmod_charmable`.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 15, 2020 at 02:18:24_

----

charm and gauge now work on NMs that have the lua mobmod.CHARMABLE set
