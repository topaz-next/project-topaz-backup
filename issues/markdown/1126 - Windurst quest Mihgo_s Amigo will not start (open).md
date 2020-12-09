**Labels:**



<a href="https://github.com/residentevil80"><img src="https://avatars2.githubusercontent.com/u/54491714?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [residentevil80](https://github.com/residentevil80)**
_Sunday Sep 13, 2020 at 15:39:23_
_Originally opened as: project-topaz/topaz - Issue 1126_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

https://ffxiclopedia.fandom.com/wiki/Mihgo%27s_Amigo
I no not have any of the quests or items to cause it to be blocked. I DO however have the trust permit.  I do not have the requirements to get her as a trust and that  is the only dialog she presents.


----
<a href="https://github.com/residentevil80"><img src="https://avatars2.githubusercontent.com/u/54491714?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [residentevil80](https://github.com/residentevil80)**
_Sunday Sep 13, 2020 at 15:50:29_

----

client ver 30200731_2 if that helps



----
<a href="https://github.com/residentevil80"><img src="https://avatars2.githubusercontent.com/u/54491714?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [residentevil80](https://github.com/residentevil80)**
_Sunday Sep 13, 2020 at 22:54:09_

----

Took a chance. Updated server (canary version) to the newest as of 9/13/20 (chat fix) and updated to latest client. Still will not give quest. 


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Wednesday Nov 04, 2020 at 13:25:01_

----

I confirm the issue. The TRUST quest is taking precedence even if you don't have started or done the Amigo quest:

    -- TRUST
    elseif player:hasKeyItem(tpz.ki.WINDURST_TRUST_PERMIT) and not player:hasSpell(901) then
        local trustFlag = (player:getRank() >=3 and 1 or 0) + (mihgosAmigo == QUEST_COMPLETED and 2 or 0)

        player:startEvent(865, 0, 0, 0, TrustMemory(player), 0, 0, 0, trustFlag)

So if you have the Windurst permit this event will be repeated, but not giving you the trust since the Amigo quest is not done.
The script to do the Amigo quest is further down, so not reachable.
