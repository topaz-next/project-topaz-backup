**Labels:**

merge ready



<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 08, 2020 at 00:38:11_
_Originally opened as: project-topaz/topaz - Issue 474_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 08, 2020 at 00:47:57_

----

You might want this one to spawn last. I think with the recent claim changes only the last one spawned will stay claimed after about 3 seconds unless engaged.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 08, 2020 at 00:53:10_

----

Probably wanna use `npcUtil.giveItem(player, 16270)` here as a condition for finishing the quest, does the same thing and checks inventory space, returns true/false.


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 08, 2020 at 01:00:54_

----

So just switch casa to the bottom of the list eh?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 08, 2020 at 01:04:58_

----

Probably, that one looks like the main target and if any of them should have their claim stick it'd be that one.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 08, 2020 at 02:18:07_

----

```lua
    elseif (csid ==890) then
        if npcUtil.giveItem(player, 16270) then
            player:setCharVar("princeandhopper",0)
            player:completeQuest(AHT_URHGAN,tpz.quest.id.ahtUrhgan.THE_PRINCE_AND_THE_HOPPER)
        end
    end
```
Doing it like this will ensure they get their item before marking as complete. If it fails to give them the item they have to make room and watch the cs again.


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 08, 2020 at 02:29:05_

----

I somehow fucked this all up I need a masterclass on github for real. 


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Apr 08, 2020 at 04:03:28_

----

Or:
```
elseif csid == 890 then
    npcUtil.completeQuest(
        player,
        AHT_URHGAN,
        tpz.quest.id.ahtUrhgan.THE_PRINCE_AND_THE_HOPPER,
        {item = 16270, var = "princeandhopper"}
    )
end
```

npcUtil.completeQuest handles:
awarding items, keyitems, gil, XP, title, and fame
setting quest-related variables to 0
completing the quest


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 08, 2020 at 04:15:53_

----

I guess the best question is what is going to be the standard moving forward?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 08, 2020 at 04:34:54_

----

That's much better, I didn't even realize we had that.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 08, 2020 at 00:47:57_

----

You might want this one to spawn last. I think with the recent claim changes only the last one spawned will stay claimed after about 3 seconds unless engaged.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 08, 2020 at 00:53:10_

----

Probably wanna use `npcUtil.giveItem(player, 16270)` here as a condition for finishing the quest, does the same thing and checks inventory space, returns true/false.


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 08, 2020 at 01:00:54_

----

So just switch casa to the bottom of the list eh?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 08, 2020 at 01:04:58_

----

Probably, that one looks like the main target and if any of them should have their claim stick it'd be that one.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 08, 2020 at 02:18:07_

----

```lua
    elseif (csid ==890) then
        if npcUtil.giveItem(player, 16270) then
            player:setCharVar("princeandhopper",0)
            player:completeQuest(AHT_URHGAN,tpz.quest.id.ahtUrhgan.THE_PRINCE_AND_THE_HOPPER)
        end
    end
```
Doing it like this will ensure they get their item before marking as complete. If it fails to give them the item they have to make room and watch the cs again.


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 08, 2020 at 02:29:05_

----

I somehow fucked this all up I need a masterclass on github for real. 


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Apr 08, 2020 at 04:03:28_

----

Or:
```
elseif csid == 890 then
    npcUtil.completeQuest(
        player,
        AHT_URHGAN,
        tpz.quest.id.ahtUrhgan.THE_PRINCE_AND_THE_HOPPER,
        {item = 16270, var = "princeandhopper"}
    )
end
```

npcUtil.completeQuest handles:
awarding items, keyitems, gil, XP, title, and fame
setting quest-related variables to 0
completing the quest


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 08, 2020 at 04:15:53_

----

I guess the best question is what is going to be the standard moving forward?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 08, 2020 at 04:34:54_

----

That's much better, I didn't even realize we had that.


----
<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 08, 2020 at 00:49:33_

----

I just realized I will need to update the footprint to only give the CS and param for those current on that stage of the fight. 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Apr 08, 2020 at 00:57:13_

----

> I just realized I will need to update the footprint to only give the CS and param for those current on that stage of the fight.

It looks like you're already doing that with the charvar
