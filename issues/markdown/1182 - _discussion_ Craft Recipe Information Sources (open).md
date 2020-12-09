**Labels:**



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Wednesday Sep 23, 2020 at 15:11:03_
_Originally opened as: project-topaz/topaz - Issue 1182_

----

Long story short (for now) - because some people are trashy I'm doing some work on recipes.

Major part of this is building a database of trustworthy crafting information. Absent a DAT scraper, I've been using information scraped from FFXIAH and BGWiki, procedurally melding it together via tools, and cross-checking the sources against each other.

I've generated the following lists of instances in which they don't agree:
[disagreements.zip](https://github.com/project-topaz/topaz/files/5275639/disagreements.zip)
(Apologies for the zip; the lists are HTML-ified for handy hyperlinks to the sources, and GitHub doesn't like straight attachment of HTML files.)

BGWiki and FFXIAH can disagree as to craft skill levels, result quantities, and even ingredient quantities.

**Crafting level or skill disagreements:**
- Main craft level: [FFXIAH Arhat's Tekko](https://www.ffxiah.com/recipes/1038) - [BGWiki Arhat's Tekko](https://www.bg-wiki.com/bg/Arhat's%20Tekko)
- Sub craft level: [FFXIAH Minnow](https://www.ffxiah.com/recipes/88) - [BGWiki Minnow](https://www.bg-wiki.com/bg/Minnow)
- Main craft skill: [FFXIAH Oak Bed](https://www.bg-wiki.com/bg/Oak%20Bed) - [BGWiki Oak Bed](https://www.bg-wiki.com/bg/Oak%20Bed)
- Both main skill and sub level: [FFXIAH Water Tank](https://www.ffxiah.com/recipes/16) - [BGWiki Water Tank](https://www.bg-wiki.com/bg/Water%20Tank)

"FFXIAH used to scrape the client, we can trust it"

**Result quantity / HQ  disagreements:**
- "Mass Production" Synths: [FFXI Lauan Lumber](https://www.ffxiah.com/recipes/3310) - [BGWiki Lauan Lumber](https://www.bg-wiki.com/bg/Lauan%20Lumber)
- "HQ as NQ" Quantity: [FFXI Rice Dumpling](https://www.ffxiah.com/recipes/1458) - [BGWiki Rice Dumpling](https://www.bg-wiki.com/bg/Rice%20Dumpling)
- HQ Quantity (Desynth): [FFXI Tekko Desynth](https://www.ffxiah.com/recipes/1182) - [BGWiki Tekko Desynth](https://www.bg-wiki.com/bg/Tekko)

"Maybe just the results were changed by retail?"

**Ingredient quantity disagreements:**
- Not clear which is correct: [FFXIAH Lord's Cuirass](https://www.ffxiah.com/recipes/1904) - [BGWiki Lord's Cuirass](https://www.bg-wiki.com/bg/Lord's%20Cuirass)
- BG clearly wrong: [FFXIAH Roshi Jinpachi](https://www.ffxiah.com/recipes/1068) - [BGWiki Roshi Jinpachi](https://www.bg-wiki.com/bg/Roshi%20Jinpachi)

**We'll have to come up with a set of rules of which information to take when. It's not always one or the other.**

BGWiki's information is more recent (with more recipes), and seems to always win in result quantity matchups.

BGWiki might suffer from ingredient quantity typos, but it's not always clear when. But ingredient quantities can be easily verified on retail. Example: I can check Lord's Cuirass myself next free period. Or people with access to retail can ask crafter friends to test.

My main concern is crafting skill level disagreements. Even if BGWiki is _certain_ about a craft's level (they usually indicate when they're unsure), they can disagree with FFXIAH. And there are some situations in which FFXIAH is claiming a subcraft level which doesn't make sense:
[FFXIAH Austere Sabots](https://www.ffxiah.com/recipes/734) - [BGWIKI Austere Sabots](https://www.bg-wiki.com/bg/Austere%20Sabots)
Why would there be a subscraft level of 1? How would a BGWiki editor even know there was a subcraft if it was 1? This makes me believe someone was prevented from crafting the boots due to the subcraft truly being 11.

Finally, these aren't in a HTML list because I needed to manually remove them from XML (and there were only a handful), but FFXIAH even has some "dead recipes":
- Empty Result: [FFXIAH Nothing 1](https://www.ffxiah.com/recipes/1020) - [BGWiki Puk Fletching](https://www.bg-wiki.com/bg/Puk_Fletching)
- Empty Result and ingredient quantity disagreement: [FFXIAH Nothing 2](https://www.ffxiah.com/recipes/1019) - [BGWiki Puk Fletching](https://www.bg-wiki.com/bg/Puk_Fletching)

Why are there empty results? How might a DAT scraper have generated that recipe entry?

**tl;dr:** What should be trusted when?

**I'd like as few "judgment calls" as possible.** The _ideal_ is that there's a set of rules we follow, and if anyone comes around in the future wondering why some recipe's information doesn't match one or the other, we can point them to this thread.

**edit:** Updated zip with ffxiah-only.html, which are recipes that have a result (ignoring quantity) and ingredient list with no corresponding recipe found on bgwiki.
- Desynth (Dummy?): [FFXIAH Recipe 3258](https://www.ffxiah.com/recipes/3258) - [BGWiki Legionaire's Knuckles](https://www.bg-wiki.com/bg/Lgn._Knuckles)
- Ingredient Mismatch: [FFXIAH Witch Nougat](https://www.ffxiah.com/recipes/3883) - [BGWiki Witch Nougat](https://www.bg-wiki.com/bg/Witch%20Nougat) (FFXIAH replaces Selbina Milk with Selbina Butter)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Sep 23, 2020 at 15:16:06_

----

(But before someone says it: I don't consider FFXIclopedia as a source.)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 23, 2020 at 15:27:47_

----

As a general rule, I think people are more likely to start a conversation (read: complain) when things are too hard, rather than when things are too easy. This conversation will result in things getting fixed, or more in-depth research being done. 

What is more likely to make someone complain: A recipe being too low level to reach a certain skill level on, or it being too high so they can't start skilling up on it when they're supposed to?


----
<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Wednesday Sep 23, 2020 at 15:34:22_

----

I don't know where FFXIAH gets its recipes from, but they also do not seem to have stopped maintaining after a point. I'd speculate that some of them may have been culled from the .dats themselves originally (before recipes were moved server side). While FFXIAH isn't perfect, there is still data that can be gleaned there from it's user base.

Since recipe caps and sub skills are often inferred based on user experience, I'd trust BGwiki as a definitive source generally, but there have to be instances where we're willing to diverge if we can confirm otherwise. Adding comments in the PR and/or SQL would be helpful here.

I don't see a path where there can be perfect data unless some figures out how to automate collecting the data directly from retail.

So as a general path, my opinion is:

1. Base the recipe on data available from BGWiki
2. Inaccuracies/disputes should source another reliable community resource or sources (good) OR provide data directly from retail to support (best). 
3. In events where its clear that the data from BGWiki is wildly inaccurate, have a fail back to a final Judgement call.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Sep 23, 2020 at 15:56:32_

----

> Since recipe caps and sub skills are often inferred based on user experience, I'd trust BGwiki as a definitive source generally

Agreed with this. People usually don't edit a page unless they have reason to believe it's wrong.

---

I was scrolling through the list again and saw another example I want to bring up:
[FFXIAH - Igqira Lappas](https://www.ffxiah.com/recipes/644)
[BGWiki - Igqira Lappas](https://www.bg-wiki.com/bg/Igqira%20Lappas)

_If_ FFXIAH was scraping, it's done so since when the [Senbaak Nagan](https://www.ffxiah.com/recipes/3891) was added to the game. Missing the subcraft on Igqira of all things is very, very strange.


----
<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Wednesday Sep 23, 2020 at 16:47:04_

----

I'm not sure who's at the helm at FFXIAH these days. You might be able to reach out to Scragg to see if he can shed any light on how it's done or was done if you want to scratch that itch.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Sep 23, 2020 at 17:28:10_

----

> How would a BGWiki editor even know there was a subcraft if it was 1?

You would occasional get a skillup. and they skillups would cease once skilled up. But I think they example was clearly a mistake and was meant to say 11.

> "FFXIAH used to scrape the client, we can trust it"

Unproven, there are a lot of indicators\* but we don't know with certainty exactly how ffxi got its recipes.

\*Like seeing the unused hidden duplicates in their lists and unreleased recipes with common SE placeholder values. _Two fiddy five anyone?_


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Sep 23, 2020 at 17:35:49_

----

> 
> 
> I'm not sure who's at the helm at FFXIAH these days. You might be able to reach out to Scragg to see if he can shed any light on how it's done or was done if you want to scratch that itch.

I haven't been able to get hold of Scragg or Jaerik in 3+ yrs. I don't think he Scragg that inbox anymore. Best bet is probably to see if Rooks can tell us or contact someone who knows on our behalf.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Sep 24, 2020 at 12:00:52_

----

I've updated the zip with ffxiah-only.html, which are recipes that have a result and ingredient list with no corresponding recipe from bgwiki's main craft lists.
- Desynth (Dummy?): [FFXIAH Recipe 3258](https://www.ffxiah.com/recipes/3258) - [BGWiki Legionaire's Knuckles](https://www.bg-wiki.com/bg/Lgn._Knuckles)
- Ingredient Mismatch: [FFXIAH Witch Nougat](https://www.ffxiah.com/recipes/3883) - [BGWiki Witch Nougat](https://www.bg-wiki.com/bg/Witch%20Nougat) (FFXIAH replaces Selbina Milk with Selbina Butter)

While some of the items in the new HTML file are result quantity mismatches, a lot of them are "FFXIAH Only" desynths which have no corresponding entry for the source item on BGWiki. Many don't have any crafting level for the desynth (see above Legionaire's Knuckles). But there are some FFXIAH recipes which do ([FFXIAH Shall Shell Desynth](https://www.ffxiah.com/recipes/471)), but still aren't listed on the source item for BGWiki ([Shall Shell](https://www.bg-wiki.com/bg/Shall_Shell))

The Witch Nougat example has caught my attention. Both sources have different ingredients _and_ results. Anyone with Cooking main on retail could see which is which (maybe try both?) - it looks like an easy recipe (may have to farm chips and almonds).

Finally, a `nil` error while trying to run the script did bring this fun recipe to light:
[FFXIAH Recipe 3821](https://www.ffxiah.com/recipes/3821)
Indeed there is, Scraag.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Sep 27, 2020 at 22:42:06_

----

In instances in which there are multiple item IDs with the same name, which do we take?

https://www.ffxiah.com/item/4399/bluetail
https://www.ffxiah.com/item/5798/bluetail

https://www.ffxiah.com/item/4472/crayfish
https://www.ffxiah.com/item/5785/crayfish

https://www.ffxiah.com/item/4428/dark-bass
https://www.ffxiah.com/item/5786/dark-bass

The one being sold on FFXIAH? Is this always the lower ID? Which ones are _we_ using?

~~This seems to be a problem unique to fish of all kinds.~~

**edit:** PUP attachments too.
https://www.ffxiah.com/item/2268/mana-conserver
https://www.ffxiah.com/item/8675/mana-conserver

And Quick Draw cards:
https://www.ffxiah.com/item/2183/dark-card
https://www.ffxiah.com/item/9771/dark-card

I'm going with the lowest ID, but this might be something to remember.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Sep 28, 2020 at 23:58:57_

----

Maybe not always the lower item ID.

https://www.ffxiah.com/item/16818/san-dorian-sword
https://www.ffxiah.com/item/17678/san-dorian-sword

(The +2 version from [Recipe 1578](https://www.ffxiah.com/recipes/1578) is ID 17679, so I'm going with 17678 on this one.)

But at least my scripts have been catching these for manual verification!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 29, 2020 at 12:17:44_

----

that 2nd sandorian they never added to game. But works in private servers since we gave it a model and mods. there are a lot of unused items like that, I think SE has the duplicate fish for a diff reason.



----
<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Tuesday Sep 29, 2020 at 16:33:25_

----

We speculated that the secondary set of fish IDs might come from MMM since there's a whole fishing system in there. There is some empirical evidence of this in the following:

http://www.ffxiah.com/item/5809

Note that the next item ID in the block (http://www.ffxiah.com/item/5810) also has a reference to MMM in the comments (albeit from the same reporter).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Sep 29, 2020 at 17:33:05_

----

Finishing up the master XML, but for the record, I am thoroughly convinced that FFXIAH's recipes _weren't_ from scraping client DATs, but from tracking synth results with Guildwork.

Four reasons:
1) Incorrect yields on many recipes (the x99 result being marked as the NQ when it should be x33), and in a couple cases, FFXIAH having the +1 of an item as the NQ (for a cooking recipe, not an "equipment upgrade"). This leads me to believe FFXIAH based its NQ information off of what came out of a Guildwork-running player doing the recipe. If it only ever sees the x99 result...

2) Zero key item requirements. At first I thought maybe they didn't know how to read KI requirements, but thinking about it from the "Guildwork tracking" perspective, how _would_ they determine which key item is required for a recipe if they're using Guildwork data? You _could_ get possessed key items on synth, but what are you going to do, slowly do process of elimination until you narrow it down to the one key item everyone has when they perform the synth? "Well, everyone who has ever done this synth has an Adventurer's Certificate, so it must be required for the recipe!" It'd be an impossible problem for them to solve with a "from Guildwork" approach, which makes me suspect it's the _reason_ FFXIAH doesn't have KIs.

3) FFXIAH not having precise levels for all crafts in a recipe has been gnawing at me. It stating values of 255 for all crafts could have an argument that it was scraped before the recipe was "real". But there are cases when it has a value for the main craft, but "unknown" for one or both subcrafts. It wouldn't make sense for it to have been scraped in that case - scraped skill levels would be either all or nothing. Since it's instead "some", I think that instead FFXIAH/Guildwork had been tracking skillups and compiling that data for a recipe's "known" levels.

4) When the data stopped, as Teo previously commented on, as being around when Guildwork went bjorked.

That said, the FFXIAH data has still been _useful_. I've been using it to cross-verify against BGWiki, and will have a list of recipes in which the sources disagree on crystal/ingredients. And even if FFXIAH's skill levels _weren't_ scraped from DATs, it still used an automated process across multiple players to compile craft levels and put the number online. I trust that a little more than a sole editor doing calculations and manually inputting their result on wiki page.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Sep 29, 2020 at 18:13:04_

----

Another small snag - there are times when FFXIAH and BGWiki disagree on the skill level for an item that's now one of the "Craft Kits" that retail has.

**FFXIAH States 9, but Bonecraft Kit 10** - [FFXIAH Recipe 453](https://www.ffxiah.com/recipes/453) - [BGWiki Bone Arrowheads](https://www.bg-wiki.com/bg/Bone%20Arrowhd.)

**FFXIAH States 28, but Bonecraft Kit 30** - [FFXIAH Recipe 484](https://www.ffxiah.com/recipes/484) - [BGWiki Beetle Mask](https://www.bg-wiki.com/bg/Beetle%20Mask)

Three possibilities:
1. "Maybe FFXIAH got the level wrong?"
2. "Maybe the skill level was changed on the item after kits were introduced?"
3. "Maybe SE just picked items for those kits that _weren't_ the level stated and BGWiki is assuming equality based on the name?"

Retail now gets skillups past the original "skill cap" of the recipe, so it may be hard to tell that something in "Bonecraft Kit 30" is actually level 28.

**edit:** [Beetle Mask was changed on BGWiki to level 30 by an editor when the kits were added. Before, it was level 28 and matched FFXIAH.](https://www.bg-wiki.com/index.php?title=Beetle_Mask&diff=383065&oldid=338595)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 29, 2020 at 21:09:18_

----

> It stating values of 255 for all crafts could have

As I mentioned on discord could also just be that the record from guildwork got garbled in transit either on its way from the client or after the fact moving from gw to ffxiah to. But I was hopeful their "recipe id" wasn't just made up. :(


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Friday Oct 09, 2020 at 11:31:56_

----

It's not that difficult to find out, you just spam Beetle mask until you cap (the probability of skillup is high enough so you can confidently determine that you reached the cap).
