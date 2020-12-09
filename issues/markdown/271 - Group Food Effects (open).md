**Labels:**

bug

feature



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:14_
_Originally opened as: project-topaz/topaz - Issue 271_

----

<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Tuesday Apr 09, 2019 at 10:51 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5831_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30190305_0


**_Source Branch_** (master/stable) **:** master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Group food effects don't affect multiple people. They should, and have scaling strength depending on party size.

The script for each of these foods (ie. black_curry_bun (5758)) has a TODO for the group effect.
Following discussion in github/DarkstarProject/darkstar - PR 5827, it should now be possible to start handling whole party buffs. 

**Links**
https://ffxiclopedia.fandom.com/wiki/Black_Curry_Bun
https://www.bg-wiki.com/bg/Lebkuchen_House
https://www.bg-wiki.com/bg/Gat._aux_Fraises



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:15_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Apr 09, 2019 at 12:14 GMT_

----

```
Group food effects don't affect multiple people.
```
pretty sure most of them do, https://ffxiclopedia.fandom.com/wiki/Group_Food_Effects

for stuff that changes based on party size, I suggest using a latent if it has to change dynamically, and effect:getPower() and the like if it does not.

Latents were recently made scriptable



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:16_

----

<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Apr 09, 2019 at 12:24 GMT_

----

Ah, I meant currently in master, rather than what the expected behavior is. At least in the quick testing I did with `black_curry_bun` in a party. Thanks for the heads up about latents, I'll take a look 👍 

