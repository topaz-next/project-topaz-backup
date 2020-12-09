**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Saturday Oct 03, 2020 at 05:03:36_
_Originally opened as: project-topaz/topaz - Issue 1238_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Wrong NPC message.

https://github.com/project-topaz/topaz/blob/7adb2f5daffdd497b763c58b986783d39e7a6664/scripts/zones/Davoi/npcs/Zantaviat.lua#L15-L32

    if (CurrentMission == tpz.mission.id.sandoria.THE_DAVOI_REPORT and player:getCharVar("MissionStatus") == 0) then
        player:startEvent(100)
    elseif (CurrentMission == tpz.mission.id.sandoria.THE_DAVOI_REPORT) then
        if (player:hasKeyItem(tpz.ki.LOST_DOCUMENT)) then
            player:startEvent(104)
        elseif (player:hasKeyItem(tpz.ki.TEMPLE_KNIGHTS_DAVOI_REPORT)) then
            player:showText(npc, ID.text.AAAA);
        else
            player:showText(npc, ID.text.BBBB);
        end
    elseif (CurrentMission == tpz.mission.id.sandoria.INFILTRATE_DAVOI and infiltrateDavoi and player:getCharVar("MissionStatus") == 0) then
        player:startEvent(102)
    elseif (CurrentMission == tpz.mission.id.sandoria.INFILTRATE_DAVOI and player:getCharVar("MissionStatus") == 9) then
        player:startEvent(105)
    else
        player:startEvent(101)
    end

"ID.text.AAAA" has the value "7410".
"ID.text.BBBB" has the value "7485".

wrong direction of NPC.
The retail NPC "Xanthavia" is hiding behind a tree.
Topaz's NPC 'Xanthaviat' is facing the opposite direction and is not hiding behind a tree.




----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Sunday Oct 04, 2020 at 06:11:22_

----

> wrong direction of NPC.
> The retail NPC "Xanthavia" is hiding behind a tree.
> Topaz's NPC 'Xanthaviat' is facing the opposite direction and is not hiding behind a tree.

I would like to add to the above.
The initial orientation of the NPCs is correct.

If player talk to the  "Zantaviat", the NPC rotates its direction to the player's direction. The problem is that the direction of the NPC "Zantaviat" does not return to its original orientation afterwards.
The problem may be that using player:showText causes the NPC's orientation to rotate in the direction of the player.


----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Sunday Oct 04, 2020 at 06:59:08_

----

When the mission "The Davoi Report" is received more than twice, the following steps must be repeated.
- Walk South until you reach a pond at (J-8). On the South bank of the pond you will find a ! target. Click on it to receive the Key ItemLost document.
- Return to Zantaviat to recieve the Key ItemTemple Knights' Davoi report.

However, the current implementation of topaz does not seem to support repeating this mission more than twice.
The mission doesn't progress even after talking to the NPC "Zantaviat".
When I talk to a guard NPC "Ambrotien", I get a fanfare for completing the mission, but the mission status is still in progress.
It will be impossible to complete any other San d'Oria missions in the future.
