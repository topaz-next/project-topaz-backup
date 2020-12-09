**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Nov 01, 2020 at 22:49:21_
_Originally opened as: project-topaz/topaz - Issue 1469_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This PR is a result of https://github.com/project-topaz/topaz/issues/1456 and Discussions on Discord about how to handle it.
It adds a new mob modifier called `SEVERE_CHANCE` that can be individually de- or increased where necessary.

We need to agree on:

- [x] default values (I set it to 5% on both any mob and BLM type [kinda superfluous])
- [x] spells that should go in this list (I added death, impact, meteor, meteor_ii and comet)
- [x] Maybe a more descriptive name (renamed to SEVERE_SPELL_CHANCE)

- [x] Built successfully today on top of freshly pulled upstream release branch and tested working as expected locally
(increased/decreased modifier from lua script on the fly)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Nov 01, 2020 at 23:18:36_

----

there were a few gaps in the list we could fill in, such as 
```lua

    SIGHT_RANGE         = 4,  -- sight range
    SOUND_RANGE         = 5,  -- sound range
    BUFF_CHANCE         = 6,  -- % chance to buff (combat only)
    GA_CHANCE           = 7,  -- % chance to use -ga spell
    HEAL_CHANCE         = 8,  -- % chance to use heal
    HP_HEAL_CHANCE      = 9,  -- can cast cures below this HP %
    SUBLINK             = 10, -- sub link group
    LINK_RADIUS         = 11, -- link radius
    DRAW_IN             = 12, -- 1 - player draw in, 2 - alliance draw in -- only add as a spawn mod!
    -- 13 Available for use
```
13 would put it closer to the existing chance mods


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:09:05_

----

don't forget this one


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:09:34_

----

brace on newline please


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:09:50_

----

got an extra blank line here


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:11:21_

----

hmm just realized the whole file has inline bracing before you got here. makes me want to auto-format the whole dang thing...We can do that separately from this pr >.>


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 00:46:52_

----

Hmmm. Slot 13 is occupied by MOBMOD_RAGE // [...] spawn mod! (OBSOLETE - use rage mixin)
Even though it's obsolete, is it safe to overwrite this? Did a search for either MOBMOB_RAGE and tpz.mobmod.RAGE and neither has any occurrences. So I'd guess there won't be an issue? Please confirm.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 01:53:44_

----

then 13 should have been mobmod rage in status.lua also.

@ibm2431 @zach2good more desync between core and lua..


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 01:54:42_

----

looks like ALL the ones marked "available for use" are in fact NOT :rage: 


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 15:53:45_

----

As discussed I'll leave this at 71 for now. The obsolete mods should be discussed independently.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 15:55:20_

----

As discussed I'll leave this at 71 for now. The obsolete mods should be discussed independently.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 15:56:50_

----

Just for clarification all these simply got their padding increased by one column to improve verbosity of the new modifier at position 71.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 16:05:07_

----

if you could infill the "missing" ones into status.lua so we don't mistake them for having being free like the comment incorrectly says, I would appreciate it.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 20:59:41_

----

After dialogue the new mod now occupies again slot 13, obsolete mods have been removed and two TODO mods marked as such. A comment has been added to the source containing the mirroring table and a comment about always editing both. See 611a174349f77bbd594a77881d7e528ed8da0b64


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 21:02:20_

----

After dialogue: fixed only for the affected lines by this PR for cleanliness of the PR itself. See ff24165b3b3b2dcc6f2b07f85ffad18954bbdbdb


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 21:02:31_

----

After dialogue: fixed only for the affected lines by this PR for cleanliness of the PR itself. See ff24165b3b3b2dcc6f2b07f85ffad18954bbdbdb


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 21:02:38_

----

After dialogue: fixed only for the affected lines by this PR for cleanliness of the PR itself. See ff24165b3b3b2dcc6f2b07f85ffad18954bbdbdb


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Nov 01, 2020 at 23:18:36_

----

there were a few gaps in the list we could fill in, such as 
```lua

    SIGHT_RANGE         = 4,  -- sight range
    SOUND_RANGE         = 5,  -- sound range
    BUFF_CHANCE         = 6,  -- % chance to buff (combat only)
    GA_CHANCE           = 7,  -- % chance to use -ga spell
    HEAL_CHANCE         = 8,  -- % chance to use heal
    HP_HEAL_CHANCE      = 9,  -- can cast cures below this HP %
    SUBLINK             = 10, -- sub link group
    LINK_RADIUS         = 11, -- link radius
    DRAW_IN             = 12, -- 1 - player draw in, 2 - alliance draw in -- only add as a spawn mod!
    -- 13 Available for use
```
13 would put it closer to the existing chance mods


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:09:05_

----

don't forget this one


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:09:34_

----

brace on newline please


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:09:50_

----

got an extra blank line here


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 00:11:21_

----

hmm just realized the whole file has inline bracing before you got here. makes me want to auto-format the whole dang thing...We can do that separately from this pr >.>


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 00:46:52_

----

Hmmm. Slot 13 is occupied by MOBMOD_RAGE // [...] spawn mod! (OBSOLETE - use rage mixin)
Even though it's obsolete, is it safe to overwrite this? Did a search for either MOBMOB_RAGE and tpz.mobmod.RAGE and neither has any occurrences. So I'd guess there won't be an issue? Please confirm.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 01:53:44_

----

then 13 should have been mobmod rage in status.lua also.

@ibm2431 @zach2good more desync between core and lua..


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 01:54:42_

----

looks like ALL the ones marked "available for use" are in fact NOT :rage: 


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 15:53:45_

----

As discussed I'll leave this at 71 for now. The obsolete mods should be discussed independently.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 15:55:20_

----

As discussed I'll leave this at 71 for now. The obsolete mods should be discussed independently.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 15:56:50_

----

Just for clarification all these simply got their padding increased by one column to improve verbosity of the new modifier at position 71.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 02, 2020 at 16:05:07_

----

if you could infill the "missing" ones into status.lua so we don't mistake them for having being free like the comment incorrectly says, I would appreciate it.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 20:59:41_

----

After dialogue the new mod now occupies again slot 13, obsolete mods have been removed and two TODO mods marked as such. A comment has been added to the source containing the mirroring table and a comment about always editing both. See 611a174349f77bbd594a77881d7e528ed8da0b64


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 21:02:20_

----

After dialogue: fixed only for the affected lines by this PR for cleanliness of the PR itself. See ff24165b3b3b2dcc6f2b07f85ffad18954bbdbdb


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 21:02:31_

----

After dialogue: fixed only for the affected lines by this PR for cleanliness of the PR itself. See ff24165b3b3b2dcc6f2b07f85ffad18954bbdbdb


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Nov 02, 2020 at 21:02:38_

----

After dialogue: fixed only for the affected lines by this PR for cleanliness of the PR itself. See ff24165b3b3b2dcc6f2b07f85ffad18954bbdbdb


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Nov 03, 2020 at 05:37:53_

----

As always, I lean in favour of "more difficult is better; too easy doesn't get fixed" - so I would want it to go up to something like 20%, but I'm not particularly bothered.  If it _feels_ about right, that's good enough. Someone like @wrenffxi probably has a feeling of where this rate should be

EDIT: I haven't been keeping up in Discord, if this has been discussed


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Nov 03, 2020 at 06:43:21_

----

I really like the idea behind "too easy doesn't get fixed". But I also think 1 out of 5 rolls is massively frequent for what this category should reflect *by default*. I remember doing Dynamis Lord back in era days and if he did that back then, the fight would've been pretty much impossible, burning through the tanks (I mean, we never filled 4 alliances and even less with each party having one tank, that sounds like legit japanese onry ^^;). I could be totally wrong though. Discord sadly didn't yield any opinions on this number. Would be nice to have  some more though.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Nov 03, 2020 at 16:04:42_

----

Another thing to consider is these rolls being independent of each other lets their order effect the outcome - we're rolling for a thing, then if it doesn't happen the next one gets rolled. By even adding another we've artificially reduced the chances of other outcomes ever so slightly. Sooo I guess its good that we're checking severe first in addition to excluding them from the other list, but in the future we should revisit spell selection so that we can be confident that 40% really means 40% (just using 40 as the example)



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Nov 03, 2020 at 16:06:15_

----

5% felt low,. 20% felt high. I though 10% was just right /goldilocks


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Nov 04, 2020 at 00:27:25_

----

> [...]in the future we should revisit spell selection so that we can be confident that 40% really means 40%[...]

I'm glad you mention that Theo, that was one of my initial worries.

As for this: today I [watched](https://www.youtube.com/watch?v=D9noDsJGhJo) [again](https://www.youtube.com/watch?v=jQWKUWJWka0) a [lot](https://www.youtube.com/watch?v=Igot1O9pxWw) of Dynamis [captures](https://www.youtube.com/watch?v=lmpSL0Yw9qI) from the [capture](https://www.youtube.com/watch?v=jQWKUWJWka0) [channel](https://www.youtube.com/watch?v=6H-beKoFDwg) [and](https://www.youtube.com/watch?v=ywPUasgxe8I) [was](https://www.youtube.com/watch?v=q0JgVMHuDyE) [quite](https://www.youtube.com/watch?v=uevyCKUMN4U) [surprised](https://www.youtube.com/watch?v=Jl0JtpozXWA).
Turns out the non-Arch bosses use death at will and rather frequently when the Arch bosses will not at all.

|                   | Dynamis Captures        |             |
|-------------------|----------------|-------------|
|                   | Regular Bosses | Arch Bosses |
| Pops              | 5              | 5           |
| Total casts       | 27             | 60          |
| of which "severe" | 5              | 2           |
| % "severe" spells | 18.52%         | 3.33%       |

This is only of 10 fights in total but the tendency is quite obvious (even though it's all just math.random(), of course). The two severe spells from Arch came both from Arch Gu'Dha Effigy by the way and were Death and Impact. Additionally this includes 2 captures of NQ Dynamis Lord and 3 of Arch Dynamis Lord and none of these used Death even once (shocking!). Given this, the rate for the three city bosses might be even higher.

So I guess **the question is if you want a higher default and adjust down or have a lower default and adjust up**, since this category will not only serve Dynamis I guess.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Nov 04, 2020 at 00:29:53_

----

Higher and adjust down seems safer due to people tending to not want us to fix anything they were benefiting from and loudly proclaiming we nerfed it.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Nov 04, 2020 at 00:30:28_

----

That's a really good point...
...Slap those 20% on there!
