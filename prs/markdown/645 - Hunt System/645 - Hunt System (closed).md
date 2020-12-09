**Labels:**

reviewed



<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Apocarypse](https://github.com/Apocarypse)**
_Thursday May 21, 2020 at 20:27:22_
_Originally opened as: project-topaz/topaz - Issue 645_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Functional hunt system implementation. The only thing missing is Evoliths, which require synergy to be working. The VNMs also do not have scripts, as they are unimplemented at this time.

Please do not squash when merging this PR as there are collaborative commits which should remain separate.

I would like to thank Kreidos for all his help on this project. He was there to assist every step of the way and definitely deserves half the credit.

Fixes #240 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 19:44:46_

----

Could use `if os.time() < player:getCharVar("[hunt]nextHunt") then`


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 19:47:04_

----

Was this changed to `clearRegimeVars`?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 19:47:17_

----

Could use `player:setCharVar("[hunt]nextHunt", getVanaMidnight())`


----
<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Apocarypse](https://github.com/Apocarypse)**
_Thursday Jun 04, 2020 at 20:02:45_

----

how about `if player:getCharVar("[hunt]nextHunt") < getVanaMidnight()then`


----
<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Apocarypse](https://github.com/Apocarypse)**
_Thursday Jun 04, 2020 at 20:02:58_

----

Yes! I'm glad you caught that.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jun 04, 2020 at 20:05:15_

----

I like this idea. Ideally we should compare against a consistent source.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 03:55:29_

----

This should be checking `os.time()`, reason being that `getVanaMidnight()` very slightly varies in what it returns, even for the same day, so if you're lucky then `getVanaMidnight` will return a midnight that's maybe 1s before the `getVanaMidnight` that is saved in the char var. This should check `if os.time() < player:getCharVar("[hunt]nextHunt") then` (it's also checking the requirement backwards, this block should execute if the char is blocked)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Jun 05, 2020 at 03:59:18_

----

I have a question. Since os.time() is lua native it always returns the system time; whereas getVanaMidnight ties into the time calculations and so could be affected by any offsets which are (or might) be implemented in the core. Couldn't that pose an issue to using os.time() which is completely independent of server time calculations?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 04:00:04_

----

I'm not sure if this is very common, but I happened to test this on Lizzy and she actually has 2 IDs, so might need to add the other one `17215868`.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 04:02:08_

----

`bounty` is nil, is this supposed to be `scyldBounty`?


----
<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Apocarypse](https://github.com/Apocarypse)**
_Friday Jun 05, 2020 at 04:03:08_

----

I asked about this and got no reply unfortunately. There are some NMs that have a single spawn point under one ID, and like 50 spawn points under another ID. In those cases, I opted for the 50. I don't know what the logic is there exactly. 


----
<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Apocarypse](https://github.com/Apocarypse)**
_Friday Jun 05, 2020 at 04:05:20_

----

Yes, I think you're right. I'll change it. 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 04:05:21_

----

Adding currency here and below?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 04:08:33_

----

This message should be moved to after you distribute the currency, then use the updated total.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 04:12:39_

----

It's still using getVanaMidnight to set the time, so that's all accounted for. This check is just seeing if the current time is past what has been determined is the next vana midnight when that var was set.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 04:36:41_

----

This will still give the old total, go with this:
```lua
    -- scylds cap at 1000
    if player:getCurrency("scyld") + scyldBounty > 1000 then
       player:setCurrency("scyld", 1000)
    else
       player:addCurrency("scyld", scyldBounty)
    end
    player:messageSpecial(msg[5])
    player:messageSpecial(msg[6], scyldBounty, player:getCurrency("scyld"))
```


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 07:28:44_

----

These should be moved to after the fee is applied, and updated with `player:getCurrency("scyld")`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 06, 2020 at 02:12:16_

----

~~tabling all the IDs of all these NMs is the wrong approach. Followup what all existing regimes do and include the regime ID at the mob, then match on regime ID instead of performing a lookup to see if that specific mob is in a table. We don't need to keep track of them all because its never going to change, and you already have that line there anyway. model it after the existing regimes instead of trying to centralize every bit of data to one place as this is a case where that just gets in the way.~~

~~`tpz.hunts.checkHunt(mob, player, isKiller)`
compare with
`tpz.regime.checkRegime(player, mob, 80, 1, tpz.regime.type.FIELDS)`
and
`tpz.regime.checkRegime(player, mob, 640, 2, tpz.regime.type.GROUNDS)`
you're trying to reinvent the wheel to separate hunts from these (understandable, a lot of code doesn't apply here) but missed why the regime ID was included.~~

now looking at this:
`tpz.hunts.checkHunt(mob, player, isKiller)`
We should not need isKiller at all as in retail all member who have the hunt regime active get credit and its not going to stack up (onMobDeath code will run once-per-member), so I suggest just go with:
`tpz.hunts.checkHunt(mob, player, RegimeIDhere)` to minimize your changes.

Edit: this could have been worded better by me, see coco's post which got straight to what it'd look like and didn't risk misunderstandings


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 06, 2020 at 02:20:44_

----

p.s. if you're thinking "but then we need to keep track of which NMs go in which regime!" no, because the regime IDs will never shift. set once done for life. :)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Saturday Jun 06, 2020 at 02:25:08_

----

I gotta disagree here on part of that. isKiller isn't necessary, you're right, but frankly I think having all the mobs tabled here with a simple lookup to a table is a much faster and better method than breaking out every ID into separate mob scripts. Regimes takes the ID it gets and combs through a table using a for loop anyway to find the mob which is far from elegant. This solution involves one direct check to one table and I gotta go with the performance method here.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Saturday Jun 06, 2020 at 03:07:21_

----

Switching to `tpz.hunts.checkHunt(mob, player, RegimeIDhere)` would actually solve the multiple ID mobs issue all at once and would require minimal changes. `checkHunt` becomes:
```lua
    function tpz.hunts.checkHunt(mob, player, RegimeIDhere)
        local huntZone = player:getCharVar("[hunt]zone")
        local huntId = player:getCharVar("[hunt]id")
        local playerHunt = zone[huntZone].hunt[huntId]

        -- required NM has been defeated
        if player:getCharVar("[hunt]status") == 1 and huntId == RegimeIDhere then
           player:messageBasic(tpz.msg.basic.FOV_DEFEATED_TARGET + 20)
           player:setCharVar("[hunt]status", 2)
        end
    end
```
but that would also require removing all the mob IDs from the tables and updating all the mob files as well.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 06, 2020 at 03:28:46_

----

@cocosolos that is what I was going for. It does suck to re-edit all those mob scripts, but they all did have to have an edit to start with so its not like these didn't have code going to them. That said I will volunteer to make the mob script changes if apoc wants to take this road.

the alternative is harder - alterations to support multiple mobID elements and then the inevitable future problems that come with mobIDs later


((if anyone can come up with a 3rd option, I'm all ears)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 19:44:46_

----

Could use `if os.time() < player:getCharVar("[hunt]nextHunt") then`


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 19:47:04_

----

Was this changed to `clearRegimeVars`?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 19:47:17_

----

Could use `player:setCharVar("[hunt]nextHunt", getVanaMidnight())`


----
<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Apocarypse](https://github.com/Apocarypse)**
_Thursday Jun 04, 2020 at 20:02:45_

----

how about `if player:getCharVar("[hunt]nextHunt") < getVanaMidnight()then`


----
<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Apocarypse](https://github.com/Apocarypse)**
_Thursday Jun 04, 2020 at 20:02:58_

----

Yes! I'm glad you caught that.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jun 04, 2020 at 20:05:15_

----

I like this idea. Ideally we should compare against a consistent source.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 03:55:29_

----

This should be checking `os.time()`, reason being that `getVanaMidnight()` very slightly varies in what it returns, even for the same day, so if you're lucky then `getVanaMidnight` will return a midnight that's maybe 1s before the `getVanaMidnight` that is saved in the char var. This should check `if os.time() < player:getCharVar("[hunt]nextHunt") then` (it's also checking the requirement backwards, this block should execute if the char is blocked)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Jun 05, 2020 at 03:59:18_

----

I have a question. Since os.time() is lua native it always returns the system time; whereas getVanaMidnight ties into the time calculations and so could be affected by any offsets which are (or might) be implemented in the core. Couldn't that pose an issue to using os.time() which is completely independent of server time calculations?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 04:00:04_

----

I'm not sure if this is very common, but I happened to test this on Lizzy and she actually has 2 IDs, so might need to add the other one `17215868`.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 04:02:08_

----

`bounty` is nil, is this supposed to be `scyldBounty`?


----
<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Apocarypse](https://github.com/Apocarypse)**
_Friday Jun 05, 2020 at 04:03:08_

----

I asked about this and got no reply unfortunately. There are some NMs that have a single spawn point under one ID, and like 50 spawn points under another ID. In those cases, I opted for the 50. I don't know what the logic is there exactly. 


----
<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Apocarypse](https://github.com/Apocarypse)**
_Friday Jun 05, 2020 at 04:05:20_

----

Yes, I think you're right. I'll change it. 


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 04:05:21_

----

Adding currency here and below?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 04:08:33_

----

This message should be moved to after you distribute the currency, then use the updated total.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 04:12:39_

----

It's still using getVanaMidnight to set the time, so that's all accounted for. This check is just seeing if the current time is past what has been determined is the next vana midnight when that var was set.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 04:36:41_

----

This will still give the old total, go with this:
```lua
    -- scylds cap at 1000
    if player:getCurrency("scyld") + scyldBounty > 1000 then
       player:setCurrency("scyld", 1000)
    else
       player:addCurrency("scyld", scyldBounty)
    end
    player:messageSpecial(msg[5])
    player:messageSpecial(msg[6], scyldBounty, player:getCurrency("scyld"))
```


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday Jun 05, 2020 at 07:28:44_

----

These should be moved to after the fee is applied, and updated with `player:getCurrency("scyld")`


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 06, 2020 at 02:12:16_

----

~~tabling all the IDs of all these NMs is the wrong approach. Followup what all existing regimes do and include the regime ID at the mob, then match on regime ID instead of performing a lookup to see if that specific mob is in a table. We don't need to keep track of them all because its never going to change, and you already have that line there anyway. model it after the existing regimes instead of trying to centralize every bit of data to one place as this is a case where that just gets in the way.~~

~~`tpz.hunts.checkHunt(mob, player, isKiller)`
compare with
`tpz.regime.checkRegime(player, mob, 80, 1, tpz.regime.type.FIELDS)`
and
`tpz.regime.checkRegime(player, mob, 640, 2, tpz.regime.type.GROUNDS)`
you're trying to reinvent the wheel to separate hunts from these (understandable, a lot of code doesn't apply here) but missed why the regime ID was included.~~

now looking at this:
`tpz.hunts.checkHunt(mob, player, isKiller)`
We should not need isKiller at all as in retail all member who have the hunt regime active get credit and its not going to stack up (onMobDeath code will run once-per-member), so I suggest just go with:
`tpz.hunts.checkHunt(mob, player, RegimeIDhere)` to minimize your changes.

Edit: this could have been worded better by me, see coco's post which got straight to what it'd look like and didn't risk misunderstandings


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 06, 2020 at 02:20:44_

----

p.s. if you're thinking "but then we need to keep track of which NMs go in which regime!" no, because the regime IDs will never shift. set once done for life. :)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Saturday Jun 06, 2020 at 02:25:08_

----

I gotta disagree here on part of that. isKiller isn't necessary, you're right, but frankly I think having all the mobs tabled here with a simple lookup to a table is a much faster and better method than breaking out every ID into separate mob scripts. Regimes takes the ID it gets and combs through a table using a for loop anyway to find the mob which is far from elegant. This solution involves one direct check to one table and I gotta go with the performance method here.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Saturday Jun 06, 2020 at 03:07:21_

----

Switching to `tpz.hunts.checkHunt(mob, player, RegimeIDhere)` would actually solve the multiple ID mobs issue all at once and would require minimal changes. `checkHunt` becomes:
```lua
    function tpz.hunts.checkHunt(mob, player, RegimeIDhere)
        local huntZone = player:getCharVar("[hunt]zone")
        local huntId = player:getCharVar("[hunt]id")
        local playerHunt = zone[huntZone].hunt[huntId]

        -- required NM has been defeated
        if player:getCharVar("[hunt]status") == 1 and huntId == RegimeIDhere then
           player:messageBasic(tpz.msg.basic.FOV_DEFEATED_TARGET + 20)
           player:setCharVar("[hunt]status", 2)
        end
    end
```
but that would also require removing all the mob IDs from the tables and updating all the mob files as well.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jun 06, 2020 at 03:28:46_

----

@cocosolos that is what I was going for. It does suck to re-edit all those mob scripts, but they all did have to have an edit to start with so its not like these didn't have code going to them. That said I will volunteer to make the mob script changes if apoc wants to take this road.

the alternative is harder - alterations to support multiple mobID elements and then the inevitable future problems that come with mobIDs later


((if anyone can come up with a 3rd option, I'm all ears)
