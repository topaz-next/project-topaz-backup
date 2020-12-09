**Labels:**

hold



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 18:33:40_
_Originally opened as: project-topaz/topaz - Issue 366_

----

Added ID for message (as it's not part of CS)
When loading into the boat, it will store the Vanadiel hour and minute.
It will check the time it should be arriving depending on the boat schedule.
It will subtract the time the boat will dock and the time the char zoned in then use that as
a timer so the text shows to the player on the correct time.
Once this is approved I'll do the same thing to the other boats
Also removed semicolons

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 18:39:47_

----

Should this have a = 0 just to be started and not a nil


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Feb 20, 2020 at 19:42:27_

----

What happens if a player leaves the boat after zoning in?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Feb 20, 2020 at 19:48:30_

----

Since dock minute is always 40, you might spare yourself the variable declaration above; you're only using it here.

(And if you're only assigning based on one of three sets of dockHours, you could save yourself doing the math every time by instead setting `dockTime = integer` in the if)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 20:33:28_

----

they do not get the message, i guess timers get reset after zoning.
I tried with !zone gm command but now that you mention it i am going to try using warp spell or ring.

Nice catch =)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 20:34:47_

----

will do. I just added the var in case it was seen as a magic number lol. Will be happy to remove it.

I'll play around with your other suggestion :cat: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 20:35:14_

----

will set it as a zero and test out. thank you @KnowOne134  :cat: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Feb 20, 2020 at 22:37:58_

----

One thing you might look into is potentially setting a timer on a nearby NPC (invisible or otherwise). It's not like _they're_ going anywhere~


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Feb 21, 2020 at 04:51:13_

----

@ibm2431  i tried doing:
```lua
    GetNPCByID(17014822):timer(1000 * earthSecsUntilDock, function(player) player:messageSpecial(ID.DOCKING_IN_NASHMAU) end)
```
and it crashes the server. That ID is for the ship captain. Am i doing your suggestion wrong?

Also I was able to confirm that the message doesn't show if the player warps out of the zone before the ship docks.

Let me know otherwise if the timer needs to moved or it can stay on the player, do not see an issue with the timer on the player ^^;;


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Feb 21, 2020 at 04:55:56_

----

@ibm2431  im think i wanna keep the minute declaration so it can be easily understood when reading the formula.

I am not doing a static docktime as the reason why i did this is because im taking in consideration the time the player zones into the zone to start the timer, if for example they are running on a potatoe and the loading area needs more time time before the player gets loaded into the zone then if using a static time, they might never see the message. Or also if they log out or disconnect and reconnect while still on the ship then the timer can take in consideration the time they just zoned back into the ship.

Sorry if it sounds complicated but we can take it on discord to try to explain myself a bit better


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Feb 21, 2020 at 17:02:38_

----

well the player would no longer be there for `player:messageSpecial()` calls to keep working, so that is expected - do the whole thing without the player, make it an area message. Pretty sure that's how retail handles the message while on the boat. 


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 18:39:47_

----

Should this have a = 0 just to be started and not a nil


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Feb 20, 2020 at 19:42:27_

----

What happens if a player leaves the boat after zoning in?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Feb 20, 2020 at 19:48:30_

----

Since dock minute is always 40, you might spare yourself the variable declaration above; you're only using it here.

(And if you're only assigning based on one of three sets of dockHours, you could save yourself doing the math every time by instead setting `dockTime = integer` in the if)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 20:33:28_

----

they do not get the message, i guess timers get reset after zoning.
I tried with !zone gm command but now that you mention it i am going to try using warp spell or ring.

Nice catch =)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 20:34:47_

----

will do. I just added the var in case it was seen as a magic number lol. Will be happy to remove it.

I'll play around with your other suggestion :cat: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 20:35:14_

----

will set it as a zero and test out. thank you @KnowOne134  :cat: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Feb 20, 2020 at 22:37:58_

----

One thing you might look into is potentially setting a timer on a nearby NPC (invisible or otherwise). It's not like _they're_ going anywhere~


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Feb 21, 2020 at 04:51:13_

----

@ibm2431  i tried doing:
```lua
    GetNPCByID(17014822):timer(1000 * earthSecsUntilDock, function(player) player:messageSpecial(ID.DOCKING_IN_NASHMAU) end)
```
and it crashes the server. That ID is for the ship captain. Am i doing your suggestion wrong?

Also I was able to confirm that the message doesn't show if the player warps out of the zone before the ship docks.

Let me know otherwise if the timer needs to moved or it can stay on the player, do not see an issue with the timer on the player ^^;;


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Feb 21, 2020 at 04:55:56_

----

@ibm2431  im think i wanna keep the minute declaration so it can be easily understood when reading the formula.

I am not doing a static docktime as the reason why i did this is because im taking in consideration the time the player zones into the zone to start the timer, if for example they are running on a potatoe and the loading area needs more time time before the player gets loaded into the zone then if using a static time, they might never see the message. Or also if they log out or disconnect and reconnect while still on the ship then the timer can take in consideration the time they just zoned back into the ship.

Sorry if it sounds complicated but we can take it on discord to try to explain myself a bit better


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Feb 21, 2020 at 17:02:38_

----

well the player would no longer be there for `player:messageSpecial()` calls to keep working, so that is expected - do the whole thing without the player, make it an area message. Pretty sure that's how retail handles the message while on the boat. 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 03:14:50_

----

still need to do one last update as there is another message spoken by NPC, please hold


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 19:46:22_

----

It's ready to be reviewed.
#pleaseBeGentle :rofl: 
Added Global for transport and boat messages for boat going to Al Zahbi


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 25, 2020 at 20:08:14_

----

GitHub seems to be having some issues detecting that kain has pushed changes to his branch; we're troubleshooting.
