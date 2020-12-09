**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday Sep 06, 2020 at 09:30:30_
_Originally opened as: project-topaz/topaz - Issue 1071_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

I flipped the switch and swapped out travis and appveyeor for github actions and a couple of things have needed to be fixed:
- Make sure there are no stray bad-casts existing in `release`
- Make sure clang-format only looks at changes in cpp/h files
