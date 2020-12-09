**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:27_
_Originally opened as: project-topaz/topaz - Issue 290_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [isotor](https://github.com/isotor)**
_Wednesday May 08, 2019 at 04:57 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5984_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30190328_2


**_Source Branch_** (master/stable) **:** master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

![Untitled546](https://user-images.githubusercontent.com/43398624/57349840-59df8580-7164-11e9-8ad8-e90eb737ce85.png)

Image shows "Sanction received" message *(also received buff - cropped out)* when blown off by an Imperial Gate Guard for not meeting the required rank for interaction. Issue resulting from c6ca2a4 which omitted `if csid ==` check when transitioning from NPC to global script.

