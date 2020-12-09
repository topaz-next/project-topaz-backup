**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:43_
_Originally opened as: project-topaz/topaz - Issue 29_

----

<a href="https://github.com/SearainGaruda"><img src="https://avatars0.githubusercontent.com/u/13070051?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [SearainGaruda](https://github.com/SearainGaruda)**
_Monday Jun 29, 2015 at 10:31 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 1632_

----

This needs to be addressed before mass DRK-zerging takes over entire servers, turning endgame into a joke.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:44_

----

<a href="https://github.com/TheMuffinPirate"><img src="https://avatars3.githubusercontent.com/u/11020352?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TheMuffinPirate](https://github.com/TheMuffinPirate)**
_Thursday Jul 02, 2015 at 00:14 GMT_

----

In addition to this its also currently set to 33 damage for some reason in the sql




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:45_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Friday Jul 03, 2015 at 10:41 GMT_

----

corrected the damage in github/DarkstarProject/darkstar/commit/c4771b4d4815b0d371f3639fc762b785d51b4dd9
not sure how the multiple attacks is even working considering it has no entries in item_mods or item_latents




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:47_

----

<a href="https://github.com/Desufire"><img src="https://avatars2.githubusercontent.com/u/11659700?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Desufire](https://github.com/Desufire)**
_Friday Jul 03, 2015 at 21:45 GMT_

----

It's in the weapon sql. There's an attack column and kraken shows 8. Octave shows 8 as well. I noticed that with occ. attk twice weapons, there's is a 2 in the column. I adjusted the octave to 2 instead of 8 on my server. It only swings twice now which works for all until I get around learning how to make a latent mod. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:48_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Friday Jul 03, 2015 at 22:16 GMT_

----

`INSERT INTO `item_latents` VALUES(itemid, modid, modvalue, latentId, latentParam);`
you can find the latentId in `latent_effect.h` and find the latent id in `latent_effect_container.cpp`to get a better idea of how the param affects the latent's activation

not really sure which mods to use (though im guessing MOD_DOUBLE_ATTACK / MOD_QUADRUPLE_ATTACK)
so i leave the rest to teschnei :p




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:49_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 04, 2015 at 19:55 GMT_

----

I think this latent would need a modifier for changing the hit count value from 1 to whatever (and probably multiple latent triggers, for the different lv checks and hit counts http://ffxiclopedia.wikia.com/wiki/Octave_Club), rather than using double attack/quad attack mods. And the database entry in item_weapon.sql should be changed to 1.


