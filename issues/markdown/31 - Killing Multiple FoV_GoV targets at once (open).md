**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:53_
_Originally opened as: project-topaz/topaz - Issue 31_

----

<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [m241dan](https://github.com/m241dan)**
_Friday Jul 17, 2015 at 15:42 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 1738_

----

If you kill multiple GoV/FoV targets simultaneously, maybe only 1/3 of them will count towards your page. I can't think up a valid strategy to counteract this, some sort of lua call queue maybe? I dunno. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:54_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 18, 2015 at 18:55 GMT_

----

may be related, not sure: 1 shot killing targets (aoe or not) causes them to register dead before ever claimed, and nothing in onMobDeath registers for the player. Which would include FoV/GoV kills and some Dynamis stuff too.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:55_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Saturday Jul 18, 2015 at 19:46 GMT_

----

That's how it works on retail though




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:56_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 18, 2015 at 20:34 GMT_

----

teschnei Which, the multi kill or one hit kill or both? been to long for me, don't remember this stuff ;.;




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:57_

----

<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Saturday Jul 18, 2015 at 21:58 GMT_

----

Personally, I don't remember doing many pages on retail. But, from a code perspective, all these mobs that we are aga nuking, takes a few, so they are claimed. Though, maybe not red? I can try with them all being red and see if that works.

EDIT: I guess red and claimed same thing.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:58_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Saturday Jul 18, 2015 at 23:39 GMT_

----

Both I think, actually. I know this is the case for abyssea lights, so it
would not surprise me if it was the case for any onMobDeath related thing




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:10:59_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Jul 18, 2015 at 23:59 GMT_

----

Back when I played I used to be able to AoE magic kill for magic related light in Abyssea. Used to trio farm with a blue mage friend and this was how we'd max it out really fast. Disappointing if they nerfed that. The 1 shot kill thing...In dyna if I one shot a statue the mobs it should spawn never pop. I never was never able to do that on retail and retails dyna system is now totally different, so no idea if this is could be a problem elsewhere or not.

m241dan I don't think its actually the claim that is the issue. Last attacker is whats its checking to decide who the "killer", if I recall correctly from last time I messed with that code. 

Btw, in retail we can't actually keep claim on as many mobs as we can on DSP. Sort of unimplemented behavior there, not sure I'd really call that a bug so much as "not done yet"..In retail attacking a different mob will un-claim the previous one. People generally think its one claim per party but when I played it was definitely 1 claim per person, and many times in party I would see multiple red named mobs if we were all targeting something different. In DSP I can hold claim on 20 mobs using 1 character. And seems way easier to hold a claim too (anecdotally, as I can't really compare nowadays).


