**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:03:14_
_Originally opened as: project-topaz/topaz - Issue 277_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [isotor](https://github.com/isotor)**
_Tuesday Apr 16, 2019 at 12:25 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5854_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30190328_2


**_Source Branch_** (master/stable) **:** master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

As much as I like rocking around town in my Trotters/Crimson Cuisses/Aketon for a base +36% IMS shouldn't be possible. Excerpt from the relevant [wiki page](https://ffxiclopedia.fandom.com/wiki/Movement_Speed):

> - Movement speed modifying equipment will stack with all forms of movement speed effects, other than Chocobo and Cheer.
> - **Boosts to movement from multiple pieces of equipment will not stack with each other. The largest boost is the one the player will receive.**
> - However, movement speed decrease from equipment will stack. 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:03:15_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Apr 16, 2019 at 12:43 GMT_

----

Preference for resolution here: 2 modifiers, one that stacks and one that doesn't. Right now we are using the same mod for both, with negative values for speed decrease.
`MOD_MOVE` <- exists
`MOD_MOVE_NOSTACK` <- doesn't


