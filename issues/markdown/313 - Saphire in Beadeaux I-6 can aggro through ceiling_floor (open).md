**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:12_
_Originally opened as: project-topaz/topaz - Issue 313_

----

<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Sep 17, 2019 at 00:45 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6221_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
30190904_2

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
walk on the top part in I-6 in Beadeaux while level 75 and you should be able to aggro monsters that are below the floor.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:13_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 17, 2019 at 19:33 GMT_

----

with or without a navmesh in the zone?

This is expected behavior when there is no navmesh, because we really don't have a good way of preventing it without a navmesh without making the mobs nearsighted. What I did for zones I wasn't planning to give a navmesh in was modify `CMobController::CanDetectTarget` to restrict the height a little bit more. That's in the `mob_controller` source code. As a side effect mobs will fail to properly aggro near small ledges.. The default is 8 yalms I think. In retail vertical range is huge unless there is an obstacle. with no navmesh, there are no obstacles.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:14_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 17, 2019 at 19:39 GMT_

----

```
 you should be able
```
I read that as "shouldn't".  If they are supposed to and are not...Entirely diff problem than I was addressing :rofl: 



----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Saturday Feb 22, 2020 at 01:15:19_

----

Actually they should NOT be able to in retail and they in fact are doing so on Topaz. Can confirm this killed me this morning during LB3+Magicite. I believe what he meant was "if you try this, you should be able to aggro them to reproduce the bug when it is not supposed to happen normally". Please correct me if this is a wrong interpretation of your bug @kaincenteno 
