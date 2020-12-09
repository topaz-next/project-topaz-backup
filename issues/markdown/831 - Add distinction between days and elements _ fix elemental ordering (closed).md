**Labels:**



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 12:33:34_
_Originally opened as: project-topaz/topaz - Issue 831_

----

They may not know it yet, but this Pull Request will make some people unhappy. But it's _long_ overdue.

---

For those unaware of the problem (skip to the next horizontal rule if you're already familiar):

A long time ago, someone decided to make enums go in the following order:
> Firesday, Earthsday, Watersday, Windsday, Iceday, Lightningsday, Lightsday, Darksday

This was the correct decision, as it follows retail. However, a later decision then came:
> When asked what element the current day is, we'll return the current day.

But on retail - with the exception of days of the week and Avatars (and their abilities) - elements follow the elemental wheel:
> Fire Ice Wind Earth Thunder Water Light Dark

Everything that retail does referencing elements follows that order: spell IDs, crafting crystal item IDs, elemental ability IDs, models, etc.

(Yes @TeoTwawki, I know spikes don't, but those are the exception~! 😉 )

The mismatch between retail's standard elemental ordering and ours has a long list of rippling effects.

**For some examples see:**
https://github.com/DarkstarProject/darkstar/issues/6002

These effects at their most benign require additional bridge tables which shouldn't be necessary. One recent example being the [mapping table that @Omnione needed for Geomancer bubble effects and models](https://github.com/project-topaz/topaz/blob/1a942bbe006d6e2b0778177b9940dbff9e33bcc2/scripts/globals/geo.lua#L14-L41) - which was the last straw. At their worst the elemental ordering mismatch causes incorrect elemental behavior when wires get crossed from using the correct order to our incorrect order.

---

So this Pull Request:
1) Creates a distinction between days of the week and magical elements
2) Adjusts all things referencing magical elements to do so in the corrected elemental order
3) Adjusts things referencing _the current day_ to check _the day_ and _not_ its element; _this distinction is important_

Forewarning: I will have missed something. I don't know what it is yet. I've done the best I can to find and address all references to days and elements that I can think of.

**I deliberately broke this up into multiple commits for ease of review. Use the commit-by-commit review feature!**

For example, I broke the SQL changes into "two steps" of commits. The "first step" commit replaces the old values with a string, so a reviewer can quickly gauge that the old values were correctly picked up and marked. The "second step" commit replaces those strings with the new, updated value. So don't fret about SQL change diff, just verify that yes, I can indeed correctly use regex~!

**I have deliberately not touched crafting due to #779 reworking the system and outright removing many of the references currently present!** Either @Xaver-DaRed or I will have to rebase and adjust our PRs accordingly depending on what gets merged when. **Any branch from this PR should _not_ go into release or canary until changes to the crafting system have been finalized and the branch adjusted to correct crafting elements (if still required).**

I'll be doing a "review" of this PR to preemptively answer questions a reviewer might have. I've been working on this over the course of a week, and may come across something that needs fixing. Will push follow-up commits if I do.

Closes #291 

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 10, 2020 at 12:45:13_

----

> (Yes @TeoTwawki, I know spikes don't, but those are the exception~! wink )

The subeffect orders, they haunt me so! WHY SE? WHY?!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 15:43:20_

----

61e492c is me finalizing a retreat from reordering skillchains. While dealing with elements, I found that they didn't match retail's order (see message IDs), and began "resorting them while I'm here".

When I realized the full depth of the reordering, I decided to shelve it and retreat from capsizing both myself and reviewers. I apparently missed a bit during my retreat.
