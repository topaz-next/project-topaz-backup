**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Friday Oct 02, 2020 at 12:54:00_
_Originally opened as: project-topaz/topaz - Issue 1232_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

If the quest "The Medicine Woman" is QUEST_ACCEPTED or QUEST_COMPLETED, the message of the NPC should change.

https://github.com/project-topaz/topaz/blob/50e64bd5fa324a22e260b5c79a3213fb3510d186/scripts/zones/Northern_San_dOria/npcs/Abeaule.lua#L26-L51
```
    elseif (medicineWoman == QUEST_ACCEPTED) then
        if (player:hasKeyItem(tpz.ki.COLD_MEDICINE) == false) then
            -- Abeaule : Grandma Amora's house is in Hound Alley. Well, if you don't know what it is, you can ask someone on the street. Well, good luck with that.
            player:showText(npc, ID.text.AAAA)
        else 
            player:startEvent(614)
        end
    else
        -- Abeaule : I can't thank you enough for all the help you've given me, I just can't thank you enough.
        player:showText(npc, ID.text.BBBB)

    end
```

"ID.text.AAAA" has the value "11325".
"ID.text.BBBB" has the value "11327".

https://github.com/project-topaz/topaz/blob/50e64bd5fa324a22e260b5c79a3213fb3510d186/scripts/zones/Southern_San_dOria/npcs/Amaura.lua#L24-L48

```
        elseif (amaurasFormulaKI == true) then
        -- Amaura : When you have gathered everything you need, you can bring it here. Then I will make you some medicine to cure the common cold.
           player:showText(npc, ID.text.AAAA)
        -- Amaura : Take those pills with you as soon as possible.
        elseif (coldMedicine == true) then
           player:showText(npc, ID.text.BBBB)
```

"ID.text.AAAA" has the value "8016".
"ID.text.BBBB" has the value "8019".



