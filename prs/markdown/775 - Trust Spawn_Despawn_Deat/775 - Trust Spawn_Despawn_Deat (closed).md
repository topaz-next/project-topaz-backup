**Labels:**

approved

focus



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Friday Jun 26, 2020 at 11:25:33_
_Originally opened as: project-topaz/topaz - Issue 775_

----

Ended up completing this feature once I tracked down the required packet and the message offsets.

**Done:**
messageCombat and trust messages

Swapping out hardcoded values for spell table entries.

Swap out hard-coded trust ID values for tabled spellID values in these:

Table the system_messages used in trust.lua

Maybe rename getSeekingParty to isSeekingParty

Add timer for last time a player joined a party or when the party was formed, for the last trust error message

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 16:54:53_

----

since you renamed the paclket, maybe rename the table to match its new name?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 16:55:47_

----

I expect using the term "synergy" will be confusing once we have synergy craft skill work started.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 22:28:21_

----

OH! Ima dunce these are yellow system3 type aren't they, i mistook this as an enum for the combatMessage packet you did.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Jul 08, 2020 at 14:57:52_

----

Does this need to be here rather than msg.lua?, im only asking as we usually put these messages in msg.lua and call from that, and it seems that you allready call tpz.msg for messages.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Jul 08, 2020 at 17:51:17_

----

It doesn't _need_ to be here, but this is following the pattern from basic messages since everything has to flow through core to be able to have the right packet sent out


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Jul 08, 2020 at 20:31:45_

----

Ah ok, got ya, ok carry on lol


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Jul 08, 2020 at 20:33:21_

----

and wow totaly missed that MSGSYSTEM_MSGSYSTEM lol, glad you caught that


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 11:49:52_

----

I worry about starting message ID shifting. I don't know the last time it's happened on the low end, but I don't know if this trust global will be on the minds of people running text ID tools should it happen.

Would it be possible to define a very-first-starting-trust message ID in `msg`, and then calculate offsets based on that?
`local message_id = tpz.msg.combat.GLOBAL_TRUST_OFFSET + ((trust_id - x) * 100)`
The global would need to be adjusted if the _size_ of trust message blocks change, but they'd be a little more resistant if SE decides to throw a couple random messages before the trust block.

Variable naming could be a bit clearer - what's being passed in isn't a message ID, but a message offset. Complication in that you're also calculating a _trust_ offset. Maybe `trust_offset` + `message_offset`.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 11:55:47_

----

Are we certain the message selected is random? There's no priority system? I've done a lot of partying with ROV versions of The Princesses, and I remember them _always_ commenting about Iroha.

I don't know how far your retail character is, so I'll tag @project-topaz/researcher :
1. Summon Iroha II
2. Summon The Princesses II
3. See if The Princesses ever comment about each other versus Iroha


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 11:56:12_

----

👍 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 12:00:53_

----

"Target" or "Speaker"?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 12:06:40_

----

You're not using these enums in core~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 12:09:57_

----

I don't remember, but are we already blocking party invites to players if trusts are present? (Either a party leader using trusts sending an invite to a free person, or a player-only party sending an invite to someone with trusts out)

Not a requirement for this PR if we're not; just making sure we don't forget any loose threads~


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 11, 2020 at 17:57:00_

----

if its a per zone thing (as in, its in the string dats of each zone, even if they all have the same ID now) it should really be in the IDs.lua anyway just for this reason. if its not in the zones dat, we generally won't need to worry about it shifting. (I'm still in favor of offsets where we can, vs enuming all the stuff and things, just FYI))

I most zones we have several IDs that are generally the same in every zone - we still IDs.lua them because they will eventually get shifted,
![image](https://user-images.githubusercontent.com/6871475/87230484-5e15bd00-c37e-11ea-9695-ff97cd618c2d.png)



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Jul 12, 2020 at 12:52:31_

----

_Seems_ random...


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Jul 12, 2020 at 12:53:14_

----

I've decided to remove them (for now), because I don't want to chase down all of the other hard coded uses of messageSystem...


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Jul 12, 2020 at 12:54:36_

----

Not really, on the core end everything is pretty much unlimited and the only blocking happens on the lua side. The way trusts are handled in and around a player/mixed party is all sorts of wrong. That'll have to be a whole research and dev leg on its own before release :(


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jul 12, 2020 at 16:24:13_

----

~~I believe there is a priority system of sorts based on what order they were summoned in on retail, but someone will need to confirm that~~ _Vidya says I'm wrong_


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 16:54:53_

----

since you renamed the paclket, maybe rename the table to match its new name?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 16:55:47_

----

I expect using the term "synergy" will be confusing once we have synergy craft skill work started.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 22:28:21_

----

OH! Ima dunce these are yellow system3 type aren't they, i mistook this as an enum for the combatMessage packet you did.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Jul 08, 2020 at 14:57:52_

----

Does this need to be here rather than msg.lua?, im only asking as we usually put these messages in msg.lua and call from that, and it seems that you allready call tpz.msg for messages.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Jul 08, 2020 at 17:51:17_

----

It doesn't _need_ to be here, but this is following the pattern from basic messages since everything has to flow through core to be able to have the right packet sent out


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Jul 08, 2020 at 20:31:45_

----

Ah ok, got ya, ok carry on lol


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Jul 08, 2020 at 20:33:21_

----

and wow totaly missed that MSGSYSTEM_MSGSYSTEM lol, glad you caught that


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 11:49:52_

----

I worry about starting message ID shifting. I don't know the last time it's happened on the low end, but I don't know if this trust global will be on the minds of people running text ID tools should it happen.

Would it be possible to define a very-first-starting-trust message ID in `msg`, and then calculate offsets based on that?
`local message_id = tpz.msg.combat.GLOBAL_TRUST_OFFSET + ((trust_id - x) * 100)`
The global would need to be adjusted if the _size_ of trust message blocks change, but they'd be a little more resistant if SE decides to throw a couple random messages before the trust block.

Variable naming could be a bit clearer - what's being passed in isn't a message ID, but a message offset. Complication in that you're also calculating a _trust_ offset. Maybe `trust_offset` + `message_offset`.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 11:55:47_

----

Are we certain the message selected is random? There's no priority system? I've done a lot of partying with ROV versions of The Princesses, and I remember them _always_ commenting about Iroha.

I don't know how far your retail character is, so I'll tag @project-topaz/researcher :
1. Summon Iroha II
2. Summon The Princesses II
3. See if The Princesses ever comment about each other versus Iroha


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 11:56:12_

----

👍 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 12:00:53_

----

"Target" or "Speaker"?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 12:06:40_

----

You're not using these enums in core~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 11, 2020 at 12:09:57_

----

I don't remember, but are we already blocking party invites to players if trusts are present? (Either a party leader using trusts sending an invite to a free person, or a player-only party sending an invite to someone with trusts out)

Not a requirement for this PR if we're not; just making sure we don't forget any loose threads~


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 11, 2020 at 17:57:00_

----

if its a per zone thing (as in, its in the string dats of each zone, even if they all have the same ID now) it should really be in the IDs.lua anyway just for this reason. if its not in the zones dat, we generally won't need to worry about it shifting. (I'm still in favor of offsets where we can, vs enuming all the stuff and things, just FYI))

I most zones we have several IDs that are generally the same in every zone - we still IDs.lua them because they will eventually get shifted,
![image](https://user-images.githubusercontent.com/6871475/87230484-5e15bd00-c37e-11ea-9695-ff97cd618c2d.png)



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Jul 12, 2020 at 12:52:31_

----

_Seems_ random...


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Jul 12, 2020 at 12:53:14_

----

I've decided to remove them (for now), because I don't want to chase down all of the other hard coded uses of messageSystem...


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Jul 12, 2020 at 12:54:36_

----

Not really, on the core end everything is pretty much unlimited and the only blocking happens on the lua side. The way trusts are handled in and around a player/mixed party is all sorts of wrong. That'll have to be a whole research and dev leg on its own before release :(


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jul 12, 2020 at 16:24:13_

----

~~I believe there is a priority system of sorts based on what order they were summoned in on retail, but someone will need to confirm that~~ _Vidya says I'm wrong_


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jun 26, 2020 at 12:16:15_

----

might be worth renaming that packet/message while its still young: 
https://github.com/project-topaz/topaz/search?q=CMessageDebugPacket&unscoped_q=CMessageDebugPacket
