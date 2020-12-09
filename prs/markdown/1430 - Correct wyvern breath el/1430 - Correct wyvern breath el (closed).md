**Labels:**

approved



<a href="https://github.com/rude-jerk"><img src="https://avatars0.githubusercontent.com/u/9592857?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [rude-jerk](https://github.com/rude-jerk)**
_Sunday Oct 25, 2020 at 05:27:39_
_Originally opened as: project-topaz/topaz - Issue 1430_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

https://www.bg-wiki.com/bg/Wyvern_(Dragoon_Pet)

> 
> The selected breath is determined exclusively by an opponent's elemental resistances at the time of activation
> 
> Magic damage reduction, elemental damage reduction and absorption, elemental magic accuracy buffs such as Klimaform, or equipment such as the Drachen Armet/+1 or Vishap Armet/+1/+2/+3 have no bearing on a wyvern's choice of breath.
> 
> Effects that lower enemy resistances such as Threnody or Skillchains are factored into this choice.
> 
> In the event of a tie for lowest resistance, the element is selected in the following order of Fire → Ice → Wind → Earth → Thunder → Water.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 25, 2020 at 17:58:06_

----

You can cut the second loop by assigning your `breath` as you're stepping through the table the first time. This will be guaranteed to only be a single breath when you exit the loop because your resistance comparisons are strictly less than and don't include equal to. Then you can `table.insert(breaths, breath)` directly.


----
<a href="https://github.com/rude-jerk"><img src="https://avatars0.githubusercontent.com/u/9592857?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [rude-jerk](https://github.com/rude-jerk)**
_Sunday Oct 25, 2020 at 19:45:06_

----

In making this change I noticed that I needed to convert to using ipairs, as the table order was arbitrary using pairs. Corrected this at the same time!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 25, 2020 at 20:01:02_

----

Gotta a non-newline brace here~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 25, 2020 at 17:58:06_

----

You can cut the second loop by assigning your `breath` as you're stepping through the table the first time. This will be guaranteed to only be a single breath when you exit the loop because your resistance comparisons are strictly less than and don't include equal to. Then you can `table.insert(breaths, breath)` directly.


----
<a href="https://github.com/rude-jerk"><img src="https://avatars0.githubusercontent.com/u/9592857?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [rude-jerk](https://github.com/rude-jerk)**
_Sunday Oct 25, 2020 at 19:45:06_

----

In making this change I noticed that I needed to convert to using ipairs, as the table order was arbitrary using pairs. Corrected this at the same time!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 25, 2020 at 20:01:02_

----

Gotta a non-newline brace here~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Oct 25, 2020 at 20:20:03_

----

When elements are fixed in release we might be able to remove the two tables altogether and just use Flame Breath and Fire element as offsets.
```lua
local lowest = 0
local lowest_res = target:getMod(tpz.mod.FIRERES)
for i = 1, i <= 5, 1 do
    local res = target:getMod(tpz.mod.FIRERES + i)
    if res < lowest_res then
        lowest = i
        lowest_res = res
    end
end
table.insert(breaths, tpz.jobAbility.FLAME_BREATH + lowest)
```

But for now the tables are needed because the elements in release follow the wrong order.
