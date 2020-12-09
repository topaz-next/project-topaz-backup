**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:44_
_Originally opened as: project-topaz/topaz - Issue 232_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jul 15, 2018 at 13:57 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5088_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
n/a

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
I messed up in Darkstar Issue 5028 by forgetting I can't get entities across map servers. I knew gotoPlayer worked cross map server so swapped it into where setPos was thinking it was an easy/quick fix.. I knew the function I was using took the name as input and did `entity:getName()` but if the leader is in a diff map server we have no pointer to get the name from. or get their `isInMogHouse()` result. My thoughts are: I either need the name of a party leader stored someplace where we don't at all do that yet so I can use sql query to get info on that character OR I need the message server to tell the appropriate map server to do this crap. neither is appealing to me, suggestions welcome.


(*yes* I know spoilers testing blah blah, I still tested that better than half our contributor pull requests do - I at least didn't break anything else while not really fixing the problem,)


