**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Monday Oct 12, 2020 at 03:37:34_
_Originally opened as: project-topaz/topaz - Issue 1335_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

If you check "Cavernous Maw" in "Batallia Downs", "Rolanberry Fields" or "Sauromugue Champaign", the "Cait Sith" event starts.
After that, the first event when you warp to the past world (the cutscene with Carlisle, Lysander and Barnabas riding in the chocobo) is missing.

https://github.com/project-topaz/topaz/blob/ce4efc04260c6e325e044cc7e30226e705621d74/scripts/zones/Batallia_Downs_%5BS%5D/Zone.lua#L12-L18
You can add a cutscene with the following code
```
function onZoneIn(player, prevZone)
    local cs = -1
    if (player:getXPos() == 0 and player:getYPos() == 0 and player:getZPos() == 0) then
        player:setPos(-500.451, -39.71, 504.894, 39)
    end
    if (player:getCurrentMission(WOTG) == tpz.mission.id.wotg.CAVERNOUS_MAWS) then
      cs = 700
    end
    return cs
end
function onEventFinish(player, csid, option)
    if (csid == 700) then
        player:completeMission(WOTG, tpz.mission.id.wotg.CAVERNOUS_MAWS)
        player:addMission(WOTG, tpz.mission.id.wotg.BACK_TO_THE_BEGINNING)
        player:addKeyItem(tpz.ki.PURE_WHITE_FEATHER)
        player:messageSpecial(ID.text.KEYITEM_OBTAINED, tpz.ki.PURE_WHITE_FEATHER)
    end
end
```
https://github.com/project-topaz/topaz/blob/ce4efc04260c6e325e044cc7e30226e705621d74/scripts/zones/Rolanberry_Fields_%5BS%5D/Zone.lua#L12-L18
You can add a cutscene with the following code
```
function onZoneIn(player, prevZone)
    local cs = -1
    if player:getXPos() == 0 and player:getYPos() == 0 and player:getZPos() == 0 then
        player:setPos(-376.179, -30.387, -776.159, 220)
    end
    if (player:getCurrentMission(WOTG) == tpz.mission.id.wotg.CAVERNOUS_MAWS) then
      cs = 700
    end
    return cs
end
```
https://github.com/project-topaz/topaz/blob/ce4efc04260c6e325e044cc7e30226e705621d74/scripts/zones/Sauromugue_Champaign_%5BS%5D/Zone.lua#L16-L37
You can add a cutscene with the following code
Only "Sauromugue_Champaign_[S]" needed to use "player:updateEvent" to play the cutscene successfully.
```
function onZoneIn(player, prevZone)
    local cs = -1
    if (player:getXPos() == 0 and player:getYPos() == 0 and player:getZPos() == 0) then
        player:setPos(-104, -25.36, -410, 195)
    end
    if (player:getCurrentMission(WOTG) == tpz.mission.id.wotg.CAVERNOUS_MAWS) then
      cs = 700
    elseif (prevZone == tpz.zone.ROLANBERRY_FIELDS_S and player:getQuestStatus(CRYSTAL_WAR, tpz.quest.id.crystalWar.DOWNWARD_HELIX) == QUEST_ACCEPTED and player:getCharVar("DownwardHelix") == 2) then
        cs = 3
    end
    return cs
end
function onEventUpdate(player, csid, option)
  if (csid == 700) then
    player:updateEvent(2);
  end
end
function onEventFinish(player, csid, option)
    if (csid == 3) then
        player:setCharVar("DownwardHelix", 3)
    elseif (csid == 700) then
        player:completeMission(WOTG, tpz.mission.id.wotg.CAVERNOUS_MAWS)
        player:addMission(WOTG, tpz.mission.id.wotg.BACK_TO_THE_BEGINNING)
        player:addKeyItem(tpz.ki.PURE_WHITE_FEATHER)
        player:messageSpecial(ID.text.KEYITEM_OBTAINED, tpz.ki.PURE_WHITE_FEATHER)
    end
end
```

I moved the mission progress flag to "zone.lua" and thought it was ok to remove it from the following
The following code does not display "player:messageSpecial(ID.text.KEYITEM_OBTAINED, tpz.ki.PURE_WHITE_FEATHER)" (L123).
https://github.com/project-topaz/topaz/blob/ce4efc04260c6e325e044cc7e30226e705621d74/scripts/globals/maws.lua#L118-L133

