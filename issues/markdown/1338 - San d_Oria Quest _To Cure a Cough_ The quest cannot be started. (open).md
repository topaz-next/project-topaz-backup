**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Monday Oct 12, 2020 at 08:04:13_
_Originally opened as: project-topaz/topaz - Issue 1338_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

The wiki has the following instructions
https://www.bg-wiki.com/bg/To_Cure_a_Cough
- Once you have heard Nenne's story, go into the first house on Watchdog Alley (G-7) and go upstairs into a bedroom and on the table there is a ???. Click this and the option to read a diary will appear. Finish reading the diary entirely (continue paging through) to continue to the next portion.
- Speak to Amaura (G-6) who will ask for Thyme moss.

In progress, you need to read the diary to page 3. (L28)
The defect condition is "toCureaCough == QUEST_ACCEPTED" (L27)
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Southern_San_dOria/npcs/Diary.lua#L14-L31

The condition that the "Quest" is ACCEPTED is that the NPC "Amaura" generates the event ID 645 (L40)
However, this event ID "645" does not occur until you read the diary to page 3.
There is an inconsistency between the diary and the NPC "Amaura".
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Southern_San_dOria/npcs/Amaura.lua#L38-L40
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Southern_San_dOria/npcs/Amaura.lua#L63-L64

I think we can remove the requirement that the third page of the diary be displayed.
```
    elseif diaryPage == 2 then
        if medicineWoman == QUEST_COMPLETED and aSquiresTestII == QUEST_COMPLETED then
                player:startEvent(641)  -- reads page 3
        end
```

As an addendum, there is a lack of variation in the dialogue.
https://github.com/project-topaz/topaz/blob/2283a60ac71724ba1e82f604efca3c47498dd83a/scripts/zones/Southern_San_dOria/npcs/Amaura.lua#L38-L46
```
    elseif (player:getCharVar("DiaryPage") == 3 or toCureaCough == QUEST_ACCEPTED) then
        if (player:hasKeyItem(tpz.ki.THYME_MOSS) == false and player:hasKeyItem(tpz.ki.COUGH_MEDICINE) == false) then
            player:startEvent(645) -- need thyme moss for cough med
        elseif (player:hasKeyItem(tpz.ki.THYME_MOSS) == true) then
            player:startEvent(646) -- receive cough med for Nenne
        elseif (player:hasKeyItem(tpz.ki.COUGH_MEDICINE) == true) then

           -- Amaura : Hurry up and get that cough medicine.Off you go. I'm sure it will come in handy.
          
        end
```

The text ID is "7943".
You should see the following lines
"Amaura : Hurry up and get that cough medicine.Off you go...I'm sure it will come in handy."
Add "tpz.ki.COUGH_MEDICINE" to the parameter for inserting the item name in the line.
