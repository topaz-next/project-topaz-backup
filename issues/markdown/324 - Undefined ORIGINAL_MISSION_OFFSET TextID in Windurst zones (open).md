**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:48_
_Originally opened as: project-topaz/topaz - Issue 324_

----

<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Saturday Nov 16, 2019 at 22:44 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6288_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** N/A


**_Source Branch_** (master/stable) **:** master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Several NPCs in Windurst zones reference an undefined variable ORIGINAL_MISSION_OFFSET, for example ...
github/DarkstarProject/darkstar/blob/master/scripts/zones/Windurst_Woods/npcs/Rakoh_Buuma.luaDarkstar Issue L25

This is supposed to be ID.text.ORIGINAL_MISSION_OFFSET, a TextID that should be defined in the zone's IDs.lua, but isn't.  You can see similar configuration in Bastok, for example:

(Bastok Markets ID.text.ORIGINAL_MISSION_OFFSET defined)
github/DarkstarProject/darkstar/blob/master/scripts/zones/Bastok_Markets/IDs.luaDarkstar Issue L23

(and used)
github/DarkstarProject/darkstar/blob/master/scripts/zones/Bastok_Markets/npcs/Cleades.luaDarkstar Issue L43

However, I don't know what message the NPC is supposed to say, so I can't infill the missing TextID.

*note: I checked out old version of the code, before we tabled all the text IDs, and all the Windy zones were missing ORIGINAL_MISSION_OFFSET in the old TextIDs.lua too, so that didn't help.*

