**Labels:**

bug

feature



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:09:09_
_Originally opened as: project-topaz/topaz - Issue 311_

----

<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Friday Aug 16, 2019 at 04:25 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6194_

----

Using this issue to track Dynamis TODOs as I work my way through adding our stuff to DSP. If anyone fixes any of these points, please reference this issue and I'll keep this list up-to-date.

* Check/add droplists for all mobs. (Done: Va, Bu, Qu, Ta)
* Figure out how Jeuno lottery NMs work, and code their spawn mechanics.
* Check NMs for missing immunities, spells, skills, true detection, battle mechanics.
* Code usable items, such as those that lock NM abilities.
* What do Vanguard Eyes do?
* NMs in Dreamworld zones should use dreamworld mixin, even if they're beastmen? [BgWiki indicates so](https://www.bg-wiki.com/bg/Category:DynamisDarkstar Issue Special_Proc_System_Notes_for_.22Dreamworld.22_zones).




----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Saturday Jul 25, 2020 at 13:52:34_

----

For Jeuno NMs: 
It seems that the server will spawn a given NM 10 minutes after kill, rotating the 2 or 3 possible IDs for this NM.
I have no idea why they do this, for us it would be much simpler to decrease respawn rate and keep only 1 ID per NM (they have mostly the same spawn position also)

