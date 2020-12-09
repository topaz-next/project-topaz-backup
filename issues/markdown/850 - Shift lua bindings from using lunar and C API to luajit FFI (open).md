**Labels:**



<a href="https://github.com/bluekirby0"><img src="https://avatars3.githubusercontent.com/u/1157452?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [bluekirby0](https://github.com/bluekirby0)**
_Wednesday Jul 15, 2020 at 03:24:13_
_Originally opened as: project-topaz/topaz - Issue 850_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

I want to discuss the possibility of moving all of the lua bindings away from lunar and the C API for several reasons, and I propose luajit's FFI implementation as an alternative.

Motivating factors:
#296 would be fixed by this in a way that will improve rather than degrade performance, which would add proper support to arm64 (aarch64) platforms without requiring 32-bit builds.
Bindings would be simple, lightly decorated exported C functions that just take normal arguments and return normal types, and have full access to the core C++ structures inside. This makes the code easier to read, follow, and understand since we aren't manually manipulating the lua stack from the bindings.
Luajit is capable of caching calls to FFI functions far more effectively than it can for C API functions, which lunar uses as its backend. As it stands, common subroutines dealing with bindings can be cached, but little else, providing only a slight performance improvement for using luajit over the standard lua distribution with regards to interaction between core and scripting.
It would be far less scary to add new bindings in general, and might facilitate moving more code to scripts where appropriate.


Pseudo-code example of what FFI bindings would look like from the lua side (which is where the binding code will actually live with FFI):
```
local ffi = require("ffi")
ffi.cdef[[
int blah(const char* name, int value);
]]
blah = ffi.C.blah
blah("someguy",4)
```
Its mostly just copying header code into a string with all of the relevant ##typedef and such so that luajit can understand the underlying C types. This gets easier the more bindings we add since most of the definitions will already be included from existing bindings, usually just allowing a new binding to be copied straight from a header file.


Motivating example of what a current binding would look like when modified for FFI:
```
#ifdef WIN32
  #define FFI_BINDING __declspec(dllexport) __cdecl
#else
  #define FFI_BINDING __cdecl
#endif

    FFI_BINDING CBaseEntity* GetNPCByID(uint32 npcid, CInstance* PInstance)
    {
        CBaseEntity* PNpc = nullptr;

        if (PInstance)
        {
            PNpc = PInstance->GetEntity(npcid & 0xFFF, TYPE_NPC);
        }
        else
        {
            PNpc = zoneutils::GetEntity(npcid, TYPE_NPC);
        }

        return PNpc;
    }
```

as opposed to [the original function](https://github.com/project-topaz/topaz/blob/08fcc59f5fc1a5a929037ca24b13ce9cec8f287f/src/map/lua/luautils.cpp#L335)

Initial implementation can be done by putting all bindings in a single lua file and then requiring it from common.lua with aliases defining all the original function names from the old bindings as FFI calls to the new bindings. That should allow all existing scripts to continue working as they have been, though I do believe there might be unforseen issues arising from any change this massive and sweeping.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Jul 23, 2020 at 01:38:57_

----

This kind of idea will be good for maybe being brought in Staff discussion. Could @bluekirby0  be brought in to the staff meeting next week as a special guest? :cat: 
