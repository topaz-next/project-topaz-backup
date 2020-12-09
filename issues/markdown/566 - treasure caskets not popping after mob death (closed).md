**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Saturday May 02, 2020 at 02:53:30_
_Originally opened as: project-topaz/topaz - Issue 566_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
on canary branch, when killing a mob and casket_drop_rate is 0.1 or 1, no treasure chest show up afterwards. Tried it on sarutabaruta and runfare.



----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday May 02, 2020 at 09:00:07_

----

This was cuased by a local var not being checked correctly

issue is fixed in PR #568


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday May 02, 2020 at 17:01:52_

----

@Omnione now they pop, but cannot be interacted with (wasn't sure if i had to open a new bug)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday May 08, 2020 at 00:57:16_

----

Remaining unopenable issue fixed in #573
