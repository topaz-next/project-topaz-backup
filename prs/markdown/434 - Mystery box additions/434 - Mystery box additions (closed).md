**Labels:**

focus

reviewed



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Sunday Mar 22, 2020 at 01:34:15_
_Originally opened as: project-topaz/topaz - Issue 434_

----

Adds a function to load vectors full of obtainable item ids from each mystery box dial on map init. Adds a function to select a random item id from one of those vectors, using the dial number as an argument. Updated Arbitrix to use this function and give out items, and hold onto an item until collected by the player when inventory is full.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 25, 2020 at 21:01:11_

----

Can shrink this option logic with the following:
```lua
if option == 4 then
    -- peek
else
    local dial = math.floor(option / 8)
    local option_type = option % 8
    local dial_used = 0
    local dial_cost = costs[dial]
    local dial_mask = false
    if dial >= 6 then
        dial_mask = dial - 6
        dial_used = player:getMaskBit(gobbieBoxUsed, dial_mask)
    end
    switch (option_type): caseof
        [1] = function()
            if dial_used then
                player:updateEvent(1, dial, 2) -- already used this dial
            elseif dailyTallyPoints >= dial_cost then
                itemid = player:selectDailyItem(dial)
                player:setCharVar("gobbieBoxHoldingItem", itemid)
                player:setCurrency("daily_tally", dailyTallyPoints - dial_cost)
                if dial_mask then
                    player:setMaskBit(gobbieBoxUsed, "gobbieBoxUsed", dial_mask, true)
                end
                player:updateEvent(itemid, dial, 0)
            else
                player:updateEvent(1, dial, 1) -- not enough points
            end
        end,
        [2] = function()
            if player:getFreeSlotsCount() == 0 then
                player:updateEvent(holdingItem, 0, 0, 1) -- inventory full, exit event
                player:messageSpecial(ID.text.ITEM_CANNOT_BE_OBTAINED + 2) -- generic "Cannot obtain the item."
            end
        end,
        [5] = function()
            if holdingItem > 0 and npcUtil.giveItem(player, holdingItem) then
                player:setCharVar("gobbieBoxHoldingItem", 0)
            end
            player:updateEvent(specialDialUsed, adoulinDialUsed, pictlogicaDialUsed, wantedDialUsed, 0, 0, hideOptionFlags, dailyTallyPoints)
        end,
    end
end
```

Will need a `costs` table somewhere. But in Arbitrix is okay - you don't need to globalize this just yet!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 25, 2020 at 21:11:52_

----

`npcUtil.giveItem` will handle the slot count and displaying unable to obtain for you:
```lua
if not npcUtil.giveItem(player, player:getCharVar("gobbieBoxHoldingItem") then
    player:setCharVar("gobbieBoxHoldingItem", 0)
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 25, 2020 at 21:39:14_

----

I'm leaning towards keeping all the logic for selection in a single place, so the binding just passes the Char and dial to `daily::` and returns the final result.

_Ideally_ we'd have the select daily util function be exposed to Lua instead of adding yet another binding to baseentity, but I don't feel strongly enough to _press_ that particular route. 😅 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Mar 25, 2020 at 21:47:08_

----

I actually started by putting the rerolling directly in daily::SelectItem, but it involved adding a loop for each dial case, which is why I moved it here.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Mar 25, 2020 at 21:48:19_

----

npcUtil.giveItem actually gives a different message than this. "Unable to obtain \<item\>." vs "Unable to obtain the item."


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Mar 25, 2020 at 21:50:57_

----

This looks a lot better. I kinda just threw this together to demonstrate the item selection, but I'll make these edits and make sure everything works right.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 25, 2020 at 21:55:08_

----

Oh right, the mystery box doesn't say what the item is, does it? Nevermind then!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 25, 2020 at 21:01:11_

----

Can shrink this option logic with the following:
```lua
if option == 4 then
    -- peek
else
    local dial = math.floor(option / 8)
    local option_type = option % 8
    local dial_used = 0
    local dial_cost = costs[dial]
    local dial_mask = false
    if dial >= 6 then
        dial_mask = dial - 6
        dial_used = player:getMaskBit(gobbieBoxUsed, dial_mask)
    end
    switch (option_type): caseof
        [1] = function()
            if dial_used then
                player:updateEvent(1, dial, 2) -- already used this dial
            elseif dailyTallyPoints >= dial_cost then
                itemid = player:selectDailyItem(dial)
                player:setCharVar("gobbieBoxHoldingItem", itemid)
                player:setCurrency("daily_tally", dailyTallyPoints - dial_cost)
                if dial_mask then
                    player:setMaskBit(gobbieBoxUsed, "gobbieBoxUsed", dial_mask, true)
                end
                player:updateEvent(itemid, dial, 0)
            else
                player:updateEvent(1, dial, 1) -- not enough points
            end
        end,
        [2] = function()
            if player:getFreeSlotsCount() == 0 then
                player:updateEvent(holdingItem, 0, 0, 1) -- inventory full, exit event
                player:messageSpecial(ID.text.ITEM_CANNOT_BE_OBTAINED + 2) -- generic "Cannot obtain the item."
            end
        end,
        [5] = function()
            if holdingItem > 0 and npcUtil.giveItem(player, holdingItem) then
                player:setCharVar("gobbieBoxHoldingItem", 0)
            end
            player:updateEvent(specialDialUsed, adoulinDialUsed, pictlogicaDialUsed, wantedDialUsed, 0, 0, hideOptionFlags, dailyTallyPoints)
        end,
    end
end
```

Will need a `costs` table somewhere. But in Arbitrix is okay - you don't need to globalize this just yet!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 25, 2020 at 21:11:52_

----

`npcUtil.giveItem` will handle the slot count and displaying unable to obtain for you:
```lua
if not npcUtil.giveItem(player, player:getCharVar("gobbieBoxHoldingItem") then
    player:setCharVar("gobbieBoxHoldingItem", 0)
end
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 25, 2020 at 21:39:14_

----

I'm leaning towards keeping all the logic for selection in a single place, so the binding just passes the Char and dial to `daily::` and returns the final result.

_Ideally_ we'd have the select daily util function be exposed to Lua instead of adding yet another binding to baseentity, but I don't feel strongly enough to _press_ that particular route. 😅 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Mar 25, 2020 at 21:47:08_

----

I actually started by putting the rerolling directly in daily::SelectItem, but it involved adding a loop for each dial case, which is why I moved it here.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Mar 25, 2020 at 21:48:19_

----

npcUtil.giveItem actually gives a different message than this. "Unable to obtain \<item\>." vs "Unable to obtain the item."


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Mar 25, 2020 at 21:50:57_

----

This looks a lot better. I kinda just threw this together to demonstrate the item selection, but I'll make these edits and make sure everything works right.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 25, 2020 at 21:55:08_

----

Oh right, the mystery box doesn't say what the item is, does it? Nevermind then!
