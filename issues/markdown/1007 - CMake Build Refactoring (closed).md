**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Wednesday Aug 26, 2020 at 14:13:11_
_Originally opened as: project-topaz/topaz - Issue 1007_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

**TODO**
**Work**
- ~~**Get it working.**~~
- Linux builds
  - ~~Commandline 32/64~~
- Windows builds
  - ~~Commandline (CMake) 32/64~~
  -  ~~VS 2017 32/64 (Generated SLN and CMake)~~
  -  ~~VS 2019 32/64 (Generated SLN, CMake, File > Open > Cmake)~~
  - ~~VS Code (It is expected that users write their own tasks.json)~~
  - ~~CLion~~
- ~~IDE-friendly folder structures generated from CMakeLists.txt~~
- ~~Only valid targets generated from CMakeLists.txt~~
- ~~Audit flags on Windows & Linux~~
- ~~Break out dependencies into _proper_ FindModule.cmake types/files~~
- ~~Port over defines etc. from old `cmake/compiler.cmake`~~
- Update CI
- ~~Resources & Icons~~
- ~~Ensure builds are multi-threaded by default~~
- Compare before/after build and link times
- Compare before/after binary sizes
- If debug, force save debug logs


**Documentation**
- User instructions (VS Contains CMake already - what to click on, auto-generate SLN script, instructions for Linux + OSX, Adding files)
- Support (and instructions) for CMake-Gui

**TODO After**
- Remove all the other random stuff lurking around in the repo
- Remove global link/include statements - refine down to target level
- Investigate why the mishmash of static/object type libraries works and find out the best practice way to lay it out
- Retool search server to use the main() defined in common/kernel.cpp
- Create issues for removing all of the TODO options in CompilerWarnings.cmake (Tag with "Good First Issue")
- Create issues for fixing all of the include paths, they won't need to be relative anymore

**Out of Scope/Not needed**
- LuaJIT fallback to using Lua51 - log messages to see what you're using



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 26, 2020 at 05:53:01_

----

No progress on this. HOWEVER. I think I should reign back the scope of this to _just_ be a transition to CMake and instructions for how to generate a SLN file. 

Updating all the dependencies etc can come afterwards. It's a big piece of work and doesn't need to be made _bigger_


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Sep 26, 2020 at 17:33:07_

----

> **and instructions for how to generate a SLN file.**

Right into the readme we see landing at the projects github page, please. Coz we're gonna get a lot of "how do I do this?" after the change.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 30, 2020 at 05:08:41_

----

> Right into the readme we see landing at the projects github page, please. Coz we're gonna get a lot of "how do I do this?" after the change.

I'm feeling a `BUILD_INSTRUCTIONS` file. People will skip over the docs 100%, if there's a file we can list and then point them at when they come asking questions thats a good thing.

The best thing is that anyone who was building the project before with VS2017 or VS2019 already has the CMake that comes with Visual Studio, so the build is guaranteed to work. People on other platforms will just have to use an updated one-liner (but likely won't need to).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 01, 2020 at 20:18:05_

----

> I'm feeling a BUILD_INSTRUCTIONS file. People will skip over the docs 100%, if there's a file we can list and then point them at when they come asking questions thats a good thing.

If you link your file in the readme near the top of it somewhere in 

<h2>

```diff
- BIG! Highlighted! Print! -
```

</h2>
I can feel that too. Coz new file ppl gonna miss otherwise. But at the point of doing it elsewhere you may as well have put build instructions in the wiki and have it linked in readme, which is what most projects do (although our docs folder still has a special place in my old man heart). 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 23, 2020 at 16:42:47_

----

**YEET**
