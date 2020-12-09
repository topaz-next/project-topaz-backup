**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:31_
_Originally opened as: project-topaz/topaz - Issue 28_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jun 22, 2015 at 23:31 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 1618_

----

things I have seen happen after outrunning a mobs tp attack as it readies it, some or all of these may or may not happen, seemingly randomly but **only** if I ran out of range of a tp attack it was preparing:
- mob ceases all action: no melee, no movement, no nothing
- mob loses ability to do anything but melee (if I am standing in range...it seems unable to follow me).
- mob becomes unable to despawn or die properly. I can empty its HP bar and obtain drops, but it stays standing there and never keels over.
- mob turns invisible/has no model, but can still be targeted. if the mob has not ceased action, it will continue to invisibly melee me.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:32_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Jun 23, 2015 at 00:39 GMT_

----

A similar thing happens if a tp move gets stunned. It can also call various player WS animations, stretching out the mob model strangely. It's always the same animation for the same move, though, so I think it's just using the mob animation value but ends up calling a different animation type.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:33_

----

<a href="https://github.com/dazusu"><img src="https://avatars0.githubusercontent.com/u/7009763?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dazusu](https://github.com/dazusu)**
_Tuesday Jun 23, 2015 at 07:56 GMT_

----

I had these issues when attempting to implement Dark Ixion, including animations crewing up completely.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:35_

----

<a href="https://github.com/helixhamin"><img src="https://avatars1.githubusercontent.com/u/2202779?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [helixhamin](https://github.com/helixhamin)**
_Wednesday Jun 24, 2015 at 11:07 GMT_

----

I have seen these issues when stunning them also. They become modern art, with some strange effects sometimes randomly going off.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:36_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jun 25, 2015 at 13:12 GMT_

----

Loki79 tells me despawning a mob while its busy/people fighting it can produce similar effects




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:37_

----

<a href="https://github.com/nasomi"><img src="https://avatars0.githubusercontent.com/u/6567800?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nasomi](https://github.com/nasomi)**
_Friday Jul 24, 2015 at 17:43 GMT_

----

despawning a mob under any circustamnces while engaged causes the monster to disappear.

OnMobFight() is executing every 1 second, not 3 as intended.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:38_

----

<a href="https://github.com/Loki79"><img src="https://avatars2.githubusercontent.com/u/10149850?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Loki79](https://github.com/Loki79)**
_Friday Jul 24, 2015 at 17:49 GMT_

----

Ok to be a bit more clear on this despawning a mob during fight is causing the model to disappear, while  the name is still visible and the mob is target-able and continues to take dmg while not performing any actions towards the players.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:39_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 24, 2015 at 17:51 GMT_

----

> OnMobFight() is executing every 1 second, not 3 as intended.

1 is actually intended, it just doesn't work very well compared to having it at 3 (remember the collibri animation bug? see its onMobFight where I worked around that).




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:40_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Sunday Sep 20, 2015 at 06:47 GMT_

----

Just confirmed the mob skill interrupt packet is broken and always plays a random mob ability instead of clearing the charging up animation. I'll keep testing to reproduce the other issues.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:41_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Saturday Mar 05, 2016 at 15:56 GMT_

----

TeoTwawki Can you look into this. Last time I checked the packet for interrupt mobskill was broken.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:42_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Nov 18, 2016 at 04:55 GMT_

----

If its really broken packet.. here's a cap https://yadi.sk/d/Hodv1fw0yse7R

I dunno wtf to do with it


