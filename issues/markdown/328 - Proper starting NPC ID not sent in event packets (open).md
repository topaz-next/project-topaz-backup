**Labels:**

bug



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jan 08, 2020 at 17:45:36_
_Originally opened as: project-topaz/topaz - Issue 328_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened or fixed
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

On retail, when an event start packet is sent to a player, included in it is the ID of the mob which "started" the event (see just about any capture with IDView/EventView running). _Some_ times this _should_ be the player's ID, but _most_ times it is the NPC that the player is talking to.

But currently, [lua_baseentity will _always_ send the event packet with the player's ID as the "initiator"](https://github.com/project-topaz/topaz/blob/3eb1c1570f276c8510300a2993fc225fc50d4ba7/src/map/lua/lua_baseentity.cpp#L1044-L1057). This causes some addons (like box destroyer, I believe) to not work, because those addons expect a valid NPC's ID, not the player's. (And is otherwise just inaccurate behavior).

This might be a "hard fix" though. At that point in core, the initiating NPC isn't being passed in at all, because we treat the player as the only object involved in an event (because currently, players invoke events, not NPCs). We might have to shift which entity involved in a conversation initiates the event and/or how.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jan 09, 2020 at 11:07:10_

----

Addendum: Putting the weight of handling events completely on NPCs may assist with solving #319 
