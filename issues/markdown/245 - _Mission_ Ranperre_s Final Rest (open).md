**Labels:**

bug

good first issue



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:40_
_Originally opened as: project-topaz/topaz - Issue 245_

----

<a href="https://github.com/Ninjistix"><img src="https://avatars1.githubusercontent.com/u/12572974?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Ninjistix](https://github.com/Ninjistix)**
_Friday Dec 07, 2018 at 03:57 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5445_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [X] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [X] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
30181103_0

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

San d'Oria Mission 6-2

The steps for 

* Return to Prince Trion who'll instruct you to go see the Gate Guard. The Gate Guard will tell you that it will take some time to decipher. 
-does not work, visiting the prince room does nothing, but talking to the guard twice will make him accept the KI.

* Zone and talk to the guard again who will tell you to see Prince Trion.
-does not work, I checked the code and it has a wait clause of 1 gameday before the guard lets you progress

edit: removed remaining steps, worked as normal.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:41_

----

<a href="https://github.com/zynjec"><img src="https://avatars3.githubusercontent.com/u/17911103?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zynjec](https://github.com/zynjec)**
_Friday Dec 07, 2018 at 03:59 GMT_

----

The gate guard is currently doing a real life day wait (which should have been a game day wait to begin with), but now it seems to be instant/requires zoning on retail.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:42_

----

<a href="https://github.com/Ninjistix"><img src="https://avatars1.githubusercontent.com/u/12572974?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Ninjistix](https://github.com/Ninjistix)**
_Friday Dec 07, 2018 at 04:06 GMT_

----

yeah according to https://www.bg-wiki.com/bg/San_d%27Oria_Mission_6-2

and a few other guides I found for the mission, it should be just a zone and not the wait.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:43_

----

<a href="https://github.com/tagban"><img src="https://avatars1.githubusercontent.com/u/7320004?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [tagban](https://github.com/tagban)**
_Friday Dec 07, 2018 at 13:50 GMT_

----

Ran into this before. Can be pretty easily adjusted iirc.

