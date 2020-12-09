**Labels:**

help wanted

research needed



<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [m241dan](https://github.com/m241dan)**
_Sunday Aug 16, 2020 at 16:18:52_
_Originally opened as: project-topaz/topaz - Issue 957_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Aug 16, 2020 at 17:00:55_

----

This behavior isn't universal. I believe SE started doing it with ToAU when they moved it from being the jobs 2hr special to being just a non-subable JA. The left all the old mobs alone, but these were mostly NMs (a lot of the old spear wielding mobs were actually not drg job). We will want some way to prevent those older drg mobs/NMs from doing this if something does not already prevent it. If something already does, I think its appropriate to leave a comment in the code there.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Sunday Aug 16, 2020 at 17:24:37_

----

> This behavior isn't universal. I believe SE started doing it with ToAU when they moved it from being the jobs 2hr special to being just a non-subable JA. The left all the old mobs alone, but these were mostly NMs (a lot of the old spear wielding mobs were actually not drg job). We will want some way to prevent those older drg mobs/NMs from doing this if something does not already prevent it. If something already does, I think its appropriate to leave a comment in the code there.

We should get some research and tackle this appropriately then? Though, I suppose we could just region lock it. If region ToAU or greater...


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 17, 2020 at 01:40:31_

----

Its not that its region specific just they did not update existing mobs, but started making new ones work this way. Probably need to control via mobmod and or mixin, as new mobs in old zones would get the new behavior,

Like you fight Steelbiter Gudrud, is Wyvern is still on a 2hr timer. You fight the old Orcish Dragoons in Monastic Cavern and they still have no Wyvern at all. Every mob created after SE changed DRG's 2hr pop them while idle (including new orcs). Doing a region check would probably cover 90% of them because that would have been right around ToAU's debut and there wouldn't be much being added in older zones, but I believe we'd have some newer BCNM mobs being affected still (which admittedly do not exist in Topaz yet).


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Aug 18, 2020 at 12:32:13_

----

ix'aern drg also does not start with idle wyvern, though i know that's also a special case.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Aug 18, 2020 at 13:53:37_

----

Looks like when they updated dynamis, they kept with the old style of wyvern = 2hr. except they depop when master is dead now and didn't use to do that. No more angry pseudo pet following me around dynamis (I just ran through dyna sandy on retail for an item I needed). 

I think we might be able to do this by region after all, if we confirm newer bcnm drg mobs also follow the old behavior.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Tuesday Aug 18, 2020 at 14:01:20_

----

> ix'aern drg also does not start with idle wyvern, though i know that's also a special case.

this is a good concern, but does he not? I seem to remember retail he would pop with his whole crew, and we'd have someone kite while we zone nuked. But, we're like... 10 years removed at this point, so I'll defer to you. Perhaps we'll need a special case?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Aug 18, 2020 at 14:51:45_

----

> 
> 
> > ix'aern drg also does not start with idle wyvern, though i know that's also a special case.
> 
> this is a good concern, but does he not? I seem to remember retail he would pop with his whole crew, and we'd have someone kite while we zone nuked. But, we're like... 10 years removed at this point, so I'll defer to you. Perhaps we'll need a special case?

I totally forgot till just now how that fella worked, this is what we do currently:
```lua
function onMobFight(mob, target)
    -- Spawn the pets if they are despawned
    -- TODO: summon animations?
    local mobId = mob:getID()
    local x = mob:getXPos()
    local y = mob:getYPos()
    local z = mob:getZPos()

    for i = mobId + 1, mobId + 3 do
        local wynav = GetMobByID(i)
        if not wynav:isSpawned() then
            local repopWynavs = wynav:getLocalVar("repop") -- see Wynav script
            if mob:getBattleTime() - repopWynavs > 10 then
                wynav:setSpawn(x + math.random(1, 5), y, z + math.random(1, 5))
                wynav:spawn()
                wynav:updateEnmity(target)
            end
        end
    end
end
```

.. so every 10 seconds..


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Aug 18, 2020 at 16:50:43_

----

Yeah, i just popped him the other day for damage testing on retail. He just sits there, and only spawned wynavs on engage (sorry im challenged on mobile and cant quote) 


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Tuesday Aug 18, 2020 at 16:59:02_

----

> Yeah, i just popped him the other day for damage testing on retail. He just sits there, and only spawned wynavs on engage (sorry im challenged on mobile and cant quote)

Okay, will make changes. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Aug 18, 2020 at 17:14:39_

----

iirc he will continue to call them after they die also, which is why it got done in onMobFight in the script
