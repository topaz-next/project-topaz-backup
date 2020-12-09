**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:18_
_Originally opened as: project-topaz/topaz - Issue 272_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [isotor](https://github.com/isotor)**
_Monday Apr 15, 2019 at 05:44 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5843_

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

__Steps to reproduce:__
- Kill a bee at level 2 > get 90 exp > kill another > get 108 exp _(+20% / Chain 1 bonus)_
- You will continue receiving 108 exp for subsequent kills until you take a break _(Chain multiplier doesn't increase further)_
- If you're idle for a few minutes (break the chain timer) and kill another bee, it will award 90 exp again
- This occurs at all levels

---------------------------

__Update/ Clarification:__
- Outside of an existing chain, killing **any** exp-awarding mob [sets the chain modifier to 1](github/DarkstarProject/darkstar/blob/e4c9bc9fd9a17e05f85bb2eb3f43601204b543e7/src/map/utils/charutils.cppDarkstar Issue L3318), enabling +20% exp from any subsequent mobs until the chain time expires. Killing enemies below EM with this modifier active does not print chain notifications to the player (i.e. *"Chain 1! ..."*), but does award +20% exp.

Expected behavior: 
1. only EM+ mobs should set an exp modifier above 0 *(or, "tee up the chain")*
2. only EM+ mobs should give bonus chain exp when a chain is teed up

Unsure what happens on retail if you interrupt a chain with a mob below EM but kill another EM within the original chaintime window *(i.e. I'm not sure if that EP/DC in between resets the chain or is ignored)*



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:19_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [isotor](https://github.com/isotor)**
_Monday Apr 15, 2019 at 05:48 GMT_

----

Just for clarification/ stating the obvious, you shouldn't receive a chain bonus on kills that check below EM: https://ffxiclopedia.fandom.com/wiki/Experience_Chain

> The bonus is obtained by defeating monsters that check as Even Match or tougher (EM+) within a time limit that starts when the last EM+ mob is killed.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:21_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Apr 22, 2019 at 14:43 GMT_

----

clarification needed:
you are chaining things weaker than even or the chain bonus is failing to higher when it is actually supposed to?

coz I know I can't chain easy prey's on stock darkstar master (normally)



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:22_

----

<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Apr 22, 2019 at 14:59 GMT_

----

Now that TeoTwawki has prompted me, I've tried killing (DC) bees at Lv2 for 90xp, but a chain never forms. I'm not sure what sort of madness I was under before when I thought I had a fix for this...



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:24_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday May 14, 2019 at 23:43 GMT_

----

> Unsure what happens on retail if you interrupt a chain with a mob below EM but kill another EM within the original chaintime window (i.e. I'm not sure if that EP/DC in between resets the chain or is ignored)

if you kill a weaker mob but then still kill the EM or higher tier mob before the time is up, it still continues the chain. mobs below EM are just straight up ignored and the real condition is only time since last EM+ was killed



----
<a href="https://github.com/TrueSalmon"><img src="https://avatars1.githubusercontent.com/u/16270541?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TrueSalmon](https://github.com/TrueSalmon)**
_Monday Nov 09, 2020 at 19:50:17_

----

If you kill a chainworthy mob (EM or higher) while under the influence of the "fake chain 1" you can get real chain 1 on the EM or higher and the subsequent EP-DC kills will be "fake chain 2" exp, so x1.24.
