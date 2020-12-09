**Labels:**

merge ready



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Thursday Mar 12, 2020 at 19:55:10_
_Originally opened as: project-topaz/topaz - Issue 416_

----

…y one minute (from next midnight)

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This closes https://github.com/project-topaz/topaz/issues/413

https://www.bg-wiki.com/bg/Chasing_Quotas


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Mar 16, 2020 at 23:02:55_

----

I'm holding off on merge due to the char_var name change. I _personally_ feel the chances of a server having a character who triggered the wait but never finished it are very slim, so I'd be willing to merge as-is. But I'll leave this open in case someone wants to make the argument for a migration script.

(We can make sure the var name change is mentioned in whatever @zircon-tpl is planning for the next digest~)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Mar 17, 2020 at 08:49:02_

----

I'm happy to use the old name, it's pretty obvious what it does when you look at it with context and I'd rather not burden operators with a migration for such a little fix.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 18, 2020 at 01:12:31_

----

That works, thanks Zach!
