**Labels:**

good first issue

research needed



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Thursday Nov 26, 2020 at 18:56:25_
_Originally opened as: project-topaz/topaz - Issue 1535_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

It came up in a discussion between me and @TeoTwawki: When picking `Trick Attack` targets, we just iterate through all alliance/party members (and now trusts), and then check to see if they're in the right place for TA.

What about huge shared events like Domain Invasion? What about on a mob that's been "Call for Help"'d?

Initial thinking is that it checks the mob's enmity list and excludes pets, but includes players and trusts. 

Retail research on this would be much appreciated.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Nov 26, 2020 at 19:05:43_

----

additional thought: can another person trick onto my adventuring fellow in such situations?
