**Labels:**

reviewed



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Thursday Oct 15, 2020 at 05:06:20_
_Originally opened as: project-topaz/topaz - Issue 1363_

----

I'm sure there are plenty of servers who believe the lottery rates are too high or too low for their liking. This adds 2 flags to adjust the Chance and Cooldown on Lottery NMs.

This allows for some interesting options, such as turning the rates down and setting cooldowns to 0 thus having all NMs be a rare true-lottery. Or of course you could disable all Lottery spawns entirely if you want, I ain't your boss. :shrug: 

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 15, 2020 at 05:11:29_

----

This is similar to what I do on my server, except that I imposed a minimum time before applying the reduction on repop time (didn't want any lotto less than 20 min long while universally cutting it)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Oct 15, 2020 at 05:13:28_

----

> This is similar to what I do on my server, except that I imposed a minimum time before applying the reduction on repop time (didn't want any lotto less than 20 min long while universally cutting it)

I like this idea myself. I was concerned about having too many flags (wanted it short and simple), but if it's something enough people care about I could add a minimum time as another flag.

**edit** - I know some servers are masochists, so I kind of assumed most people would be using it to lower the rates, ha ha.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Oct 15, 2020 at 08:47:07_

----

Since I saw some discussion on Discord.

For future reference, _my_ general opinion (others may vary) is:

Measurement is:
1. How many lines of existing code does the setting effect? Lower is better. _versus_
2. How many in-game events does the setting have an effect on? Higher is better.

Examples:
- Bad: Setting which requires a huge code switch with 20-50+ lines of code. Not a good setting.
- Bad: Setting which [only affects one thing an NPC does that players may not even interact with](https://github.com/project-topaz/topaz/blob/release/scripts/globals/settings.lua#L153). Also not a good setting.
- Good: Setting which modifies only 2 lines of code and has an effect any time a mob is killed. Potentially a good setting.

EXP_RATE, NM_LOTTERY_CHANCE, ENABLE_ROE, are all good settings. They have a huge effect on gameplay, yet are lightweight from a code maintenance perspective.

[AQUAVEIL_COUNTER](https://github.com/project-topaz/topaz/blob/release/scripts/globals/settings.lua#L134) and [BLINK_SHADOWS](https://github.com/project-topaz/topaz/blob/release/scripts/globals/settings.lua#L131) are bad settings. They do only affect one line, but they also [only affect one _event_](https://github.com/project-topaz/topaz/blob/release/scripts/globals/spells/blink.lua#L16) (casting of a single spell).

[USE_ADOULIN_WS_CHANGES](https://github.com/project-topaz/topaz/blob/release/scripts/globals/settings.lua#L82) is right on the cusp. It affects a lot (all weaponskill uses), but it's borderline cumbersome to maintain (if checks [in each WS file](https://github.com/project-topaz/topaz/blob/release/scripts/globals/weaponskills/aeolian_edge.lua#L22-L31), if checks inside [WS calculation functions](https://github.com/project-topaz/topaz/blob/release/scripts/globals/weaponskills.lua#L79-L83)). At some point the logic needs restructuring so that scripts treat SOA changes as _default_ and pre-SOA under a legacy setting. But it's probably for the best we don't breathe on WS too hard until we're ready to redo them from scratch.

Basically, I measure the worth of a setting as the biggest bang for its lines of code.

But I will insist that anything to do with a setting must be capable of being used by the vanilla current client. If you need an old client to be able to make use of a setting, it'd be a hard no from me.
