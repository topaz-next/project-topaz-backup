**Labels:**

bug



<a href="https://github.com/SirGouki"><img src="https://avatars3.githubusercontent.com/u/11664236?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [SirGouki](https://github.com/SirGouki)**
_Friday Mar 06, 2020 at 01:58:56_
_Originally opened as: project-topaz/topaz - Issue 403_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

server branch: master

- [x] searched existing issues (http://github.com/project-topaz/topaz/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

NOTE: I'm using the term delay in this context to refer to resetting auto attack, making you wait the full time till your next attack.

Reproduction:
  use /ja "" <t> to activate a job ability after it is on cool down, during combat.
  for example, attempt to steal from an enemy, then repeatedly use /ja "Steal" <t> or a macro that contains that.  You will never auto attack as this is resetting the auto attack delay even though the skill isn't firing (and not all JA's should be doing this in the first place i.e. dances allow you to attack while using them)

Expected:
  /ja commands should not be triggering a delay on Job Abilities that do not normally trigger a delay, nor should it be causing a delay if the JA is on cool down.  Retail does not do this.

This was first brought to my attention by Tankfest from Resolute, and it is happening on a clean Topaz-master server on my LAN, with all job abilities.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Friday Mar 06, 2020 at 02:03:36_

----

https://www.youtube.com/watch?v=Lf6-Zbp8XM0
thanks to Luzzy@Resolute for showcasing this.
