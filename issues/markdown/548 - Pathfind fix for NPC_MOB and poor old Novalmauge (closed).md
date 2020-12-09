**Labels:**

hold



<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 29, 2020 at 22:55:33_
_Originally opened as: project-topaz/topaz - Issue 548_

----

• Addition of npcBasicPath to pathfind.lua, this pathfind function requires paths to be set in a linear fashion like this example
local path =
{
    [1] = {1.000, 2.000, 3.000},
    [2] = {2.000, 2.000, 3.000},
    [3] = {3.000, 2.000, 3.000},
    [4] = {2.000, 2.000, 3.000}
}
This way the path returns to the origin from the last path point to the first, i.e a circle.
the npcBasicPath will keep track of what path point the npc is on by the newly added m_pathPoint in npcentity.

• As stated above i have added a m_pathPoint to npcentity and given the the entity a getter and setter to help keep track of the npc's path.

• Adjusted Novalmauge's script to reflect the changes.

He's walk animation still seems a bit buggy but its about as good as i could get it.
But atleast it shouldn't crash the server anymore.
 
This should fix the following bug
Novalmauge causes server crash due to pathing. #493

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Aug 22, 2020 at 08:47:17_

----

I think you've taken care of all semicolons and random things in Lua, but if you could take a merge of release just to be sure that would be grand
