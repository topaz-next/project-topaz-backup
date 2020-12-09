**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:52:35_
_Originally opened as: project-topaz/topaz - Issue 224_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Wiggo32](https://github.com/Wiggo32)**
_Saturday May 19, 2018 at 13:34 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4877_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30180427_2


**_Source Branch_** (master/stable) **:** master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Go spawn a pet and check the resistances on it. There are none. 

I think I've isolated the problem to:
github/DarkstarProject/darkstar/blob/2f9765a31516b04da21a65600233db02aafb5bdf/src/map/utils/petutils.cppDarkstar Issue L764
Where spawnpet doesn't seem to be pulling from the database the same way spawnmobpet does right underneath it.
I've tried fiddling with it (basically just attempts to get the code duplicated into the spawnpet function) but haven't had much success. 
I may be way off base here but, this is all I have with my limited programming knowledge.



