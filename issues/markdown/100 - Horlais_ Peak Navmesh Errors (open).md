**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:35_
_Originally opened as: project-topaz/topaz - Issue 100_

----

<a href="https://github.com/dazusu"><img src="https://avatars0.githubusercontent.com/u/7009763?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [dazusu](https://github.com/dazusu)**
_Monday Mar 07, 2016 at 21:35 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2880_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

**_Client Version_** (type `/ver` in game) **:**
30160203_0

**_Server Version_** (type `revision` in game) **:**
1da5803

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
This error is spammed when a monster is engaged in Horlais' Peak:

[07/Mar] [22:30:39][1;31m[Navmesh Error][0m CNavMesh::raycastPoint startRef is invalid (0.000000, 0.000000, 0.000000) (139)
[07/Mar] [22:30:39][1;31m[Navmesh Error][0m CNavMesh::raycastPoint startRef is invalid (0.000000, 0.000000, 0.000000) (139)
[07/Mar] [22:30:39][1;31m[Navmesh Error][0m CNavMesh::raycastPoint startRef is invalid (0.000000, 0.000000, 0.000000) (139)
[07/Mar] [22:30:39][1;31m[Navmesh Error][0m CNavMesh::raycastPoint startRef is invalid (0.000000, 0.000000, 0.000000) (139)
[07/Mar] [22:30:39][1;31m[Navmesh Error][0m CNavMesh::raycastPoint startRef is invalid (0.000000, 0.000000, 0.000000) (139)
[07/Mar] [22:30:39][1;31m[Navmesh Error][0m CNavMesh::raycastPoint startRef is invalid (0.000000, 0.000000, 0.000000) (139)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:36_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Monday Mar 07, 2016 at 21:39 GMT_

----

Looks like a mob is stuck at 0 0 0. Will fix that.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:38_

----

<a href="https://github.com/dazusu"><img src="https://avatars0.githubusercontent.com/u/7009763?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dazusu](https://github.com/dazusu)**
_Tuesday Mar 08, 2016 at 00:08 GMT_

----

The mob in question isn't stuck at 0,0,0, it's a mob I've just implemented - it has a position in the database; and popped it infront of me; when engaged, it spams that error.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:39_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Mar 08, 2016 at 00:16 GMT_

----

sounds more like a problem with your mob than the navmesh

On Mon, Mar 7, 2016 at 5:08 PM, Liam Conlan notificationsgithub.com
wrote:

> The mob in question isn't stuck at 0,0,0, it's a mob I've just implemented
> - it has a position in the database; and popped it infront of me; when
>   engaged, it spams that error.
> 
> —
> Reply to this email directly or view it on GitHub
> github/DarkstarProject/darkstar - Issue 2880Darkstar Issue issuecomment-193517847
> .




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:40_

----

<a href="https://github.com/dazusu"><img src="https://avatars0.githubusercontent.com/u/7009763?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dazusu](https://github.com/dazusu)**
_Tuesday Mar 08, 2016 at 13:29 GMT_

----

bendangelo  let's discuss this in more detail when you next have some free time to jump on IRC. There's certain situations where pathing fails; and re-attempts are spammed at such a rate that dsp chokes/dies/becomes incredibly laggy and unusable without restarting. I'm talking about situations other than the one discussed in this issue too.

Perhaps some cooldown on attempts to remap a path after a failure; or not attempting to path mobs where there's an obvious issue with the mobs configuration that's going to cause issues.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:27:42_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Tuesday Mar 08, 2016 at 15:30 GMT_

----

Ok.


