**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Oct 09, 2020 at 16:07:36_
_Originally opened as: project-topaz/topaz - Issue 1299_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

- You can watch the mission start cutscene as many times as you want. Once you've seen it, the door should be locked.
https://github.com/project-topaz/topaz/blob/bdef7042ccc1791f4e3ae330255fbc5c5b87f1f0/scripts/zones/RuLude_Gardens/npcs/_6r5.lua#L23-L31
```
        elseif player:getRank() == 4 and
            currentMission == tpz.mission.id.sandoria.NONE and
            getMissionRankPoints(player, 13) == 1 and
            MissionStatus == 0
        then
            if player:hasKeyItem(tpz.ki.ARCHDUCAL_AUDIENCE_PERMIT) then
                player:startEvent(130, 1)
            else
                player:startEvent(130)
            end
```

- NPC "Aldo" has the wrong line of dialogue.
NPC "Aldo" is talking about the future where he died before the "Fickblix death cutscene" in Castle Oztroja.
https://github.com/project-topaz/topaz/blob/bdef7042ccc1791f4e3ae330255fbc5c5b87f1f0/scripts/zones/Lower_Jeuno/npcs/Aldo.lua#L22-L23
```
    elseif (player:getCurrentMission(player:getNation()) == tpz.mission.id.nation.MAGICITE) then
      if (player:getCharVar("MissionStatus") <= 3) then
          player:startEvent(161)
      else
          player:startEvent(183)
      end
```

- The dialogues of NPC "Yin Pocanakhu" will change during the mission.
https://github.com/project-topaz/topaz/blob/bdef7042ccc1791f4e3ae330255fbc5c5b87f1f0/scripts/zones/Lower_Jeuno/npcs/Yin_Pocanakhu.lua#L13-L17
```
    if (player:getCharVar("BorghertzHandsFirstTime") == 2) then
        player:startEvent(220)
    elseif (player:getCurrentMission(player:getNation()) == tpz.mission.id.nation.MAGICITE and player:getCharVar("MissionStatus") == 3) then
        player:startEvent(210)
    else
        player:startEvent(209)
    end
```

- The dialogues of NPC "Yin Muckvix" will change during the mission.
https://github.com/project-topaz/topaz/blob/bdef7042ccc1791f4e3ae330255fbc5c5b87f1f0/scripts/zones/Lower_Jeuno/npcs/Muckvix.lua#L15-L23
```
    if player:hasKeyItem(tpz.ki.SILVER_BELL) and not player:hasKeyItem(tpz.ki.YAGUDO_TORCH) then
        if player:getCharVar("YagudoTorchCS") == 1 then
            player:startEvent(184)
        else
            player:startEvent(80)
        end
    elseif (player:getCurrentMission(player:getNation()) == tpz.mission.id.nation.MAGICITE) then
      if player:getCharVar("FickblixCS") == 1 then
          player:startEvent(81)
      else
        player:startEvent(79)
      end
    else
        player:startEvent(15)
    end
```


