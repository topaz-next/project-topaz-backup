**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Aug 23, 2020 at 20:42:22_
_Originally opened as: project-topaz/topaz - Issue 997_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This was noticed by Hiro (Canaria player) unable to proceed with Axe trial.

Thank you Xastranh (for helping with SQL values) and @jarmengaud  (for testing)


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Aug 27, 2020 at 21:49:24_

----

can grab flags and flag data from here, also is it "the bashe" or "bashe" if just "bashe", then put 32 in the name_prefix field
https://github.com/KnowOne134/NPC-MOB-Logger/blob/557707325c4a9c8a25c8253ced75ca0ca100a120/npclogger/Tables/Sauromugue%20Champaign.lua#L50


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Aug 27, 2020 at 22:01:26_

----

do we not need a mob group to set its level? what level is it spawning as? 
neat to know that it is spawning without setting a spawn_type in mob_groups though,honestly!


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Aug 28, 2020 at 02:40:40_

----

@59blargedy  it has a mob_group.sql  lol

it spawns from 54 to 55

```INSERT INTO `mob_groups` VALUES (49,6583,120,'Bashe',0,32,3142,3300,0,54,55,0);```


----
<a href="https://github.com/Xastranh"><img src="https://avatars1.githubusercontent.com/u/70107447?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xastranh](https://github.com/Xastranh)**
_Friday Aug 28, 2020 at 04:16:02_

----

@59blargedy It should be "The Bashe" when being targeted, based on your LUA pull (which has the flag at 0) and youtube videos found of the fight that supports this ( https://www.youtube.com/watch?v=j0gqdVlKFCU&start=53 ) 

With the the LUA documentation you provided, we've updated EntityFlags (3->139) and animationsub (0->8) Flag itself is still at 0, I'm unable to pull it, even looking at the packet provided in the LUA through PVLV. Any assistance if this needs fixing, or documentation on what exactly 'flag' does (it's a pretty generic name tbh) would be appreciated.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Aug 27, 2020 at 21:49:24_

----

can grab flags and flag data from here, also is it "the bashe" or "bashe" if just "bashe", then put 32 in the name_prefix field
https://github.com/KnowOne134/NPC-MOB-Logger/blob/557707325c4a9c8a25c8253ced75ca0ca100a120/npclogger/Tables/Sauromugue%20Champaign.lua#L50


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Aug 27, 2020 at 22:01:26_

----

do we not need a mob group to set its level? what level is it spawning as? 
neat to know that it is spawning without setting a spawn_type in mob_groups though,honestly!


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Aug 28, 2020 at 02:40:40_

----

@59blargedy  it has a mob_group.sql  lol

it spawns from 54 to 55

```INSERT INTO `mob_groups` VALUES (49,6583,120,'Bashe',0,32,3142,3300,0,54,55,0);```


----
<a href="https://github.com/Xastranh"><img src="https://avatars1.githubusercontent.com/u/70107447?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xastranh](https://github.com/Xastranh)**
_Friday Aug 28, 2020 at 04:16:02_

----

@59blargedy It should be "The Bashe" when being targeted, based on your LUA pull (which has the flag at 0) and youtube videos found of the fight that supports this ( https://www.youtube.com/watch?v=j0gqdVlKFCU&start=53 ) 

With the the LUA documentation you provided, we've updated EntityFlags (3->139) and animationsub (0->8) Flag itself is still at 0, I'm unable to pull it, even looking at the packet provided in the LUA through PVLV. Any assistance if this needs fixing, or documentation on what exactly 'flag' does (it's a pretty generic name tbh) would be appreciated.


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Tuesday Aug 25, 2020 at 18:06:45_

----

I have pulled this change on my test server, and verified that you could pop the NM by killing the placeholder lizard.
I also verified that during the NM only uses Baleful Gaze TP move

-Tokenr


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Aug 28, 2020 at 04:13:52_

----

changes made to flag by @Xastranh  =)


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Aug 28, 2020 at 05:20:06_

----

thank you for rebasing and fixing the conflict @Kreidos 
