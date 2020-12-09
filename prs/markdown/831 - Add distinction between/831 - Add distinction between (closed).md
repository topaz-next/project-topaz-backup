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
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 13:04:53_

----

[Because days of the week aren't "weather"](https://github.com/ibm2431/topaz/blob/master/scripts/globals/weather.lua#L30-L40). And [time](https://github.com/ibm2431/topaz/blob/master/scripts/globals/weather.lua#L42-L52) isn't either.

Due to the importance of days and weather, and how some mods reference them, `status.lua` was modified to require this new `world` global. As such, files which required both `status` and `weather` just had `weather` removed for being redunant.

Side: We'll have to revisit our global require system in the future. `status.lua` has become a "catch-all" for "important things I don't know where to put", and a bunch of the enums which need to be required should just always be available without requiring a scripter to know and remember to include a certain global.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 13:09:10_

----

"Pet IDs" were one of the things already following the true elemental order, but their listed `element` in `pet_list` did not. So this script was trying to map their true-element-order ID to the old day-of-the-week elemental ordering. Confusing, huh?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 13:49:25_

----

`tpz.magic.dayElement` can be used to determine any given day's element; it's in `magic.lua`

While it can be used for determining the current day's element, there's a handy `VanadielDayElement()` function given to you by core _without_ need to `tpz.magic.dayElement[VanadielDayOfTheWeek()]`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 13:53:40_

----

There is an enum in core for "enspell IDs", which these effect scripts need to match.

(There isn't a copy of that enum table in lua.)

When messing with enspells, I discovered that Endark II wasn't in there; so I gave it a spot, and pushed blood weapon back.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 13:54:53_

----

For the first 8 "enspell IDs", the ID matches the spell's element. So I told the tier I scripts to use a relevant element in effort to reduce magic numbers in scripts.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 13:55:35_

----

In core, the "enspell IDs" are aligned such as:
Elemental Tier Is
Elemental Tier IIs
Other "enspell" effects (blood weapon)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 13:56:24_

----

This is the first example of a script no longer needed the `weather` global due to it already requiring `status`.

Sorry if I merge conflict you on #796 , @wrenffxi 😦 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:02:25_

----

Regarding the removal of `elementalObiStrong` and `elementalObiWeak`:
> 
ibm2431: So. We apparently calculate day/element/obi bonuses/penalties in three separate locations in magic.lua
ibm2431: And all of them are wrong in some fashion or another
ibm2431: For most of them, we're checking to see if the caster is wearing the obi matching the "weak" element when casting a spell on the wrong day

ibm2431: Let's assume fire, since that's the one element enum we have right:
https://github.com/project-topaz/topaz/blob/release/scripts/globals/magic.lua#L35
https://github.com/project-topaz/topaz/blob/release/scripts/globals/magic.lua#L750-L777
ibm2431: Comes out to:
```
ele = fire -- spell:getElement()
if weather == rain then -- tpz.magic.singleWeatherWeak[ele]
    if chance < 0.33 or caster:mod(tpz.mod.FORCE_WATER_DWBONUS) then -- elementalObiWeak[ele]
        dayWeatherBonus = dayWeatherBonus - 0.10
```
ibm2431: Which will weaken fire magic in rain 100% of the time if the caster is wearing Suirin Obi; not Karin Obi
aether: oh should it be FORCE_FIRE_DWBONUS?
ibm2431: That's what it should be resolving to, yeah
ibm2431: I've already addressed it in this commit I'm working on, but it'll take maybe a week to PR it
ibm2431: I simply axed both "elementalObiStrong" and "elementalObiWeak"; replacing them with just "elementalObi"


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:05:53_

----

Just standard removal of magic numbers when I found them. There were sections of code dealing with elements which I missed on my first pass because they weren't referencing the word element or any actual elemental name - just numbers.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:09:29_

----

The four elements which can be chosen from for Crystal Weapon (confirmed to match old wiki's description, search Discord for "crystal weapon" for discussion) just happen to be the first four days of the week.

Elements start at 1, since `ELEMENT_NONE` is 0.

Days of the week start at 0, as that's the very first day of the week when a server is set to its earliest epoch - there is no "Nonday".

The previous code started from 6 to match the beginning _damageType_ for fire (various physical types are listed in the damageType before Fire is).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:16:32_

----

This is one such instance when behavior depending on the _current day_ should be referencing _the current day_ and _not an "element"_.

In defense of the previous scripter, `VanadielDayElement()` _was_ the only way to get the current day, because it _was_ one in the same as the current day of the week. I'm adding `VanadielDayOfTheWeek()` myself in this PR.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:19:20_

----

This is another example of why the distinction between days and elements is important~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:23:54_

----

I tried to avoid changing unrelated things during my journeys, but couldn't resist here.

The localVar set and printf weren't needed, as it's _impossible_ for lua to reach csid 529's eventFinish unless core started it.

There are checks built into core which set a character's current CS when `player:startEvent` is called. Even if a player tries to inject a fake event option (ie: "finish") packet, core (and by extension lua scripts) ignore it unless core itself had already marked the player as currently being on that event.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:34:28_

----

As all furniture has elemental auras, `item_furnishing`'s element field was "base 0 == fire". 

_And_ oddly enough, unlike a lot of other things which followed "day of the week" numbering, the table already followed the true elemental order.

This combination lead to much confusion on my part when first examining this file and "1" was listed as the element for pieces of furniture which wikis were listing as ice (as opposed to "fire" or "earth").

To avoid such confusion in the future, and make sure _all_ references to elements are consistent, I incremented the "element" for all furniture by 1.

So "8" == darkness == [Chocobo Bedding's listed element](https://www.bg-wiki.com/bg/Chocobo_Bedding)
"6" == water == [Simple Bed's listed element](https://www.bg-wiki.com/bg/Simple_Bed)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:41:38_

----

Remember to review commit-by-commit, it's easier!

Here's some links to modifiers both before and after my changing:
[Before - "current" mods](https://github.com/ibm2431/topaz/blob/ecd6264e51ce7c35b2a91cb688ee57329cfe1d24/src/map/modifier.h)
[After - some mods changed to align with new elemental order](https://github.com/ibm2431/topaz/blob/7792b82e678e29f6e8eae30fd0904ec929a397a7/src/map/modifier.h)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:42:54_

----

For even more confusion later: `pet_list` was using the day-of-the-week values for `element`, but `mob_family_system` was using the true-elemental ordering in its `element` field for the purposes of crystal drops!

So you had Ice Spirits pets with `element` of 5, which were members of the Ice Elemental family with `element` of 2!

Honestly, now that the elemental ordering has been corrected, this `element` column could probably be removed from `pet_list`. But I didn't want to rock the boat too much in a single PR.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:51:14_

----

Heads up, anyone who modifies `spell_list` with non-retail changes!

(I know this includes you, @Lynnea1320 😅 )

We're changing a bunch of element IDs for spells!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:54:02_

----

Elemental IDs for currently unimplemented spells were _not_ adjusted. Such line comments are _already_ out of date and are missing spell_family definitions.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:55:32_

----

I believe I looked into this, and I wasn't able to find anywhere that actually used these elements which were being set. I think this can be removed later.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:56:59_

----

In the ultimate irony, there has _always_ been a definition for Elements which go in the _correct_ order. _But it was never once used anywhere!_


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:58:29_

----

Elements for furnishings are now base 1, but the `elements` table defined up above (unchanged, you'll have to expand up) is, of course, base zero. You'll see this a couple places on the core side.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 15:04:44_

----

I went back and forth on this. I originally considered having elements be part of the time object, but that didn't feel entirely right:
- Elements are really only referenced in the context of combat (spell elements)
- We currently have GetWeather in `battleutils`, I wanted GetDayElement to be in there with it, and I was hesitant to create yet another header/util for "common world" functions (too much rocking the boat for one PR)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 15:09:14_

----

Enspells required some restructuring, as the subeffect array had a rather confusing order with listed Light/Dark _first_ (I'm not certain why this was done) and then the normal elements (in day-of-week order).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 15:14:52_

----

[Endark II](https://www.bg-wiki.com/bg/Endark_II) wasn't in this table.

"Enspell Rolling Thunder" is never used - the [ability simply uses Enthunder instead](https://github.com/ibm2431/topaz/blob/master/scripts/globals/abilities/pets/rolling_thunder.lua).

So Blood Weapon's "enspell ID" got pushed back by one.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 15:17:54_

----

I didn't change the ordering in this array due to the fact that weather is currently in an... odd... order. You might have to expand down to see it. This is in both core [and lua](https://github.com/ibm2431/topaz/blob/master/scripts/globals/weather.lua#L6-L23).

This may be of interest to @Kreidos 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 15:22:44_

----

While I was investigating where to put `GetDayElement` (ie: "here in the time object?") I came across:
`case  0: m_TimeType = TIME_NIGHT`, and _assumed_ it should be `TIME_MIDNIGHT`. Other line diffs were just spacing since `MIDNIGHT` is longer than `EVENING`.

Yell at me if my assumption was wrong, @Kreidos 


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Jul 10, 2020 at 15:30:04_

----

Whoops! That one wasn't me, but I did miss it when I did the TOTD fix. Good catch.

Edit: At least the returned value was correct, it looks like only the Lua was dependent on m_TimeType, and nothing is using it right now.


----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Friday Jul 10, 2020 at 15:34:40_

----

Okay I'll keep an eye out for this.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Jul 10, 2020 at 15:46:54_

----

The WEATHER enum stores the actual packet/client values for weather so the order there is accurate and should probably stay unchanged. As well, nothing that changes here should affect weather in-game or in the DB as those only rely on the WEATHER enum being correct. :)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 15:51:05_

----

Huh. I guess [I should have checked](https://github.com/Windower/Resources/blob/master/resources_data/weather.lua#L3-L23). 

Come on SE, why do you do such things to us. 😢 

I'll amend the comment - and maybe place a few others in weather enums - so others don't make the same assumption I did.

Thanks, Kreidos~


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 10, 2020 at 16:37:17_

----

I think there was a plan top use them, before they got put into script instead. So its kinda redundant.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 10, 2020 at 16:47:36_

----

short version: CS event injection is only a concern for _parameters_ and not the csid itself. 



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 10, 2020 at 16:55:36_

----

>  there is no "Nonday".

irl we call it Monday. Monday tries to return us all to non existence by sucking. Vanadiel doesn't know how lucky it is to not have Monday.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 10, 2020 at 16:58:51_

----

if pet ID is arbitrary and none are capped (I thought the early ones were and then at higher IDs we through packet info out the window) we could shift them up by one having fire start at 1 and then they'd align without addition.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 10, 2020 at 17:00:03_

----

..in a future pr because who wants to fix the other pr's depending on the pet ids, right?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 10, 2020 at 17:08:32_

----

thanks for the warning. I have a bunch of replace rows (I was too lazy for update statements, so I copypasted then edited a column value) to mod enmity. I'll need to update my rows.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 13:04:53_

----

[Because days of the week aren't "weather"](https://github.com/ibm2431/topaz/blob/master/scripts/globals/weather.lua#L30-L40). And [time](https://github.com/ibm2431/topaz/blob/master/scripts/globals/weather.lua#L42-L52) isn't either.

Due to the importance of days and weather, and how some mods reference them, `status.lua` was modified to require this new `world` global. As such, files which required both `status` and `weather` just had `weather` removed for being redunant.

Side: We'll have to revisit our global require system in the future. `status.lua` has become a "catch-all" for "important things I don't know where to put", and a bunch of the enums which need to be required should just always be available without requiring a scripter to know and remember to include a certain global.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 13:09:10_

----

"Pet IDs" were one of the things already following the true elemental order, but their listed `element` in `pet_list` did not. So this script was trying to map their true-element-order ID to the old day-of-the-week elemental ordering. Confusing, huh?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 13:49:25_

----

`tpz.magic.dayElement` can be used to determine any given day's element; it's in `magic.lua`

While it can be used for determining the current day's element, there's a handy `VanadielDayElement()` function given to you by core _without_ need to `tpz.magic.dayElement[VanadielDayOfTheWeek()]`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 13:53:40_

----

There is an enum in core for "enspell IDs", which these effect scripts need to match.

(There isn't a copy of that enum table in lua.)

When messing with enspells, I discovered that Endark II wasn't in there; so I gave it a spot, and pushed blood weapon back.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 13:54:53_

----

For the first 8 "enspell IDs", the ID matches the spell's element. So I told the tier I scripts to use a relevant element in effort to reduce magic numbers in scripts.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 13:55:35_

----

In core, the "enspell IDs" are aligned such as:
Elemental Tier Is
Elemental Tier IIs
Other "enspell" effects (blood weapon)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 13:56:24_

----

This is the first example of a script no longer needed the `weather` global due to it already requiring `status`.

Sorry if I merge conflict you on #796 , @wrenffxi 😦 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:02:25_

----

Regarding the removal of `elementalObiStrong` and `elementalObiWeak`:
> 
ibm2431: So. We apparently calculate day/element/obi bonuses/penalties in three separate locations in magic.lua
ibm2431: And all of them are wrong in some fashion or another
ibm2431: For most of them, we're checking to see if the caster is wearing the obi matching the "weak" element when casting a spell on the wrong day

ibm2431: Let's assume fire, since that's the one element enum we have right:
https://github.com/project-topaz/topaz/blob/release/scripts/globals/magic.lua#L35
https://github.com/project-topaz/topaz/blob/release/scripts/globals/magic.lua#L750-L777
ibm2431: Comes out to:
```
ele = fire -- spell:getElement()
if weather == rain then -- tpz.magic.singleWeatherWeak[ele]
    if chance < 0.33 or caster:mod(tpz.mod.FORCE_WATER_DWBONUS) then -- elementalObiWeak[ele]
        dayWeatherBonus = dayWeatherBonus - 0.10
```
ibm2431: Which will weaken fire magic in rain 100% of the time if the caster is wearing Suirin Obi; not Karin Obi
aether: oh should it be FORCE_FIRE_DWBONUS?
ibm2431: That's what it should be resolving to, yeah
ibm2431: I've already addressed it in this commit I'm working on, but it'll take maybe a week to PR it
ibm2431: I simply axed both "elementalObiStrong" and "elementalObiWeak"; replacing them with just "elementalObi"


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:05:53_

----

Just standard removal of magic numbers when I found them. There were sections of code dealing with elements which I missed on my first pass because they weren't referencing the word element or any actual elemental name - just numbers.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:09:29_

----

The four elements which can be chosen from for Crystal Weapon (confirmed to match old wiki's description, search Discord for "crystal weapon" for discussion) just happen to be the first four days of the week.

Elements start at 1, since `ELEMENT_NONE` is 0.

Days of the week start at 0, as that's the very first day of the week when a server is set to its earliest epoch - there is no "Nonday".

The previous code started from 6 to match the beginning _damageType_ for fire (various physical types are listed in the damageType before Fire is).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:16:32_

----

This is one such instance when behavior depending on the _current day_ should be referencing _the current day_ and _not an "element"_.

In defense of the previous scripter, `VanadielDayElement()` _was_ the only way to get the current day, because it _was_ one in the same as the current day of the week. I'm adding `VanadielDayOfTheWeek()` myself in this PR.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:19:20_

----

This is another example of why the distinction between days and elements is important~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:23:54_

----

I tried to avoid changing unrelated things during my journeys, but couldn't resist here.

The localVar set and printf weren't needed, as it's _impossible_ for lua to reach csid 529's eventFinish unless core started it.

There are checks built into core which set a character's current CS when `player:startEvent` is called. Even if a player tries to inject a fake event option (ie: "finish") packet, core (and by extension lua scripts) ignore it unless core itself had already marked the player as currently being on that event.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:34:28_

----

As all furniture has elemental auras, `item_furnishing`'s element field was "base 0 == fire". 

_And_ oddly enough, unlike a lot of other things which followed "day of the week" numbering, the table already followed the true elemental order.

This combination lead to much confusion on my part when first examining this file and "1" was listed as the element for pieces of furniture which wikis were listing as ice (as opposed to "fire" or "earth").

To avoid such confusion in the future, and make sure _all_ references to elements are consistent, I incremented the "element" for all furniture by 1.

So "8" == darkness == [Chocobo Bedding's listed element](https://www.bg-wiki.com/bg/Chocobo_Bedding)
"6" == water == [Simple Bed's listed element](https://www.bg-wiki.com/bg/Simple_Bed)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:41:38_

----

Remember to review commit-by-commit, it's easier!

Here's some links to modifiers both before and after my changing:
[Before - "current" mods](https://github.com/ibm2431/topaz/blob/ecd6264e51ce7c35b2a91cb688ee57329cfe1d24/src/map/modifier.h)
[After - some mods changed to align with new elemental order](https://github.com/ibm2431/topaz/blob/7792b82e678e29f6e8eae30fd0904ec929a397a7/src/map/modifier.h)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:42:54_

----

For even more confusion later: `pet_list` was using the day-of-the-week values for `element`, but `mob_family_system` was using the true-elemental ordering in its `element` field for the purposes of crystal drops!

So you had Ice Spirits pets with `element` of 5, which were members of the Ice Elemental family with `element` of 2!

Honestly, now that the elemental ordering has been corrected, this `element` column could probably be removed from `pet_list`. But I didn't want to rock the boat too much in a single PR.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:51:14_

----

Heads up, anyone who modifies `spell_list` with non-retail changes!

(I know this includes you, @Lynnea1320 😅 )

We're changing a bunch of element IDs for spells!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:54:02_

----

Elemental IDs for currently unimplemented spells were _not_ adjusted. Such line comments are _already_ out of date and are missing spell_family definitions.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:55:32_

----

I believe I looked into this, and I wasn't able to find anywhere that actually used these elements which were being set. I think this can be removed later.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:56:59_

----

In the ultimate irony, there has _always_ been a definition for Elements which go in the _correct_ order. _But it was never once used anywhere!_


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 14:58:29_

----

Elements for furnishings are now base 1, but the `elements` table defined up above (unchanged, you'll have to expand up) is, of course, base zero. You'll see this a couple places on the core side.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 15:04:44_

----

I went back and forth on this. I originally considered having elements be part of the time object, but that didn't feel entirely right:
- Elements are really only referenced in the context of combat (spell elements)
- We currently have GetWeather in `battleutils`, I wanted GetDayElement to be in there with it, and I was hesitant to create yet another header/util for "common world" functions (too much rocking the boat for one PR)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 15:09:14_

----

Enspells required some restructuring, as the subeffect array had a rather confusing order with listed Light/Dark _first_ (I'm not certain why this was done) and then the normal elements (in day-of-week order).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 15:14:52_

----

[Endark II](https://www.bg-wiki.com/bg/Endark_II) wasn't in this table.

"Enspell Rolling Thunder" is never used - the [ability simply uses Enthunder instead](https://github.com/ibm2431/topaz/blob/master/scripts/globals/abilities/pets/rolling_thunder.lua).

So Blood Weapon's "enspell ID" got pushed back by one.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 15:17:54_

----

I didn't change the ordering in this array due to the fact that weather is currently in an... odd... order. You might have to expand down to see it. This is in both core [and lua](https://github.com/ibm2431/topaz/blob/master/scripts/globals/weather.lua#L6-L23).

This may be of interest to @Kreidos 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 15:22:44_

----

While I was investigating where to put `GetDayElement` (ie: "here in the time object?") I came across:
`case  0: m_TimeType = TIME_NIGHT`, and _assumed_ it should be `TIME_MIDNIGHT`. Other line diffs were just spacing since `MIDNIGHT` is longer than `EVENING`.

Yell at me if my assumption was wrong, @Kreidos 


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Jul 10, 2020 at 15:30:04_

----

Whoops! That one wasn't me, but I did miss it when I did the TOTD fix. Good catch.

Edit: At least the returned value was correct, it looks like only the Lua was dependent on m_TimeType, and nothing is using it right now.


----
<a href="https://github.com/Lynnea1320"><img src="https://avatars3.githubusercontent.com/u/38861984?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Lynnea1320](https://github.com/Lynnea1320)**
_Friday Jul 10, 2020 at 15:34:40_

----

Okay I'll keep an eye out for this.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Friday Jul 10, 2020 at 15:46:54_

----

The WEATHER enum stores the actual packet/client values for weather so the order there is accurate and should probably stay unchanged. As well, nothing that changes here should affect weather in-game or in the DB as those only rely on the WEATHER enum being correct. :)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 10, 2020 at 15:51:05_

----

Huh. I guess [I should have checked](https://github.com/Windower/Resources/blob/master/resources_data/weather.lua#L3-L23). 

Come on SE, why do you do such things to us. 😢 

I'll amend the comment - and maybe place a few others in weather enums - so others don't make the same assumption I did.

Thanks, Kreidos~


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 10, 2020 at 16:37:17_

----

I think there was a plan top use them, before they got put into script instead. So its kinda redundant.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 10, 2020 at 16:47:36_

----

short version: CS event injection is only a concern for _parameters_ and not the csid itself. 



----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 10, 2020 at 16:55:36_

----

>  there is no "Nonday".

irl we call it Monday. Monday tries to return us all to non existence by sucking. Vanadiel doesn't know how lucky it is to not have Monday.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 10, 2020 at 16:58:51_

----

if pet ID is arbitrary and none are capped (I thought the early ones were and then at higher IDs we through packet info out the window) we could shift them up by one having fire start at 1 and then they'd align without addition.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 10, 2020 at 17:00:03_

----

..in a future pr because who wants to fix the other pr's depending on the pet ids, right?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 10, 2020 at 17:08:32_

----

thanks for the warning. I have a bunch of replace rows (I was too lazy for update statements, so I copypasted then edited a column value) to mod enmity. I'll need to update my rows.


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
