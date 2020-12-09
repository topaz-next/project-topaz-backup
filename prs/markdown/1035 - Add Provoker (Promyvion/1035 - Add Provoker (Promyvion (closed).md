**Labels:**

approved

reviewed



<a href="https://github.com/triple-lariat"><img src="https://avatars1.githubusercontent.com/u/30502556?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [triple-lariat](https://github.com/triple-lariat)**
_Saturday Aug 29, 2020 at 18:14:18_
_Originally opened as: project-topaz/topaz - Issue 1035_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

All implemented behavior for Provoker is based on the capture and noted behavior by Jimmayus: https://youtu.be/0fSKlDz5bWU
There didn't seem to be any apparent way to add a dummy ability for its elemental affinity change aside from using the existing "vulture_1" mob skill, so I put those changes in as well.

For the most part, Provoker's behavior matches the elemental affinity change of Kam'lanaut, so its script is largely adapted from Kam'lanaut's.

Furthermore, though Provoker has Enspells currently in Topaz, the capture indicates that Provoker's enspell effect comes from its current elemental affinity. 

Lastly, the double attack and accuracy boost are based on observations that Provoker had a fairly high accuracy against a 75 RDM and double attacked fairly often. 



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Aug 29, 2020 at 21:09:36_

----

suggestion:
```lua
function onAdditionalEffect(mob, target, damage)
    local element = mob:getLocalVar("element")
    local index =
    {
        [1] = tpz.mob.ae.ENFIRE,
        [2] = tpz.mob.ae.ENSTONE,
        [3] = tpz.mob.ae.ENWATER,
        [4] = tpz.mob.ae.ENAERO,
        [5] = tpz.mob.ae.ENBLIZZARD,
        [6] = tpz.mob.ae.ENTHUNDER,
        [7] = tpz.mob.ae.ENLIGHT,
        [8] = tpz.mob.ae.ENDARK
    }
    if index[element] then
        return tpz.mob.onAddEffect(mob, target, damage, index[element], {chance = 1000})
    else
        return 0, 0, 0 -- Just in case its somehow not got a variable set
    end
end
```
then we don't have to do all that if/elseif. The else in my sample above can be ripped out if the mob spawns in with the en-effect already active for its element. I do not know if retail does that I have no looked at the capture. if it does we probably want to set a random element at spawn time just so there is no tiny milliseconds gap between its AI trying to swing at you and the variable being set by onMobFight to throw an explainable nil that seemingly can't  be reproduced when you try to reproduce it later :)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Aug 29, 2020 at 21:12:47_

----

considering wiki claims it hits hard as well as having double attack I'm wondering if maybe one of its jobs should be war, but I'll leave well enough alone for now and say this is fine if we have indications besides the additional effect that its a rdm (wiki will often see one thing that looks like what  job has, and then just declare a mob to be that job.. its often wrong or forgets that mobs can have more than 1)


----
<a href="https://github.com/triple-lariat"><img src="https://avatars1.githubusercontent.com/u/30502556?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [triple-lariat](https://github.com/triple-lariat)**
_Saturday Aug 29, 2020 at 23:33:57_

----

There doesn't seem to be any substantial proof that its job is RDM aside from the misconception that it casts its enspell effects. Unless someone more knowledgeable than I am about mob jobs wants to chime in I think I'll go ahead and change its job to WAR.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Saturday Aug 29, 2020 at 23:50:20_

----

https://docs.google.com/spreadsheets/d/1YBoveP-weMdidrirY-vPDzHyxbEI2ryECINlfCnFkLI/edit#gid=0
I'd go with war/pld with a family bonus of 10% defp per jimmayus/meloetta's data. that would give the double attack. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 31, 2020 at 11:39:00_

----

With the job change remember to update the onMobInitialize section. you'd be adding 25 on top of what warrior already gets at this level (setMod instead of addmod would enforce it having only 25, while removing the line would rely on what warrior has native at this lv)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 09:34:50_

----

If there's only simple logic going on, please drop the brackets
```lua
if changeTime == 0 then
    ...
```

Same for the rest of the file etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 09:35:27_

----

newelement -> newElement for clarity please


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 09:44:56_

----

I know you inherited this from what was already in the db, but could we change this to be something a little more descriptive? `provoker_2hr` or something would probably work. That change would need to be reflected here, in this file's name and the entry in mob_skills


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Sep 03, 2020 at 15:56:16_

----

@zach2good it's used by other mobs as well and that is what reports out from actionview in captures. changing the name will make finding and using it potentially difficult.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 18:09:15_

----

Aha, makes sense! Disregard this comment!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 18:10:48_

----

You're almost there, there are still some simple logic blocks (like that while loop) that don't need brackets. Then we're good to go


----
<a href="https://github.com/triple-lariat"><img src="https://avatars1.githubusercontent.com/u/30502556?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [triple-lariat](https://github.com/triple-lariat)**
_Thursday Sep 03, 2020 at 18:27:16_

----

Sorry but are there actually any more unnecessary brackets aside from the while loop? I'm not too familiar with which other brackets may be optional in Lua quite yet, and I don't want to make a bunch of separate commits because I missed something else!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 18:28:37_

----

just me :)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Aug 29, 2020 at 21:09:36_

----

suggestion:
```lua
function onAdditionalEffect(mob, target, damage)
    local element = mob:getLocalVar("element")
    local index =
    {
        [1] = tpz.mob.ae.ENFIRE,
        [2] = tpz.mob.ae.ENSTONE,
        [3] = tpz.mob.ae.ENWATER,
        [4] = tpz.mob.ae.ENAERO,
        [5] = tpz.mob.ae.ENBLIZZARD,
        [6] = tpz.mob.ae.ENTHUNDER,
        [7] = tpz.mob.ae.ENLIGHT,
        [8] = tpz.mob.ae.ENDARK
    }
    if index[element] then
        return tpz.mob.onAddEffect(mob, target, damage, index[element], {chance = 1000})
    else
        return 0, 0, 0 -- Just in case its somehow not got a variable set
    end
end
```
then we don't have to do all that if/elseif. The else in my sample above can be ripped out if the mob spawns in with the en-effect already active for its element. I do not know if retail does that I have no looked at the capture. if it does we probably want to set a random element at spawn time just so there is no tiny milliseconds gap between its AI trying to swing at you and the variable being set by onMobFight to throw an explainable nil that seemingly can't  be reproduced when you try to reproduce it later :)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Aug 29, 2020 at 21:12:47_

----

considering wiki claims it hits hard as well as having double attack I'm wondering if maybe one of its jobs should be war, but I'll leave well enough alone for now and say this is fine if we have indications besides the additional effect that its a rdm (wiki will often see one thing that looks like what  job has, and then just declare a mob to be that job.. its often wrong or forgets that mobs can have more than 1)


----
<a href="https://github.com/triple-lariat"><img src="https://avatars1.githubusercontent.com/u/30502556?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [triple-lariat](https://github.com/triple-lariat)**
_Saturday Aug 29, 2020 at 23:33:57_

----

There doesn't seem to be any substantial proof that its job is RDM aside from the misconception that it casts its enspell effects. Unless someone more knowledgeable than I am about mob jobs wants to chime in I think I'll go ahead and change its job to WAR.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Saturday Aug 29, 2020 at 23:50:20_

----

https://docs.google.com/spreadsheets/d/1YBoveP-weMdidrirY-vPDzHyxbEI2ryECINlfCnFkLI/edit#gid=0
I'd go with war/pld with a family bonus of 10% defp per jimmayus/meloetta's data. that would give the double attack. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 31, 2020 at 11:39:00_

----

With the job change remember to update the onMobInitialize section. you'd be adding 25 on top of what warrior already gets at this level (setMod instead of addmod would enforce it having only 25, while removing the line would rely on what warrior has native at this lv)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 09:34:50_

----

If there's only simple logic going on, please drop the brackets
```lua
if changeTime == 0 then
    ...
```

Same for the rest of the file etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 09:35:27_

----

newelement -> newElement for clarity please


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 09:44:56_

----

I know you inherited this from what was already in the db, but could we change this to be something a little more descriptive? `provoker_2hr` or something would probably work. That change would need to be reflected here, in this file's name and the entry in mob_skills


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Sep 03, 2020 at 15:56:16_

----

@zach2good it's used by other mobs as well and that is what reports out from actionview in captures. changing the name will make finding and using it potentially difficult.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 18:09:15_

----

Aha, makes sense! Disregard this comment!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 18:10:48_

----

You're almost there, there are still some simple logic blocks (like that while loop) that don't need brackets. Then we're good to go


----
<a href="https://github.com/triple-lariat"><img src="https://avatars1.githubusercontent.com/u/30502556?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [triple-lariat](https://github.com/triple-lariat)**
_Thursday Sep 03, 2020 at 18:27:16_

----

Sorry but are there actually any more unnecessary brackets aside from the while loop? I'm not too familiar with which other brackets may be optional in Lua quite yet, and I don't want to make a bunch of separate commits because I missed something else!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 18:28:37_

----

just me :)


----
<a href="https://github.com/triple-lariat"><img src="https://avatars1.githubusercontent.com/u/30502556?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [triple-lariat](https://github.com/triple-lariat)**
_Wednesday Sep 02, 2020 at 17:15:20_

----

It absolutely slipped my mind! Thanks for letting me know!



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 18:39:01_

----

Merging this into it's own feature branch means that it'll get merged into `canary` in the next update (in a few days maybe). It'll then get battle tested for _some length of time_ and then snuck into `release`. Congrats on your first PR!
