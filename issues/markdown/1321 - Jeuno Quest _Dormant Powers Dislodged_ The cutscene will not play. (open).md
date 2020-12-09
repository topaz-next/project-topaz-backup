**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Sunday Oct 11, 2020 at 06:42:03_
_Originally opened as: project-topaz/topaz - Issue 1321_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

The cutscene will not play. (Press the Cancel button to complete the quest.)

https://github.com/project-topaz/topaz/blob/238303c14a5ca81f125e00b80bb92bf24378bec2/scripts/zones/RuLude_Gardens/npcs/Nomad_Moogle.lua#L28-L31

Event ID "10138" is wrong.  (L30) This event ID will not play anything.
The correct event ID is "10191".

```
    elseif (trade:hasItemQty(2955,1) == true and trade:hasItemQty(503,1) == true and trade:getGil() == 0 and trade:getItemCount() == 2 and meritCount > 9) then
        if (player:getQuestStatus(JEUNO,tpz.quest.id.jeuno.DORMANT_POWERS_DISLODGED) == QUEST_ACCEPTED) then
            player:startEvent(10191);

```
The correct procedure to follow
https://www.bg-wiki.com/bg/Dormant_Powers_Dislodged

- Speak the the Nomad Moogle again to begin a mini-game.
- When the Nomad Moogle tells you to start, wait ten seconds and then select "Push!".
  - If you are too fast or slow you get to repeat the process.
  - Each time the Nomad Moogle says "..." that counts off one second. For example, the fifth "..." would be the fifth second into the 10 seconds timer.
  - After the screen shows close up's of the participants, it will show a close up of you, once the scene changes to the close up of you, press enter to "Push!"

It's hard for me to make the above mini-game happen in a script.
But if the mini-game is successful, you can play a successful cutscene in the script below.

```
function onTrigger(player,npc)
    elseif (player:getQuestStatus(JEUNO,tpz.quest.id.jeuno.DORMANT_POWERS_DISLODGED) == QUEST_ACCEPTED and player:getCharVar("DormantPowersDislodgedProgress") >= 1) then
        player:startEvent(10192);

function onEventUpdate(player,csid,option)
    if (csid == 10192) then
        player:updateEvent(2);
        player:setCharVar("DormantPowersDislodgedProgress", 2);
    end
```
```
function onEventFinish(player,csid,option)

    elseif (csid == 10191) then
        player:setCharVar("DormantPowersDislodgedProgress", 1);
        player:tradeComplete();
    elseif (csid == 10192) then
        if (player:getCharVar("DormantPowersDislodgedProgress") == 2) then
            player:setMerits(meritCount - 10);
            player:addFame(JEUNO,50);
            player:levelCap(95);
            player:completeQuest(JEUNO,tpz.quest.id.jeuno.DORMANT_POWERS_DISLODGED);
            player:messageSpecial(ID.text.YOUR_LEVEL_LIMIT_IS_NOW_95);
            player:addKeyItem(tpz.ki.SOUL_GEM);
            player:messageSpecial(ID.text.KEYITEM_OBTAINED,tpz.ki.SOUL_GEM);
            player:setCharVar("DormantPowersDislodgedProgress", 0);
        else
            player:setCharVar("DormantPowersDislodgedProgress", 1);
        end
```

