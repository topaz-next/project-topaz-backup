**Labels:**

WIP



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Thursday Feb 20, 2020 at 09:37:12_
_Originally opened as: project-topaz/topaz - Issue 362_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

**TODO:**
Clean up commit history
Verify EXP bonus is suitable
Test Gilgamesh's sub job letter workflow front to back
Address the rest of the PR comments

**Doing in later PRs:**
Balance Ophiotaurus and Siren fights
Other Rhapsody in .* bonuses

**DONE:**
Structure of RoV 1-1 to 1-18 ✔️ 
Handling of Mhuara/Selbina paths ✔️ 
CS's in all starting zones ✔️ 
Undo auto-format in status.lua etc. ✔️ 
Triple check my port didn't squish anyone else's changes ✔️ 
Push to my server and make available for testing ✔️ 
Replace things that were squished in topaz port ✔️ 
KeyItem based subjob handling ✔️ 
Testing: Ring My Bell: First character lockout and use of `rhapsodies.lua`: ✔️ 

**Testing Notes:**
All RoV missions from 1-1 to 1-18 are scripted.
You will need to set ENABLE_ROV to 1
Later on you will need rank 3
Towards the end you will need to set you nation mission to 16 (defeated shadowlord)

**Mhaura path:**
!setplayervar <name> RhapsodiesStatus 2

**Selbina path:**
!setplayervar <name> RhapsodiesStatus 1

**Items for SET_FREE:**
Ekokoko:
!additem 9083 3

Abelard
!additem 9082 3

**Ophiotaurus spawn:**
!setmission 13 20
