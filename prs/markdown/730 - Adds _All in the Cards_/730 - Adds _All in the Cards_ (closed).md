**Labels:**

reviewed



<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Monday Jun 15, 2020 at 19:43:06_
_Originally opened as: project-topaz/topaz - Issue 730_

----

Adds "All in the Cards" repeatable quest to Chululu to help increase server supply of Tarut Cards used in the "Collect Taru Cards" pre-req quest for Sleepga II quest line."

Currently setup to require "All in the Cards" and "Rubbish Day" to be completed first.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 04:42:08_

----

Should probably check `>= QUEST_ACCEPTED` since this is repeatable.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 04:46:41_

----

Does this actually get removed from your completed quests if you start it again?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 04:55:32_

----

```lua
if npcUtil.completeQuest(player, JEUNO, ALL_IN_THE_CARDS, {
        gil = 600,
        title = tpz.title.CARD_COLLECTOR,
        var = {"AllInTheCards_date"} })
then
    trade:confirm()
```


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 05:01:14_

----

```lua
if npcUtil.tradeHas(trade, {558, 559, 561, 562}, true) then
    player:startEvent(10114) -- Finish quest "All in the Cards"
end
````


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 05:07:51_

----

CSIDs 10110, 10113, and 10112 can probably all put into the same block
```lua
if (csid == 10110 or csid == 10112 or csid == 10113) and option == 0 then
--or--
if csid == 10112 or ((csid == 10110 or csid == 10113) and option == 0) then
```


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 05:09:58_

----

Change to `getMidnight()` as the charvar then you can get rid of `realday`.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 05:10:21_

----

If you use `getMidnight()` as the charvar, you can just do this:
```lua
os.time() < cdate -- need to wait till jp midnight
os.time() >= cdate -- good to complete
```


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 05:11:50_

----

```lua
if npcUtil.giveItem(player, {{card, 5}}) then
    player:setCharVar("AllInTheCards_date", getMidnight())
end
```


----
<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Sunday Jun 28, 2020 at 17:27:16_

----

Yes, I believe it does. Was the only method I knew of allowing it to be repeatable. Rookie things, right?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 28, 2020 at 17:29:48_

----

repeatables normally don't delete. they stay in the completed list till activated again and jump straight to active.


----
<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Sunday Jun 28, 2020 at 17:46:15_

----

The More You Know™, the less ghetto your PRs are. :P


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Jul 06, 2020 at 02:06:27_

----

This will need to check that AllInTheCards >= QUEST_ACCEPTED for people repeating the quest. Something like:
```lua
elseif AllInTheCards >= QUEST_ACCEPTED then
    if cdate >= os.time() then
        player:startEvent(10111) 
    elseif cdate == 0 then
        player:startEvent(10113)
    elseif cdate < os.time() then
        player:startEvent(10112) 
    end
```
Once a quest is marked as complete it stays that way unless it's manually deleted. Adding the quest again doesn't set it back to accepted. Once you complete the quest, it will always give you cs 10113 and never continue to the stuff past this block. I'm not sure how this quest is supposed to progress, but you will probably need to add a localvar to track whether the player has denied this quest/timer isn't up yet so that they can talk again and get the next quest dialogue.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Jul 06, 2020 at 02:08:52_

----

You can get rid of this:
```lua
        if (player:getFreeSlotsCount() == 0) then
            player:messageSpecial(ID.text.ITEM_CANNOT_BE_OBTAINED,13083);
        else
```
and just have the npcUtil.completeQuest.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jul 26, 2020 at 20:02:13_

----

Remove the "end" right before here and use `elseif` - the only reason to use two separate if/end blocks is if both things can execute, which here that is not the case.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jul 26, 2020 at 20:17:10_

----

indentation went a little odd around here due to tabs.


----
<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Sunday Jul 26, 2020 at 20:31:18_

----

Weird how that got formatted. Silly me, assuming EditorConfig took care of it all. On my end, all lined up. 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Jul 26, 2020 at 20:34:20_

----

May be some leftover tabs in the file, and it's lining up in your editor because the "indent space" for a tab is set to be equal width to four actual spaces. End result is it looks okay on your screen, but if that tab space amount is different on a different display (ie: here on GitHub) it'll no longer line up.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jul 29, 2020 at 20:55:01_

----

I think the only other issue I see is there is nothing in onEventFinish that sets `Cardstemp` for this CS, so after they accept the quest but before they complete it, while they're waiting, the other quests aren't accessible. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 29, 2020 at 21:02:35_

----

> Silly me, assuming EditorConfig took care of it all. 

it actually should have. dunno why it didn't.


----
<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Wednesday Aug 05, 2020 at 13:36:20_

----

Change made,  coco


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 04:42:08_

----

Should probably check `>= QUEST_ACCEPTED` since this is repeatable.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 04:46:41_

----

Does this actually get removed from your completed quests if you start it again?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 04:55:32_

----

```lua
if npcUtil.completeQuest(player, JEUNO, ALL_IN_THE_CARDS, {
        gil = 600,
        title = tpz.title.CARD_COLLECTOR,
        var = {"AllInTheCards_date"} })
then
    trade:confirm()
```


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 05:01:14_

----

```lua
if npcUtil.tradeHas(trade, {558, 559, 561, 562}, true) then
    player:startEvent(10114) -- Finish quest "All in the Cards"
end
````


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 05:07:51_

----

CSIDs 10110, 10113, and 10112 can probably all put into the same block
```lua
if (csid == 10110 or csid == 10112 or csid == 10113) and option == 0 then
--or--
if csid == 10112 or ((csid == 10110 or csid == 10113) and option == 0) then
```


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 05:09:58_

----

Change to `getMidnight()` as the charvar then you can get rid of `realday`.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 05:10:21_

----

If you use `getMidnight()` as the charvar, you can just do this:
```lua
os.time() < cdate -- need to wait till jp midnight
os.time() >= cdate -- good to complete
```


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jun 21, 2020 at 05:11:50_

----

```lua
if npcUtil.giveItem(player, {{card, 5}}) then
    player:setCharVar("AllInTheCards_date", getMidnight())
end
```


----
<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Sunday Jun 28, 2020 at 17:27:16_

----

Yes, I believe it does. Was the only method I knew of allowing it to be repeatable. Rookie things, right?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 28, 2020 at 17:29:48_

----

repeatables normally don't delete. they stay in the completed list till activated again and jump straight to active.


----
<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Sunday Jun 28, 2020 at 17:46:15_

----

The More You Know™, the less ghetto your PRs are. :P


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Jul 06, 2020 at 02:06:27_

----

This will need to check that AllInTheCards >= QUEST_ACCEPTED for people repeating the quest. Something like:
```lua
elseif AllInTheCards >= QUEST_ACCEPTED then
    if cdate >= os.time() then
        player:startEvent(10111) 
    elseif cdate == 0 then
        player:startEvent(10113)
    elseif cdate < os.time() then
        player:startEvent(10112) 
    end
```
Once a quest is marked as complete it stays that way unless it's manually deleted. Adding the quest again doesn't set it back to accepted. Once you complete the quest, it will always give you cs 10113 and never continue to the stuff past this block. I'm not sure how this quest is supposed to progress, but you will probably need to add a localvar to track whether the player has denied this quest/timer isn't up yet so that they can talk again and get the next quest dialogue.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Monday Jul 06, 2020 at 02:08:52_

----

You can get rid of this:
```lua
        if (player:getFreeSlotsCount() == 0) then
            player:messageSpecial(ID.text.ITEM_CANNOT_BE_OBTAINED,13083);
        else
```
and just have the npcUtil.completeQuest.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jul 26, 2020 at 20:02:13_

----

Remove the "end" right before here and use `elseif` - the only reason to use two separate if/end blocks is if both things can execute, which here that is not the case.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jul 26, 2020 at 20:17:10_

----

indentation went a little odd around here due to tabs.


----
<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Sunday Jul 26, 2020 at 20:31:18_

----

Weird how that got formatted. Silly me, assuming EditorConfig took care of it all. On my end, all lined up. 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Jul 26, 2020 at 20:34:20_

----

May be some leftover tabs in the file, and it's lining up in your editor because the "indent space" for a tab is set to be equal width to four actual spaces. End result is it looks okay on your screen, but if that tab space amount is different on a different display (ie: here on GitHub) it'll no longer line up.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jul 29, 2020 at 20:55:01_

----

I think the only other issue I see is there is nothing in onEventFinish that sets `Cardstemp` for this CS, so after they accept the quest but before they complete it, while they're waiting, the other quests aren't accessible. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 29, 2020 at 21:02:35_

----

> Silly me, assuming EditorConfig took care of it all. 

it actually should have. dunno why it didn't.


----
<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Wednesday Aug 05, 2020 at 13:36:20_

----

Change made,  coco


----
<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Thursday Jul 02, 2020 at 21:52:41_

----

Made requested changes, tested all of her quests. Seems good to go here.


----
<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Tuesday Jul 07, 2020 at 02:05:20_

----

> Few more things from me, also a lot of extra spaces/tabs/lines that should be removed. Check the [style guide](https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md#style-guide). 

Sorry about that, wasn't aware of it until Teo mentioned it the other day to me in a PM. I will get this adjusted soon and resubmitted.


----
<a href="https://github.com/zircon-tpl"><img src="https://avatars0.githubusercontent.com/u/60901633?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zircon-tpl](https://github.com/zircon-tpl)**
_Thursday Jul 23, 2020 at 04:17:54_

----

Hello, @Era-Lusiphur !

I am ensuring that this Pull Request has not been forgotten. Is there anything you might need assistance with?


----
<a href="https://github.com/Era-Lusiphur"><img src="https://avatars0.githubusercontent.com/u/61239975?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Era-Lusiphur](https://github.com/Era-Lusiphur)**
_Thursday Jul 23, 2020 at 18:14:06_

----

> I am ensuring that this Pull Request has not been forgotten. Is there anything you might need assistance with?

Just been busy with other things. I apologize about the delay. 


----
<a href="https://github.com/zircon-tpl"><img src="https://avatars0.githubusercontent.com/u/60901633?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zircon-tpl](https://github.com/zircon-tpl)**
_Thursday Jul 23, 2020 at 20:45:08_

----

That is perfectly acceptable! Please do not hesitate to let us know if we may assist in some manner. Project Topaz strives to work with Contributors!
