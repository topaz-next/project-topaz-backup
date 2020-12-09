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
