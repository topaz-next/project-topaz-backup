**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:46_
_Originally opened as: project-topaz/topaz - Issue 323_

----

<a href="https://github.com/Hokuten85"><img src="https://avatars2.githubusercontent.com/u/13441190?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Hokuten85](https://github.com/Hokuten85)**
_Friday Nov 15, 2019 at 14:54 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6282_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
0.0.8319

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Should be able to reproduce this by attempting to confirmSlot or confirmItem on a trade involving Gil with an amount over 255, and then call trade:confirmTrade(). All of the amount parameters in the functions involved are defined as uint8.

src/map/trade_container.cpp
getConfirmedStatus
setConfirmedStatus

src/map/trade_container.h
getConfirmedStatus
setConfirmedStatus
std::vector<uint32>	    m_confirmed;




----
<a href="https://github.com/SirGouki"><img src="https://avatars3.githubusercontent.com/u/11664236?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [SirGouki](https://github.com/SirGouki)**
_Wednesday Feb 19, 2020 at 07:44:08_

----

This is caused by using uint8 in the affected areas in the source.  Easy fix.  ( I am not currently set up to fix stuff for topaz just yet).

I'd recommend using uint32 since uint16 would limit it to 65535, but I don't know if there's a better type just yet (max gil is 999,999,999, but the max you can trade is 1,000,000 due to anti-RMT patches.), uint32 can hold a value up to 4,294,967,295.  I suspect the trade limit has increased because it was also put on the delivery box, but there are items retail going for 40mil on AH.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 19, 2020 at 11:43:36_

----

@TeoTwawki Was this fixed by https://github.com/project-topaz/topaz/commit/66c9041a04fd299c8e671af168f656c5668d17c1 ?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Feb 19, 2020 at 12:13:36_

----

yes


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 19, 2020 at 12:14:25_

----

Fixed by: https://github.com/project-topaz/topaz/commit/66c9041a04fd299c8e671af168f656c5668d17c1
