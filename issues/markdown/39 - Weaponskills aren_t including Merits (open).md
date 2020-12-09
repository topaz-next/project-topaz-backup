**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:44_
_Originally opened as: project-topaz/topaz - Issue 39_

----

<a href="https://github.com/naurond"><img src="https://avatars0.githubusercontent.com/u/13634564?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [naurond](https://github.com/naurond)**
_Tuesday Aug 04, 2015 at 02:22 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 1867_

----

There's either code missing in weaponskill.lua or too much code in battleutils/attackround.cpp

Let's take triple attack for example:

battleutils.cpp and attackround.cpp both get MOD_TRIPE_ATTACK_RATE into tripleAttack (or however they're exactly called), then checks if the character has the TA trait and if so it adds MERIT_TRIPLE_ATTACK_RATE to the tripleAttack to get the total.

weaponskill.lua only gets the MOD_TRIPLE_ATTACK_RATE but never checks for the MERIT_...

So either battleutils and attackround have a too high rate (if MOD_... already includes MERIT_...) or the weaponskills have a too low rate (if MOD_... does not include MERIT_...).

This applies to other merits for weaponskills as well, like double attack, critrate and probably some others I can't recall right now (possibly accuracy (ambush)?).


