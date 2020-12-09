**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday Oct 25, 2020 at 11:17:19_
_Originally opened as: project-topaz/topaz - Issue 1432_

----

This is the power of CMake!

Build with `TRACY_ENABLE` to turn on the profiling, otherwise, everything will get stripped away and has no effect on the build.

This PR adds support for the Tracy client in topaz_game. Once the game is built and running, you can connect the server to it to see the beautiful stats in realtime:

![image](https://user-images.githubusercontent.com/1389729/97106613-832f0100-16cb-11eb-8452-267e406bceb9.png)

We are hardcoded to v0.7.3, different versions of client and server are not compatible!

https://github.com/wolfpld/tracy/releases/tag/v0.7.3

**GUIDE**

https://github.com/project-topaz/topaz/wiki/Performance-Profiling-with-Tracy

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Oct 27, 2020 at 14:38:41_

----

Note to self:
```
To report data, use the TracyPlot(name, value) macro.
To configure how plot values are presented by the profiler, you may use the TracyPlotConfig(name,
format) macro, where format is one of the following options:
• tracy::PlotFormatType::Number – values will be displayed as plain numbers.
• tracy::PlotFormatType::Memory – treats the values as memory sizes. Will display kilobytes,
megabytes, etc
```

```cpp
//what:
//LUA_GCCOUNT: returns the current amount of memory (in Kbytes) in use by Lua.
//LUA_GCCOUNTB: returns the remainder of dividing the current amount of bytes of memory in use by Lua by 1024.
//LUA_API int (lua_gc) (lua_State *L, int what, int data);

#ifdef TRACY_ENABLE
TracyPlotConfig("Lua Memory Usage", tracy::PlotFormatType::Memory);
TracyPlot("Lua Memory Usage", lua_gc(L, LUA_GCCOUNT, 0) / 1024); // from kb to b
#endif
```
