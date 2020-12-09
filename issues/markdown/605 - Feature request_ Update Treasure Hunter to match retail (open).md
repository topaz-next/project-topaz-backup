**Labels:**

bug



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Saturday May 09, 2020 at 20:10:00_
_Originally opened as: project-topaz/topaz - Issue 605_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

SE released the mechanism behind treasure hunter recently, but the Topaz model for applying treasure hunter really only matches up with "very common" and "common" items:

![image](https://user-images.githubusercontent.com/37684138/81483872-1a73cb00-91f6-11ea-8dc4-f3153eabedba.png)

We can convert the % drop rate from the mob_droplist table into rarity categories (with quality checks) and adjust the c++ for treasure hunter to apply them correctly.
