**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Friday May 08, 2020 at 18:21:58_
_Originally opened as: project-topaz/topaz - Issue 595_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

changed drop rate for items dropped by huge wasp and pygmaioi with help of ffxidb and SEs table for TH with drop rates.



----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday May 08, 2020 at 18:22:45_

----

FFXI wiki doesn't have a % droprate for item, so I just used the same as the dewdrop for mandragoras


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday May 08, 2020 at 19:12:46_

----

FFXIDB drop data for bee pollen [(konschtat)](http://ffxidb.com/zones/108/huge-wasp), [(la theine)](http://ffxidb.com/zones/102/huge-wasp), and [dewdrop](http://ffxidb.com/zones/117/pygmaioi).

They don't seem to align with the [known Treasure Hunter buckets](https://www.bg-wiki.com/bg/Treasure_Hunter). But this data may be skewed by the fact that these particular items were added _after_ the mobs were originally added, so their percentages are artificially lower.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday May 08, 2020 at 20:06:26_

----

@ibm2431 should we use FFXIDB as our source of truth for item drop rates?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday May 08, 2020 at 20:35:10_

----

When possible, as it tabulates data it sees while people use the FFXIDB plugin. So it's a step above some random anecdotes on wikis.

But due to how _these_ particular drops were added to the game, this may need a special determination, as it might be possible for FFXIDB to give wrong percentages.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday May 08, 2020 at 20:38:08_

----

Addendum: For these, I'd be okay with whatever source aligns closest to a TH bucket.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday May 08, 2020 at 21:27:35_

----

A TH bucket? what does a TH bucket mean @ibm2431 ? (sorry for my ignorance)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday May 08, 2020 at 22:48:21_

----

SE "recently" released fairly exact specifics on how [Treasure Hunter](https://www.bg-wiki.com/bg/Treasure_Hunter) works in a QA thread. With the exception of "shared slot" items, items all have a "rarity", and the rate that item drops under various levels of Treasure Hunter will be dependent on that rarity value, or, "bucket".

Example: An item with a rate of "Uncommon" will drop 10% of the time with no TH, 12% of the time with TH1, 15% of the time with TH2, etc.

![github](https://user-images.githubusercontent.com/13112942/81455075-97af2980-917d-11ea-8518-d4bc42e94e44.png)

So theoretically we can look at this in reverse: If some player calculated dataset of an item's drop rate is showing an item dropping 4% of the time with TH0, and 6.5% of the time with TH2, that item is most likely in the "Rare" category (drop rate, not the yellow identifier on the item box).

4% at TH0 is too high for Very Rare, and too low for Uncommon. Someone might chalk it up to there not being enough data, but the TH2 datapoint also lines up with the item being "Rare" and nothing else.

Now that we know how TH _actually works as confirmed by SE_, we could theoretically go back and correct a ton of values to be more accurate. But that would be _a huge project_, so it's on my mental dream list.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday May 08, 2020 at 23:56:16_

----

Hi @ibm2431 

What do you think of it now? =)

It actually makes much sense now as currently i was able to even get a drop of 4 leaf mandragora bud, it should be at least SUPER RARE as it gives you 50 goblin mystery points.

I hope the changes are now up to your standard (yes i know they can be improved further >.>'' )


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday May 09, 2020 at 00:42:10_

----

Just a reference note for when estimating what they should be at for rarity,wiki lumps all TH enhanced drops together along with drops that had no TH, and FFXIDB merges all the tiers of TH above 3. This means in many cases the rate is going to be lower than depicted and explains why sometimes its show lower than TH2, as in the following table (beehive chip).

TH tier| wiki | ffxidb rates | "very Common" off chart
------------ |------------ | ------------ | -------------
0 | 28.0 | 19.7 | 24.0 
1 | 28.0 | 37.5 | 48.0 
2 | 28.0 | 52.2 | 56.0 
3 | 28.0 | 50.5 | 60.0 

ffxidb purports a sample size of 4556 out of 19208, however I think that is the total reported for all tiers, a given tier may have a bigger or smaller portion of that sample size. Note bee pollen was added late in the games life yet has the same reported sample size.

wiki says 128/457 for its sample size, but all TH tiers are merged into one average rate.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday May 09, 2020 at 01:39:39_

----

@TeoTwawki 

Only 3 times on these 2 mobs have increase drop rate:
insect wing from 3.0% to 5.0%
behive chip from 23% to 24%
Pinch of Yuhtunga sulfur from 4.0% to 5.0%

All other items have either stayed the same rate, or dropped.

I understand an audit of all items need to be done. Looking forward to see who volunteers :cat: 




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday May 09, 2020 at 01:42:31_

----

@kaincenteno my comment about rates isn't intended to say yours are all wrong, its meant to bring the topic of how we pick the rarity tier up for feedback like I thought you wanted from our discord discussion?


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday May 09, 2020 at 01:56:39_

----

@TeoTwawki thats a good question, "how do we pick the rarity tier"

my thought for it would be to grab an avarage of the item from wiki and ffxidb and take in consideration the rate that we currently have on SQL (as most likely it was assessed in the past)
From there check the price that the item sells. If the item is cheap on ffxiah then it means its abundant and the rate should increase to the next level (so if it was uncommon before, it should now be common) and if the price is expensive then it should go the other way around.

This is how i ended up with those porcentages. Other ideas are welcomed, unless they japanese community has a more accurate drop rate from the table that SE provided would be perfect :+1: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 09, 2020 at 18:02:21_

----

> it should be at least SUPER RARE as it gives you 50 goblin mystery points

This is a surprise to see. Do different items have different mystery point values depending on drop rarity? ...Can... can we ping drop rates on an item just by giving it to the goblin...?

> however I think that is the total reported for all tiers, a given tier may have a bigger or smaller portion of that sample size

That's gross. I hadn't noticed that before. It effectively makes ffxidb useless for comparing TH tiers.

> From there check the price that the item sells. If the item is cheap on ffxiah then it means its abundant and the rate should increase to the next level

For most things, there isn't much correlation between an item's drop rate and its market value. Depending on what the item is, they could be "expensive" on AH, but are actually quite a common drop from an out-of-the-way mob that people don't feel like killing. There's also artificial inflation/deflation introduced by NPCs (ie: static guild shop NPCs) and content systems which allow people to get items through points (ie: alexandrite from ambuscade).

With how retail is these days and how I value time more than gil, I'm willing to spend an "expensive" amount of gil (30k+) on some random item I need if doing so saves me the 15-20 minutes of going out into the field and poking a mob for it.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday May 09, 2020 at 18:11:43_

----

> From there check the price that the item sells. If the item is cheap on ffxiah then it means its abundant and the rate should increase to the next level (so if it was uncommon before, it should now be common) and if the price is expensive then it should go the other way around.

um. from the view of the player some stupidly common drop may actually have value as a synth mat or a stupidly rare item might be worthless to them. pricing doesn't have anything to do with drop rates in practice after years of changes and old gear becoming obsoleted.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 09, 2020 at 18:15:21_

----

Actually, different items having different mystery point values depending on rarity won't work, as I believe different mobs will drop the _same_ item at different rates.

On the rates being proposed here on this specific PR: I'll admit I'm pretty ambivalent. The ROV items are either Rare or Very Rare. 1/100 seems a bit low from my experience (I've gotten them for 6 characters at this point). But I did so with my TH9 THF.

Looking at one of my logs:
```
The meticulously illuminated text within explains that adventurers may travel to the location of any previous books visited after paying a sum of gil or the requisite amount of tabs.
=== Area: La Theine Plateau ===
Search result: 4 people found in this area.
--- TH Mode: On ---
Huge Wasp is out of range.
Unable to see Huge Wasp.
[Nedaltic] 383 hit > Huge Wasp
Nedaltic defeats Huge Wasp.
You find a clump of bee pollen on the Huge Wasp.
You find a pot of honey on the Huge Wasp.
Nedaltic's lot for the clump of bee pollen: 695 points.
```

And another:
```
You have expended 100 kinetic units and will be transported to another locale.
=== Area: La Theine Plateau ===
--- TH Mode: On ---
Huge Wasp is out of range.
[Nedaltic] 431 hit > Huge Wasp
Nedaltic defeats Huge Wasp.
You find a clump of bee pollen on the Huge Wasp.
Nedaltic's lot for the clump of bee pollen: 525 points.
Nedaltic obtains a clump of bee pollen.
[Nedaltic] 330 hit > Huge Wasp
Nedaltic defeats Huge Wasp.
You find a beehive chip on the Huge Wasp.
Hanatori obtains a beehive chip.
Search result: 7 people found in this area.
Target out of range.
=== Area: Ordelle's Caves ===
=== Area: La Theine Plateau ===
Huge Wasp is out of range.
[Nedaltic] 437 hit > Huge Wasp
Nedaltic defeats Huge Wasp.
You find an insect wing on the Huge Wasp.
Huge Wasp is out of range.
[Nedaltic] 350 hit > Huge Wasp
Nedaltic defeats Huge Wasp.
You find an insect wing on the Huge Wasp.
You find a clump of bee pollen on the Huge Wasp.
Nedaltic's lot for the clump of bee pollen: 235 points.
Nedaltic obtains a clump of bee pollen.
```

I'll go with whatever matches _some_ data.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday May 09, 2020 at 18:20:03_

----

closing PR as there's no data to match with


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday May 09, 2020 at 18:20:27_

----

~~don't do that. it was good enough~~
~~wtf dude.~~

edit:
Kain is going through some irl stuff and doesn't have time for this :(

Sorry for semi OT chatter we put on the PR Kain.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday May 09, 2020 at 19:59:45_

----

reopening PR, can't focus on this request but leaving it here open in case there needs to be a discussion overall for all item droplist in SQL (since treasure hunter currently doesn't align with the info from SE)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday May 09, 2020 at 22:40:28_

----

Future readers: We have discussed Bee Pollen rates on Discord. If you have questions, feel free to ask and we can dig up a link to the messages~!
