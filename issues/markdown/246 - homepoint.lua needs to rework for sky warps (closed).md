**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:45_
_Originally opened as: project-topaz/topaz - Issue 246_

----

<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [ShelbyZ](https://github.com/ShelbyZ)**
_Sunday Dec 16, 2018 at 18:02 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5487_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [🔫] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [🔫] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
30181205+0

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
github/DarkstarProject/darkstar/blob/2992d2ac7dbfccb2e08f30f593b484bc554c3619/scripts/globals/homepoint.luaDarkstar Issue L178
When warping around sky the option is 3 and would not charge the player.

github/DarkstarProject/darkstar/blob/2992d2ac7dbfccb2e08f30f593b484bc554c3619/scripts/globals/homepoint.luaDarkstar Issue L179
The above does produce an hpIndex within the homepoints table when option is 3

github/DarkstarProject/darkstar/blob/2992d2ac7dbfccb2e08f30f593b484bc554c3619/scripts/globals/homepoint.luaDarkstar Issue L188
We should no longer call setPos on the player as the event will handle teleporting the player.  We may also consider removing the x,y,z, rotation and zone from the table.




----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Monday Mar 09, 2020 at 18:03:18_

----

Hello. I'm unable to produce any issue regarding Homepoint teleports in Sky on master as of 03/09/2020. It was probably fixed in Nation teleport changes PR by Cryptexx back in october 2019. Feel free to reopen an issue if you come across something new. Thank you.
