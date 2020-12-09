**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:08_
_Originally opened as: project-topaz/topaz - Issue 137_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Deadwing888](https://github.com/Deadwing888)**
_Thursday Sep 15, 2016 at 21:28 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3368_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **not a client issue**

**_Server Version_** (type `revision` in game) **f8175463415d4964d3deb2492d73a1bd03b548c6**

**_Source Branch_** (master/stable) **master**

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**

DSP currently has no is no form of curse immunity, which is a big deal for high HP HNM which should not be receiving the curse spikes effect of igqira/genie gear. 

Furthermore MOD_CURSERES was exhibiting unexpected behavior. When given a value of 100, curse effect from misery staff appeared to be a 100% proc rate. When given a value of -100 the proc rate seemed low, but it still proc'd.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:09_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Friday Sep 16, 2016 at 19:47 GMT_

----

Good point, I can take a look at this.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:10_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 20, 2016 at 03:02 GMT_

----

Related: It looks like DSP is treating resist[status] the same as resist[element] which is wrong.

When a resist[status] "procs" its an entirely different chatlog message (its not messageBasic like the existing resist message, its right between cover and magic burst messages in the client) than if you just resist from magic evasion (which is a messageBasic type).

Edit: actually looks like its just an additional short text preceding the usual message, is how the client has it done. `Resist! <usual resist message here>` like when PLD's cover goes off, rather the 2 fully different messages.  In order to have 2 differing messages that way, it seems likely that status resist are checked separately form the meva calculations, in addition to any duration reductions they provide. Wiki's description of Resist Sleep supports this.

https://www.bg-wiki.com/bg/Resist_Sleep

```
Causes the Sleep status effect to be fully resisted a certain percentage of the time, regardless of how it is being inflicted. 
```

http://ffxiclopedia.wikia.com/wiki/Resist_Sleep

```
This trait greatly shortens the duration of sleep type status effects by increasing the chance of half duration resists.
Gives a small chance to completely resist the effect of sleep status. When it procs the text will be preceeded by "Resist!" in a similar fashion to Cover. 
```




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:11_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Tuesday Sep 20, 2016 at 15:54 GMT_

----

Okay so there are actually 3 types of resist sleep. 

Type one is what BG explains, which is similar to what you would get from a trait. It provides a flat dice roll change to resist the spell and gives a resist! message when it does.

Type two is what ffxiclopedia explains. This is the type of res sleep you get from the resist sleep barspell. I have seen it have absolutely no effect on sleep landing rate, but it does decrease duration of the effect once it has landed.

Type three is mobs only, and functions identical to meva (but only for that particular enfeeble). Some debuff resistances are coded this way currently in dsp. It is important that the individual debuff meva be able to accept a negative value. For instance Fafnir is susceptible to paralyze, but not ice nukes. There is currently no way to replicate this behavior because a mod paralyzeres of -100 will cause fafnir's every hit to be paralyzed (even without casting the enfeeble).




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:37:12_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 20, 2016 at 16:11 GMT_

----

The ffxiclopedia page is trying to cover everything not any one type, and then their general resistance page pretty much ignores all of it to focus on meva. Makes it a little difficult to sort out exactly what we should be doing when combined with retails low rates on the traits and gear bonuses. Retail has those gradually build resistance and lose resistance thing as well (immunobreaks). But I think I got us to far off your curse topic.

Pretty much the situation on mobs should be random vs mod_curseres, and if mod_curseres number wins..no curse at all.


