**Labels:**

bug

help wanted



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:46:02_
_Originally opened as: project-topaz/topaz - Issue 192_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Oct 17, 2017 at 18:17 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4133_

----

Retail validation needed for several cases. So we'll need a retail player with access to a few of these items.

All our "Enchantment: Ensomething" items that do enspell effects are wrong.

They call this with a nil spell (coz they are not a spell)

```lua
function doEnspell(caster,target,spell,effect)

    if (effect==EFFECT_BLOOD_WEAPON) then
        target:addStatusEffect(EFFECT_BLOOD_WEAPON,1,0,30);
        return;
    end

    local duration = 180;
    if (caster:hasStatusEffect(EFFECT_COMPOSURE) == true and caster:getID() == target:getID()) then
        duration = duration * 3;
    end
    --calculate potency
    local magicskill = target:getSkillLevel(ENHANCING_MAGIC_SKILL);

    local potency = 3 + math.floor((6*magicskill)/100);
    if (magicskill>200) then
        potency = 5 + math.floor((5*magicskill)/100);
    end

    if (target:addStatusEffect(effect,potency,0,duration)) then
        spell:setMsg(230);
    else
        spell:setMsg(75);
    end
end;
```

So that setMsg() call fails, and so does the calculating based on enfeeb skill on most cases since it'll be a melee job using the item. Pretty sure these don't even vary like that in retail anyway. Coz they aren't an actual enspell.

So we need `doEnspell()` [replaced ](github/DarkstarProject/darkstar/blob/5078b8b1b71c30af4a5fbcb9075787e5a9a3cd3f/scripts/globals/items/aero_mufflers.luaDarkstar Issue L20)with `target:addStatusEffect()` with retail basepower and duration. 

Most of the power values are likely on wiki. I did a quick check and saw effect power mentioned but not duration. I don't think the last all the way to the items recast.

Go forth minions! This is an easy job for anybody that can craft or purchase a few enspell enchanted items on retail.

**Not to be confused with items that have "Additional Effect: something" on them. Don't even touch those or add any new ones at this time.**

Of course if I am wrong about any of the above after checking on retail, please post that here.




----
<a href="https://github.com/gweivyth"><img src="https://avatars2.githubusercontent.com/u/37130689?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [gweivyth](https://github.com/gweivyth)**
_Wednesday Mar 18, 2020 at 03:19:51_

----

Packets and YouTube video attached. 

https://youtu.be/N2Tp5hkK-xY

[packets_3.17.2020-23_10_36.txt](https://github.com/project-topaz/topaz/files/4346772/packets_3.17.2020-23_10_36.txt)



----
<a href="https://github.com/gweivyth"><img src="https://avatars2.githubusercontent.com/u/37130689?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [gweivyth](https://github.com/gweivyth)**
_Wednesday Mar 18, 2020 at 03:25:24_

----

@TeoTwawki <3  Hey buddy. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 18, 2020 at 17:44:23_

----

That bot garbles some things when it imports issues off the other project..

No packets are needed btw. just need values plugged in to whatever script as an addStatusEffect.

Wrong:
```lua
function onItemUse(target)
    local effect = tpz.effect.ENAERO
    doEnspell(target,target,nil,effect)
end
```

Right:
```lua
function onItemUse(target)
    target:addStatusEffect(tpz.effect.ENAERO, powerHere, 0, durationHere)
end
```

