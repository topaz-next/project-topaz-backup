**Labels:**



<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [m241dan](https://github.com/m241dan)**
_Thursday Aug 20, 2020 at 14:50:50_
_Originally opened as: project-topaz/topaz - Issue 985_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

I believe we need a family mixin for Uragnites to support their "going into shell" behaviour.

https://www.bg-wiki.com/bg/Category:Uragnite

Their TP moves will also need to be updated because they are only supposed to use certain TP moves while in shell vs out of shell.



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 20, 2020 at 16:30:23_

----

for the skills: mixin can change the skill list and we use 2 lists ***or*** check the animationsub value in onMobSkillcheck in the involved skills. I am not aware of any exceptions an NM might have to the in shell/out shell rules on this.
