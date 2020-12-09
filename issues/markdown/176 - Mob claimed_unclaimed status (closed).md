**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:44:06_
_Originally opened as: project-topaz/topaz - Issue 176_

----

<a href="https://github.com/Jessland86"><img src="https://avatars1.githubusercontent.com/u/28382433?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Jessland86](https://github.com/Jessland86)**
_Tuesday May 16, 2017 at 15:04 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3876_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30170304_1

**_Server Version_** (type `revision` in game) **:**
581b5e7da03d7e1f088057abccf4e5af4334a1c5

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
If a party or alliance has claim on a mob and someone outside the alliance/party gets on the hate list and the party/alliance wipes the mob will not go unclaimed till every one on the hate list is dead or zones.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:44:07_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Wednesday Jul 05, 2017 at 22:49 GMT_

----

This is more or less correct behavior. Some of the ways mob can go white (disengaging weapon for instance) are not handled properly, but claim should hold on whoever has it irrespective of the hate list.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:44:08_

----

<a href="https://github.com/Jessland86"><img src="https://avatars1.githubusercontent.com/u/28382433?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Jessland86](https://github.com/Jessland86)**
_Friday Jul 07, 2017 at 04:40 GMT_

----

I worded it incorrectly then, the mob will stay red claimed to a dead alliance and not go white until everyone is dead. Allowing an alliance to zombie kill things without chance of the mob ever going white and allowing other players a chance to kill it.

I also notice another interesting thing. Just attempting to claim a mob puts you on the hate list. even if the spell or JA. Heck even clicking "attack" and getting the message "Cannot attack. Your target is already claimed." puts you on the hate list. 

So on servers that actually have lots of competition to claim things the actual party that gets claim is basically safe to zombie the mob to death because lots of other players are on the hate list and it will stay red till everyone wipes or zones it.



----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Thursday Jun 25, 2020 at 15:02:33_

----

Hello, I'm unable to reproduce this on the canary branch as of 06/25/2020.

Claimed a mob with character A.
Tried to attack said mob with character B and got the "Cannot attack. Your target is already claimed." message.
Character A dies or zone.
Mob goes unclaimed and trying to attack it multiple times with character B while it was claimed by A didn't generate any hate (when it went unclaimed it didn't attack B).
