**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:17_
_Originally opened as: project-topaz/topaz - Issue 315_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Wednesday Oct 09, 2019 at 18:01 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6235_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** n/a


**_Source Branch_** (master/stable) **:** master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

(Preface: This _is_ a case of an "implemented", but ~~broken~~ inaccurate quest in DSP. Not an unimplemented one.)

Derrick in Lower Jeuno is supposed to start SAVE_THE_CLOCK_TOWER ([BG link](https://www.bg-wiki.com/bg/Save_the_Clock_Tower)). [He does not.](github/DarkstarProject/darkstar/blob/master/scripts/zones/Lower_Jeuno/npcs/Derrick.lua)

In fact, [he never has](github/DarkstarProject/darkstar/commit/5ce875d1e671573966dc38fb7b7f1f3f35cf2baa).

I suspect that some of those `QUEST_ACCEPTED` should be `QUEST_AVAILABLE`.
...He will also need to actually make a call to `player:addQuest` in the event finishes.

(Oh, and the fame check is missing, too.)

**edit**:
After doing some more digging, apparently we have [the door responsible for a previous quest (A Clock Most Delicate) automatically starting Save the Clock Tower, without talking to Derrick](github/DarkstarProject/darkstar/blob/master/scripts/zones/Upper_Jeuno/npcs/_6s2.lua).

While the door's event does mention the petition, both [BG](https://www.bg-wiki.com/bg/Save_the_Clock_Tower) and [FFXIclopedia](https://ffxiclopedia.fandom.com/wiki/Save_the_Clock_Tower) say Derrick is what starts the quest.

**edit 2**:
So it turns out my original title was correct. The prerequisite quest, A Clock Most Delicate ([FFXIclopedia](https://ffxiclopedia.fandom.com/wiki/A_Clock_Most_Delicate)), _can't_ be started, so Save the Clock Tower can't be either. Let's run through this:

So at the moment, [Galmut's Door in Upper Jeuno is what is (erroneously) starting Save the Clock Tower](github/DarkstarProject/darkstar/blob/master/scripts/zones/Upper_Jeuno/npcs/_6s2.luaDarkstar Issue L62-L63). (Side note: If you trigger this door on DSP, Galmut will appear and say "Oh, it's you...", as if he had previously met you despite the player not having done so. I can't say for certain that this is inaccurate behavior without checking retail.)

On DSP, starting Save the Clock Tower happens immediately upon completing A Clock Most Delicate, which is (correctly) started by said door.

[But to gain access to the door](github/DarkstarProject/darkstar/blob/master/scripts/zones/Upper_Jeuno/npcs/_6s2.luaDarkstar Issue L20-L23), you must speak with Collet (and have requisite fame), who will set a char var to give you access, so you can trigger the door and start A Clock Most Delicate proper (which, again, is required for Save the Clock Tower).

[However, Collet's script is checking if `aClockMostdelicate` is `QUEST_AVAILABLE`, without having actually assigned the variable to anything.](github/DarkstarProject/darkstar/blob/master/scripts/zones/Upper_Jeuno/npcs/Collet.luaDarkstar Issue L22-L24) And, well, [she's always been broken](github/DarkstarProject/darkstar/commit/ecbd13686e2950963bb418943c3215562a2de61eDarkstar Issue diff-7a40ae230a471b8a5a747ebdcae38a33).

So A Clock Most Delicate can't be started, and therefore, the entire quest line can't as well.

**edit 3**:
Apparently, when it was tested, [that variable was being set globally via Galmut's Door.](github/DarkstarProject/darkstar/commit/a94b81d2d89b1cad6357974bb59b4f1feaf7247fDarkstar Issue diff-6e3f2a1871e8b8bd5de5062fc847f4da)
([The global assignment got fixed](github/DarkstarProject/darkstar/commit/14223ce7a31515db7494aec7beb5f8b25e8b04fdDarkstar Issue diff-6e3f2a1871e8b8bd5de5062fc847f4da).)



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:18_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Oct 09, 2019 at 20:37 GMT_

----

addvar/addcharvar: exists

Teo: (ಠ_ಠ)

its not like modifiers where we will always increment then decremented. no, we are going to be looking for a SPECIFIC value later, and its saner to set that EXACT value so that scriptwriters and debuggers know at a glance what value they are checking for in their getCharVar.

In before bossman tells you to make a delCharVar to decrement..

