**Labels:**



<a href="https://github.com/davismj"><img src="https://avatars2.githubusercontent.com/u/3845823?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [davismj](https://github.com/davismj)**
_Wednesday Oct 14, 2020 at 00:16:29_
_Originally opened as: project-topaz/topaz - Issue 1356_

----

Duration was 60, should be 90 according to all sources.

The `applyPlayerResistance` method in monstertpmoves.lua had its signature updated a long time ago, changing the 5th argument from the spell school to the accuracy bonus. Sleepga was not updated and so was receiving a flat accuracy bonus of tpz.skill.ELEMENTAL_MAGIC (38, I think). I've removed that.

Accordiong to ffxiclopedia, Sleepga was supposed to receive an unknown accuracy bonus based on summoning skill. These generally are some factor of summoning magic skill over cap. I've added that bonus with a factor of 1.0.

Sources
- https://www.bg-wiki.com/bg/Sleepga_(Blood_Pact)
- https://ffxiclopedia.fandom.com/wiki/Sleepga_(Blood_Pact)
- http://wiki.ffo.jp/html/2230.html

Closes #257

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [ ] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/davismj"><img src="https://avatars2.githubusercontent.com/u/3845823?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [davismj](https://github.com/davismj)**
_Wednesday Oct 14, 2020 at 00:19:25_

----

is there a table for ice element?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 15, 2020 at 11:32:05_

----

`spell_data` is already required by `magic`, no big deal, just reference for next time 👍 


----
<a href="https://github.com/davismj"><img src="https://avatars2.githubusercontent.com/u/3845823?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [davismj](https://github.com/davismj)**
_Wednesday Oct 14, 2020 at 00:19:25_

----

is there a table for ice element?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 15, 2020 at 11:32:05_

----

`spell_data` is already required by `magic`, no big deal, just reference for next time 👍 
