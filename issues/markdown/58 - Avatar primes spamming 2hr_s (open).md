**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:39_
_Originally opened as: project-topaz/topaz - Issue 58_

----

<a href="https://github.com/LionelGrimm"><img src="https://avatars3.githubusercontent.com/u/15353291?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [LionelGrimm](https://github.com/LionelGrimm)**
_Wednesday Oct 28, 2015 at 01:24 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2340_

----

Dunno if this is a new or old issue. Just tried to fight Garuda, it did 4 Aerial Blasts. Fought Leviathan, it did 5 tidal waves. Ifrit also started spamming Inferno near death. They're basically using 2hr's as tp moves.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:40_

----

<a href="https://github.com/nesstea"><img src="https://avatars0.githubusercontent.com/u/1483915?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nesstea](https://github.com/nesstea)**
_Thursday Oct 29, 2015 at 15:43 GMT_

----

It's coded to do so. It can queue up to 5 of them and then it can die.

```
            if ((astralFlows==0 and hpPercent <= 80) or
            (astralFlows==1 and hpPercent <= 60) or
            (astralFlows==2 and hpPercent <= 40) or
            (astralFlows==3 and hpPercent <= 20) or
            (astralFlows==4 and hpPercent <= 1)) then               
                mob:useMobAbility(592);
                astralFlows = astralFlows + 1;
                mob:setLocalVar("astralflows",astralFlows);

                if (astralFlows>=5) then
                    mob:setUnkillable(false);
                end
            end
```




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:41_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Oct 29, 2015 at 15:44 GMT_

----

Oh, it totally doesn't do that on retail. I killed them last week, only got
one off before dying




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:42_

----

<a href="https://github.com/nesstea"><img src="https://avatars0.githubusercontent.com/u/1483915?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nesstea](https://github.com/nesstea)**
_Thursday Oct 29, 2015 at 17:22 GMT_

----

I'll take care of them tonight. KJ, these have a chance to not 2hour right? I remember them using a 2hour most of the time, but not every time.

If that is true, I'll have to code their 2hour in the onmobfight.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:43_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2015 at 17:24 GMT_

----

This happened when someone tried to script the "A Shantotto Ascension" Version of the Primes, and the check to make sure you were in that version of the battlefield failed. So it behaved correctly for their test for the thing they were doing, but borked the regular fights. Its been this way for a long long time and it is crazy that it took till now for anyone to issue report it.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:44_

----

<a href="https://github.com/nesstea"><img src="https://avatars0.githubusercontent.com/u/1483915?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nesstea](https://github.com/nesstea)**
_Thursday Oct 29, 2015 at 17:25 GMT_

----

Well Teo, most people only do it up to 3 times and it worked. Not a huge deal. I'll take care of it later.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:45_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2015 at 17:25 GMT_

----

This throws nil: github/DarkstarProject/darkstar/blob/master/scripts/zones/Cloister_of_Frost/mobs/Shiva_Prime.luaDarkstar Issue L20




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:46_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2015 at 17:26 GMT_

----

here to: github/DarkstarProject/darkstar/blob/master/scripts/zones/Cloister_of_Frost/mobs/Shiva_Prime.luaDarkstar Issue L47




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:47_

----

<a href="https://github.com/nesstea"><img src="https://avatars0.githubusercontent.com/u/1483915?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nesstea](https://github.com/nesstea)**
_Thursday Oct 29, 2015 at 17:33 GMT_

----

Seems like getBattlefield seems to be the culprit? 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:49_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2015 at 17:34 GMT_

----

Or casing or something, I dunno didn't really check that far rl keeping me from doing much.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:50_

----

<a href="https://github.com/nesstea"><img src="https://avatars0.githubusercontent.com/u/1483915?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nesstea](https://github.com/nesstea)**
_Thursday Oct 29, 2015 at 17:36 GMT_

----

Are there differently coded Prime avatars in those zones? Wondering why it was coded this way to begin with.

edit: http://ffxiclopedia.wikia.com/wiki/Sugar-coated_Directive




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:51_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2015 at 18:18 GMT_

----

There are multiple versions of each Prime Avatar mob in each cloister. But they all have the same database name so they all ran same script.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:52_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 29, 2015 at 18:23 GMT_

----

Worth noting: 
The thing we are talking about is by HP, not by TP. So if the primes are in fact using their astral flow as a regular mobskill by TP, that's an entirely diff bug than nesstea and I have been talking about.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:53_

----

<a href="https://github.com/nesstea"><img src="https://avatars0.githubusercontent.com/u/1483915?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nesstea](https://github.com/nesstea)**
_Tuesday Nov 03, 2015 at 07:51 GMT_

----

Can I effectively grab the battlefield ID the mob is in? I keep getting nil...


