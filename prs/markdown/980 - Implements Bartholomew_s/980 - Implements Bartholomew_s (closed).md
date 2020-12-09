**Labels:**

reviewed



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Wednesday Aug 19, 2020 at 23:53:53_
_Originally opened as: project-topaz/topaz - Issue 980_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes #978 

https://ffxiclopedia.fandom.com/wiki/Talk:Bartholomew%27s_Knife


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Aug 20, 2020 at 00:57:03_

----

any chance we could use better naming convention then "QM3"? I know there are some client limitations here so maybe ignore this. Teo can probably weigh in. 


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Aug 20, 2020 at 00:57:45_

----

I think this needs to be followed up by a timer. 

Though, I'm not finding any research, there is a limited window on how long the pillar remains "charged" for? If I'm wrong, no worries and ignore me. 


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Aug 20, 2020 at 00:58:36_

----

My understanding is, if you trade that knife and don't get it, it essentially "breaks" like an orb and you can never trade that same knife again. You need to steal a fresh one.

This may require a core change unless you can use the same mechanic we use to break orbs?


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Aug 20, 2020 at 01:11:25_

----

Testimonies clearly conflict on this.  That aside, burning these knives somehow will require some special code if that's how you guys want to do it.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Aug 20, 2020 at 01:12:05_

----

Conflicting accounts on this, but I thought this had been debunked.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Aug 20, 2020 at 01:53:27_

----

Well... it would be nice to implement this once and completely, but that's not my call to make. The "good enough" approach bugs me because we'll never come back to it, but again that's personal preference. 


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Aug 20, 2020 at 01:59:11_

----

Well, if so, no worries then. 


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Aug 20, 2020 at 05:21:45_

----

I looked at the main page for the knife again, someone said in 2020 that it is guaranteed burnt when you try to trade and it fails... Implementation of this is beyond my knowledge, but don't let this PR languish just because it's not 100% :(


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Aug 20, 2020 at 08:26:55_

----

Agreed.  One of my eventual TODOs is getting rid of all these numbered QMs in npc_list/scripts, and replacing them with more meaningful names.  Client NPC ID shifts sometimes add/remove/shift QMs in a way that messes up the order within a zone.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Friday Aug 21, 2020 at 01:56:30_

----

Just need to know what name to change it to.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Friday Aug 21, 2020 at 02:07:44_

----

I would say just leave it for now, unfortunately. That way it still matches up with the name in the database. 


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 05, 2020 at 19:20:30_

----

After delving into how WS points are stored for weapons, we could use the "extra" field in char_inventory for each item to store if it's burnt or not.  The exact usage of this field is a little beyond me, but with a little guidance I could add it if you guys want it.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Sep 05, 2020 at 21:29:36_

----

> Well... it would be nice to implement this once and completely, but that's not my call to make. The "good enough" approach bugs me because we'll never come back to it, but again that's personal preference.

if someone can _prove it_ I'll make sure it isn't forgotten. I don't trust some random comment on wiki to be the end all be all for it though. Whichever way its implemented initially, this is still worthy of an issue until verified.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Aug 20, 2020 at 00:57:03_

----

any chance we could use better naming convention then "QM3"? I know there are some client limitations here so maybe ignore this. Teo can probably weigh in. 


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Aug 20, 2020 at 00:57:45_

----

I think this needs to be followed up by a timer. 

Though, I'm not finding any research, there is a limited window on how long the pillar remains "charged" for? If I'm wrong, no worries and ignore me. 


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Aug 20, 2020 at 00:58:36_

----

My understanding is, if you trade that knife and don't get it, it essentially "breaks" like an orb and you can never trade that same knife again. You need to steal a fresh one.

This may require a core change unless you can use the same mechanic we use to break orbs?


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Aug 20, 2020 at 01:11:25_

----

Testimonies clearly conflict on this.  That aside, burning these knives somehow will require some special code if that's how you guys want to do it.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Aug 20, 2020 at 01:12:05_

----

Conflicting accounts on this, but I thought this had been debunked.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Aug 20, 2020 at 01:53:27_

----

Well... it would be nice to implement this once and completely, but that's not my call to make. The "good enough" approach bugs me because we'll never come back to it, but again that's personal preference. 


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Thursday Aug 20, 2020 at 01:59:11_

----

Well, if so, no worries then. 


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Aug 20, 2020 at 05:21:45_

----

I looked at the main page for the knife again, someone said in 2020 that it is guaranteed burnt when you try to trade and it fails... Implementation of this is beyond my knowledge, but don't let this PR languish just because it's not 100% :(


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Thursday Aug 20, 2020 at 08:26:55_

----

Agreed.  One of my eventual TODOs is getting rid of all these numbered QMs in npc_list/scripts, and replacing them with more meaningful names.  Client NPC ID shifts sometimes add/remove/shift QMs in a way that messes up the order within a zone.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Friday Aug 21, 2020 at 01:56:30_

----

Just need to know what name to change it to.


----
<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Friday Aug 21, 2020 at 02:07:44_

----

I would say just leave it for now, unfortunately. That way it still matches up with the name in the database. 


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 05, 2020 at 19:20:30_

----

After delving into how WS points are stored for weapons, we could use the "extra" field in char_inventory for each item to store if it's burnt or not.  The exact usage of this field is a little beyond me, but with a little guidance I could add it if you guys want it.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Sep 05, 2020 at 21:29:36_

----

> Well... it would be nice to implement this once and completely, but that's not my call to make. The "good enough" approach bugs me because we'll never come back to it, but again that's personal preference.

if someone can _prove it_ I'll make sure it isn't forgotten. I don't trust some random comment on wiki to be the end all be all for it though. Whichever way its implemented initially, this is still worthy of an issue until verified.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 10, 2020 at 06:53:37_

----

So, is my thinking right here?

```
Brigandish Blade dies
QM3/Pillar is "charged" with a localVar
Someone tries to trade Buccaneer's Knife to it, and it _might_ return Bart's Knife if the pillar is charged
Pillar is then uncharged
```

I suspect there might be some kind of timer here, else I could come and kill Brigandish Blade and then wander off, allowing some unrelated party to swing by an hour later and try to trade their knife?

For this "knife getting burned" thing, I think this is a good opportunity for someone (me, teo, anyone comfortable with core bindings) to write a get/setItemExtraData binding. 

Finally, I think the best options would be to put on a 1 minute timer, and add the "knfie being burned" thing as precautions (since they aren't hard) and then someone can come and debunk these claims later. My fear is that if we do something "good enough" it will stay _incomplete_ forever, until someone does the worlds most in-depth audit. Which is never.



----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Thursday Sep 10, 2020 at 23:57:09_

----

When checking the ???. that spawns Brigandish Blade:

INCOMING < NPC Chat (0x036):  NPC: 17502582 (???)
Message: 7226.
("You sense an evil presence lurking in the shadows...")

Two different Buccaneer's Knives in and still unable to get the Bartholomew's Knife. I'll edit once I get it (if I can).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Sep 10, 2020 at 23:57:35_

----

> and add the "knfie being burned" thing as precautions (since they aren't hard)

easy enough for those of us that disbelieve/don't want to just comment out too.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Sep 11, 2020 at 00:00:27_

----

@UynGH try to cap the item data when you get a new knife and after using that knife. the theory is that the knife gets "burned" like an orb, and if we can see that in its data that's confirmation if they did it that way (not seeing it doesn't prove its good for more trades, but it will save a lot of extra effort checking if we do happen to see it).


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Friday Sep 11, 2020 at 00:26:11_

----

Correct dialogue now added to brigandine blade's ??? spawn, qm2.

Thanks for looking into that nyu <3


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 19, 2020 at 12:25:51_

----

Since Tank said he was going to be away from the community for a while and we've been arguing trying to prove or disprove the logic here, and then doing deep dives into what mechanisms would be best to "burn" a knife, I think it would be best to just get it in and follow up with an issue.
