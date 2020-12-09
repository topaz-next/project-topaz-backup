**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Monday Aug 31, 2020 at 01:02:30_
_Originally opened as: project-topaz/topaz - Issue 1044_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

When you kill the 4th skeleton and the 5th skele pops, the chest pops as well, so you can just get the booty and peace.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Monday Aug 31, 2020 at 01:43:15_

----

Problem is here:     
```
if reraises == 4 then
    mob:getBattlefield():setLocalVar("lootSpawned", 0)
end
```
in Ghul-I-Beaban.lua... this causes the loot to spawn after the 4th reraise.
