**Labels:**

focus

merge ready



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 07:56:30_
_Originally opened as: project-topaz/topaz - Issue 361_

----

Changed BEGINNINGS to check correct AF1 global
Position of flans not accurate to retail as there's no captures for a full alliance fighting BCNM
renamed blank npc to Blu_Af2 so it's easier to tell what purpose it serves.
Immortal Flans do not have any special AI or move sets that differences them from other flans.
Thank you @Wiggo32  for capturing this quest.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 15:04:51_

----

Just for readability of the code could you add local getqueststatus(..., omens) and then add that to the check with has envelope.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 15:05:18_

----

Can use the above local here also then


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 15:07:03_

----

Can we change the charger to the quest name. Quest_Omens for all scripts? Thoughts?


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 15:11:16_

----

No need for this script as it has no info at this time


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 15:12:34_

----

Is this the only thing this npc in the game does is deal with blu quest?


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 16:32:52_

----

As far as i know it is only used for BLU AF2 quest. It's a blank npc on the floor. I can change it back but just named it before as on other PRs i submitted before i was asked to name it something related to what it is used for if its a blank or duplicate. (was just trying to avoid having to have discussions about it lol but again no issues changing it back just need confirmation :cat:  )


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 16:34:27_

----

Should I just delete it?  :scream_cat: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 16:34:57_

----

Charger? what does that mean? :sweat_smile: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 16:39:03_

----

For sure but the check for envelope is only being used once. From old PRs I have submitted on the other project that shall not be named, I was told to do that only if it is being used more than once for readability :cat: 

Tagging @ibm2431  for second opinion.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 16:39:49_

----

Tagging @TeoTwawki  for his insight in naming unnamed npcs :cat: 


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 16:48:25_

----

Sorry. Phone and auto correct. 
CharVar is what that was meant to be


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 16:50:25_

----

Just the readability part. Like just looking at the code I wouldn't know it's for this quest because the check is just an envelope ki that I don't know where it comes from


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 16:51:03_

----

Git delete yes. Unless you want to add something into the lua for the mob


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 17:47:49_

----

Sure we can, that will help with readability :cat:
I'll change it today


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Feb 20, 2020 at 20:24:52_

----

General rule was that you could assign a variable if it makes an unreadably long line shorter, but...

I feel bad for `player:hasCompletedQuest()`, everyone always forgets it exists.

(edit: This is in reference to assigning a local to quest status to shorten lines when checking it against QUEST_COMPLETE)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Feb 20, 2020 at 21:01:26_

----

it has no other uses, name doesn't much matter since blank in game except for being readable/recognizable to us humans.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 21, 2020 at 21:45:53_

----

You're squishing your commas~!

(In lots of places)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 21, 2020 at 21:46:59_

----

Empty Vessel is the BLU unlock quest


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 21, 2020 at 21:57:27_

----

Do me a favor and use `setLocalVar` and `getLocalVar` instead. I don't know if Waould is already using one if you've refused a divination (and if not, could you adjust that?), but `needToZone` should be phased out and eventually removed because it's "zone global" without a specified reason.

edit: Or, alternatively, be refactored to _take_ a reason and keep them straight.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 21, 2020 at 22:00:15_

----

Does the event handle denying the player if they don't have enough gil? Or do you need to?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 21, 2020 at 22:02:52_

----

Either way, be sure to check the player's gil!

I think delGil won't take gil below 0, but there's still the message below, and it's good to keep the habit~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 21, 2020 at 22:23:24_

----

So question: Do additional flans spawn in front of an inside player's eyes as more players enter the battlefield? Should we be checking party numbers as players enter, or when the battlefield is initially set up?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 21, 2020 at 22:39:00_

----

Would you happen to know if Waoud offers a divination after speaking with Lathuya? This startEvent here is correct based off of Wiggo's capture, but he didn't speak with Waoud again between Lathuya and completion. (I wouldn't have either.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 21, 2020 at 22:40:51_

----

Unless ships are involved. Don't ask me why.

(And I'd quip that "Omens" would be more clear than "Af2")

edit: This is in reference to names being whatever you want. Come on, GitHub.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Feb 22, 2020 at 02:34:00_

----

> ships

coz moving zone parts.

also certain bcnm entrance (divine might..) and door etc, expect the name to match wtf they reference.

those are usually (nut not always named the hex value of whatever Nth position they exist in zone, prefixed with a symbol like: `_07f` or matching the fourcc of their accompanying animation loop for objects that just sit and sparkle but can't be clicked on (holiday decorations will animate automatically if correctly named).

/endClientTrivia


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Feb 22, 2020 at 02:35:57_

----

even if it does, never trust the event - injections a thing


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 22:36:15_

----

Fixed. Will be pushing change soon.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 22:36:40_

----

fixed. Will push change soon.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 22:46:01_

----

Deleted. Pushing change soon.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 22:55:34_

----

changing it back to 15, until there's a confirmation that this blank npc is not used for something else (can't be proven as most of Aht Ughan quests/misisions are not scripted).

Change will be seen on the next push (in a few minutes)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 23:02:15_

----

added spaces to commas through the file (most of the file was previously scripted by someone else)
Push coming soon


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 23:03:15_

----

oh crap that's right. Thanks for mentioning it. Reverting this.
Push coming soon


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 23:05:08_

----

moved it to begginings, i knew somewhere else needed to be fixed lol


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 23:06:49_

----

@ibm2431  The event handles the check if they dont have enough gil.
No changes done here


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 23:08:02_

----

No need to check the player's Gil as the check is part of the params for it.

No changes made here.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 23:10:07_

----

Flans are really far away from the players eyes, They cannot be seen from @Wiggo32 's capture. If the logic on this needs to be changed a capture with 4+ people would be needed to verify how do they pop. 

Let me know if any change is needed here :cat: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 23:11:37_

----

I'm unsure if it offers divination afterwards. No capture was done for this part.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Feb 26, 2020 at 00:47:02_

----

created localvar WaoudNeedToZone.

Pushing changes soon


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Feb 26, 2020 at 01:01:46_

----

I'm positive that it doesn't have any missions involved nor any non blu quest.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Feb 26, 2020 at 01:11:20_

----

resolved


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Wednesday Feb 26, 2020 at 01:49:29_

----

there is a function player:needToZone()


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Feb 26, 2020 at 01:58:01_

----

ah thanks for the catch @KnowOne134 , let me murder it with kindness


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Feb 26, 2020 at 01:59:24_

----

@KnowOne134 i dont see it on my end. You might be looking at a wrong commit?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Feb 26, 2020 at 02:18:35_

----

just generally you don't want a var (in this case `local needToZone`) that has same name as a function. I recall ibm wanting to phase said function out.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Feb 26, 2020 at 02:27:26_

----

alright. Changing it @TeoTwawki  😸 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Feb 26, 2020 at 02:32:32_

----

changed to waoudNeedToZone :smile_cat: 

resolving comment


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 26, 2020 at 19:23:11_

----

I might prefer a:
```lua
if omens >= QUEST_ACCEPTED then
    if omensProgress == 3 then
        ...etc
    elseif omens == QUEST_COMPLETED then
        -- default dialogue
    end
end
```

instead of checking for quest progress by seeing if a character has a key item or not. In my view, key items are just shiny baubles that are given to you as a side effect of your actual progress (the variable) - not the progress themselves.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 26, 2020 at 20:36:27_

----

Packet injection is a thing 😉 

When params are sent to the client in a `startEvent`, those params only tell a client how to change the display of the event. The resulting "option" that's sent by the client to the server is entirely under the client's control, and there's no way to prevent / guarantee a client can _only_ send certain options back to the server after being given specific params by us.

So instead, we need to be sure to _never trust the client_ and always re-verify that "meaningful" options they send (ie: resulting in giving items, or in this case, deleting gil) are actually valid and that we're not being lied to.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 26, 2020 at 20:43:45_

----

While waiting for other players to enter a BCNM, players have a tendency to run up to the edge of the mobs' aggro range.

Going to tag @KnowOne134 and @cocosolos here as they do more work with BCNMs than me - how would we go about setting the number of flans based on registrant party size? Set a "local-but-not-lua-local" var for number of flans needed during `onBattlefieldRegister`? Can we spawn all the required flans at once in `onBattlefieldInitialise`?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Feb 26, 2020 at 22:25:33_

----

If you wanna use party/alliance size you can use onBattlefieldInitialise and get the party size with ```battlefield:getInitiator():getPartySize()``` or ```battlefield:getInitiator():getAllianceSize()```. Players do get locked out once one of the mobs is engaged so onBattlefieldEnter works as well, depends on how you want the mobs to spawn. For example if someone does an early pull before everyone enters, should they still be fighting the full amount of mobs?


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Mar 01, 2020 at 06:23:40_

----

ah got it, but in this case it's deleting gil so I would assume if someone is trying to cheat then they must be really dumb to cheat to delete their items lol.

If we are trying to avoid cheating then it would be for other stuff like unlocking this job without meeting the criteria.

I can go and change this and make all the onEventFinish to have the same requirements that started that event :cat: let me know.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Mar 01, 2020 at 07:17:53_

----

looks nicer :+1:  thank you @ibm2431  


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Mar 01, 2020 at 07:20:14_

----

after thinking it, you are right @ibm2431 :cat:  it makes sense to not be fooled by those cheaters that like to mess the game experience.

I only included it inside the OMENS onEventFinish. But did it fully on Lathuya. Maybe it could be a good project to be placed on the projects section :sunglasses: 


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 15:04:51_

----

Just for readability of the code could you add local getqueststatus(..., omens) and then add that to the check with has envelope.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 15:05:18_

----

Can use the above local here also then


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 15:07:03_

----

Can we change the charger to the quest name. Quest_Omens for all scripts? Thoughts?


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 15:11:16_

----

No need for this script as it has no info at this time


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 15:12:34_

----

Is this the only thing this npc in the game does is deal with blu quest?


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 16:32:52_

----

As far as i know it is only used for BLU AF2 quest. It's a blank npc on the floor. I can change it back but just named it before as on other PRs i submitted before i was asked to name it something related to what it is used for if its a blank or duplicate. (was just trying to avoid having to have discussions about it lol but again no issues changing it back just need confirmation :cat:  )


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 16:34:27_

----

Should I just delete it?  :scream_cat: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 16:34:57_

----

Charger? what does that mean? :sweat_smile: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 16:39:03_

----

For sure but the check for envelope is only being used once. From old PRs I have submitted on the other project that shall not be named, I was told to do that only if it is being used more than once for readability :cat: 

Tagging @ibm2431  for second opinion.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 16:39:49_

----

Tagging @TeoTwawki  for his insight in naming unnamed npcs :cat: 


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 16:48:25_

----

Sorry. Phone and auto correct. 
CharVar is what that was meant to be


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 16:50:25_

----

Just the readability part. Like just looking at the code I wouldn't know it's for this quest because the check is just an envelope ki that I don't know where it comes from


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 20, 2020 at 16:51:03_

----

Git delete yes. Unless you want to add something into the lua for the mob


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Feb 20, 2020 at 17:47:49_

----

Sure we can, that will help with readability :cat:
I'll change it today


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Feb 20, 2020 at 20:24:52_

----

General rule was that you could assign a variable if it makes an unreadably long line shorter, but...

I feel bad for `player:hasCompletedQuest()`, everyone always forgets it exists.

(edit: This is in reference to assigning a local to quest status to shorten lines when checking it against QUEST_COMPLETE)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Feb 20, 2020 at 21:01:26_

----

it has no other uses, name doesn't much matter since blank in game except for being readable/recognizable to us humans.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 21, 2020 at 21:45:53_

----

You're squishing your commas~!

(In lots of places)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 21, 2020 at 21:46:59_

----

Empty Vessel is the BLU unlock quest


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 21, 2020 at 21:57:27_

----

Do me a favor and use `setLocalVar` and `getLocalVar` instead. I don't know if Waould is already using one if you've refused a divination (and if not, could you adjust that?), but `needToZone` should be phased out and eventually removed because it's "zone global" without a specified reason.

edit: Or, alternatively, be refactored to _take_ a reason and keep them straight.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 21, 2020 at 22:00:15_

----

Does the event handle denying the player if they don't have enough gil? Or do you need to?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 21, 2020 at 22:02:52_

----

Either way, be sure to check the player's gil!

I think delGil won't take gil below 0, but there's still the message below, and it's good to keep the habit~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 21, 2020 at 22:23:24_

----

So question: Do additional flans spawn in front of an inside player's eyes as more players enter the battlefield? Should we be checking party numbers as players enter, or when the battlefield is initially set up?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 21, 2020 at 22:39:00_

----

Would you happen to know if Waoud offers a divination after speaking with Lathuya? This startEvent here is correct based off of Wiggo's capture, but he didn't speak with Waoud again between Lathuya and completion. (I wouldn't have either.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Feb 21, 2020 at 22:40:51_

----

Unless ships are involved. Don't ask me why.

(And I'd quip that "Omens" would be more clear than "Af2")

edit: This is in reference to names being whatever you want. Come on, GitHub.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Feb 22, 2020 at 02:34:00_

----

> ships

coz moving zone parts.

also certain bcnm entrance (divine might..) and door etc, expect the name to match wtf they reference.

those are usually (nut not always named the hex value of whatever Nth position they exist in zone, prefixed with a symbol like: `_07f` or matching the fourcc of their accompanying animation loop for objects that just sit and sparkle but can't be clicked on (holiday decorations will animate automatically if correctly named).

/endClientTrivia


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Feb 22, 2020 at 02:35:57_

----

even if it does, never trust the event - injections a thing


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 22:36:15_

----

Fixed. Will be pushing change soon.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 22:36:40_

----

fixed. Will push change soon.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 22:46:01_

----

Deleted. Pushing change soon.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 22:55:34_

----

changing it back to 15, until there's a confirmation that this blank npc is not used for something else (can't be proven as most of Aht Ughan quests/misisions are not scripted).

Change will be seen on the next push (in a few minutes)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 23:02:15_

----

added spaces to commas through the file (most of the file was previously scripted by someone else)
Push coming soon


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 23:03:15_

----

oh crap that's right. Thanks for mentioning it. Reverting this.
Push coming soon


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 23:05:08_

----

moved it to begginings, i knew somewhere else needed to be fixed lol


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 23:06:49_

----

@ibm2431  The event handles the check if they dont have enough gil.
No changes done here


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 23:08:02_

----

No need to check the player's Gil as the check is part of the params for it.

No changes made here.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 23:10:07_

----

Flans are really far away from the players eyes, They cannot be seen from @Wiggo32 's capture. If the logic on this needs to be changed a capture with 4+ people would be needed to verify how do they pop. 

Let me know if any change is needed here :cat: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Feb 25, 2020 at 23:11:37_

----

I'm unsure if it offers divination afterwards. No capture was done for this part.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Feb 26, 2020 at 00:47:02_

----

created localvar WaoudNeedToZone.

Pushing changes soon


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Feb 26, 2020 at 01:01:46_

----

I'm positive that it doesn't have any missions involved nor any non blu quest.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Feb 26, 2020 at 01:11:20_

----

resolved


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Wednesday Feb 26, 2020 at 01:49:29_

----

there is a function player:needToZone()


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Feb 26, 2020 at 01:58:01_

----

ah thanks for the catch @KnowOne134 , let me murder it with kindness


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Feb 26, 2020 at 01:59:24_

----

@KnowOne134 i dont see it on my end. You might be looking at a wrong commit?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Feb 26, 2020 at 02:18:35_

----

just generally you don't want a var (in this case `local needToZone`) that has same name as a function. I recall ibm wanting to phase said function out.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Feb 26, 2020 at 02:27:26_

----

alright. Changing it @TeoTwawki  😸 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Feb 26, 2020 at 02:32:32_

----

changed to waoudNeedToZone :smile_cat: 

resolving comment


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 26, 2020 at 19:23:11_

----

I might prefer a:
```lua
if omens >= QUEST_ACCEPTED then
    if omensProgress == 3 then
        ...etc
    elseif omens == QUEST_COMPLETED then
        -- default dialogue
    end
end
```

instead of checking for quest progress by seeing if a character has a key item or not. In my view, key items are just shiny baubles that are given to you as a side effect of your actual progress (the variable) - not the progress themselves.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 26, 2020 at 20:36:27_

----

Packet injection is a thing 😉 

When params are sent to the client in a `startEvent`, those params only tell a client how to change the display of the event. The resulting "option" that's sent by the client to the server is entirely under the client's control, and there's no way to prevent / guarantee a client can _only_ send certain options back to the server after being given specific params by us.

So instead, we need to be sure to _never trust the client_ and always re-verify that "meaningful" options they send (ie: resulting in giving items, or in this case, deleting gil) are actually valid and that we're not being lied to.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 26, 2020 at 20:43:45_

----

While waiting for other players to enter a BCNM, players have a tendency to run up to the edge of the mobs' aggro range.

Going to tag @KnowOne134 and @cocosolos here as they do more work with BCNMs than me - how would we go about setting the number of flans based on registrant party size? Set a "local-but-not-lua-local" var for number of flans needed during `onBattlefieldRegister`? Can we spawn all the required flans at once in `onBattlefieldInitialise`?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Feb 26, 2020 at 22:25:33_

----

If you wanna use party/alliance size you can use onBattlefieldInitialise and get the party size with ```battlefield:getInitiator():getPartySize()``` or ```battlefield:getInitiator():getAllianceSize()```. Players do get locked out once one of the mobs is engaged so onBattlefieldEnter works as well, depends on how you want the mobs to spawn. For example if someone does an early pull before everyone enters, should they still be fighting the full amount of mobs?


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Mar 01, 2020 at 06:23:40_

----

ah got it, but in this case it's deleting gil so I would assume if someone is trying to cheat then they must be really dumb to cheat to delete their items lol.

If we are trying to avoid cheating then it would be for other stuff like unlocking this job without meeting the criteria.

I can go and change this and make all the onEventFinish to have the same requirements that started that event :cat: let me know.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Mar 01, 2020 at 07:17:53_

----

looks nicer :+1:  thank you @ibm2431  


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Mar 01, 2020 at 07:20:14_

----

after thinking it, you are right @ibm2431 :cat:  it makes sense to not be fooled by those cheaters that like to mess the game experience.

I only included it inside the OMENS onEventFinish. But did it fully on Lathuya. Maybe it could be a good project to be placed on the projects section :sunglasses: 
