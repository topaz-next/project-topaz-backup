**Labels:**

bug



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Feb 22, 2020 at 23:42:41_
_Originally opened as: project-topaz/topaz - Issue 376_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

The following zones are missing skylines
Xarcabard [S]
Beaucedine Glacier [S]
Castle Zvhal Bailey [S]


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Feb 22, 2020 at 23:51:41_

----

What do you mean by missing skylines?


----
<a href="https://github.com/Setz0r"><img src="https://avatars0.githubusercontent.com/u/3248222?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Setz0r](https://github.com/Setz0r)**
_Saturday Feb 22, 2020 at 23:54:15_

----

this is the result of the zone's initial weather not being set properly.  these zones do not support clear weather, so it will render as black void.

needs to be set to .normal instead of .common.

also the zone in packet does not contain proper weather information.

zone structure needs to include "previous weather" and related timestamps.  

I had added a struct for weather info
```c
struct weatherInfo_t
{
    WEATHER         weather;
    uint32          timestamp;
    uint16          transitionTime;
};

    weatherInfo_t   m_prevWeather;          // Previous Weather
    weatherInfo_t   m_weather;              // Current Weather
    weatherInfo_t   m_nextWeather;          // Next Weather
```
zone in packet:
```c

    ref<uint16>(0x68) = PChar->loc.zone->GetWeather().weather;
    ref<uint16>(0x6A) = PChar->loc.zone->GetPrevWeather().weather;
    ref<uint32>(0x6C) = PChar->loc.zone->GetWeather().timestamp;
    ref<uint32>(0x70) = PChar->loc.zone->GetPrevWeather().timestamp;
    ref<uint16>(0x74) = PChar->loc.zone->GetWeather().transitionTime;
    ref<uint16>(0x76) = PChar->loc.zone->GetPrevWeather().transitionTime;
```



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Feb 22, 2020 at 23:55:09_

----

oh so the literal backgound of the zone then
