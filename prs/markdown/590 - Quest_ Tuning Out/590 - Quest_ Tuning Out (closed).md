**Labels:**

merge ready



<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [InoUno](https://github.com/InoUno)**
_Wednesday May 06, 2020 at 19:21:32_
_Originally opened as: project-topaz/topaz - Issue 590_

----

Next quest after the Tuning In quest, which was added in: #564

[Wiki page](https://ffxiclopedia.fandom.com/wiki/Tuning_Out)
[Test Video](https://www.youtube.com/watch?v=Kosx845G82o)

Notes:
* I tried the fight as a 75WAR to see how the difficult the Nasus are, and it matched the testimonials on the wiki page pretty well.
* ~~The Nasus positions I've added are just a semi-circle around the QM. I haven't been able to try the quest in retail, so I don't know how they spawn there.~~
* I took inspiration from other places in the codebase with regards to the progress of the quest and kill count on the Nasus. Is there a better approach to this now, or is this the way to go?

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 10:52:20_

----

Could be wrong, but I believe that once this fires, the mob will always despawn at that the end of the timer, even if it re-engages later.

We do have a mobMod for idle despawn, usage looks something like this:
```lua
-- mobs_script.lua
function onMobInitialize(mob)
    mob:setMobMod(tpz.mobMod.IDLE_DESPAWN, 120)
end
```
And it'll handle idle despawn for you automagically after that, without you having to worry about engage/disengage.


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Sunday May 10, 2020 at 17:21:44_

----

Nice, I'll use that instead then.
The code I had was something I found on another mob, and just reused it expecting it to be what I needed.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday May 10, 2020 at 19:53:39_

----

This ID looks like it should be `7820`. Think everything else looks good though.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 10, 2020 at 20:04:11_

----

Oh, on closer examination of the ID file, could you move this `17281590` definition up a bit to be in numerical order after the `BLUE_RAFFLESIA_OFFSET = 17281586,` offset?


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Sunday May 10, 2020 at 20:04:59_

----

Small test: 
![image](https://user-images.githubusercontent.com/774909/81509332-12a54b00-930a-11ea-8345-8e99a16c3da8.png)

I guess the higher bit is used for something that hides the NPC who's saying the message?
(`40588 - 2^15 = 7820`)



----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Sunday May 10, 2020 at 20:05:19_

----

In the capture, it doesn't have the `???: ` infront.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday May 10, 2020 at 20:07:40_

----

Don't pass `true` in the call to `messageText`, that's what's showing the NPC name.

Edit: Pass `false` instead, it defaults to `true`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 10, 2020 at 20:13:13_

----

[The messageText packet when called with `false` actually adds that offset you've found to the passed-in messageID to set that higher bit.](https://github.com/project-topaz/topaz/blob/release/src/map/packets/message_text.cpp#L36-L38)


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Sunday May 10, 2020 at 20:15:09_

----

Aha, interesting. Will change ID to the lower one and pass `false` then.

Question, where did you find the 7820 ID?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday May 10, 2020 at 20:16:57_

----

[POLUtils](https://github.com/Windower/POLUtils)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 10:52:20_

----

Could be wrong, but I believe that once this fires, the mob will always despawn at that the end of the timer, even if it re-engages later.

We do have a mobMod for idle despawn, usage looks something like this:
```lua
-- mobs_script.lua
function onMobInitialize(mob)
    mob:setMobMod(tpz.mobMod.IDLE_DESPAWN, 120)
end
```
And it'll handle idle despawn for you automagically after that, without you having to worry about engage/disengage.


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Sunday May 10, 2020 at 17:21:44_

----

Nice, I'll use that instead then.
The code I had was something I found on another mob, and just reused it expecting it to be what I needed.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday May 10, 2020 at 19:53:39_

----

This ID looks like it should be `7820`. Think everything else looks good though.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 10, 2020 at 20:04:11_

----

Oh, on closer examination of the ID file, could you move this `17281590` definition up a bit to be in numerical order after the `BLUE_RAFFLESIA_OFFSET = 17281586,` offset?


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Sunday May 10, 2020 at 20:04:59_

----

Small test: 
![image](https://user-images.githubusercontent.com/774909/81509332-12a54b00-930a-11ea-8345-8e99a16c3da8.png)

I guess the higher bit is used for something that hides the NPC who's saying the message?
(`40588 - 2^15 = 7820`)



----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Sunday May 10, 2020 at 20:05:19_

----

In the capture, it doesn't have the `???: ` infront.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday May 10, 2020 at 20:07:40_

----

Don't pass `true` in the call to `messageText`, that's what's showing the NPC name.

Edit: Pass `false` instead, it defaults to `true`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 10, 2020 at 20:13:13_

----

[The messageText packet when called with `false` actually adds that offset you've found to the passed-in messageID to set that higher bit.](https://github.com/project-topaz/topaz/blob/release/src/map/packets/message_text.cpp#L36-L38)


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Sunday May 10, 2020 at 20:15:09_

----

Aha, interesting. Will change ID to the lower one and pass `false` then.

Question, where did you find the 7820 ID?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday May 10, 2020 at 20:16:57_

----

[POLUtils](https://github.com/Windower/POLUtils)


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday May 06, 2020 at 19:53:19_

----

Just a quick initial comment, you can find captured data for the quest here to adjust the spawn points:
https://discordapp.com/channels/443544205206355968/446470173008855050/644777354165616653
and you can make requests for future captures so that you have exact data


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Wednesday May 06, 2020 at 20:03:21_

----

Cool, didn't know that existed. Will check it out and change the PR accordingly


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 10:58:52_

----

I'll go ahead and label this as WIP since you intend to check out the capture. Feel free to yell at us if we fail to notice you've added new commits!


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Sunday May 10, 2020 at 17:57:55_

----

Changes are in.

I noticed while looking at the capture that some of the IDs don't match up with current server/client IDs. I'm assuming this is because there's been updates since the capture was done, that has moved/changed some of these?

* The QM has ID 172815589 in the capture, but in topaz the QM in the same spot has ID 17281590. The one with ID *89 does exist on topaz, but it's a bit further from the edge and is not visible by default. 
* In the capture, the message "A swarm appeared" has ID 40593, while in the latest retail client it has ID 40588 (which I've added to this PR).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 10, 2020 at 19:33:44_

----

Yeah, client updates will sometimes shift both NPC IDs _and_ Message IDs! So sometimes if a capture is older the IDs may not align with what the current client uses.


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Sunday May 10, 2020 at 20:26:47_

----

ID changes are in.
