**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:59_
_Originally opened as: project-topaz/topaz - Issue 135_

----

<a href="https://github.com/thedax"><img src="https://avatars2.githubusercontent.com/u/4482745?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [thedax](https://github.com/thedax)**
_Wednesday Sep 07, 2016 at 03:54 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3354_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [X] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
N/A

**_Server Version_** (type `revision` in game) **:**
5f431dab25e47484570d8a891ddf6c5c727f216f

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
This doesn't seem to be ARM or x86 specific, as it happens on both: if you try to compile the server with O0 instead of O1 or O2 (the default), the build will fail:

dsgame-navmesh.o: In function `CNavMesh::findRandomPosition(position_t const&, float)':
/home/dax/darkstar/src/map/navmesh.cpp:327: undefined reference to`CNavMesh::ERROR_NEARESTPOLY'
/home/dax/darkstar/src/map/navmesh.cpp:333: undefined reference to `CNavMesh::ERROR_NEARESTPOLY'
/home/dax/darkstar/src/map/navmesh.cpp:342: undefined reference to`CNavMesh::ERROR_NEARESTPOLY'
collect2: error: ld returned 1 exit status
Makefile:1196: recipe for target 'dsgame' failed
make: **\* [dsgame] Error 1

On my x86 box I'm using gcc 6.2.0 and on my Pi 3 I'm using 6.1.0.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:00_

----

<a href="https://github.com/Cloudef"><img src="https://avatars2.githubusercontent.com/u/480330?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Cloudef](https://github.com/Cloudef)**
_Wednesday Sep 07, 2016 at 07:14 GMT_

----

Seems like compiler bug.

Constant variable definitions in class declaration are only okay if you don't need their _address_.
I assume with -O0 the compiler generates code that needs the address of `CNavMesh::ERROR_NEARESTPOLY` somewhere.

Not arguing with the sanity of this yet another C++ language "feature",
but it may be best to change the `ERROR_NEARESTPOLY` constant into enum instead, such as:
`enum { ERROR_NEARESTPOLY = -1; };`


