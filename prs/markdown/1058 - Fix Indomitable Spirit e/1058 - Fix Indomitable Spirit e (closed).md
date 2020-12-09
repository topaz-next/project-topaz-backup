**Labels:**

exploit

reviewed



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Saturday Sep 05, 2020 at 00:39:43_
_Originally opened as: project-topaz/topaz - Issue 1058_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes #1057 

Fixes a logic error in his script that allowed players to double trigger this npc to get a free ebisu.

Also makes the timer respect next CQ, not next day as it was originally scripted.

Thanks to Lusiphur for reporting the issue and assisting with the fix ^.^

Testing:
```
1. Gave myself KI Serpent Rumors, ensured quest is not in log
2. Talked to Irmilant, he gave me the dialogue for quest accept, quest shows up in log now.
3. Talked to him several more times, did not give Ebisu as expected, always gives general dialogue.
4. Traded him Saber Shoot and Opal Silk, he correctly gave quest trade dialogue.  Received IndomitableSpiritTimer variable == 1599487200
5. Talked to several times, he always gives "Wait" dialogue.
6. I manually subtracted 1 from my charVar, IndomitableSpiritTimer, to simulate that I got my variable before this current CQ cycle
7. Talked to him again, received dialogue for quest complete, received ebisu rod, and quest shows completed in log.  charVar was cleared from database.
8. Talked to him many times again, always received new general dialogue for those that have completed this quest.
9. Tossed Ebisu rod I just got.
10. Traded the two items needed again, then repeated steps 5-8.
```


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 05, 2020 at 00:45:03_

----

I should also comment that the reason people were able to double trigger this NPC for ebisu to be given without trading the items was because the logic was checking that 1. the player was on the quest and 2. the current day ~= player:getCharVar("IndomitableSpiritVar")... so if the player never had that var set, it would be 0 and this would always be true, giving the rod:

original line 35: ```elseif (Indomitable == QUEST_ACCEPTED or Indomitable == QUEST_COMPLETED) and realday ~= player:getCharVar("IndomitableSpiritVar") then```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 05, 2020 at 09:14:04_

----

Thanks for the follow up testing!
