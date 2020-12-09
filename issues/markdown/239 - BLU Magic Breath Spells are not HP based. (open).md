**Labels:**

bug

focus



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:19_
_Originally opened as: project-topaz/topaz - Issue 239_

----

<a href="https://github.com/Dynas13"><img src="https://avatars0.githubusercontent.com/u/36946058?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Dynas13](https://github.com/Dynas13)**
_Saturday Sep 08, 2018 at 08:01 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5221_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
30180427_4

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
All breath spells for BLU are using MND as a modifier for it's damage. This is incorrect. MND is used to determine the additional effect like silence, burn, frost, etc. The damage itself should be based on current HP. To reproduce just lower your current hp and use spell. Raise HP and use spell, spell damage is virtually the same. 

Different breath spells have different HP modifiers.
Heat Breath is 50% current HP
Frost Breath is 33% current HP
Flying Hip Press is 33% current HP
Hecatomb Wave is 25% current HP
Radiant Breath is 20% current HP
Magnetite Cloud is 16% current HP
Bad Breath is 12% current HP
Poison Breath is 10% current HP




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:20_

----

<a href="https://github.com/waterlgndx"><img src="https://avatars0.githubusercontent.com/u/1085232?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [waterlgndx](https://github.com/waterlgndx)**
_Saturday Sep 08, 2018 at 18:15 GMT_

----

Some sample links to bg:
https://www.bg-wiki.com/bg/Frost_Breath
https://www.bg-wiki.com/bg/Hecatomb_Wave
https://www.bg-wiki.com/bg/Heat_Breath

github/DarkstarProject/darkstar/blob/77dfdcdaebac7d4fdd4c1d630593eda3df5f56c8/scripts/globals/spells/bluemagic/heat_breath.luaDarkstar Issue L44 

from github/DarkstarProject/darkstar/blob/master/scripts/globals/bluemagic.lua lines 43-46
```
INT_BASED = 1;
CHR_BASED = 2;
MND_BASED = 3;
```
lines 199-210
```
    local statBonus = 0;
    local dStat = 0; -- Please make sure to add an additional stat check if there is to be a spell that uses neither INT, MND, or CHR. None currently exist.
    if (statMod == INT_BASED) then -- Stat mod is INT
        dStat = caster:getStat(dsp.mod.INT) - target:getStat(dsp.mod.INT)
        statBonus = (dStat)* params.tMultiplier;
    elseif (statMod == CHR_BASED) then -- Stat mod is CHR
        dStat = caster:getStat(dsp.mod.CHR) - target:getStat(dsp.mod.CHR)
        statBonus = (dStat)* params.tMultiplier;
    elseif (statMod == MND_BASED) then -- Stat mod is MND
        dStat = caster:getStat(dsp.mod.MND) - target:getStat(dsp.mod.MND)
        statBonus = (dStat)* params.tMultiplier;
    end
```

I haven't really gone through the rest of the source to be able to tell if this is something that could be achieved by adding a `statMod` of `HP_BASED` but maybe that'd be a place to start?  The dmg formulas look like they might be a bit different for each spell but I'd think dsp has something to support the variants already.  For example one of the notes in heat breath reads: 

> Base damage is equal to players current HP divided by 2, but is subject to fractional resists.

I'm guessing other spells are also subject to fractional resists? (is that the same as an elemental resist? or is it more extreme?)



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:22_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Saturday Sep 08, 2018 at 22:14 GMT_

----

I believe the main problem with this is that the formulas for mob BLU breath spells aren't known. If they were to use the player formulas, they'd just one shot everyone with the spells.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:23_

----

<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Sep 08, 2018 at 22:30 GMT_

----

The formula is know not the resist and rates

On Sat, Sep 8, 2018, 5:14 PM Hozu <notificationsgithub.com> wrote:

> I believe the main problem with this is that the formulas for mob BLU
> breath spells aren't known. If they were to use the player formulas, they'd
> just one shot everyone with the spells.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 5221Darkstar Issue issuecomment-419676289>,
> or mute the thread
> <github/notifications/unsubscribe-auth/Ah94A5nqE9iqfvm3QAqsKtVaSke1V4UGks5uZEE0gaJpZM4WfxXv>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:24_

----

<a href="https://github.com/hargrave81"><img src="https://avatars1.githubusercontent.com/u/4106934?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [hargrave81](https://github.com/hargrave81)**
_Thursday Apr 18, 2019 at 11:05 GMT_

----

While the resistance rates may not be specifically known, can they not be generalized to help make this ability slightly more accurate?

