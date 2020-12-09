**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Thursday Oct 01, 2020 at 16:02:33_
_Originally opened as: project-topaz/topaz - Issue 1224_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

The conditional statement is inserted in an improper position. 
If the quest "Trust: San d'Oria" is ACCEPTED, L37-L38 can never be executed.

https://github.com/project-topaz/topaz/blob/8785668a9924bcf3fb4701b565fb92a7abc3979b/scripts/zones/Southern_San_dOria/npcs/Gondebaud.lua#L26-L44

    if player:getMainLvl() >= 5 and ENABLE_TRUST_QUESTS == 1 then
        if TrustSandoria == QUEST_AVAILABLE and (TrustWindurst == QUEST_COMPLETED or TrustBastok == QUEST_COMPLETED) then
            player:startEvent(3504)
        elseif TrustSandoria == QUEST_AVAILABLE and TrustWindurst == QUEST_AVAILABLE and TrustBastok == QUEST_AVAILABLE then
            player:startEvent(3500)
        elseif player:hasKeyItem(tpz.ki.RED_INSTITUTE_CARD) then
            player:startEvent(3501)
        end
    elseif TrustSandoria == QUEST_COMPLETED then
        player:startEvent(3502)
    else
        player:startEvent(3505)
    end





----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Wednesday Oct 07, 2020 at 12:17:58_

----

Again, corrected.

```
if player:getMainLvl() >= 5 and ENABLE_TRUST_QUESTS == 1 then
    if TrustSandoria == QUEST_AVAILABLE and (TrustWindurst == QUEST_COMPLETED or TrustBastok == QUEST_COMPLETED) then
        player:startEvent(3504)
    elseif TrustSandoria == QUEST_AVAILABLE and TrustWindurst == QUEST_AVAILABLE and TrustBastok == QUEST_AVAILABLE then
        player:startEvent(3500)
    elseif player:hasKeyItem(tpz.ki.RED_INSTITUTE_CARD) then
        player:startEvent(3501)
    elseif TrustSandoria == QUEST_COMPLETED then
        player:startEvent(3502)
    end
else
    player:startEvent(3505)
end
```

"Trust : Bastok" does the same.
https://github.com/project-topaz/topaz/blob/dbbb9b698e6a9f1a6bbf87a40249b18d6253821e/scripts/zones/Port_Bastok/npcs/Clarion_Star.lua#L26-L44

```
    if player:getMainLvl() >= 5 and ENABLE_TRUST_QUESTS == 1 then
        if TrustBastok == QUEST_AVAILABLE and (TrustWindurst == QUEST_COMPLETED or TrustSandoria == QUEST_COMPLETED) then
            player:startEvent(438)
        elseif TrustBastok == QUEST_AVAILABLE and TrustWindurst == QUEST_AVAILABLE and TrustSandoria == QUEST_AVAILABLE then
            player:startEvent(434)
        elseif player:hasKeyItem(tpz.ki.BLUE_INSTITUTE_CARD) then
            player:startEvent(435)
        elseif TrustBastok == QUEST_COMPLETED then
            player:startEvent(436)
        end
    else
        player:startEvent(442)
    end
```




----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Thursday Oct 08, 2020 at 03:23:39_

----

"Trust: Windurst" does the same.

https://github.com/project-topaz/topaz/blob/dbbb9b698e6a9f1a6bbf87a40249b18d6253821e/scripts/zones/Windurst_Woods/npcs/Wetata.lua#L26-L44

```
    if player:getMainLvl() >= 5 and ENABLE_TRUST_QUESTS == 1 then
        if TrustWindurst == QUEST_AVAILABLE and (TrustBastok == QUEST_COMPLETED or TrustSandoria == QUEST_COMPLETED) then
            player:startEvent(867)
        elseif TrustWindurst == QUEST_AVAILABLE and TrustBastok == QUEST_AVAILABLE and TrustSandoria == QUEST_AVAILABLE then
            player:startEvent(863)
        elseif player:hasKeyItem(tpz.ki.GREEN_INSTITUTE_CARD) then
            player:startEvent(864)
        elseif TrustWindurst == QUEST_COMPLETED then
            player:startEvent(861)
        end
    else
        player:startEvent(868)
    end
```
