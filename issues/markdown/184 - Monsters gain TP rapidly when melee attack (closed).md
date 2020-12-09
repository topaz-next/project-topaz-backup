**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:11_
_Originally opened as: project-topaz/topaz - Issue 184_

----

<a href="https://github.com/ghost"><img src="https://avatars3.githubusercontent.com/u/10137?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [ghost](https://github.com/ghost)**
_Sunday Aug 06, 2017 at 06:24 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3969_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30170707_1


**_Server Version_** (type `revision` in game) **:** 
Revision: d428456385e41c5120155badf126d8c8c1981d88


**_Source Branch_** (master/stable) **:** Master


**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
TeoTwawki asked me to report this here regarding DPS using the a pre2014 retail update to TP gain, http://ffxiclopedia.wikia.com/wiki/Tactical_Points

Just a very brief (not actual numbers) example: Using SAM as the example, SAM gains ~250tp per swing. SAM hits Fafnir, Fafnir gets 250tp. Where as Fafnir hits SAM, SAM gets ~50tp.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:13_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Aug 06, 2017 at 06:26 GMT_

----

Note: I already checked that it wasn't something silly like storetp working the wrong direction, and that the tp gains look like they did back when I actually still played retail. I never checked what the change was described on wiki was or if we did that already, told him open this and tag me so I don't forget him (again)



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:14_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Sunday Aug 06, 2017 at 07:02 GMT_

----

what does "off" mean? 

I don't understand what the issue is



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:15_

----

<a href="https://github.com/ghost"><img src="https://avatars3.githubusercontent.com/u/10137?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ghost](https://github.com/ghost)**
_Sunday Aug 06, 2017 at 07:05 GMT_

----

Monsters/NMs are weaponskilling really rapidly, when you throw more then 1-2 people on them. Like they will ws back to back with very few auto attacks themselves.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:18_

----

<a href="https://github.com/Cloudef"><img src="https://avatars2.githubusercontent.com/u/480330?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Cloudef](https://github.com/Cloudef)**
_Sunday Aug 06, 2017 at 13:42 GMT_

----

goblins at least are very dangerous with their full tp bombs, but then again it is sort of fun in own way.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:20_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Monday Aug 07, 2017 at 05:39 GMT_

----

Is modern retail's TP formula no longer attacker tp (before storetp) +3.0?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:21_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 07, 2017 at 05:59 GMT_

----

looking at bg, the _description_ went from:

Delay | TP gained
------------ | -------------
\<180 | 8.0+((Delay-180)×1.5)÷180
180\~450 | 8.0+((Delay-180)×6.5)÷270
450\~480 | 14.5+((Delay-450)×1.5)÷30
480\~530 | 17.0+((Delay-480)×1.5)÷50
\>530 | 17.5+((Delay-530)×3.5)÷470 

to the much simpler:

Base Monster physical damage TP gained = Player Base TP per hit (before Store TP but after Delay reduction) + 3 TP

***And this happened at the same time TP went from three digits to four.***
I been busy reinstalling software to laptop for the last couple days so I have not looked at the codebase to see if that is what we already have. We already have the 4 digit TP, of course.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:22_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Aug 07, 2017 at 06:01 GMT_

----

Deadwing888  so modern *should* be what you said. If DSP matches that, this can't but what the OP thought.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:23_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Sunday Aug 13, 2017 at 22:09 GMT_

----

They appear to model the same behavior in terms of tp fed. It is possible the simpler formula was not recognized until we could easily see fractional TP.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:24_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Sunday Aug 13, 2017 at 22:21 GMT_

----

Oh sorry it just clicked to me what Raelious (hey buddy) is speaking of. The actual issue here is the way TP moves are being handled once the mob has over 100.0TP basically DSP has this TP_USE_CHANCE thing which actually doesn't emulate retail in any fashion.

It runs so often that even a very low TP_USE_CHANCE triggers the TP moves at or near 100.0 mob tp all the time regardless of HP. No value for TP_USE_CHANCE will emulate retail. For instance soloing cactrot rapido on retail, he won't spontaneously decide to use a TP move if no fresh TP was fed to him unless his HP was dropped below 50% or 25%. Other than those scenarios he has a randomly assigned TP value to go at, it's a static value and if he doesn't hit it he won't tp move no matter how much time passes.

Disclosure: I have not built DSP modern in some time, so I'm not aware of edits this system may have already undergone.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:26_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Aug 13, 2017 at 23:01 GMT_

----

Deadwing888 thats what I thought talkin to him on discord, till we started talking about multihit. might be multiple probs that add up to mob "goes" too often? Coz I don't notice any prob with like, lizards in dunes.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:27_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Sunday Aug 13, 2017 at 23:43 GMT_

----

The whole concept of a "TP_USE_CHANCE" is non retail. It should be a TP_USE_PERCENT which is set on mob spawn and on mob weaponskill; a random 100.0-300.0 with exceptions to go automatically under 200.0 under 50% and 100.00 under 25%.

But yes TP_USE_CHANCE is called way too often to have it actually modulate tp frequency in its current non retail form.

