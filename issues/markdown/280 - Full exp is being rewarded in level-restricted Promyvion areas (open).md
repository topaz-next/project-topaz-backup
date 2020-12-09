**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:03:23_
_Originally opened as: project-topaz/topaz - Issue 280_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [isotor](https://github.com/isotor)**
_Friday Apr 19, 2019 at 17:17 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5874_

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

Issue relevant for 75-cap servers. The correct behavior is outlined [here](https://ffxiclopedia.fandom.com/wiki/Promyvion_Guide?oldid=70377):

> Experience earned in a level-capped zone is either... 
> 1) You earn the xp you'd get if your class were at it's full level. 
> 2) You earn 1/2 the xp of your capped job. 
> ... whichever is greater. If you're on a lv31 main capped down to 30, you'll get lots of xp and can do xp chains. If you're on a 60 main capped down to 30, you'll get 1/2 the xp a lv30 would earn, and you can't do xp chains. 

__tl;dr:__ exp should be calculated based on your "uncapped" job level, to a minimum of 50% of the exp a level 30 character would earm _(or 40 for Vahzl)_, and you can't do exp chains.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:03:25_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Apr 19, 2019 at 17:45 GMT_

----

I'm on the fence about implementing this directly into the restriction or as a setting. that was added in to curb ppl using those restricted zones to reach lv cap, and then the restriction was later done away with entirely anyway.

