**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:32_
_Originally opened as: project-topaz/topaz - Issue 36_

----

<a href="https://github.com/Zenny89"><img src="https://avatars0.githubusercontent.com/u/12732496?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Zenny89](https://github.com/Zenny89)**
_Friday Jul 31, 2015 at 01:42 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 1827_

----

When fighting Tinnin, whenever the mob used either Pyric Bulwark (immune to physical damage) or Polar Bulwark (immune to magical damage), Flaming Crush was completely blocked despite being part physical and part magical damage.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:33_

----

<a href="https://github.com/Kthulupwns"><img src="https://avatars1.githubusercontent.com/u/11568537?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Kthulupwns](https://github.com/Kthulupwns)**
_Friday Jul 31, 2015 at 04:11 GMT_

----

This skims on a bigger issue which is just the way pet damage (not specifically summoner) is calculated. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:34_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Oct 06, 2015 at 16:23 GMT_

----

Looking at the script it has literally phys damage times magic resist. But that's not what's causing it - what is is that value is then put into addMobBonuses, part of which checks against the MDT- mod, which would be maxed out with magic shield. So uh... yeah this doesn't work like retail at all.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:35_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Oct 06, 2015 at 16:25 GMT_

----

How does it work, then? The wikis description is not very good (a physical
attack that deals fire damage, which would do exactly what happens)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:36_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Oct 06, 2015 at 16:31 GMT_

----

The BG wiki links imply that the entire damage is modified by MAB, and is
blocked entirely by physical immunity. You're saying that despite being
modified by MAB/mdb, it is not affected by magic immunity?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:37_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Oct 06, 2015 at 17:31 GMT_

----

It is affected by magic immunity on DSP. On retail I was told that it's something like 2 hits physical one hit magical. As for how it actually works on retail... ???????




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:38_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Oct 06, 2015 at 17:35 GMT_

----

Well, 2 physical hits 1 magical hit isn't very informative when people on
the forums claim that physical immunity stops it and MAB does affect the
whole move. Remind me to ask Byrth tonight and I'll get an answer




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:40_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Oct 06, 2015 at 17:42 GMT_

----

In any case, I believe it might be able to magic burst on DSP, but I haven't actually tested it to be sure.


