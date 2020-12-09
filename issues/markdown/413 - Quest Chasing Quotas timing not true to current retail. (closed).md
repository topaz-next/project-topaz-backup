**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Thursday Mar 12, 2020 at 16:54:05_
_Originally opened as: project-topaz/topaz - Issue 413_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

When you trade Ceraulian the gold hairpin, you must wait until server midnight to continue the quest.  Current retail requires you to wait just one minute.

`    elseif (csid == 17) then
        player:setCharVar("ChasingQuotas_Progress",1);
        player:setCharVar("ChasingQuotas_date", getMidnight());`
