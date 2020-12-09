**Labels:**



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 04:45:11_
_Originally opened as: project-topaz/topaz - Issue 379_

----

This is a prerequisite for DarkstarProject/xiloader#7.

This change adds support for a new command in the login code to support
changing a users password. It simply verifies the users login similarly
to the existing flow, and then makes another request over the socket for
the new password. Then it updates the SQL.

Tested locally. Have a set of changes ready for xiloader as well, but
this work is required first.

NOTE: There is definitely some refactoring that could be done in this
file to reduce the amount of nested braces and to reduce duplicated code.
I tried to touch as little existing code as possible in this change to
reduce the risk of introducing a regression.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


