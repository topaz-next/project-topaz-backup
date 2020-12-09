**Labels:**



<a href="https://github.com/TableCafe"><img src="https://avatars2.githubusercontent.com/u/40038940?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [TableCafe](https://github.com/TableCafe)**
_Wednesday Sep 16, 2020 at 05:07:04_
_Originally opened as: project-topaz/topaz - Issue 1144_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Empyrean aftermaths do not give the proper proc chance of 30%, 40%, 50% for the three tiers of TP.

![image](https://user-images.githubusercontent.com/40038940/93294396-5af0e000-f7b8-11ea-9a43-b5b6eca9def1.png)
[https://www.bg-wiki.com/bg/Empyrean_Aftermath](url)

https://github.com/project-topaz/topaz/blob/9c8ca0c0c5f4c8dc98bc9deb9d72c0d4ebad59b1/src/map/utils/attackutils.cpp#L164-L169

based on the code in attackutils.cpp the mod power is divided by 10, meaning the power in the aftermath LUA needs to be increased by a factor of 10 in order to give the proper proc rate.

https://github.com/project-topaz/topaz/blob/9c8ca0c0c5f4c8dc98bc9deb9d72c0d4ebad59b1/scripts/globals/aftermath.lua#L185-L204

In my testing the current setup gives us a 3%, 4%, 5% proc rate.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Sep 16, 2020 at 05:10:16_

----

Somebody forgot we use 1000 to represent 100% so that we can hand partial percentage points like 12.5%
