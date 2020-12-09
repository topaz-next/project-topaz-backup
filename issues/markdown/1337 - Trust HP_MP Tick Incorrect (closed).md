**Labels:**

focus



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Monday Oct 12, 2020 at 07:24:27_
_Originally opened as: project-topaz/topaz - Issue 1337_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

From @MarianArlt 

I'll post this here to avoid even more issues. People are frustrated about the further Trust nerfs. I don't want to comment on that. I want to share a recent experience from trial retail.
Ironically I thought that Trusts were slightly OP with their MP refresh, so I started to watch and note down on retail (I created the trial account for the rank bar issue). I wanted to take a video today but it seems my trial expired.

I noted things down on good old paper and only had Mihli Aliapoh, Adelheid and Excenmille as lab rats.
I found that the following was true:

The first MP tick after disengaging was the longest. I got inconsistent notes, probably because of network lags I didn't notice at the time. Sometimes it didn't tick until after 25 seconds (pretty positive that was lag) and the fastest I got on several notes was 15 seconds.

The second and the third tick were 10 seconds.

All ticks after that were 3 seconds.

The first three ticks were a lower amount (you could call it the base amount) then they got doubled by the fourth tick.

The MP regenerated in that fashion was not a flat 3% but rather it increased by the Trust's level.

At Lv17 Mihli Aliapoh would regenerate 3mp for the first three ticks and then 6mp for every tick after that.
At Lv18 she would regenerate 4mp (2.45% of her total 163mp) and then 8mp for every tick after that.
At Lv19 she would regenerate 5mp (2.94% of her total 170mp) and then 10mp for every tick after that.
Adelheid was regenerating the same amount despite having less in total (first three ticks 2.68% of her total 149mp at Lv18).

I'm not 100% sure (cause I missed to write down his Lvl) but I think the note of Excenmille shows that at Lv18 he would regenerate 1 base mp less than the mages but with the same pattern.

using /heal did not affect neither the tick pattern nor the amount of mp restored.

Generally speaking healing was rather conservative and MP aware. I would not receive cure instantly when dropping to yellow. Rather a few HP below that.

I would not get healed at all for quite a while if the Trust had very little MP

Maybe more retail people could chime in with additional and higher lvl Trust observations. @jarmengaud? This is from a trial played this October.




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 12, 2020 at 07:24:48_

----

Reminder from ibm:
General reminder that Clear Mind is a thing~


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 12, 2020 at 07:29:49_

----

When I did my testing for this, I took _Nanaa Mihgo Lv99 (not i119)_ into battle, because I know she doesn't have any regen or traits that would affect healing rates. I only roughly counted a few ticks, and it was _more than 3s_, _closer to 10s_. The amount was _always_ 5%, give or take 0.5% because of rounding errors etc. 

I'll obviously go back and retest this.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 12, 2020 at 07:34:01_

----

Maybe it's just because of the low levels? I found it interesting that Excenmille being a melee ticked for slightly less. Also I wouldn't rely on only one trust. Maybe there are more that don't have Traits to compare to?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 12, 2020 at 11:34:40_

----

> People are frustrated about the further Trust nerfs. 

Seeing this said is frustrating even as an outside observer. This isn't even close to a nerf. Trusts are an obviously in progress feature, its not like "whelp trusts suck now back to soloing/multiboxing everything" the man literally is simply trying to make them retail accurate and they clearly have multiple ways in which they need modified to get there. :facepalm: 

As for the tick rate on heals, I expected it the same as players, where the 1st tick takes 20 sec and the ticks thereafter come in at 10 sec. Looking at retail _my freakin self_ its plain to see them coming at 10 sec intervals and not differing per trust at all. The only thing I can suggest is making the setting that adjusts players healing tick delay also affect trusts or giving them their own.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 12, 2020 at 17:28:14_

----

If I had created this as an issue in the first place I wouldn't even have put that phrase there Teo ;) (It was merely the reason in my head why I posted this observation of mine which I had put aside before without mentioning anywhere) I think anybody closely understanding how much work you guys are putting into this would not state it like that. But the end-user usually doesn't and some people seem to have never played retail before or care to investigate. Please don't feel in any way emotionally affected by such statements. You're all awesome.

Now your retail report differs though. That's interesting. Even if I said my ping was maybe bad and that's why I got funny results, and I did use the stopwatch on my mobile, then still all the ticks after the third *always* came in *extremely fast* rounding to 3s. Even when I noticed a slightly higher ping it would be 5 or 6 seconds and be the exception not the rule.

Also the observation that the MP restored per tick *doubled* after the third tick is not made up. Would you think that might be some low level feature? Or maybe a selling trick to trial accounts? I mean, I definitely didn't make this up.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 12, 2020 at 17:31:45_

----

my brain was just screeching "why does the player think this is a nerf? why? why why why?! :sob: :sob: :sob: "


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 12, 2020 at 17:32:40_

----

for what its worth I never make it to a 4th tick without them being full healed, or having died already. so I'm seeing tick 2 and 3 at 10s each.

edit: I am in basic i119 gear, no su gear, and have no done any of the quests that would enhance my trusts nor any mastery from the new sheol areas.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Oct 13, 2020 at 17:40:42_

----

Fixed in https://github.com/project-topaz/topaz/pull/1341
