**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Thursday Oct 08, 2020 at 08:51:30_
_Originally opened as: project-topaz/topaz - Issue 1282_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

When you complete a quest, the message "You have obtained 600 gil" is displayed twice, but the actual amount of gil increase is 600 gil. (L16/L19, L38)
Also, the rate is not calculated for some of the acquired gil. (L38)

https://github.com/project-topaz/topaz/blob/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e/scripts/zones/Windurst_Woods/npcs/Illu_Bohjaa.lua#L12-L42

```
function onEventFinish(player, csid, option)
    if csid == 333 and option == 1 then
        player:addQuest(WINDURST, tpz.quest.id.windurst.CREEPY_CRAWLIES)
    elseif (csid == 335)  then
        player:completeQuest(WINDURST, tpz.quest.id.windurst.CREEPY_CRAWLIES)
        player:addTitle(tpz.title.CRAWLER_CULLER)
        player:addGil(GIL_RATE*600)
        player:tradeComplete()
    end
end

```
