**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Tuesday Aug 18, 2020 at 21:19:54_
_Originally opened as: project-topaz/topaz - Issue 973_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

From Wiki:  "Receives a damage immunity effect at 1% HP.  Must be hit by a Buccaneer's Knife (which can be stolen from it) to remove its damage immunity effect."

This needs to be coded.

Thanks to Nireya@GoldSaucer for reporting this issue.





----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Aug 18, 2020 at 21:36:42_

----

Related: our "unkillable" flag prevents any hp loss. we need a version that lets hp go down but prevents death - if you try to script this to just flag unkillable at low HP, you can bypass the immunity by doing enough damage to jump over the point it would kick in.
