**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday Oct 25, 2020 at 08:44:20_
_Originally opened as: project-topaz/topaz - Issue 1431_

----

CMake: Stop using 3.12 features -> we specify using 3.10 (and that is what's bundled in Ubuntu 18.04 LTS).
Strange that the CI (which is 18.04 LTS) never complained...

**Further reading**
OBJECT libraries are bags of compiled objects, that don't have their dependencies figured out. They are great for splitting out sections of the build into their own steps that can be cached and then brought together at link time. 

However, they can't have dependencies added to them until 3.12 :(

So we have to use STATIC libs, which need to have their dependencies linked correctly at every stage, not just final link time.

I always thought you couldn't have a chain of static lib dependencies in cmake
```
A (static) -> B (static) -> C (executable)
```
I was under the assumption that C wouldn't get the symbols from A. I'm sure I encountered this issue at work a few years ago, which is why I had to use OBJECT libs. 

Though... that might have been a quirk of cross-compiling for iOS....

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


