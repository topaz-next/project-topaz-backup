**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:08_
_Originally opened as: project-topaz/topaz - Issue 129_

----

<a href="https://github.com/dwardlow"><img src="https://avatars1.githubusercontent.com/u/21171687?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [dwardlow](https://github.com/dwardlow)**
_Monday Aug 22, 2016 at 10:27 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3324_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
N/A

**_Server Version_** (type `revision` in game) **:**
Current

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**

The Dhalmel "Healing Breeze" MobAbility is correctly flagged as AoE in the database, but currently it is only healing the caster (the mob itself), and is not healing anyone/anything else (such as a Beastmaster who has charmed the mob. It triggers a message stating that the Beastmaster has recovered X HP, however they are never actually healed!)

From what I can see this appears to be due to an incorrect parameter in Healing_Breeze.lua

I think that the line 
_return MobHealMove(mob, mob:getMaxHP() \* potency / 100);_
should probably be changed to 
_return MobHealMove(target, mob:getMaxHP() \* potency / 100);_
in order for the mob's PAI targets to properly get the heal applied against them.

(see the similar skills spring_water.lua and whispering_wind.lua which both return _MobHealMove(target, HealValue)_)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:36:09_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Monday Aug 22, 2016 at 18:28 GMT_

----

AoE mobskills that target itself/other mobs are currently only affecting mobs of the same family as the user. That will require a change in the core somewhere.


