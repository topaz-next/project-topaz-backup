**Labels:**

improvement



<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 09, 2020 at 20:23:12_
_Originally opened as: project-topaz/topaz - Issue 481_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Comments in some places state regain mods are multiplied by 10, and in most places they is no longer the case - it gets taken as is. modifier.h has such a comment, and in the core no multiplication happens.

And the _status effect_ for regain, a multiplication by 10 takes place meaning you have to remember the _effect_ needs to be fed lower power values. But the _modifier_ regain set by the effect does not. 

Easy fix for someone who has some time to kill, just check what the comments currently say and correct them as needed.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Apr 10, 2020 at 01:45:32_

----

additional note: probably would be a good idea to audit the comments of both `modifier.h` and `status .lua` in the near future. this isn't the only outdated thing in them.
