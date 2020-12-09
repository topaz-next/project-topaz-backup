**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Saturday Sep 19, 2020 at 18:46:17_
_Originally opened as: project-topaz/topaz - Issue 1163_

----

**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

The code for the Red Mage Artifact quest **Enveloped in Darkness** (RDM AF2) seems to be outdated if one can trust either [ffxiclopedia.fandom](https://ffxiclopedia.fandom.com/wiki/Enveloped_in_Darkness) or [bg-wiki](https://www.bg-wiki.com/bg/Enveloped_in_Darkness). The last step of this quest is an interaction with a ??? in Crawler's Nest which takes two key items and then waits for the next day to turn over to be able to click again and receive the item **Warlock's Boots**.

The code for this quest is written in [/scripts/zones/Crawlers_Nest/npcs/qm8.lua](https://github.com/project-topaz/topaz/blob/release/scripts/zones/Crawlers_Nest/npcs/qm8.lua)

The file still uses a real day wait timer from back in the day for this, when on the wiki sites it says "max 40s" and "re-zone". **I did not create a pull request for this as I wouldn't know the *exact* timing used by current retail.** But from common sense it seems that the timer was simply removed and due to server connectivity it may take some time. Making a re-zone condition is just pretty contrary to the current retail concept it would seem.

The variable is set on line [19-20](https://github.com/project-topaz/topaz/blob/6a1473ca2640d5226c2571b097de305adb171a3e/scripts/zones/Crawlers_Nest/npcs/qm8.lua#L19):
*(btw note how the comment refers to an old unused variable)*

    local cdate = player:getCharVar("theCrimsonTrial_date")
    local realday = tonumber(os.date("%j")) -- %M for next minute, %j for next day

And the check for this is made from line [22-27](https://github.com/project-topaz/topaz/blob/6a1473ca2640d5226c2571b097de305adb171a3e/scripts/zones/Crawlers_Nest/npcs/qm8.lua#L22), specifically on line 24-27:

    if (player:hasKeyItem(tpz.ki.CRAWLER_BLOOD) == true and player:hasKeyItem(tpz.ki.OLD_BOOTS) == true) then
        player:startEvent(4)
    elseif (cprog == 1 and cdate == realday) then
        player:messageSpecial(ID.text.EQUIPMENT_COMPLETELY_PURIFIED)
    elseif (cprog == 1 and cdate ~= realday) then
        player:startEvent(5)

From what it seems this check could be simply removed and instead say only `elseif (cprog == 1) then player:startEvent(5)` to click the ??? twice and receive the quest reward. But again, I have no means to confirm the *exact* retail code for this. I'm referring to the common wiki entries.

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**  

Accept the quest "Enveloped in Darkness" and get to the point where you "bury" the two necessary key items ([line 44](https://github.com/project-topaz/topaz/blob/6a1473ca2640d5226c2571b097de305adb171a3e/scripts/zones/Crawlers_Nest/npcs/qm8.lua#L44)). Click again immediately or wait a bit and click again. Line 25 will execute. Should be given quest reward instead.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Sep 19, 2020 at 22:26:03_

----

its ~40s or zone (prolly takes at least that long to zone anyway) we can do this with a localvar instead of charvar
