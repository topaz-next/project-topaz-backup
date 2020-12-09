**Labels:**

improvement



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Saturday Oct 03, 2020 at 15:41:51_
_Originally opened as: project-topaz/topaz - Issue 1243_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

```
// If enmity is a one-to-many list held by monsters to track who "they hate",
// notoriety is the many-to-one opposite list held by players (or other targets of enmity) to track who "hates them".
```

A PC should be able to do a simple lookup to see if any mobs have hate towards them. Currently, they have to look at their `mobSpawnList`, iterate through all of their `EnmityContainers` and see if they're on any of those lists. It's been this way forever, so it doesn't appear to be too much of a performance drain, but we also need this sort of lookup for something like: `char:hasEnmity()` or generating lists of things to target with auras etc.

It's actually very simple, it piggybacks _entirely_ off of `EnmityContainer`.

**Design**
To support stability, every call into this container should fail gracefully. I'm starting to think that `clear` doesn't need to exist, since the regular enmity container checks for if a target is in zone, or is alive: the two conditions that this container might clear itself in. 
It would make more sense to just use the underlying data structure, but not all exposed calls are safe. So wrapping it and only exposing safe calls was the way I chose.

**Testing**
- Being aggro'd adds the mob to your list
- Zone with hate
- Die with hate
- AOE a bunch of mobs who hate you
- Kiting and counting mobs with: `ShowStatus("Aggro: %n", PNotorietyContainer->size());`
- Tested with PLD, WAR & DRG enmity changing abilities
- I've also been testing this in my `trust` branch, the checks to see if you have enmity before you can summon trusts, and the checks before trusts start "resting" now work as intended.
- Wait long enough for zone cleanup after logout

**Done**
- Container, piggybacking on `EnmityContainer`
- Basic testing
- Binding: `hasEnmity()`
```lua
local hasEnmity = player:hasEnmity()
```
- Binding `getNotorietyList()`
```lua
    local list = player:getNotorietyList()
    for _, entry in pairs(list) do
        print(entry:getName())
    end
```
- Plug into Auras
- Test with enmity reducing/resetting abilities


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Oct 04, 2020 at 14:21:33_

----

I've been hyping this up as the blocker for many different features for about 6 months, so now that it's finally here and it piggybacks off of something that is incredibly battle-tested, I'm happy to merge it straight into `release`. I will of course act as front-line support if it breaks anything and have my finger hovering over the revert button.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Oct 04, 2020 at 20:58:14_

----

`PNotorietyContainer`

not sure about that naming but I got nothing better yet lol


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Oct 09, 2020 at 17:38:08_

----

Iterators... that was painful to fix
