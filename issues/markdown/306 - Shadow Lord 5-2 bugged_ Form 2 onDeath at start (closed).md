**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:57_
_Originally opened as: project-topaz/topaz - Issue 306_

----

<a href="https://github.com/DanteMccloud"><img src="https://avatars1.githubusercontent.com/u/19355762?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [DanteMccloud](https://github.com/DanteMccloud)**
_Thursday Jun 27, 2019 at 01:56 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6114_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30190605_0


**_Source Branch_** (master/stable) **:** Master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Currently 5-2 is an auto win. You enter and in 20 seconds it is over.

According to KnowOne, Wiggo, and Lotus it has to do with Shadow Lord Form 2 not being spawned at the start.

before the bcnm rewrite it would flag a mob as dead in its onDeath or whatever and then the bcnm would end when every mob was flagged as killed
it may be something as simple as the flag is set at the start by accident

Lotus says: before the bcnm rewrite it would flag a mob as dead in its onDeath or whatever and then the bcnm would end when every mob was flagged as killed
it may be something as simple as the flag is set at the start by accident

I was thinking maybe ... wouldn't it be easier for 5-2 to set the BCNM win reqs to player mission var 5 and then set form two ondeath to +1 the mission var since you enter at var 3 the "fake death" would set it to 4 and form 1 dies and spawns form 2 and killing it would set it to 5. would that not accomplish basically the same goal? or and i insane?



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 28, 2020 at 15:52:34_

----

I'm going to assume @cocosolos fixed this with bcnm-phase. If not, re-open~
