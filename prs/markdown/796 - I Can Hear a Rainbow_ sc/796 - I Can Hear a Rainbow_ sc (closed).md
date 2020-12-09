**Labels:**

merge ready



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Jul 02, 2020 at 15:30:37_
_Originally opened as: project-topaz/topaz - Issue 796_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

* remove from scripts/globals, and rewrite in scripts/quests
* make the color data more easily readable
* localVar the variable used in eventUpdate, which removes the need for onEventFinish
* clear the correct charVar on quest completion
* rainbow controlled by localVar on rainbow NPC, which removes need for server variable

update: per feedback,

* ignore weather set by SCH<sup>1</sup>
* use set constructor for color data
* swap order of quest check vs ruby check

<sup>1</sup>Two issues had to be solved here.  First, there wasn't a way to get weather from zone into LUA.  To resolve this, I added a zone:getWeather() binding.  Second, during onZoneIn, the players's zone is not yet set, causing player:getZone() to return null.  To resolve this, I added an optional bool isZoning parameter to player:getZone(), which will instead return the player's destination zone.



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 15, 2020 at 17:20:25_

----

We have a [set constructor](https://github.com/project-topaz/topaz/blob/release/scripts/globals/common.lua#L35-L45) which will do this for you from a simple table:
```lua
zones = set{
    tpz.zone.VALKURM_DUNES,
    tpz.zone.ROLANBERRY_FIELDS,
    tpz.zone.CAPE_TERIGGAN,
   -- etc
}


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 15, 2020 at 18:26:47_

----

Maybe swap order of quest status check and `hasItem`. HasItem iterates over everything in the bag, whereas quest status is a quick return. Checking for status first means we only ping inventory if player is on the quest.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 15, 2020 at 18:29:22_

----

`entity:getWeather()` will return SCH weather too; are those lost on zoning? Does the effect loss include logging?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 15, 2020 at 20:30:22_

----

use zone entities weather instead. sch 'weather' doesn't work for smn quest


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Jul 15, 2020 at 23:01:08_

----

I don't currently see a way to get zone's weather into LUA, so will have to either add a getWeather binding to lua_zone, and/or add an optional ignoreScholar bool parameter to player:getWeather.  Any preference?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 16, 2020 at 11:47:39_

----

when the object type isn't a player or mob, it assumed we want zone weather:
```lua
inline int32 CLuaBaseEntity::getWeather(lua_State *L)
{
    TPZ_DEBUG_BREAK_IF(m_PBaseEntity == nullptr);

    WEATHER weather = WEATHER_NONE;
    if (m_PBaseEntity->objtype & TYPE_PC || m_PBaseEntity->objtype & TYPE_MOB)
        weather = battleutils::GetWeather((CBattleEntity*)m_PBaseEntity, false);
    else
        weather = zoneutils::GetZone(m_PBaseEntity->getZone())->GetWeather();

    lua_pushinteger(L, weather);

    return 1;
}
```
so you can get the zone (from the player if need be) and then
`zone:getWeather()`
works



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 16, 2020 at 11:49:39_

----

`player:getZone():getWeather()`

for example


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 16, 2020 at 11:51:55_

----

Sorry I see what you are saying about it not being in lua_zone...I thought we already had this functionality in use elsewhere already.

Quick search says I am wrong


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 15, 2020 at 17:20:25_

----

We have a [set constructor](https://github.com/project-topaz/topaz/blob/release/scripts/globals/common.lua#L35-L45) which will do this for you from a simple table:
```lua
zones = set{
    tpz.zone.VALKURM_DUNES,
    tpz.zone.ROLANBERRY_FIELDS,
    tpz.zone.CAPE_TERIGGAN,
   -- etc
}


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 15, 2020 at 18:26:47_

----

Maybe swap order of quest status check and `hasItem`. HasItem iterates over everything in the bag, whereas quest status is a quick return. Checking for status first means we only ping inventory if player is on the quest.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jul 15, 2020 at 18:29:22_

----

`entity:getWeather()` will return SCH weather too; are those lost on zoning? Does the effect loss include logging?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 15, 2020 at 20:30:22_

----

use zone entities weather instead. sch 'weather' doesn't work for smn quest


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Jul 15, 2020 at 23:01:08_

----

I don't currently see a way to get zone's weather into LUA, so will have to either add a getWeather binding to lua_zone, and/or add an optional ignoreScholar bool parameter to player:getWeather.  Any preference?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 16, 2020 at 11:47:39_

----

when the object type isn't a player or mob, it assumed we want zone weather:
```lua
inline int32 CLuaBaseEntity::getWeather(lua_State *L)
{
    TPZ_DEBUG_BREAK_IF(m_PBaseEntity == nullptr);

    WEATHER weather = WEATHER_NONE;
    if (m_PBaseEntity->objtype & TYPE_PC || m_PBaseEntity->objtype & TYPE_MOB)
        weather = battleutils::GetWeather((CBattleEntity*)m_PBaseEntity, false);
    else
        weather = zoneutils::GetZone(m_PBaseEntity->getZone())->GetWeather();

    lua_pushinteger(L, weather);

    return 1;
}
```
so you can get the zone (from the player if need be) and then
`zone:getWeather()`
works



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 16, 2020 at 11:49:39_

----

`player:getZone():getWeather()`

for example


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 16, 2020 at 11:51:55_

----

Sorry I see what you are saying about it not being in lua_zone...I thought we already had this functionality in use elsewhere already.

Quick search says I am wrong


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 02, 2020 at 15:45:44_

----

thankyouwrenthatscriptnamealwaysbotheredme


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Monday Jul 20, 2020 at 00:04:10_

----

Updated PR per feedback.  Description lists changes.
