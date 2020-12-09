**Labels:**

bug



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Sunday Mar 15, 2020 at 02:33:04_
_Originally opened as: project-topaz/topaz - Issue 428_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Currently, if you have any quest that requires a cutscene at the house of the hero in windy woods, the summoner unlock quest reminder takes priority over it.  I've had to have people finish the unlock quest before doing the Wild Card quest event at the house of the hero several times now because they are stuck behind the SMN unlock quest event.  The wiki doesn't say anything about this possibility on the Wild Card quest, and a QoL improvement is to simply move the SMN unlock quest reminder to the bottom of the conditional checks as such:

\scripts\zones\Windurst_Walls\npcs\\_6n2.lua --
```lua
function onTrigger(player,npc)
    local ThePuppetMaster = player:getQuestStatus(WINDURST,tpz.quest.id.windurst.THE_PUPPET_MASTER);
    local ClassReunion = player:getQuestStatus(WINDURST,tpz.quest.id.windurst.CLASS_REUNION);
    local CarbuncleDebacle = player:getQuestStatus(WINDURST,tpz.quest.id.windurst.CARBUNCLE_DEBACLE);
    -- Check for Missions first (priority?)
    if (player:getCurrentMission(WINDURST) == tpz.mission.id.windurst.LOST_FOR_WORDS and player:getCharVar("MissionStatus") == 5) then
        player:startEvent(337);
    else
        ----------------------------------------------------
        -- SMN unlock quest
        if (player:getQuestStatus(WINDURST,tpz.quest.id.windurst.I_CAN_HEAR_A_RAINBOW) == QUEST_AVAILABLE and player:getMainLvl() >= 15 and player:hasItem(1125)) then
            player:startEvent(384,1125,1125,1125,1125,1125,1125,1125,1125);
        ----------------------------------------------------
        -- The Puppet Master (AF weapon)
        elseif (player:getMainLvl() >= AF1_QUEST_LEVEL and player:getMainJob() == tpz.job.SMN and ThePuppetMaster == QUEST_AVAILABLE and player:needToZone() == false and ClassReunion ~= QUEST_ACCEPTED and CarbuncleDebacle ~= QUEST_ACCEPTED) then -- you need to be on SMN as well to repeat the quest
            player:startEvent(402); -- Carby asks for your help, visit Juroro
        elseif (player:getQuestStatus(WINDURST,tpz.quest.id.windurst.THE_PUPPET_MASTER) == QUEST_ACCEPTED and player:getCharVar("ThePuppetMasterProgress") == 1) then
            player:startEvent(403); -- reminder to visit Juroro
        ----------------------------------------------------
        -- Class Reunion (AF pants)
        elseif (player:getMainLvl() >= AF2_QUEST_LEVEL and player:getMainJob() == tpz.job.SMN and ThePuppetMaster == QUEST_COMPLETED and ClassReunion == QUEST_AVAILABLE and player:needToZone() == false) then
            player:startEvent(413); -- Carby asks for your help again.
        ----------------------------------------------------
        -- Carbuncle Debacle (AF head)
        elseif (player:getMainLvl() >= AF3_QUEST_LEVEL and player:getMainJob() == tpz.job.SMN and ClassReunion == QUEST_COMPLETED and CarbuncleDebacle == QUEST_AVAILABLE and player:needToZone() == false) then
            player:startEvent(415); -- Carby begs for your help
        ----------------------------------------------------
		-- SOB Quest Line
        elseif (player:hasKeyItem(tpz.ki.JOKER_CARD)) then
            player:startEvent(387,0,tpz.ki.JOKER_CARD);
        elseif (player:getCharVar("WildCard") == 1) then
            player:startEvent(386);
        elseif (player:getCharVar("OnionRings") == 1) then
            player:startEvent(289);
        elseif (player:getCharVar("KnowOnesOnions") == 1) then
            player:startEvent(288,0,4387);
        ----------------------------------------------------
		-- SMN Unlock quest Reminder
        elseif (player:getQuestStatus(WINDURST,tpz.quest.id.windurst.I_CAN_HEAR_A_RAINBOW) == QUEST_ACCEPTED) then
            player:startEvent(385,1125,1125,1125,1125,1125,1125,1125,1125);
        else
            player:messageSpecial(ID.text.DOORS_SEALED_SHUT); -- "The doors are firmly sealed shut."
        end;
    end;

    return 1;
end;
```



----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Sunday Mar 15, 2020 at 02:38:55_

----

That being said, I see there's another reminder event in there I didn't see before with the PUP quest line.  Perhaps that should be moved behind the SoB cutscenes too.
