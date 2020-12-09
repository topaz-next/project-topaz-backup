**Labels:**

bug



<a href="https://github.com/dev-parkins"><img src="https://avatars3.githubusercontent.com/u/6394929?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [dev-parkins](https://github.com/dev-parkins)**
_Thursday Jul 23, 2020 at 20:47:06_
_Originally opened as: project-topaz/topaz - Issue 880_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Steps to Reproduce: 
- Quest Crying Over Onions Flagged
- Thief Level 40
- Speaking with NPC any number of times, will only reference Crying Over Onions quest

Expected Behavior
- First dialogue: Related to Crying Over Onions quest
- Second dialog: Related to Tenshodo Showdown quest

OR

- First Dialogue: Related to Tenshodo Showdown quest
- Second Dialogue: Related to Crying Over Onions quest

Should be some temporary flag to allow next dialogue to execute that is cleared on zone that will mark Mana orb dialogue as read. Alternatively, moving the elseif statement for Tenshodo Showdown before Crying Over Onions should resolve.


----
<a href="https://github.com/dev-parkins"><img src="https://avatars3.githubusercontent.com/u/6394929?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [dev-parkins](https://github.com/dev-parkins)**
_Thursday Jul 23, 2020 at 21:35:42_

----

In $/scripts/zones/Windurst_Woods/npcs/Nanaa_Mihgo.lua:
![image](https://user-images.githubusercontent.com/6394929/88341028-b25f5c00-ccf1-11ea-8439-4848714a5bb8.png)

