**Labels:**



<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Sunday Sep 13, 2020 at 12:00:25_
_Originally opened as: project-topaz/topaz - Issue 1122_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

When I talk to Angelica of Windurst Waters, the quest does not start.

https://github.com/project-topaz/topaz/blob/ef5935b2ed20a6710422cfebd8b0f2940addbaf1/scripts/zones/Windurst_Waters/npcs/Angelica.lua#L18-L22

If the conditions for starting the quest are met, Event ID:87 will be executed.

https://github.com/project-topaz/topaz/blob/ef5935b2ed20a6710422cfebd8b0f2940addbaf1/scripts/zones/Windurst_Waters/npcs/Angelica.lua#L70-L98

onEventFinish has nothing to do with event ID:87.
When the quest starts in onEventFinish, the event ID:92 is provided, which does not match the event ID in onTrigger.




----
<a href="https://github.com/eyes-and-brain"><img src="https://avatars0.githubusercontent.com/u/71148313?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [eyes-and-brain](https://github.com/eyes-and-brain)**
_Sunday Sep 13, 2020 at 12:03:10_

----

Sorry, I think I misunderstood a bit. I'll close it once.
