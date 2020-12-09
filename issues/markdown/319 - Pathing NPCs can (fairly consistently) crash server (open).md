**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:26_
_Originally opened as: project-topaz/topaz - Issue 319_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Saturday Oct 19, 2019 at 21:39 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6250_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 301907xx_x


**_Source Branch_** (master/stable) **:** master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Was working on some addons, and figured I would use [Red Ghost](github/DarkstarProject/darkstar/blob/master/scripts/zones/Port_Jeuno/npcs/Red_Ghost.lua) in Port Jeuno to test. Problem is he somewhat consistently crashes the server if he's spoken to a couple times after the first (after which his pathing breaks and he stops walking).

I suspect all NPCs set to path could cause this same crashing behavior.

I do use Enternity, so that may (or may not) be involved.

**Debugger Output:**

DEBUG_BREAK_IF thrown in [CAIContainer, Line 160](github/DarkstarProject/darkstar/blob/master/src/map/ai/ai_container.hDarkstar Issue L160)

**Call Stack:**
- DSGame-server.exe!CAIContainer::ForceChangeState<CInactiveState,CBaseEntity * &,std::chrono::duration<__int64,std::ratio<1,10000000>> &,bool &>(CBaseEntity * & <args_0>, std::chrono::duration<__int64,std::ratio<1,10000000>> & <args_1>, bool & <args_2>) Line 160
- DSGame-server.exe!CAIContainer::Inactive(std::chrono::duration<__int64,std::ratio<1,10000000>> _duration, bool canChangeState) Line 165
- DSGame-server.exe!CLuaBaseEntity::wait(lua_State * L) Line 1945
- DSGame-server.exe!Lunar<CLuaBaseEntity>::thunk(lua_State * L) Line 173
- [External Code]	
- lua51.dll![Frames below may be incorrect and/or missing, no symbols loaded for lua51.dll]
- DSGame-server.exe!parse(char * buff, unsigned int * buffsize, sockaddr_in * from, map_session_data_t * map_session_data) Line 596
- DSGame-server.exe!do_sockets(fd_set * rfd, std::chrono::duration<__int64,std::ratio<1,10000000>> next) Line 376
- DSGame-server.exe!main(int argc, char * * argv) Line 270
- [External Code]	

**Autos:**
- 1
    - m_stateStack 
    - { size=11 }
    - std::stack<std::unique_ptr<CState,std::default_delete<CState>> ,std::deque<std::unique_ptr<CState,std::default_delete<CState>>,std::allocator<std::unique_ptr<CState,std::default_delete<CState>>>>>
- 2 
  - this
  - 0x190955d0 {EventHandler={eventListeners={ size=0 } } TargetFind=empty PathFind=unique_ptr {m_PTarget=0x18c475c8 {m_flags=27 name_prefix=32 ' ' widescan=1 '\x1' } m_points={ size=0 } m_turnPoints=...} ...}
  - CAIContainer *




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:27_

----

<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Oct 19, 2019 at 21:43 GMT_

----

That and pathing NPC (patrol) after reaching last co-ordinator stop moving. 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:28_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 19, 2019 at 21:53 GMT_

----

It is all npc’s I remember demo changing some scripts to avoid it but it was never proper fixed. They need to “pause” when an event is triggered and then resume their event is done (messageSpecial should be able to just go without stopping them I think.. but I think neither of these behaviors happens now)

As for paths stopping - there is supposed to be a script command to check for end of path and another to restart it. This implies their full set of coordinates already takes them back to where they started or else they teleport. I don’t know of one or both of these are broken or just missing.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:29_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Oct 19, 2019 at 22:04 GMT_

----

Judging by the call stack, I think this case might just be NPCs [that call `wait()`](github/DarkstarProject/darkstar/blob/master/scripts/zones/Port_Jeuno/npcs/Red_Ghost.luaDarkstar Issue L48-L59).

I can harass [Jorin](github/DarkstarProject/darkstar/blob/master/scripts/zones/Western_Adoulin/npcs/Jorin.lua) all I want without him throwing the server in the garbage bin...!

edit: Unless you meant it is all pathing npcs. In which case, nevermind me...!



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:30_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Oct 19, 2019 at 23:07 GMT_

----

yes, I did mean that. All npc's that get interrupted when pathing. (which we used `wait(somenumber)` to do)



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:32_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Sunday Oct 20, 2019 at 19:33 GMT_

----

I brought this up a very long time ago. The solution I was given was "Don't click on the NPC that many times so fast" I fixed this by removing all "wait" commands from NPC scripting. Pathfind is borked and needs reworked.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:33_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Oct 21, 2019 at 01:20 GMT_

----

Could we potentially use `npc:speed(0)` to replace wait?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:34_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 21, 2019 at 01:29 GMT_

----

If it even worked it’d be a non optimal pita - you’d need to store the original speed and set it back after. 

Might not even really work though. I wonder if it just set move speed and the pathing engine would keep moving the object to the next pos anyway while they appeared to just slide instead of walk.





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:35_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 21, 2019 at 16:25 GMT_

----

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
This is the version of wait NPC's use. The mob AI controller has a diff version that involves the server tick. I do not think we should be expecting this to work with `wait(0)` nor expecting a behavior of "keep waiting until event ends" which is how it was being used. TL;DR dsp derps again!

I think we need to do something different at the core to genuinely do "wait till my event ends".



----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Mar 25, 2020 at 04:08:35_

----

could this be related to the decimal point issue discussed in discord re: mob pathing?


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Mar 25, 2020 at 04:12:22_

----

related to issue #292 
