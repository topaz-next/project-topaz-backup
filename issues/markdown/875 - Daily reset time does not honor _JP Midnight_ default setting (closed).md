**Labels:**

crafting



<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [jarmengaud](https://github.com/jarmengaud)**
_Monday Jul 20, 2020 at 19:56:21_
_Originally opened as: project-topaz/topaz - Issue 875_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Things that are supposed to reset daily or weekly (tally, guild items,...), are not resetting at JP midnight with default configuration, even though by default:
TIMEZONE_OFFSET = 9.0 -- Offset from UTC used to determine when "JP Midnight" is for the server.  Default is JST (+9.0). 

If you look at the time_server.cpp code, you will see things like:
    //Midnight
    if (CVanaTime::getInstance()->getSysHour() == 0 && CVanaTime::getInstance()->getSysMinute() == 0)

so it is hardcoded that reset will happen at midnight for the server local time zone. And cannot be changed by a configuration either.

Would probably fix:
https://github.com/project-topaz/topaz/issues/22



----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Monday Jul 20, 2020 at 19:57:20_

----

Well of course, you could change the server time zone for JST, but I am not sure admins would like this...


----
<a href="https://github.com/Altalus"><img src="https://avatars1.githubusercontent.com/u/194725?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Altalus](https://github.com/Altalus)**
_Thursday Jul 23, 2020 at 14:43:26_

----

Darkstar had the `vanadiel_time_offset` setting in the `conf/map.conf` but it seems topaz does not :)
