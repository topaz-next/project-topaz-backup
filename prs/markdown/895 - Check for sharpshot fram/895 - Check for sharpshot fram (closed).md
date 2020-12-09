**Labels:**

reviewed



<a href="https://github.com/TheWhaler"><img src="https://avatars0.githubusercontent.com/u/28814616?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TheWhaler](https://github.com/TheWhaler)**
_Monday Jul 27, 2020 at 12:24:47_
_Originally opened as: project-topaz/topaz - Issue 895_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

I noticed that on Tantalus the harlequin frame was doing ranged attacks even when it shouldn't at pretty much every tick that it wasn't doing something earlier in the process. Added in a frame check to the TryRangedAttack function.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 00:58:02_

----

Since we're returning false outside of this parent if check, we can combine the frame check into the same check as the cooldown check, and remove the inner `return false`.


----
<a href="https://github.com/TheWhaler"><img src="https://avatars0.githubusercontent.com/u/28814616?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TheWhaler](https://github.com/TheWhaler)**
_Wednesday Jul 29, 2020 at 17:46:56_

----

Doh cs101 change made ;)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 29, 2020 at 00:58:02_

----

Since we're returning false outside of this parent if check, we can combine the frame check into the same check as the cooldown check, and remove the inner `return false`.


----
<a href="https://github.com/TheWhaler"><img src="https://avatars0.githubusercontent.com/u/28814616?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TheWhaler](https://github.com/TheWhaler)**
_Wednesday Jul 29, 2020 at 17:46:56_

----

Doh cs101 change made ;)
