**Labels:**



<a href="https://github.com/Diresheep"><img src="https://avatars3.githubusercontent.com/u/19691572?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Diresheep](https://github.com/Diresheep)**
_Sunday May 31, 2020 at 09:20:01_
_Originally opened as: project-topaz/topaz - Issue 670_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

While attempting to install a server as per the wiki instructions, make fails to find header files with this error

https://pastebin.com/CzWaV9wg

Attempting make again shows a different set of failures, but I cannot for the life of me figure out why they cannot be found. 

src Directory:   https://i.imgur.com/1cgBMmt.png

Not sure if this is a problem with my setup or something to do with the automake setup, but any help would be appreciated






----
<a href="https://github.com/SirGouki"><img src="https://avatars3.githubusercontent.com/u/11664236?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [SirGouki](https://github.com/SirGouki)**
_Tuesday Jul 07, 2020 at 22:21:01_

----

```bash
In file included from src/common/kernel.cpp:25:0:
src/common/../common/taskmgr.h:30:15: fatal error: any: No such file or directory
compilation terminated.
```

This is the error you posted in pastebin (I'd recommend posting specific errors in the issue itself).  You did not post the other error you got.  It would appear that kernel.cpp is expecting taskmgr.h to be somewhere else, judging by the look of the error it's appending the `src/common` onto `../common`.  My suggestion would be to open kernel.cpp with a text editor and look for the line that says
```c++
#include "../common/taskmgr.h"
```
and see what it is, and change it to what it should be (or open the Make file and remove the extra append if I'm correct in my guess).  If that works, respond back with what you had to do, so that it can be documented/a better fix applied.

Edit:
I took a look into kernel.cpp, it is indeed correctly calling
```c++
#include "../common/taskmgr.h"
```
Which is causing make to turn it into `src/common/../common/taskmgr.h`. While this should still work, I suspect the OS you're using doesn't like this, and you may need to edit the make file to ignore appending the paths to the source files.


----
<a href="https://github.com/Diresheep"><img src="https://avatars3.githubusercontent.com/u/19691572?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Diresheep](https://github.com/Diresheep)**
_Thursday Jul 09, 2020 at 07:04:26_

----

You, sir, are a godsend. It was an OS issue. It seems that Ubuntu 16.04 just didn't work with that syntax, and doing a release upgrade to 18.04 LTS made it work. Didn't really want to try that, but it's working now! Thank you.
