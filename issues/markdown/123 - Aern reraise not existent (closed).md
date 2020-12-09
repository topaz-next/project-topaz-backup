**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:55_
_Originally opened as: project-topaz/topaz - Issue 123_

----

<a href="https://github.com/nesstea"><img src="https://avatars0.githubusercontent.com/u/1483915?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [nesstea](https://github.com/nesstea)**
_Saturday May 07, 2016 at 02:53 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3146_

----

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30160329_1

**_Server Version_** (type `revision` in game) **:** Not sure (UNKNOWN). I rebuilt on May 1st.

**_Source Branch_** (master/stable) **:** master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
 All Aern mobs do not reraise. They should die, plop to the ground, and then randomly subanim 3 and come back to life. Ix DRK doesn't reraise either, but needs to reraise multiple times.

Ideally, needs a mobmod with the value considered; mobmod of 30 would be reraising 30 times, decrementing by 1 each time. This would assume all the subanimations are the same and Aern family only.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:56_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Saturday May 07, 2016 at 03:30 GMT_

----

For normal aerns it's roundabout a 50% chance they reraise once, and if they've reraised once they will not reraise if killed a second time.

A normal aern killed twice will yield exp for both kills, but will only award drops for the second kill.

Edit: they reraise red-claimed to whoever killed them. They have trace hate on anyone who was on the active hate list when they died.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:57_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Saturday May 07, 2016 at 04:20 GMT_

----

Doubtful that I will bother with a mobmod.  Most likely as a script mixin,
but I'll have to add something to be able to pop the death/despawn state

On Fri, May 6, 2016 at 9:30 PM, Deadwing888 notificationsgithub.com
wrote:

> For normal aerns it's roundabout a 50% chance they reraise once, and if
> they've reraised once they will not reraise if killed a second time.
> 
> A normal aern killed twice will yield exp for both kills, but will only
> award drops for the second kill.
> 
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly or view it on GitHub
> github/DarkstarProject/darkstar - Issue 3146Darkstar Issue issuecomment-217603253




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:32:59_

----

<a href="https://github.com/nesstea"><img src="https://avatars0.githubusercontent.com/u/1483915?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nesstea](https://github.com/nesstea)**
_Saturday May 07, 2016 at 14:59 GMT_

----

KJ could you record it for learning purposes?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:33:00_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Tuesday Sep 20, 2016 at 23:14 GMT_

----

actually it's not fixed for all aerns so guess i'll reopen




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:33:01_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Sep 20, 2016 at 23:18 GMT_

----

And the reraise chance is 100% right now  :)




----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Monday Mar 09, 2020 at 20:30:00_

----

Hello. I'm unable to reproduce this issue on master as of 03/09/2020 (Aern were reraising, can't confirm the % but they were, and not 100%). Feel free to reopen an issue if you come across something new regarding this. Thank you.
