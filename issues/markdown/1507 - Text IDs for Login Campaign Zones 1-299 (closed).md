**Labels:**

reviewed



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Nov 12, 2020 at 08:29:26_
_Originally opened as: project-topaz/topaz - Issue 1507_

----

![image](https://user-images.githubusercontent.com/26943220/98914927-19aa4300-247e-11eb-8c59-98df61e3f563.png)


This has bee verified with November Release
Only 3 IDs were added per zones in preparation for Login Campaign.
Another PR will be submitted once this one is approved to complete
all of the IDs for the missing zones

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits (no tested everysingle one but have extracted them using polutils)




----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Nov 12, 2020 at 09:04:09_

----

Just to explain a bit. These 3 IDs are needed to show the greeting for the campaign and if there's points bring carried over from last month. Then afterwards it shows the daily points being added. Calling it a night now but will open a new PR with the zones missing tomorrow =)

I hope I can finish this before Thanksgiving so it could be a nice gift to the community =)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Nov 12, 2020 at 09:50:10_

----

To make sure everyone is on the same page going forward, this is how I was imagining login campaign would work:

**New file:** `scripts/globals/events/login_campaign.lua`
**Defines:** `tpz.events.loginCampaign`
**Defines:** `tpz.events.loginCampaign.onGameIn(player)`

Called here, or similar:
https://github.com/project-topaz/topaz/blob/release/scripts/globals/player.lua#L188

Since if you're playing, and midnight passes, then you zone: you get credit for the login campaign.

```lua
tpz.events.loginCampaign.isCampaignActive() = function 
    -- return date == validLoginCampaignDates etc.
    -- return true -- manually changes by operators
end

tpz.events.loginCampaign.onGameIn(player) = function 
    if not tpz.events.loginCampaign.isCampaignActive() then
        return
    end

    ...
end
```

Once all of that is done, you have pretty free reign for how to lay out `login_campaign.lua`.
- I would recommend a function at the top something like `tpz.events.loginCampaign.isCampaignActive()` that people can hardcode as true or false, or put in date range checks, or whatever. 
- You could be storing "have I gotten my prize today" as a charVar of getNextMidnight (or whatever it is), and then check `currentTime >=  getNextMidnight`
- Remember there is some funky carry-over logic with points: `NOTE: Campaign points expire after the end of the redeem period for each campaign. Up to 1500 points may be transferred to the next month, but anything further is lost.`
- After a quick look, they look like they run for 21-22 days, I don't think you need to build any calendar logic for this, leave that for people to fill out `isCampaignActive` with, but you _will_ need to consider the transition between campaign off, campaign on and back to campaign off. 
- I have no strong opinions on how/where the prizes should be stored. You _can_ see that each campaign is _mostly_ the same year to year: https://www.bg-wiki.com/bg/Repeat_Login_Campaign/Past_Login_Campaign_Rewards, with certain categories coming and going, but remaining mostly the same. Making it as modular as possible would be best:
```lua
local allYearPrizes = { ... }
local cipherPrizes = { ... }
local nmPopItemPrizes = { ... }

local prizeTable =
{
    [0]  =  { allYearPrizes, cipherPrizes, nmPopItemPrizes }, -- Jan
    [1]  =  { allYearPrizes, nmPopItemPrizes }, -- Feb
    [2]  =  { allYearPrizes, cipherPrizes }, -- Mar
}

player:startEvent(cutscene, displayOptions(prizeTable [month]))
```

- I imagine this is a thing people would want to customize, so I'm OK with _well laid out and commented_ lua tables inside `scripts/globals/events/login_campaign.lua`, but @ibm2431 and @TeoTwawki probably have different opinions to me. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Nov 12, 2020 at 12:48:25_

----

I'm guessing Item table for the moogle will likely be easiest to handle as sub-tables per point cost category or just be tables per cost category, but tabled items are fine whatever way fits with the cs event flow. 

And the give player x at login can probably have a table of which campaign gives what stuff (like special gobdial keys, adjur dial keys, mog pells) can be tabled similarly to Zach's example.

I don't think anything else will need a table and the logic flow Zach laid out sounds fine to me. Might even be small enough to have just been a local function at the top of player.lua but I guess the item tables could be large enough to warrant that new global.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Nov 12, 2020 at 12:50:17_

----

I have one sole request here: amend the commit message to say text ids - these aren't zone ids, and reading the history looking for one when you see the other will cause future folks to be mislead

this can be done at merge time via squash


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Nov 12, 2020 at 13:04:34_

----

Personally, I'd like us to start moving towards lua packages, so the fewer local functions the more sane we'll be later (I'm currently going _insane_ with these mob scripts).

It may be beneficial to have prizes as their own file, separate from the campaign package/methods. Unless retail phoned it in, I don't think any two login campaigns are _exactly_ the same item-for-item (even for same month). Server operators will be editing it regardless. So .gitignore might be desired in this case.

Again, I'm not sure if login campaigns are repeated on a monthly basis from one year to the next. If they aren't, then defining a year's worth of login campaigns isn't necessary on our end.
<https://www.bg-wiki.com/bg/Repeat_Login_Campaign/Past_Login_Campaign_Rewards#October_2019_-_Campaign_No._76>
<https://www.bg-wiki.com/bg/Repeat_Login_Campaign/Past_Login_Campaign_Rewards#October_2020_-_Campaign_No.88>


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Nov 12, 2020 at 13:06:29_

----

As an additional thought: Going forward I do _not_ want to see PRs every month for the most recent login campaign.

I don't know how tied into the monthly client they are.


----
<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Thursday Nov 12, 2020 at 13:58:22_

----

> As an additional thought: Going forward I do _not_ want to see PRs every month for the most recent login campaign.
> 
> I don't know how tied into the monthly client they are.

Rewards definitely rotate monthly, and are inconsistent annually for the same month (Mounts/etc). I'm not sure there's another way to stay current unless the CS reads fixed values from the client like you suggest.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Nov 12, 2020 at 14:06:36_

----

It'll be pretty safe to make "base" collections of items per-cost and have those available, and then leave it up to server operators to set their own campaign times and which goodies are available. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Nov 12, 2020 at 14:44:44_

----

> 
> 
> It'll be pretty safe to make "base" collections of items per-cost and have those available, and then leave it up to server operators to set their own campaign times and which goodies are available.

This. 1000x this. Make it easy to tweak by owner and let them have at it.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Nov 12, 2020 at 15:38:26_

----

Hi everyone thank you for your feedback. <3

I have already written the basics for the greeter moogle displaying items, but it's out of scope for this PR. I will be pushing the actual logic of it tonight as I'm trying to do this in small batches for easy reviewing =)

I'll fix the double space and change the name in the next 5 minutes and the title of it as request by @zach2good  and @TeoTwawki 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Nov 12, 2020 at 15:40:36_

----

My concern is that I have a vague recollection of Zynjec once saying that the monthly items were client side and couldn't be set arbitrarily.

I'm fine with some base examples, and perhaps documentation of how to update prizes, but I don't want us to be responsible for yet another thing to update and maintain just for the sake of downstream server's player retention rates.

"This item is out of my server's era, how do I remove it from the menu?"
"I tried to learn the new mount this month but my server crashed, how fix?"
"I purchased this item but got something else, what do I do? I last updated my client a year ago."
"This new item that just got added doesn't have a model ID!"

We're already blessed beyond what's deserved to have Wren consistently update IDs so that _the game works_. If rewards _are_ tied to client version, I'd rather keep Pandora's box firmly in the court of server operators.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Nov 12, 2020 at 15:49:28_

----

> My concern is that I have a vague recollection of Zynjec once saying that the monthly items were client side and couldn't be set arbitrarily.
> 
> I'm fine with some base examples, and perhaps documentation of how to update prizes, but I don't want us to be responsible for yet another thing to update and maintain just for the sake of downstream server's player retention rates.
> 
> "This item is out of my server's era, how do I remove it from the menu?"
> "I tried to learn the new mount this month but my server crashed, how fix?"
> "I purchased this item but got something else, what do I do? I last updated my client a year ago."
> "This new item that just got added doesn't have a model ID!"
> 
> We're already blessed beyond what's deserved to have Wren consistently update IDs so that _the game works_. If rewards _are_ tied to client version, I'd rather keep Pandora's box firmly in the court of server operators.

Dont worry IBM <3 prizes are NOT hardcoded to the client, that was my first assumtion but thank G-d i was wrong lol.
It's an easy table that can be updated. Once that PR gets put in I'll write down about it. 

I have already thought ahead since I know people want the oldschool experience of a switch to not enable it so people can just ignore it's existance or the existance of the login points =) (#gimmeMyEraBack lol)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Nov 12, 2020 at 16:13:26_

----

fixed @TeoTwawki  and @zach2good 

Thank you for reviewing this. Looking forward on submitting more today :cat: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Nov 13, 2020 at 06:47:57_

----

Updated for all 299 zones =)

I also created the folder for Maquette_Abdhaljs-Legion_B (it is refer to in zone_settings but the folder containing the zone.lua and IDs.lua didn't exist, only populated with the known values for login points)

@wrenffxi  can you please give this a peek  to see if any change is needed <3 I exported all zones using the November client with polutil mass extractor (Thank you @TeoTwawki  for guidance since there was no documentation handy T_T) .

Thank you everyone for your feedback =D


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 12:43:00_

----

Since we have `feature/login-campaign` now, I've retargetted this to that branch. 
