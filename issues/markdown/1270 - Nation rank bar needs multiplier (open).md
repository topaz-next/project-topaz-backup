**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Oct 07, 2020 at 20:45:45_
_Originally opened as: project-topaz/topaz - Issue 1270_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
I think everyone has noticed how the rank points gained by trading in crystals is very legacy like where you had to trade full stacks of crystals to advance to the next mission even on Rank5/6ish.
This is very out of sync with most recent guides that say "trade 1 crystal", "trade 3 crystals" etc.
But even if you raised the amount of rank points added by trading in crystals, you'd still have to trade a decent amount because the missions itself have seen no increase.
Retail has seen a very flat 2x multiplier for rank bar increase, be it by trading crystals or by doing missions. I can not speak for CP gain though when the rank is full, which shall not be the matter of this issue.

This is **extremely easy to test** and anybody with doubts can create a free trial account, do missions up to Rank 2 and do what I (and people before me) did:

1. With Rank 2 and bar empty trade 1 crystal to a guard that is not light or dark (talks on wiki pages seem to show that they do yield higher gains, I also think to recall this to be the case from back in the days; I chose wind)
2. Make a screenshot and measure the pixels of the bar after trading one crystal
3. Trade another crystal, make a screenshot and measure the total pixels of the bar now
4. Repeat 3.
5. Do Mission 2-1 for your nation, do a screenshot and measure the pixels after doing the mission.
6. Repeat 1-5 on Topaz

![topaz_retail_rank_bar_difference](https://user-images.githubusercontent.com/1492317/95385315-6913b700-08b3-11eb-8a33-5b55f7c30859.png)

According to resolution and compression/quality levels of the client there might be 1px off here and there, but I think this demonstrates very clearly that SE didn't put an overload of paid hours into overthinking this and added a plain 2-times multiplier.

I therefore suggest a simple multiplier of 2 for any rank bar gain in:
https://github.com/project-topaz/topaz/blob/abfe5dda545545f060a761e894c79d55239ada02/src/map/lua/lua_baseentity.cpp#L6113-L6132

This multiplier could then be easily reversed to not gain excessive CP in https://github.com/project-topaz/topaz/blob/abfe5dda545545f060a761e894c79d55239ada02/scripts/globals/conquest.lua#L962-L965


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 08, 2020 at 14:25:09_

----

> I think everyone has noticed how the rank points gained by trading in crystals is very legacy like where you had to trade full stacks of crystals to advance to the next mission even on Rank5/6ish.

Yeah I had no idea of any change but it used to take multiple stacks to fill the bar for later ranks.. The higher you climbed the more it took, but it you intentionally got the rank bar *almost* full and then traded 8 stacks of light/dark you got a good deal of CP for it at least in days where CP was actually worth having.

> crystal to a guard that is not light or dark (talks on wiki pages seem to show that they do yield higher gains

its relative to the npc resell value, the 6 main sell for less and light/dark for more. Our calculation should use basesell and a multiplier.
