**Labels:**

reviewed



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Friday Aug 28, 2020 at 21:54:13_
_Originally opened as: project-topaz/topaz - Issue 1020_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Tested, works well.

conquest.lua had a variable called cp in the local outposts table that was unused.  Retail functions by charging cp equivalent to 1/10 the gil cost for using outposts, so this was an easy cleanup.

![image](https://user-images.githubusercontent.com/37684138/91618032-384c7380-e93e-11ea-8541-43cafd0aa436.png)

Thanks to several people on Gold Saucer for bringing this up, and Nireya@GS for targeting the issue.
