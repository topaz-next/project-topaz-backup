**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 05:12:24_
_Originally opened as: project-topaz/topaz - Issue 1517_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Welcome to Login Points =)

I am really bad at English so I will try to explain everything as best as I can =)

**settings.lua:**
4 globals added that are needed for selecting the correct table of prices and the start and duration of the campaign. This is also so other servers can choose which login campaign they want to use (if they want to modify it) or disable it.

**logincampaign.lua:**
tpz.logincampaign.table is to contain all tables for the logincampaign, I filled it with the campaign for NOVEMBER 2019 as I started using that one as an example.

**tpz.logincampaign.points:**
is in charge of checking if point was given in a day, otherwise it gives the correct quantity, along with correct message.

**tpz.logincampaign.check:**
Is to be used inside the Greeter_Moogle.lua when starting chat. This takes care of showing the correct list of items as needed along with their prices, this is needed as some campaigns dont carry as many items.

**tpz.logincampaign.eventupdate:**
handles all eventupdates for Greeter_Moogle.lua. This shows the correct table of items that were selected from the list shown on tpz.logincampaign.check. It also takes charge of deleting the currency when an item is selected.

### TODO:

- tpz.logincampaign.points(player) needs to be added to ALL game zones for `function afterZoneIn(player)`

- Only greeter moogle working is the one in Windurst Walls, other Greeter Moogles still need to be updated. 

- ~~textIDs need to be updated for logincampaign.lua (waiting on https://github.com/project-topaz/topaz/pull/1507 to be merged to release to update)~~

- after making a purchase, the price wont update it the menu

Can this have its own feature branch as the TODO list still needs to be done.

Thank you :cat: I'm looking forward on this as it will help with retail accuracy on how Trusts and Mounts are attained.

PS: I would love to get feedback on if login campaign should be enabled by default on the latest campaign table available, or disabled on default.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 07:42:34_

----

Don't forget I already suggested how to lay all of this out:
https://github.com/project-topaz/topaz/pull/1507#issuecomment-725968992

This file should be in `globals/events` -> `globals/events/login_campaign.lua`

```lua
tpz = tpz or {}
tpz.events = tpz.events or {}
tpz.events.loginCampaign = tpz.events.loginCampaign or {}
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 07:43:05_

----

Now that I see it, this could have a better name: "items", or "prizes" etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 07:46:20_

----

I think an exhaustive list of what's available each month is probably not a pattern we want to adopt. It would be very convenient to have it all mapped out and then operators don't have to do anything - but even SE has to take the server down to swap in/out NPCs and prizes for stuff.

I think a table of items, split by cost is fine and then operators can swap in and out what they want in their tables during their maintenance.

You _could_ also split this table out into `scripts/globals/events/login_campaign_data.lua` and add that file to the gitignore list, so operators can fiddle with it without risk of collisions.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 07:48:13_

----

> tpz.logincampaign.points(player) needs to be added to ALL game zones for function afterZoneIn(player)

Have you already tried putting this check in the global call:
https://github.com/project-topaz/topaz/blob/release/scripts/globals/player.lua#L188

This 100% **should not** be added to _every_ zone. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 07:48:54_

----

Newline at end of file please


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 07:50:35_

----

Please rename these calls to line up with how they're going to be called from their NPCs:
```lua
function onTrigger(player, npc)
    tpz.events.loginCampaign.onTrigger(player)
end

function onEventUpdate(player, csid, option)
    tpz.events.loginCampaign.onEventUpdate(player, csid, option)
end
```

etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 07:52:53_

----

I think for events, we can move all the settings into the event's script and have a single setting here: `ENABLE_LOGIN_CAMPAIGN = 1 # See scripts/globals/events/login_campaign.lua for more options`


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 07:53:47_

----

It doesn't really do anything, but this NPC doesn't need _all_ of this, just the login campaign script


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 17:09:41_

----

@zach2good  having issues adding it inside OnGameIn as player:messageSpecial cannot be shown until afterZoneIn

Tried adding afterZoneIn inside player.lua but hit a stump since i think it relies on being used only inside the zone.lua files inside the zones folder


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Nov 14, 2020 at 17:47:07_

----

Might need to fetch the ID file for the player's current zone


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 18:46:30_

----

changed it to "prizes" :cat: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 18:47:10_

----

moved it to `scripts/globals/events/login_campaign_data.lua` thank you @Kreidos  for the example from roe


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 18:48:11_

----

added :smile_cat: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 18:48:39_

----

renamed, thank you for the feedback :+1: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 18:49:01_

----

removed, still not done with Greeter_Moogle as there's still others missing.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 18:50:04_

----

change the location of the file. Thank you for the feedback :cat:  looks better that way now


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 20:22:06_

----

Hi @ibm2431  :cat: 

All the logic works great (points being added only once a day) `onGameIn` but any messages sent to the player won't show because the client isn't ready to display chat packets yet.

This is the same case if using `onZoneIn` inside Zone.lua, messages not showing there either. Instead it will have to be called using `afterZoneIn`

I cannot use `afterZoneIn` from inside player.lua.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Nov 14, 2020 at 20:23:12_

----

There is a packet timing issue, if the client gets the message before it thinks it is doesn't loading the zone (on the clients side) it will drop the message without placing it into the chat log. a similar issue exists with the change music packet. If that is delayed bay some amount either by other things taking time to execute before the server sends, or an intentional delay (via the evil `timer()` function) it will display just fine in onGameIn. ***This exact issue*** is why I was desiring an afterGameIn() to be added to player.lua awhile back. `timer()` is a buggy sob in many situations but would be less evil than doing this per zone.

Please note that the timing is not consistent and can vary based on what the client PC -or- the server were doing. Can be as short as 200ms on fast hardware with minimal traffic, or as long as 2000ms (2 full seconds). And note that timer does not like being handed any function that wasn't a binding so you need do all your logic then call the timer just for the message, or face potential errors (unless you wanna rewrite `timer()` too).

```
player:timer(2000, function (player) player:messageSpecial(ID.text.CARRIED_OVER_POINTS, 0, 1500) end)
```

Even tho I am demonstrating it, I despise using timer. Up to staff how they wanna handle the situation. 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 20:35:12_

----

moved to login_campaign.lua 
This looks awesome now, much cleaner =)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Saturday Nov 14, 2020 at 20:40:21_

----

Indeed, this timing issue is just a symptom of the deeper issue of how we handle certain packets; just blasting them any time regardless of whether the client is ready.

In this case, I wouldn't expect @kaincenteno to rework the message handling system or invent a whole new delayed `afterAfterZoneIn` function so the timer is the simplest most reasonable way to get around this one issue for now. :+1: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Nov 14, 2020 at 21:03:35_

----

Since we're not in the service of players, there's no rush to merge a PR.

We can do things properly.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Nov 14, 2020 at 21:11:08_

----

@Kreidos I didn't see anybody asking him to invent `afterAfterZoneIn`

there is no reason I for example, couldn't create `afterGameIn` for use on this pr. would not be the first time one pr has gotten an assist from another pr.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 21:25:18_

----

Please mark this PR as on hold, don't really wanna delete it as everything is almost ready :smile_cat: 

I'll add this PR to the issue that already exists of the packet timing issue as @TeoTwawki  explain above :cat: 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 07:42:34_

----

Don't forget I already suggested how to lay all of this out:
https://github.com/project-topaz/topaz/pull/1507#issuecomment-725968992

This file should be in `globals/events` -> `globals/events/login_campaign.lua`

```lua
tpz = tpz or {}
tpz.events = tpz.events or {}
tpz.events.loginCampaign = tpz.events.loginCampaign or {}
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 07:43:05_

----

Now that I see it, this could have a better name: "items", or "prizes" etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 07:46:20_

----

I think an exhaustive list of what's available each month is probably not a pattern we want to adopt. It would be very convenient to have it all mapped out and then operators don't have to do anything - but even SE has to take the server down to swap in/out NPCs and prizes for stuff.

I think a table of items, split by cost is fine and then operators can swap in and out what they want in their tables during their maintenance.

You _could_ also split this table out into `scripts/globals/events/login_campaign_data.lua` and add that file to the gitignore list, so operators can fiddle with it without risk of collisions.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 07:48:13_

----

> tpz.logincampaign.points(player) needs to be added to ALL game zones for function afterZoneIn(player)

Have you already tried putting this check in the global call:
https://github.com/project-topaz/topaz/blob/release/scripts/globals/player.lua#L188

This 100% **should not** be added to _every_ zone. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 07:48:54_

----

Newline at end of file please


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 07:50:35_

----

Please rename these calls to line up with how they're going to be called from their NPCs:
```lua
function onTrigger(player, npc)
    tpz.events.loginCampaign.onTrigger(player)
end

function onEventUpdate(player, csid, option)
    tpz.events.loginCampaign.onEventUpdate(player, csid, option)
end
```

etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 07:52:53_

----

I think for events, we can move all the settings into the event's script and have a single setting here: `ENABLE_LOGIN_CAMPAIGN = 1 # See scripts/globals/events/login_campaign.lua for more options`


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 07:53:47_

----

It doesn't really do anything, but this NPC doesn't need _all_ of this, just the login campaign script


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 17:09:41_

----

@zach2good  having issues adding it inside OnGameIn as player:messageSpecial cannot be shown until afterZoneIn

Tried adding afterZoneIn inside player.lua but hit a stump since i think it relies on being used only inside the zone.lua files inside the zones folder


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Nov 14, 2020 at 17:47:07_

----

Might need to fetch the ID file for the player's current zone


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 18:46:30_

----

changed it to "prizes" :cat: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 18:47:10_

----

moved it to `scripts/globals/events/login_campaign_data.lua` thank you @Kreidos  for the example from roe


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 18:48:11_

----

added :smile_cat: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 18:48:39_

----

renamed, thank you for the feedback :+1: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 18:49:01_

----

removed, still not done with Greeter_Moogle as there's still others missing.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 18:50:04_

----

change the location of the file. Thank you for the feedback :cat:  looks better that way now


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 20:22:06_

----

Hi @ibm2431  :cat: 

All the logic works great (points being added only once a day) `onGameIn` but any messages sent to the player won't show because the client isn't ready to display chat packets yet.

This is the same case if using `onZoneIn` inside Zone.lua, messages not showing there either. Instead it will have to be called using `afterZoneIn`

I cannot use `afterZoneIn` from inside player.lua.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Nov 14, 2020 at 20:23:12_

----

There is a packet timing issue, if the client gets the message before it thinks it is doesn't loading the zone (on the clients side) it will drop the message without placing it into the chat log. a similar issue exists with the change music packet. If that is delayed bay some amount either by other things taking time to execute before the server sends, or an intentional delay (via the evil `timer()` function) it will display just fine in onGameIn. ***This exact issue*** is why I was desiring an afterGameIn() to be added to player.lua awhile back. `timer()` is a buggy sob in many situations but would be less evil than doing this per zone.

Please note that the timing is not consistent and can vary based on what the client PC -or- the server were doing. Can be as short as 200ms on fast hardware with minimal traffic, or as long as 2000ms (2 full seconds). And note that timer does not like being handed any function that wasn't a binding so you need do all your logic then call the timer just for the message, or face potential errors (unless you wanna rewrite `timer()` too).

```
player:timer(2000, function (player) player:messageSpecial(ID.text.CARRIED_OVER_POINTS, 0, 1500) end)
```

Even tho I am demonstrating it, I despise using timer. Up to staff how they wanna handle the situation. 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 20:35:12_

----

moved to login_campaign.lua 
This looks awesome now, much cleaner =)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Saturday Nov 14, 2020 at 20:40:21_

----

Indeed, this timing issue is just a symptom of the deeper issue of how we handle certain packets; just blasting them any time regardless of whether the client is ready.

In this case, I wouldn't expect @kaincenteno to rework the message handling system or invent a whole new delayed `afterAfterZoneIn` function so the timer is the simplest most reasonable way to get around this one issue for now. :+1: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Nov 14, 2020 at 21:03:35_

----

Since we're not in the service of players, there's no rush to merge a PR.

We can do things properly.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Nov 14, 2020 at 21:11:08_

----

@Kreidos I didn't see anybody asking him to invent `afterAfterZoneIn`

there is no reason I for example, couldn't create `afterGameIn` for use on this pr. would not be the first time one pr has gotten an assist from another pr.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Nov 14, 2020 at 21:25:18_

----

Please mark this PR as on hold, don't really wanna delete it as everything is almost ready :smile_cat: 

I'll add this PR to the issue that already exists of the packet timing issue as @TeoTwawki  explain above :cat: 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 09:48:53_

----

Targetted to `feature/login-campaign`
