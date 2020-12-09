**Labels:**



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 28, 2020 at 22:51:27_
_Originally opened as: project-topaz/topaz - Issue 1449_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
https://github.com/project-topaz/topaz/blob/release/src/map/status_effect.h line 82

https://github.com/project-topaz/topaz/blob/release/scripts/globals/status.lua line 182 (can’t direct link to line on mobile)


We need one single convention, either underscore and a 1 or not, but not half one cor the core and half the other in lua. This is likely what lead to the issue solved in #1448 so lets pick one and make sure all effects with multiple versions are done the same way.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Oct 29, 2020 at 00:09:57_

----

For Curse, I will merge a Pull Request that changes all "Curse 1" to just curse, and "Curse 2" (ST20) to "Zombie".


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2020 at 00:50:25_

----

am concerned having names of effects not match client will potentially cause additional confusion points. in the dats, both curses are just listed as "curse". I _swear to god_ there were _three_ but Bane is its own effect now apparently, sitting at the ID I thought was our man.
