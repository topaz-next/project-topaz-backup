**Labels:**

merge ready



<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [InoUno](https://github.com/InoUno)**
_Friday May 01, 2020 at 16:44:20_
_Originally opened as: project-topaz/topaz - Issue 564_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Added the [Tuning In](https://ffxiclopedia.fandom.com/wiki/Tuning_In) quest.

[Test video](https://www.youtube.com/watch?v=iwGovfoC8F8)

First time making a PR here. Let me know if anything should be done differently!


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday May 02, 2020 at 18:10:38_

----

If you make this line elseif csid ==886 and npcUtil.compleQuest.... then
    Player:tradeComplete()
End. 

Then it will only take the trade if it in facts completes the quest


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday May 02, 2020 at 18:11:06_

----

Can you space the params as you did rest please


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday May 02, 2020 at 18:12:47_

----

gil = 4000 * GIL_RATE,

For custom servers with custom gil rate


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday May 02, 2020 at 18:13:10_

----

Spaces between commas


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Saturday May 02, 2020 at 18:33:28_

----

Sure thing. This was just moved down from a few lines above.


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Saturday May 02, 2020 at 18:34:40_

----

I believe the `completeQuest` function handles this already:

https://github.com/project-topaz/topaz/blob/0e8fdf88df9f644fb47d037ab253e97f69cdbb84/scripts/globals/npc_util.lua#L361-L364


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Saturday May 02, 2020 at 18:40:55_

----

Good call!


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday May 02, 2020 at 18:10:38_

----

If you make this line elseif csid ==886 and npcUtil.compleQuest.... then
    Player:tradeComplete()
End. 

Then it will only take the trade if it in facts completes the quest


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday May 02, 2020 at 18:11:06_

----

Can you space the params as you did rest please


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday May 02, 2020 at 18:12:47_

----

gil = 4000 * GIL_RATE,

For custom servers with custom gil rate


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday May 02, 2020 at 18:13:10_

----

Spaces between commas


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Saturday May 02, 2020 at 18:33:28_

----

Sure thing. This was just moved down from a few lines above.


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Saturday May 02, 2020 at 18:34:40_

----

I believe the `completeQuest` function handles this already:

https://github.com/project-topaz/topaz/blob/0e8fdf88df9f644fb47d037ab253e97f69cdbb84/scripts/globals/npc_util.lua#L361-L364


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Saturday May 02, 2020 at 18:40:55_

----

Good call!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday May 02, 2020 at 14:33:03_

----

Welcome, thanks for this PR!

I haven't tested the quest yet, but from a high level look everything seems OK! Just some style issues:

**Parens, no need for extras:**
```
if var == 1 then
    ...
end
```

**Try to use npcUtil when you can:**
https://github.com/project-topaz/topaz/blob/release/scripts/globals/npc_util.lua

Here's some examples:

**Checking the contents of a trade:**
https://github.com/project-topaz/topaz/blob/8985d2af68876367592222836db1f8e5b15c8175/scripts/globals/strangeapparatus.lua#L300

**Completing a Quest:**
https://github.com/project-topaz/topaz/blob/trust/scripts/zones/Heavens_Tower/npcs/Kupipi.lua#L221-L222



----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Saturday May 02, 2020 at 14:59:47_

----

Thanks for the pointers! I'll get right on making the changes.


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Saturday May 02, 2020 at 15:16:42_

----

Changes have been made. 
Although now the lines I've added stand out in the file, because the rest of the file doesn't follow those style guidelines yet :P


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Tuesday May 05, 2020 at 02:14:14_

----

Changes are in, and I've verified that the quest still works.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday May 05, 2020 at 06:59:40_

----

LGTM! 👍 
