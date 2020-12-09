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
_Saturday Nov 14, 2020 at 09:48:53_

----

Targetted to `feature/login-campaign`
