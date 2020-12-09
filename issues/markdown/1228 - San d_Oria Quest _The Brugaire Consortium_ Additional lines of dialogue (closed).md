**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Oct 02, 2020 at 01:10:33_
_Originally opened as: project-topaz/topaz - Issue 1228_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

If the quest "The Brugaire Consortium" is QUEST_COMPLETED, the NPC "Fontoumant" is unresponsive.

https://github.com/project-topaz/topaz/blob/2c5b97f1f742b54162b49dc842aee44085c41e9e/scripts/zones/Port_San_dOria/npcs/Fontoumant.lua#L44-L64

If the quest "The Brugaire Consortium" is QUEST_COMPLETED, the event "561" should be executed.

    local TheBrugaireConsortium = player:getQuestStatus(SANDORIA, tpz.quest.id.sandoria.THE_BRUGAIRE_CONSORTIUM)

    if (TheBrugaireConsortium == QUEST_AVAILABLE) then
        player:startEvent(509)
    elseif (TheBrugaireConsortium == QUEST_ACCEPTED) then

        local prog = player:getCharVar("TheBrugaireConsortium-Parcels")
        if (prog == 11) then
            player:startEvent(511)
        elseif (prog == 21) then
            player:startEvent(512)
        elseif (prog == 31) then
            player:startEvent(515)
        else
            player:startEvent(560)
        end
    else
        player:startEvent(561)
    end

