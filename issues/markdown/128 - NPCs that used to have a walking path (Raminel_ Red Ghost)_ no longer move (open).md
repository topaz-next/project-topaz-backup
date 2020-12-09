**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:02_
_Originally opened as: project-topaz/topaz - Issue 128_

----

<a href="https://github.com/dazusu"><img src="https://avatars0.githubusercontent.com/u/7009763?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [dazusu](https://github.com/dazusu)**
_Saturday Jul 02, 2016 at 13:55 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3260_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30160602_0

**_Server Version_** (type `revision` in game) **:**
6368ffc

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:03_

----

<a href="https://github.com/personaone"><img src="https://avatars0.githubusercontent.com/u/8123295?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [personaone](https://github.com/personaone)**
_Saturday Jul 02, 2016 at 18:36 GMT_

----

Can confirm this as well. Probably has something to do with Navmeshes?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:05_

----

<a href="https://github.com/dazusu"><img src="https://avatars0.githubusercontent.com/u/7009763?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dazusu](https://github.com/dazusu)**
_Saturday Jul 02, 2016 at 20:22 GMT_

----

Shouldn't be related to Navmeshes.  NPCs that have set paths don't use 
the Navmesh system to follow them; they use a set of pre-defined 
positions which are located in the NPCs lua file in most cases.

On 02/07/2016 19:36, personaone wrote:

> Can confirm this as well. Probably has something to do with Navmeshes?
> 
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub 
> github/DarkstarProject/darkstar - Issue 3260Darkstar Issue issuecomment-230115912, 
> or mute the thread 
> github/notifications/unsubscribe/AGr14wwL3duw4JVrac-17xad2bU6sLj7ks5qRq-5gaJpZM4JDreI.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:06_

----

<a href="https://github.com/thedax"><img src="https://avatars2.githubusercontent.com/u/4482745?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [thedax](https://github.com/thedax)**
_Saturday Aug 06, 2016 at 23:59 GMT_

----

They seem to move fine for me for a little while on the latest commit (github/DarkstarProject/darkstar/commit/80077e89091f3189d5f31dbf263aec8b305715ed) & the latest client (30160728_0), but then they stop and don't seem to move again after talking to them.

Edit: Removed irrelevant info.


