**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Thursday Oct 08, 2020 at 04:43:30_
_Originally opened as: project-topaz/topaz - Issue 1275_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

item name in the message is missing. (L64)

https://github.com/project-topaz/topaz/blob/abfe5dda545545f060a761e894c79d55239ada02/scripts/zones/Windurst_Waters/npcs/Angelica.lua#L57-L68

```
                player:startEvent(93, 0, desiredBody, 0, player:getCharVar("QuestAPoseByOtherName_equip")) -- reminder
```


