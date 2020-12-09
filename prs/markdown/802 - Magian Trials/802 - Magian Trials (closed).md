**Labels:**



<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Apocarypse](https://github.com/Apocarypse)**
_Friday Jul 03, 2020 at 05:32:59_
_Originally opened as: project-topaz/topaz - Issue 802_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Gentlemen, behold! Magian Trials in (most of) its glory!

This PR makes it possible to do trials through the Orange Magian Moogle start to finish. As is, I have only implemented the "NM" paths up until they reach Abyssea content. New trials can be added by filling out the SQL and coding the appropriate hooks. After that, plug the trial and condition into the anonymous function table and you're good to go.

I tried to make this system with the future in mind, with an aim to keep it easily expandable. A little scripting may be required eventually (namely "trade" based trials and how incrementing progress is handled in general) but nothing too bad.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Friday Jul 03, 2020 at 09:07:49_

----

we should avoid functions in scripts/globals luas that sit in the global space.  instead, look at how others do it -- for example scripts/globals/treasure.lua.  So something like

```lua
tpz = tpz or {}
tpz.magian = tpz.magian or {}

.
.
.

function tpz.magian.magianOrangeOnTrade(player, npc, trade)
.
.
.
end
```


----
<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Apocarypse](https://github.com/Apocarypse)**
_Friday Jul 03, 2020 at 23:48:03_

----

I gotchu Wren


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Friday Jul 03, 2020 at 09:07:49_

----

we should avoid functions in scripts/globals luas that sit in the global space.  instead, look at how others do it -- for example scripts/globals/treasure.lua.  So something like

```lua
tpz = tpz or {}
tpz.magian = tpz.magian or {}

.
.
.

function tpz.magian.magianOrangeOnTrade(player, npc, trade)
.
.
.
end
```


----
<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Apocarypse](https://github.com/Apocarypse)**
_Friday Jul 03, 2020 at 23:48:03_

----

I gotchu Wren


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Jul 03, 2020 at 08:15:17_

----

Awesome Job @Apocarypse 

Since there's magian trials missing and you are the best knowledgeable at this, could a Wiki Page be added on how it works so whomever wants to take ownership of the Abyssea content ones, can easily refer to it. :cat: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jul 04, 2020 at 04:10:41_

----

Haven't really looked at yet, but instead of returning true, should have functions return how much progress should advance. That way can use same system for trials where progress varies depending on the factors involved.

Other thought, if trials will fall into certain categories, could axe the anonymous functions altogether and return tables telling some invocation script how to handle the information:
```lua
--trial data:
[some_id] = { condition = 'nm', reqs = { ids = set{1, 5, 6} } }
[another_id] = { condition = 'nm', reqs = { ids = set{9, 10} } }
[third_id] = { condition = 'elem_kill'], reqs = { element = tpz.magic.element.WIND } }

--magian.onmobdeath
-- may need to play with pack or unpack on the function args which come into the function
local trial_id = player:getTrialIdOnWeapon()
local trial = trial_data[trial_id]
if trial then
    local progress = magian.trials[trial.condition](trial.reqs, death_args)
    if progress > 0 then
        addProgressToWeapon()
    end
end

--magial.trials
['nm'] = function(reqs, death_args)
    local mob_id = death_args.mob:getID()
    if reqs.ids[mob_id] then
        return 1
    end
    return false
end,

['elem_kill] = function(reqs, death_args)
    local last_damage = death_args.mob:lastDamage()
    local required_type = tpz.damageType.FIRE + reqs.ele - 1
    if last_damage.type == required_type then
        local progress = 1
        local day = VanadielDayOfWeek()
        local weather = death_args.player:getWeather()
        if tpz.dayElement[day] == reqs.ele and weatherElement[weather] == reqs.ele then
             progress = 10
       elseif tpz.dayElement[day] == reqs.ele or weatherElement[weather] == reqs.ele then
            progress = 5
       end
       return progress
    end
    return false
end
```


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Saturday Jul 04, 2020 at 04:38:34_

----

Thanks ibm, great idea with returning the amount to increment the progress!

Apoc would know better than I about the future extensibility of going back to generalized functions. I personally feel it's a bit of 6 of one, half of another, and would make adding new trials less ad-hoc in nature. Each new trial means tabling new checks either way and I'm also not retail-knowledgeable enough to say how such a general way would work in all cases. 


----
<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Apocarypse](https://github.com/Apocarypse)**
_Saturday Jul 04, 2020 at 04:46:12_

----

Kreidos pretty much said what I was about to write. Love the progress return idea, will definitely put it into action. The second suggestion I'm not as sure about. If I'm understanding it, it seems like the same outcome but potentially less straight forward in regards to application of new trials? Given the scale of Magian, it's possibly going to be a long drawn out process potentially many people could contribute to, I'd like adding trials to be as straight forward as possible.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Saturday Jul 04, 2020 at 05:44:45_

----

Your way has some potential, ibm. I actually think there's actually a good clean way to maintain a bit of the best of both methods using true self-referencing object functions. This would make the code simpler while also leaving adding new trials easy and straightforward.

Basic show of concept which I suggested to Apoc over discord. Can/would be expanded but shows basic flow:
```lua
-- check functions reference themselves
checks.nm_kill = function(self, player, params)
       if params.mobid == self.reqs.mobid then 
             return self.increment
       else
             return 0
       end
    end

-- trials
    [1] = {
        check = checks.nm_kill, -- trial type is only referenced here
        reqs = { mobid = 9 },
        increment = 5
    }

trial = player:getEquippedItem(MAIN):getTrialNumber()
params = { mobid = 9 }

-- table takes care of it's own trial type, the check is always the same regardless
amt_increase = trials[trial]:check(player, params) 
increaseTrialProgress(amt_increase)
```


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Aug 20, 2020 at 03:43:29_

----

@project-topaz/developer  @project-topaz/reviewer this is another one that looks like it needs another review post fixes but should be good considering the past requests.
