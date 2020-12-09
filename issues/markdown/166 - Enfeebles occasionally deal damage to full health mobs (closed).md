**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:36_
_Originally opened as: project-topaz/topaz - Issue 166_

----

<a href="https://github.com/UnknownX7"><img src="https://avatars1.githubusercontent.com/u/12263784?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [UnknownX7](https://github.com/UnknownX7)**
_Monday Mar 13, 2017 at 06:29 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3799_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30170204_1


**_Server Version_** (type `revision` in game) **:** 3eca6693a8092e5bfaba056e780f3807f84a75d0
Also happens on ERA's private server.


**_Source Branch_** (master/stable) **:** master


**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
Casting (and landing) any enfeeble (sleep, paralyze, slow, silence, blind, bind, etc) on a mob that has never been damaged before (works on mobs claimed with dispel) will result in some types of mobs taking 1%-3% of their HP in damage. The type of mob that this works on is random, I have tried it on mobs in multiple areas, including Promyvion - Holla and Abyssea - Konschtat, sometimes the mob will stay at full health, but once you find a mob type that it works on, it will work on every one of those mobs. Resetting the area will change the type of mobs that it works on. Allowing the mob to reset afterwards, without attacking it, will cause the mob to never recover that HP. This is also reflected on other clients, anyone can see the mob lose HP and zoning in afterwards will still display them as if they were missing HP. However, damaging the mob and resetting it will cause it to heal back to full and it will no longer lose health upon enfeebling it. This also ends up happening if the mob dies and respawns; it can only happen when its the mob's first spawn.





----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Monday Mar 09, 2020 at 21:37:48_

----

Hello. This issue is related to (and a duplicate of) https://github.com/project-topaz/topaz/issues/14 but it's documented so linking them both can help. I wasn't able to reproduce this with the spells listed except for Bind so I'm going to close this one. Feel free to reopen an issue if you come across something similar, please. Thank you.
