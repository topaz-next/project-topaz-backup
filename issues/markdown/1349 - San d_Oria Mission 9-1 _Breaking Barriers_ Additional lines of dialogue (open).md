**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Tuesday Oct 13, 2020 at 07:26:29_
_Originally opened as: project-topaz/topaz - Issue 1349_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

- Add a line to the "NPC: Halver" in the "Chateau d'Oraguille" area.
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Chateau_dOraguille/npcs/Halver.lua#L61-L63
```
        -- Mission San d'Oria 9-1 Breaking Barriers (optional)
        elseif (currentMission == tpz.mission.id.sandoria.BREAKING_BARRIERS and MissionStatus == 0) then
            player:startEvent(26)
        elseif (currentMission == tpz.mission.id.sandoria.BREAKING_BARRIERS and MissionStatus == 1) then
            player:startEvent(1)
```

