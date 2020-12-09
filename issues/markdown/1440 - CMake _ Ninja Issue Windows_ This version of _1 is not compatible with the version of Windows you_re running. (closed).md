**Labels:**



<a href="https://github.com/Tom-Neverwinter"><img src="https://avatars3.githubusercontent.com/u/3943634?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Tom-Neverwinter](https://github.com/Tom-Neverwinter)**
_Tuesday Oct 27, 2020 at 17:37:25_
_Originally opened as: project-topaz/topaz - Issue 1440_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

install directory: C:/topaz so its not the spaces issue of the other issue

open the CMakeLists.txt in visual studio 16.7.7 [worked for 16.4.5ish]

select x86 release/ x86 debug 

same issue


"This version of %1 is not compatible with the version of Windows you're running. Check your computer's system information and then contact the software publisher"

Perform complete reinstall of visual studio community, just in case. [does not revert Visual Studio version]

This vm is x86 32bit not 64bit



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Oct 27, 2020 at 17:53:52_

----

I was using 16.7.6, and I've just updated to 16.7.7 - all targets work as expected.
If your VM doesn't work as expected, you can try and build with cmd:

https://github.com/project-topaz/topaz/wiki/CMake-Build-Guide#windows-commandline


----
<a href="https://github.com/Tom-Neverwinter"><img src="https://avatars3.githubusercontent.com/u/3943634?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Tom-Neverwinter](https://github.com/Tom-Neverwinter)**
_Thursday Oct 29, 2020 at 16:07:06_

----

Reverted to June of this year. updated git repo, and tortise. everything else is the same and it will not build the current branch. same issue.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 29, 2020 at 18:02:13_

----

If June won't build, there's a problem with your VM for sure 💀 


----
<a href="https://github.com/Tom-Neverwinter"><img src="https://avatars3.githubusercontent.com/u/3943634?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Tom-Neverwinter](https://github.com/Tom-Neverwinter)**
_Friday Oct 30, 2020 at 05:49:19_

----

June has built fine. it built fine up until this month. 

I literally was playing the build for the beginning of the month without issue.
when I am off work I will try and hunt down the commit.


----
<a href="https://github.com/Tom-Neverwinter"><img src="https://avatars3.githubusercontent.com/u/3943634?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Tom-Neverwinter](https://github.com/Tom-Neverwinter)**
_Monday Nov 02, 2020 at 07:44:23_

----

Installed cmake.

disable warnings as errors. generate

compile in visual studio.

resolves issue. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Nov 02, 2020 at 08:08:00_

----

What are the warnings that are tripping up your build? We won't be turning off warning-as-errors, but it'll be useful to see what you're getting


----
<a href="https://github.com/Tom-Neverwinter"><img src="https://avatars3.githubusercontent.com/u/3943634?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Tom-Neverwinter](https://github.com/Tom-Neverwinter)**
_Monday Nov 02, 2020 at 08:44:08_

----

`1> CMake generation started for configuration: 'x86-Release'.
1> Command line: "cmd.exe" /c ""c:\program files\microsoft visual studio\2019\community\common7\ide\commonextensions\microsoft\cmake\CMake\bin\cmake.exe"  -G "Ninja"  -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" -DCMAKE_INSTALL_PREFIX:PATH="C:\topaz\out\install\x86-Release" -DCMAKE_CXX_COMPILER:FILEPATH="C:/Program Files/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.27.29110/bin/Hostx86/x86/cl.exe" -DMYSQL_INCLUDE_DIR=C:\topaz\ext\include\mysql -DMYSQL_LIBRARY=C:\topaz\ext\lib\libmariadb.lib -DCMAKE_MAKE_PROGRAM="c:\program files\microsoft visual studio\2019\community\common7\ide\commonextensions\microsoft\cmake\Ninja\ninja.exe" "C:\topaz" 2>&1"
1> Working directory: C:\topaz\out\build\x86-Release
1> [CMake] CMake Error at C:\topaz\CMakeLists.txt:2 (project):
1> [CMake]   Running
1> [CMake] 
1> [CMake]    'C:/Program Files/Microsoft Visual Studio/2019/Community/Common7/IDE/CommonExtensions/Microsoft/CMake/Ninja/ninja.exe' '--version'
1> [CMake] 
1> [CMake]   failed with:
1> [CMake] 
1> [CMake]    This version of %1 is not compatible with the version of Windows you're running. Check your computer's system information and then contact the software publisher
1> [CMake] 
1> [CMake] 
1> [CMake] -- Configuring incomplete, errors occurred!
1> [CMake] See also "C:/topaz/out/build/x86-Release/CMakeFiles/CMakeOutput.log".
1> 'cmd.exe' '/c ""c:\program files\microsoft visual studio\2019\community\common7\ide\commonextensions\microsoft\cmake\CMake\bin\cmake.exe"  -G "Ninja"  -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" -DCMAKE_INSTALL_PREFIX:PATH="C:\topaz\out\install\x86-Release" -DCMAKE_CXX_COMPILER:FILEPATH="C:/Program Files/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.27.29110/bin/Hostx86/x86/cl.exe" -DMYSQL_INCLUDE_DIR=C:\topaz\ext\include\mysql -DMYSQL_LIBRARY=C:\topaz\ext\lib\libmariadb.lib -DCMAKE_MAKE_PROGRAM="c:\program files\microsoft visual studio\2019\community\common7\ide\commonextensions\microsoft\cmake\Ninja\ninja.exe" "C:\topaz" 2>&1"' execution failed with error: ''cmd.exe' '/c ""c:\program files\microsoft visual studio\2019\community\common7\ide\commonextensions\microsoft\cmake\CMake\bin\cmake.exe"  -G "Ninja"  -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" -DCMAKE_INSTALL_PREFIX:PATH="C:\topaz\out\install\x86-Release" -DCMAKE_CXX_COMPILER:FILEPATH="C:/Program Files/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.27.29110/bin/Hostx86/x86/cl.exe" -DMYSQL_INCLUDE_DIR=C:\topaz\ext\include\mysql -DMYSQL_LIBRARY=C:\topaz\ext\lib\libmariadb.lib -DCMAKE_MAKE_PROGRAM="c:\program files\microsoft visual studio\2019\community\common7\ide\commonextensions\microsoft\cmake\Ninja\ninja.exe" "C:\topaz" 2>&1"' returned with exit code: 1'.
`

https://pastebin.com/3d8vantr an error message is also generated to file


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Nov 02, 2020 at 09:11:05_

----

Updated the title of this so it's searchable, and leaving this link here:
https://gitlab.kitware.com/cmake/cmake/-/issues/18476

It appears that for whatever reason, the underlying makefile generator `Ninja` is failing on your VM. One solution to this could be swapping to `NMake` for Windows. I'll put this in my TODO list and I'll do the swap if it doesn't affect the build too much.

As long as you have a way to build, I'm going to close this issue.
