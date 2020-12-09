**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:55_
_Originally opened as: project-topaz/topaz - Issue 300_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jun 02, 2019 at 22:24 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6056_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
n/a

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Go poke Ashmaker Gotblutt (Yugott Grotto) till he, a BLM pops Manafont. Watch as your log clearly says "Manafont". Watch as he spams spells as fast as RDM Chainspell till you die horribly from to much Stonega.

Alternatively: watch someone else do this, laugh maniacally.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:56_

----

<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Jun 04, 2019 at 15:46 GMT_

----

Tested on master.  As implemented, Manafont **does** make the mob cast spells back-to-back with no pause in between, but it does **not** make the spells insta-cast like Chainspell.  What is proper retail behavior for Manafont?  Ashmaker's wiki page says `During Manafont, it spams spells like normal BLM mobs.` which makes it sounds like Manafont does at least have some effect on how often a mob should cast, if it's not supposed to be no-pause-in-between spam.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:57_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jun 04, 2019 at 16:02 GMT_

----

For manafont: cast time should still be a thing. Cooldown _between_ spells disappears. Spells become 100% non interruptible by damage as well (sleep stun etc will still work).

All blm mobs on retail, with or without manafont, will attempt to cast as soon as their cooldown is up and wiki is just pointing out that behavior doesn't change.


The intention was likely to ensure a certain NM didn't waste its time preparing actions other than spells while its non interruptible Manafont boosted spells were available.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:58_

----

<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Jun 04, 2019 at 16:09 GMT_

----

That's the behavior I'm seeing for Manafont on DSP master branch, though: spells take regular amount of time to cast, start to finish, but cooldown between spells disappears.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:59_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jun 04, 2019 at 16:10 GMT_

----

I'm seeing instant cast stonga.

no cast time at all. on master, no customization.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:05:01_

----

<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Jun 04, 2019 at 16:15 GMT_

----

Huh. That's odd.  Same for me -- master, no customizations.  Its Stonega takes just as long to cast as mine does, about 2 seconds.
https://www.youtube.com/watch?v=H4L2s6rmZ3U



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:05:02_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jun 04, 2019 at 16:39 GMT_

----

I unno what to say now, yours did aero > blizzard > stonega, the t1 nukes are low cats time so thats normal, your stonega then took the 2 seconds like expected.. Mine he did stonega > stonega > stonega all insta cast.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:05:03_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Wednesday Jun 05, 2019 at 17:26 GMT_

----

So basically, the issue is the time between spells is that the recast time on individual spells is being ignored?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:05:05_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jun 05, 2019 at 17:29 GMT_

----

there was no cast time for me on stonega (for "me" I mean, "when ashmaker decided to bury me under rocks"), but wren wasn't able to repro so now I'm at a loss for wtf was actually happening. had it been lag the casts would have seemed longer. I dunno what could cause a mistaken instacast or _apparent_ instacast.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:05:06_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jun 05, 2019 at 17:30 GMT_

----

Going to retry this on the weekend, see if it happens again while recording.



----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Feb 27, 2020 at 21:07:10_

----

I was never able to replicate this issue, and believe it can be closed, unless Teo's further tests replicate it.


----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Feb 27, 2020 at 21:27:39_

----

I havent seen it either. Closing


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Feb 27, 2020 at 22:00:11_

----

kinda forgot about it. pretty sure I had a one time fluke that never repeated (or my players would be complaining to remind me this was a thing). Somewhere Ashmaker is laughing at me. I have no idea what caused it.
