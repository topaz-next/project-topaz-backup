**Labels:**

merge ready



<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 22, 2020 at 21:07:10_
_Originally opened as: project-topaz/topaz - Issue 515_

----

• Moved loot tables to casket_loot.lua as it was a bloating caskets.lua.
• Added all remaining zone mixins, treasure_casket.lua's and checked zone ID text tables.
• Added all remaining loot tables for zones added.
• Fixed an issue where a hint would return an incorrect number.
• Fixed an issue where you cannot enter the number 10 as an input.

<!-- place 'x' mark between square [X] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 11:24:24_

----

Thoughts on doing:
```lua
if npc == nil then
    return false
end
```
To immediately abort the rest of the function?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 11:26:53_

----

Got an extra indent on this key


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 28, 2020 at 11:50:23_

----

stupid copy pasta


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 28, 2020 at 11:53:56_

----

thats a good call i'll do that


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 28, 2020 at 11:59:39_

----

im gonna add a check the see if the casket has a local var set for its spawn time too.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 28, 2020 at 12:04:03_

----

Fixed


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 28, 2020 at 12:05:30_

----

Added the the suggested change plus a check for the local var. 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 11:24:24_

----

Thoughts on doing:
```lua
if npc == nil then
    return false
end
```
To immediately abort the rest of the function?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 11:26:53_

----

Got an extra indent on this key


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 28, 2020 at 11:50:23_

----

stupid copy pasta


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 28, 2020 at 11:53:56_

----

thats a good call i'll do that


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 28, 2020 at 11:59:39_

----

im gonna add a check the see if the casket has a local var set for its spawn time too.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 28, 2020 at 12:04:03_

----

Fixed


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 28, 2020 at 12:05:30_

----

Added the the suggested change plus a check for the local var. 
