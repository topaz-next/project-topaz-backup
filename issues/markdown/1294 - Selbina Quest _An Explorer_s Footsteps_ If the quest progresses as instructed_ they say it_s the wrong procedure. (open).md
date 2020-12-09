**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Oct 09, 2020 at 07:52:17_
_Originally opened as: project-topaz/topaz - Issue 1294_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Up to the fifth location, no problem.
Sixth point, the next target is said to be "Batallia Downs", and if you achieve "Batallia Downs", you are told it is not what the instructions say.
The next target area is determined by the following loop process

https://github.com/project-topaz/topaz/blob/5213062798b92405fb84ea90c3399bce75c4bf5e/scripts/zones/Selbina/npcs/Abelard.lua#L103-L113

The parameters of startEvent are configured as follows

player:startEvent(43, 0) -- West Ronfaure
player:startEvent(43, 1) -- East Ronfaure
player:startEvent(43, 2) -- La Theine Plateau
player:startEvent(43, 3) -- Valkurm Dunes
player:startEvent(43, 4) -- Jugner Forest
player:startEvent(43, 5) -- Batallia Downs
player:startEvent(43, 6) -- North Gustaberg
player:startEvent(43, 7) -- South Gustaberg
player:startEvent(43, 8) -- Konschtat Highlands
player:startEvent(43, 9 or over) -- The target is missing.

player:startEvent(49, 0) -- Pashhow Marshlands
player:startEvent(49, 1) -- Rolanberry Fields
player:startEvent(49, 2) -- West Sarutabaruta
player:startEvent(49, 3) -- East Sarutabaruta
player:startEvent(49, 4) -- Tahrongi Canyon
player:startEvent(49, 5) -- Buburimu Peninsula
player:startEvent(49, 6) -- Meriphataud Mountains
player:startEvent(49, 7) -- Sauromugue Champaign
player:startEvent(49, 8 or over) -- The target is missing.

The script's ZoneID table consists of the following.

https://github.com/project-topaz/topaz/blob/5213062798b92405fb84ea90c3399bce75c4bf5e/scripts/zones/Selbina/npcs/Abelard.lua#L18-L37

The cause of this problem may be the "startEvent" and "ZoneID table" where the "Batallia Downs" are in a different order.
I believe the following code could fix this

```
local ZoneID =
{
    0x00001, 800,   -- West Ronfaure
    0x00002, 800,   -- East Ronfaure
    0x00004, 1000,  -- La Theine Plateau
    0x00008, 1000,  -- Valkurm Dunes
    0x00010, 1000,  -- Jugner Forest
    0x10000, 10000, -- Batallia Downs
    0x00020, 3000,  -- North Gustaberg
    0x00040, 800,   -- South Gustaberg
    0x00080, 1000,  -- Konschtat Highlands
    0x00100, 1000,  -- Pashhow Marshlands
    0x00200, 3000,  -- Rolanberry Fields
    0x00400, 800,   -- West Sarutabaruta
    0x00800, 800,   -- East Sarutabaruta
    0x01000, 1000,  -- Tahrongi Canyon
    0x02000, 1000,  -- Buburimu Peninsula
    0x04000, 1000,  -- Meriphataud Mountains
    0x08000, 10000, -- Sauromugue Champaign
}
```

Since we have changed the position of "Batallia Downs", we think we need to change the conditions for "startEvent ID" as well.

```
        else
            local tablets = player:getCharVar("anExplorer-ClayTablets")

            for zone = 1, #ZoneID, 2 do

                if tablets % (2*ZoneID[zone]) < ZoneID[zone] then
                    if zone < 18 then
                        player:startEvent(43, math.floor(zone / 2))
                    else
                        player:startEvent(49, math.floor(zone / 2) -9)
                    end

                    break
                end
            end
        end
```



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Oct 09, 2020 at 12:28:45_

----

@eyes-and-brain I just want to say thank you for finding and opening issues for all these old errors :star: 
