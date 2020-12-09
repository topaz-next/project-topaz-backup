**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday Sep 18, 2020 at 08:00:54_
_Originally opened as: project-topaz/topaz - Issue 1154_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

- Comprehensive instructions and examples for Core and Lua in docs.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 26, 2020 at 05:51:51_

----

An update on this:
The clang-format file is somewhat sane, but I've disabled the check in CI because it straight up doesn't work if people have branched off of a point that doesn't have the latest changes. This is why _I_ never had any problems - because I was always bleeding-edge up-to-date.

I'll try and write up the points in the clang-format file as a guide with examples, also some important developer workflow stuff.
