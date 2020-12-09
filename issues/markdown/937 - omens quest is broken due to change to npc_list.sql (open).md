**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Aug 13, 2020 at 20:01:51_
_Originally opened as: project-topaz/topaz - Issue 937_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

this commit https://github.com/project-topaz/topaz/commit/5fc387b866d97b1a53529d4594c854696280861c#diff-6fe9cc5ac0dffa35ca0107b315426647 renamed the npc 17056406 in npc_list.sql to blank which does not match the lua file name, it also looks that other might have been renamed back to blank (like npc 17056405)

Thank you lemon. tokenr and amira in Canaria server for helping raise this issue.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Aug 13, 2020 at 20:12:44_

----

Before my npc_list update, 17056405 and 17056406  had names of "14" and "15", which didn't have any matching lua scripts.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Thursday Aug 13, 2020 at 20:39:28_

----

maybe it might be cause the blue branch is not yet on "release" and they got overwritten once it goes merged into "canary"

I did double check and 17056405 is not tied to any script so we are good with 14 being renamed =)

but i'm confused about 17056408 i see it named "qm" in npc_list.sql but on the script itself it went from 16 to blank_toau20.lua. (havent done aht ughan missions so i haven't tested this)
