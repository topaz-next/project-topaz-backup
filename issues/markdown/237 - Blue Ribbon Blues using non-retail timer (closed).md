**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:13_
_Originally opened as: project-topaz/topaz - Issue 237_

----

<a href="https://github.com/davismj"><img src="https://avatars2.githubusercontent.com/u/3845823?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [davismj](https://github.com/davismj)**
_Sunday Jul 29, 2018 at 09:55 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5151_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 


**_Source Branch_** (master/stable) **:** 


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Kerutoto won't return the purple ribbon. See step 4:

http://ffxiclopedia.wikia.com/wiki/Blue_Ribbon_Blues




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:14_

----

<a href="https://github.com/davismj"><img src="https://avatars2.githubusercontent.com/u/3845823?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [davismj](https://github.com/davismj)**
_Sunday Jul 29, 2018 at 10:01 GMT_

----

Current code is this.

```lua
local timerDay = player:getVar("BlueRibbonBluesTimer_Day");
local currentDay = VanadielDayOfTheYear();

if (player:getVar("BlueRibbonBluesTimer_Year") < VanadielYear()) then
    player:startEvent(360); --  go to the grave  360
elseif (timerDay + 1 == VanadielDayOfTheYear() and player:getVar("BlueRibbonBluesTimer_Hour") <= VanadielHour()) then
    player:startEvent(360); --  go to the grave  360
elseif (timerDay + 2 <=  VanadielDayOfTheYear()) then
    player:startEvent(360); --  go to the grave  360
else
    player:startEvent(359); -- Thanks for the ribbon 359
end
```

Was changed from 1 VD day to a simple zone around 2016.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:16_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Sunday Jul 29, 2018 at 15:26 GMT_

----

updated your comment with syntax highlighting (click edit to see how)



----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Friday Oct 09, 2020 at 23:53:41_

----

Closed via #1033 
