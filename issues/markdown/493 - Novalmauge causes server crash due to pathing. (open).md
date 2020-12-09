**Labels:**

bug



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Monday Apr 13, 2020 at 22:19:40_
_Originally opened as: project-topaz/topaz - Issue 493_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Novalmauge has crashed our server 3-4 times before I finally caught him doing it with VS's debugger.  It has to do with his pathfinding, when I disabled that, he no longer causes crashes.  Unfortunately the callstack that told me the specifics is long lost.  The crashes occurred when players would stop him to turn in his various quests.

I believe this issue is related to #319 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Apr 13, 2020 at 22:59:00_

----

npc pathin is just broken :cry:  if it ever gets fixed it would be awesome. Also there are some npc pathing that currently work but that they are all hacky as they have a series of coordinates to make them seem retail accurate so they don't slide.

would be awesome if they npc pathing gets fixed.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Apr 13, 2020 at 23:57:29_

----

`wait()` can trigger crashes, so its any roaming NPC that uses that command to stop moving when a  player clicks on it.

copy pasta from previous discussions:

```cpp
/************************************************************************
*  Function: wait()
*  Purpose : Makes a non-PC inactive for a set amount of time
*  Example : npc:wait(10000) -- wait 10 seconds
*  Notes   : Default is 4 seconds unless specified in ms
************************************************************************/

inline int32 CLuaBaseEntity::wait(lua_State* L)
{
    DSP_DEBUG_BREAK_IF(m_PBaseEntity->objtype == TYPE_PC);

    CBattleEntity* PBattle = (CBattleEntity*)m_PBaseEntity;

    int32 waitTime = 4000;

    if (lua_isnumber(L, 1))
    {
        waitTime = (int32)lua_tonumber(L, 1);
    }
    PBattle->PAI->Inactive(std::chrono::milliseconds(waitTime), true);

    return 0;
}
```
This is the version of wait NPC's use. The mob AI controller has a diff version that involves the server tick. I do not think we should be expecting this to work with `wait(0)` nor expecting a behavior of "keep waiting until event ends" which is how it was being used. 

I think we need to do something different at the core to genuinely do "wait till my event ends".


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Friday May 01, 2020 at 10:07:05_

----

Hello! Seems to be related to this old one too: https://github.com/project-topaz/topaz/issues/186.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday May 01, 2020 at 11:46:36_

----

Note of clarification since #186 deals with 2 issues: #186 mistakenly thought the navmesh errors were related to the crash. wait() caused the crash, and navmesh error spam was due to an entity not finding its next path node. Comment replies on #186 mainly address the navmesh errors. I think there are a few more related issues to both wait and navmesh as well if all the old dsp issues were migrated.
