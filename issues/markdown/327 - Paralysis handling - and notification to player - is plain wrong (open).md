**Labels:**

bug



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jan 08, 2020 at 17:13:41_
_Originally opened as: project-topaz/topaz - Issue 327_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened or fixed
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

When an action - melee or otherwise - is interrupted due to paralysis, what _should_ happen is that an action packet is still sent out, but with a value indicating it was interrupted.

What _is_ happening is that the server [sends out a fake message packet to everyone in range](https://github.com/DarkstarProject/darkstar/blob/bba5685bcf433f04054fb0a0ecd162bc93f072c4/src/map/entities/battleentity.cpp#L1417-L1420), and simply aborts further operation.

This is not how retail handles paralysis _at all_, and causes client addons to behave incorrectly.

[Aborting further operation is also why ability/spell recast timers aren't tripped when an action is paralyzed](https://github.com/DarkstarProject/darkstar/blob/ca6150891575749ddb1f92c2dca1c74314d23375/src/map/entities/charentity.cpp#L941). The server is just sending out a completely fake message packet, and then immediately dipping out prior to checking/flagging recast timers. This is the cause of #118 and #275.
