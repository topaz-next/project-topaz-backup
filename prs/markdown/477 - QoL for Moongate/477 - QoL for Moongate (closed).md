**Labels:**

merge ready



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Apr 08, 2020 at 06:46:26_
_Originally opened as: project-topaz/topaz - Issue 477_

----

Moongate now open from 18:00 to 6:00 on full moon.
Removed semicolons at the end, and removed parenthesis on if statements.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 10:42:41_

----

Will the moon still be "full" after the final night? We wouldn't want to accidentally leave the doors untargetable. 😉


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Apr 08, 2020 at 16:38:12_

----

change to
    elseif IsMoonFull() then
as
    elseif hour == 6 and GetNPCByID(ID.npc.MOONGATE_OFFSET):untargetable() then
didnt work for some reason even tho it looks legit (i just didnt want to be valid on every single vanaday).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 09, 2020 at 01:18:02_

----

We might be able to set up a timer when we _open_ the door, but it's probably not worth it - setting it to false once a real-life hour isn't expensive (and might actually be cheaper than adding an additional timer).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 08, 2020 at 10:42:41_

----

Will the moon still be "full" after the final night? We wouldn't want to accidentally leave the doors untargetable. 😉


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Apr 08, 2020 at 16:38:12_

----

change to
    elseif IsMoonFull() then
as
    elseif hour == 6 and GetNPCByID(ID.npc.MOONGATE_OFFSET):untargetable() then
didnt work for some reason even tho it looks legit (i just didnt want to be valid on every single vanaday).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 09, 2020 at 01:18:02_

----

We might be able to set up a timer when we _open_ the door, but it's probably not worth it - setting it to false once a real-life hour isn't expensive (and might actually be cheaper than adding an additional timer).
