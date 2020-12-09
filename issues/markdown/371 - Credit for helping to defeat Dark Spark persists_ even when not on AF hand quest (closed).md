**Labels:**

bug

good first issue



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Saturday Feb 22, 2020 at 02:00:53_
_Originally opened as: project-topaz/topaz - Issue 371_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
In the script for Dark Spark, [no check is done in the `onMobDeath` before setting a `charVar` giving the player credit for killing it](https://github.com/project-topaz/topaz/blob/master/scripts/zones/Castle_Zvahl_Baileys/mobs/Dark_Spark.lua#L10-L12). This includes when you are assisting someone else with the quest and are not on the quest yourself.

If you later try to complete the quest yourself, and [manage to select the same torch as the last one which Dark Spark was spawned from (barring anything which would wipe the mob's local variable), you will instantly be given the key item without spawning it, due to already possessing credit](https://github.com/project-topaz/topaz/blob/master/scripts/zones/Castle_Zvahl_Baileys/npcs/Torch.lua#L19-L20).



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 18, 2020 at 22:24:59_

----

Fixed by #398 
