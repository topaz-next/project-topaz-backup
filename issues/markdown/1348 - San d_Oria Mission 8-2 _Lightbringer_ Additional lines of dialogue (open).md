**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Tuesday Oct 13, 2020 at 05:55:35_
_Originally opened as: project-topaz/topaz - Issue 1348_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

- Add a line to the "NPC: Halver" in the "Chateau d'Oraguille" area.
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Chateau_dOraguille/npcs/Halver.lua#L64-L66
```
        elseif (currentMission == tpz.mission.id.sandoria.LIGHTBRINGER and MissionStatus == 2) then
              --  (textID: 6824) 
        elseif
            player:hasCompletedMission(SANDORIA, tpz.mission.id.sandoria.LIGHTBRINGER) and
            player:getRank() == 9 and player:getRankPoints() == 0
        then
            -- (textID: 6836) 
```
The following is an automatic translation of the Japanese client's message. They are slightly different from the messages of our English clients.
(textID: 6824) 
Halver : Report to the King as soon as you're done. Keep this mission as private as possible. I can't let anyone else hear us.
(textID: 6836) 
Halver : I can't believe they finally found the Holy Sword! This will completely relieve my stomach ache: ....... Cohon, no, I am so pleased as a Prime Minister. I don't think so.



