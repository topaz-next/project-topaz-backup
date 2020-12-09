**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:47_
_Originally opened as: project-topaz/topaz - Issue 298_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 02, 2019 at 15:27 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6050_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
n/a

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Darkstar Issue Darkstar Issue  Ignore all of this, see new post below.. 

~~canRest() or EFFECTFLAG_NO_REST is basically broken for mobs, I am not sure which and I am to tired and frustrated to dig into this further.~~

The statsus effect disease has the following flags on it:
```cpp
    EFFECTFLAG_DEATH            = 32,   // исчезает при смерти
    EFFECTFLAG_NO_REST          = 4096,   // prevents resting, curse II, plague, disease
    EFFECTFLAG_WALTZABLE        = 16384,   // for healing waltzable spells
    EFFECTFLAG_NO_CANCEL        = 8388608, // CAN NOT CLICK IT OFF IN CLIENT
```
~~If you add it to a mob in onMobSpawn, that mob will still regenerate when idle~~ even though [this code](github/DarkstarProject/darkstar/blob/6b9f3d77eb2201b923160c50d13379d9f3b1ee8a/src/map/entities/battleentity.cppDarkstar Issue L221) in BattleEntity:
```cpp
bool CBattleEntity::CanRest()
{
    return !getMod(Mod::REGEN_DOWN) && !StatusEffectContainer->HasStatusEffectByFlag(EFFECTFLAG_NO_REST);
}
```
which is checked by [THIS CODE](github/DarkstarProject/darkstar/blob/16529492362ce75e42e2e516278809688c371b38/src/map/ai/controllers/mob_controller.cppDarkstar Issue L720) in the **mob controller:**
```cpp
            // can't rest with poison or disease
            if (PMob->CanRest())
            {
                // recover 10% health
                if (PMob->Rest(0.1f))
                {
                    // health updated
                    PMob->updatemask |= UPDATE_HP;
                }

                if (PMob->GetHPP() == 100)
                {
                    // at max health undirty exp
                    PMob->m_giveExp = true;
                }
            }
```
says it should not.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:48_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 02, 2019 at 17:08 GMT_

----

Darkstar Issue Darkstar Issue  SO SOME KNUCKLEHEAD MADE IT SO IF THE ZONE GOES EMPTY, EVERY ENTITY STILL IN IT GETS FULL HIT POINTS WHEN SOMEONE ENTERS AGAIN. OBVIOUSLY NOT WHAT HAPPENS ON RETAIL. EVER.

Some NMs on retail I was only able to solo by zoning them and the resuming the battle before they recovered. Can't do that as it stands on Darkstar.

Separate, unconfirmed: sure as F feels like idle mobs heal quicker here than they do on retail also. Tested by putting a mule in zone so it would not trip the above "empty zone refill" bug.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:49_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Sunday Jun 02, 2019 at 17:52 GMT_

----

I think the only way to handle that is by not suspending the zone timers for unoccupied zones, which obviously has some performance implications.  Maybe we could consider only suspending it if every mob is already full hp, or making a config option to not suspend them



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:51_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 02, 2019 at 18:08 GMT_

----

we should just be restoring the HP the mob previously had on resume, rather than totally resetting it.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:52_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 02, 2019 at 18:09 GMT_

----

Now I wonder - does an empty zone wipe local vars off entities that were in it, like if an NPC uses a localvar for something and the zone goes empty is that lost?

