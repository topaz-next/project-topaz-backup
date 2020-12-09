**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday Sep 27, 2020 at 13:42:23_
_Originally opened as: project-topaz/topaz - Issue 1202_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Salvaged from Dan's PR: `Beginning support for Ansible, Docker, and Jenkins #867`

This will aid in letting people automate the different processes inside containers, otherwise, it won't affect anyone at all (That is of course, unless you have these things defined on your regular system for _something else_, then things will get weird.)



**TODO**
Test it


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Sep 28, 2020 at 08:33:37_

----

For later reference:
https://dev.mysql.com/doc/refman/5.6/en/environment-variables.html
https://mariadb.com/kb/en/mariadb-environment-variables/


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Wednesday Sep 30, 2020 at 14:13:09_

----

Would it be inappropriate for me to approve this PR?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 12, 2020 at 10:12:55_

----

My main source of decision paralysis here has been "what if someone else has these things already defined, and then their stuff will fail at random and it'll be nearly impossible to debug with them".

This can be solved by prepending "TPZ_" onto the front of each var, so I'll do that later

EDIT: The goal being: Can someone define these by hand, or have them defined when spinning up a container, so they don't have to modify any conf files. Automatically modifying our conf files ... is hard, so we want to avoid that 
