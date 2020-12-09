**Labels:**

hold



<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 29, 2020 at 22:55:33_
_Originally opened as: project-topaz/topaz - Issue 548_

----

• Addition of npcBasicPath to pathfind.lua, this pathfind function requires paths to be set in a linear fashion like this example
local path =
{
    [1] = {1.000, 2.000, 3.000},
    [2] = {2.000, 2.000, 3.000},
    [3] = {3.000, 2.000, 3.000},
    [4] = {2.000, 2.000, 3.000}
}
This way the path returns to the origin from the last path point to the first, i.e a circle.
the npcBasicPath will keep track of what path point the npc is on by the newly added m_pathPoint in npcentity.

• As stated above i have added a m_pathPoint to npcentity and given the the entity a getter and setter to help keep track of the npc's path.

• Adjusted Novalmauge's script to reflect the changes.

He's walk animation still seems a bit buggy but its about as good as i could get it.
But atleast it shouldn't crash the server anymore.
 
This should fix the following bug
Novalmauge causes server crash due to pathing. #493

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 03:16:50_

----

123..2?

In either case, the table keys aren't needed; Lua will internally give un-keyed elements an increasing integer representation 😉 

(Unless you've changed the key structure with hard-indexed elements, but that's a different can of worms.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 03:20:42_

----

If change the break to be only on players, we might be able to use this pathing method for mobs too~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 03:26:51_

----

Thoughts of baking this into `initNpcAi`? Can make it take a table, grab the first point while in core, set the pos, and also potentially take a walking speed as well to set as a local var.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 03:29:40_

----

If all paroling NPCs use this new method, will `npc:wait()` still have a use? Should we consider changing the internals of `:wait()` to essentially set speed to 0? (Would pathing need to be stopped?)

If we need to keep `npc:wait()`, should there be a wrapper like `tpz.path.pause()`?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 03:31:09_

----

If the "new" initNpcAi (which has a commented TODO to change the name) ends up setting a local var to the NPC, then could add a `tpz.path.resume()` which sets the speed back and calls `npcBasicPath`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 06:40:15_

----

opinion: wait() does a lot of things besides stopping movement, it stops all the stuff and things. because of that its tempting to use it for a lot of situations that result in crashes. wait should be removed from its use in pathing scripts, but may have future use for..something.. 

could we possibly cause the event triggering core side to set the entities speed to 0 and then the event finish to restore it to its original value? :thinking: `m_event.Target` appears to be the npc in the core.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 07:43:41_

----

> m_event.Target appears to be the npc in the core

I was not aware of this - we can make event starts accurate! (On retail, the packet is the initiating NPC, but we've always invoked it directly as the "player" being the initiator)


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday May 03, 2020 at 16:52:34_

----

sounds good to me, seems a better way of doing it.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday May 03, 2020 at 16:55:44_

----

Might aswell hold this till that gets implimented if thats what you want to do, then i can change it, might have to give me a nudge to change it incase i forget lol.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday May 03, 2020 at 18:42:55_

----

yeah true, i guess i got so used to doing table like this for readability, that i just did it this way.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday May 03, 2020 at 18:43:22_

----

yeah sounds good to me


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Monday Jun 22, 2020 at 11:02:27_

----

implimented pathStop() and pathResume() to move away from using wait()


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Monday Jun 22, 2020 at 11:10:28_

----

I'm not really sure where to go with this but as we now have pathStop() and pathResume(), we will no longer get crashes when interacting with an npc that uses pathing, i think i found and converted all npc's that use pathing to use the new pathing systems.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday Jun 27, 2020 at 13:27:22_

----

This has been done now


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday Jun 27, 2020 at 13:32:40_

----

i did change the name of initNpcAI to initNpcPathing and you can now call it as npc:initNpcPathing() or pass an x,y,z to set the start position so npc:initNpcPathing(x,y,z) and also it will set the path point to 1 as default, but you can pass a 4th param to set the point also so npc:initNpcPathing(x, y, z, 5) will set the position and set the starting path point to 5. 


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday Jun 27, 2020 at 13:34:02_

----

I can look into making event set the speed to 0 at a later date if still wanted.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday Jun 27, 2020 at 13:35:53_

----

all tables that use the new system should now be a simple point i.e. {10, 10, 10} with additional extra params able to be passed if required.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 08:39:50_

----

This section really nicely highlights the benefits of this PR!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 08:41:11_

----

Looking at this "in the wild", I wonder if `general` is really the right name for the default, regular, general call?

Now that I say the other options, I guess it's as good as all the others 🤷 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 08:41:44_

----

I hope you were able to automate this process and didn't have to manage all these tables by hand...


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 08:43:14_

----

Theres some borked tab indents around here


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Aug 23, 2020 at 09:22:08_

----

Maybe refactor to `tpz.pathing.path()`, I don't know how much work that would be?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 24, 2020 at 04:52:35_

----

Why not store the original speed in a localVar instead of re-querying the database?
You can actually get and set localVars from the C++ side too, not just in lua.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 24, 2020 at 04:54:31_

----

For NPCs we could try having the event code itself stop and restart NPC movement. since `m_event.target` is the NPC entity itself. Mobs we'd still need a script command for stop/start.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 24, 2020 at 05:01:18_

----

`m_PBaseEntity->speed = 0;` actually does work, no need to recast as a battleentity for either mobs or npc's (or players). Which makes this entire function in its current form a duplicate of `speed()`

Lets improve it by having this function also store the entities current speed to a localVar prior to setting it zero. Then resume path can read that value instead of querying the database every time.

```c++
 m_PBaseEntity->SetLocalVar(lua_tostring(L, 1), (uint64_t)lua_tointeger(L, 2));
```


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Friday Aug 28, 2020 at 03:47:18_

----

do we want to place all these in an issue or ?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 28, 2020 at 04:52:47_

----

not particularly no. I'd rather see it be changed here and its such a small correction to make instead of unnecessarily adding more iops of our inefficient db connection.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 03:16:50_

----

123..2?

In either case, the table keys aren't needed; Lua will internally give un-keyed elements an increasing integer representation 😉 

(Unless you've changed the key structure with hard-indexed elements, but that's a different can of worms.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 03:20:42_

----

If change the break to be only on players, we might be able to use this pathing method for mobs too~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 03:26:51_

----

Thoughts of baking this into `initNpcAi`? Can make it take a table, grab the first point while in core, set the pos, and also potentially take a walking speed as well to set as a local var.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 03:29:40_

----

If all paroling NPCs use this new method, will `npc:wait()` still have a use? Should we consider changing the internals of `:wait()` to essentially set speed to 0? (Would pathing need to be stopped?)

If we need to keep `npc:wait()`, should there be a wrapper like `tpz.path.pause()`?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 03:31:09_

----

If the "new" initNpcAi (which has a commented TODO to change the name) ends up setting a local var to the NPC, then could add a `tpz.path.resume()` which sets the speed back and calls `npcBasicPath`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday May 03, 2020 at 06:40:15_

----

opinion: wait() does a lot of things besides stopping movement, it stops all the stuff and things. because of that its tempting to use it for a lot of situations that result in crashes. wait should be removed from its use in pathing scripts, but may have future use for..something.. 

could we possibly cause the event triggering core side to set the entities speed to 0 and then the event finish to restore it to its original value? :thinking: `m_event.Target` appears to be the npc in the core.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 03, 2020 at 07:43:41_

----

> m_event.Target appears to be the npc in the core

I was not aware of this - we can make event starts accurate! (On retail, the packet is the initiating NPC, but we've always invoked it directly as the "player" being the initiator)


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday May 03, 2020 at 16:52:34_

----

sounds good to me, seems a better way of doing it.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday May 03, 2020 at 16:55:44_

----

Might aswell hold this till that gets implimented if thats what you want to do, then i can change it, might have to give me a nudge to change it incase i forget lol.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday May 03, 2020 at 18:42:55_

----

yeah true, i guess i got so used to doing table like this for readability, that i just did it this way.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday May 03, 2020 at 18:43:22_

----

yeah sounds good to me


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Monday Jun 22, 2020 at 11:02:27_

----

implimented pathStop() and pathResume() to move away from using wait()


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Monday Jun 22, 2020 at 11:10:28_

----

I'm not really sure where to go with this but as we now have pathStop() and pathResume(), we will no longer get crashes when interacting with an npc that uses pathing, i think i found and converted all npc's that use pathing to use the new pathing systems.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday Jun 27, 2020 at 13:27:22_

----

This has been done now


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday Jun 27, 2020 at 13:32:40_

----

i did change the name of initNpcAI to initNpcPathing and you can now call it as npc:initNpcPathing() or pass an x,y,z to set the start position so npc:initNpcPathing(x,y,z) and also it will set the path point to 1 as default, but you can pass a 4th param to set the point also so npc:initNpcPathing(x, y, z, 5) will set the position and set the starting path point to 5. 


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday Jun 27, 2020 at 13:34:02_

----

I can look into making event set the speed to 0 at a later date if still wanted.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Saturday Jun 27, 2020 at 13:35:53_

----

all tables that use the new system should now be a simple point i.e. {10, 10, 10} with additional extra params able to be passed if required.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 08:39:50_

----

This section really nicely highlights the benefits of this PR!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 08:41:11_

----

Looking at this "in the wild", I wonder if `general` is really the right name for the default, regular, general call?

Now that I say the other options, I guess it's as good as all the others 🤷 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 08:41:44_

----

I hope you were able to automate this process and didn't have to manage all these tables by hand...


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 08:43:14_

----

Theres some borked tab indents around here


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Aug 23, 2020 at 09:22:08_

----

Maybe refactor to `tpz.pathing.path()`, I don't know how much work that would be?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 24, 2020 at 04:52:35_

----

Why not store the original speed in a localVar instead of re-querying the database?
You can actually get and set localVars from the C++ side too, not just in lua.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 24, 2020 at 04:54:31_

----

For NPCs we could try having the event code itself stop and restart NPC movement. since `m_event.target` is the NPC entity itself. Mobs we'd still need a script command for stop/start.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 24, 2020 at 05:01:18_

----

`m_PBaseEntity->speed = 0;` actually does work, no need to recast as a battleentity for either mobs or npc's (or players). Which makes this entire function in its current form a duplicate of `speed()`

Lets improve it by having this function also store the entities current speed to a localVar prior to setting it zero. Then resume path can read that value instead of querying the database every time.

```c++
 m_PBaseEntity->SetLocalVar(lua_tostring(L, 1), (uint64_t)lua_tointeger(L, 2));
```


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Friday Aug 28, 2020 at 03:47:18_

----

do we want to place all these in an issue or ?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 28, 2020 at 04:52:47_

----

not particularly no. I'd rather see it be changed here and its such a small correction to make instead of unnecessarily adding more iops of our inefficient db connection.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 08:47:17_

----

I think you've taken care of all semicolons and random things in Lua, but if you could take a merge of release just to be sure that would be grand
