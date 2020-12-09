**Labels:**

approved

reviewed



<a href="https://github.com/Nireya"><img src="https://avatars2.githubusercontent.com/u/17558211?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Nireya](https://github.com/Nireya)**
_Thursday Sep 10, 2020 at 07:09:55_
_Originally opened as: project-topaz/topaz - Issue 1092_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

List of changes:
Empress Hairpin lowered from 16% to 15% (Common tier).

Hunter's Longbow and Light Soleas are now pooled correctly.
http://www.ffxidb.com/zones/145/juu-duzu-the-whirlwind

Archer's Knife and Assassin's Bow are now pooled correctly.
https://ffxiclopedia.fandom.com/wiki/Hawkeyed_Dnatbat
http://www.ffxidb.com/zones/149/hawkeyed-dnatbat

Plantsbane and Power Crossbow are now pooled correctly.
https://ffxiclopedia.fandom.com/wiki/Bi%27Gho_Headtaker 
http://www.ffxidb.com/zones/147/bigho-headtaker

Fix Barbarians Sword and Demonic sword from having a chance of dropping neither.
https://ffxiclopedia.fandom.com/wiki/Moo_Ouzi_the_Swiftblade

Added Sentinels Mantle to Steelbiter Gudrud (missing drop)  and pooled it with the Lizard piercer.
https://ffxiclopedia.fandom.com/wiki/Steelbiter_Gudrud

Raised Peacock Amulet from 23% to 24% (Very common tier).

Velocious Belt lowered from 6% to 5% (Rare tier).

Trotter Boots raised from 10% to 15% (Common tier), could potentially advocate for 24% (Very Common tier based off TH0 statistics on ffxidb).
http://www.ffxidb.com/zones/110/simurgh

Dryad Staff increased from 10% to 24% (Common tier).
Damascus Ingot on Roc lowered from 6% to 5% (Rare tier).

Octave Club lowered from 8% to 5% (Rare tier).

Ridill changed from 18% to 1% drop rate (Very rare tier)...I think perhaps someone meant to have this at 1.8%? Unsure if it should be 5% or 1%, so I put it at 1% for now. Here are sources which advocated
for ~3-6%, I assume they always had TH3-TH4 though so I believe 1% seems more accurate.
https://ffxiclopedia.fandom.com/wiki/Fafnir
https://www.bluegartr.com/threads/42316-Fafnir-Nidhogg-Statistics
http://www.ffxidb.com/zones/154/fafnir

Goblin Enchanter's ingot drop rates adjusted. These plague servers badly because ingot drop rates are set so absurdly high... platinum/gold ingots at 8% when the drop rates shown on ffxidb are 0% (did they even exist) or 0.5% (Super rare tier).
http://www.ffxidb.com/search?q=goblin+enchanter

Will look at fixing more drop rates in the future but these are all "high priority" items on 75-cap servers that I was able to quickly check and fix.




----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Sep 10, 2020 at 23:35:00_

----

I'd argue that archer's knife drop should be closer to 8% rather than 10% according to ffxidb.  Other one at 92% is safe.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Sep 10, 2020 at 23:39:19_

----

Good catch on this not adding to 1000, however the drop rate seems extremely wrong according to ffxidb:
http://ffxidb.com/zones/151/moo-ouzi-the-swiftblade

Should be closer to 920 and 80.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Sep 10, 2020 at 23:35:00_

----

I'd argue that archer's knife drop should be closer to 8% rather than 10% according to ffxidb.  Other one at 92% is safe.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Sep 10, 2020 at 23:39:19_

----

Good catch on this not adding to 1000, however the drop rate seems extremely wrong according to ffxidb:
http://ffxidb.com/zones/151/moo-ouzi-the-swiftblade

Should be closer to 920 and 80.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 10, 2020 at 08:36:24_

----

(Don't worry about the CI style check, it's been freaking out on SQL checks for some reason...)


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Sep 10, 2020 at 23:17:56_

----

It's not a requirement for putting items in this database, but I think most of us have begun tagging what each of these items is (and often what's dropping it) as we add or fix them so that it's quick for reviewers to look at and people scanning the .sql to understand.  Up to you if you want to go back and add comments for them.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Sep 10, 2020 at 23:43:16_

----

skew is a factor no matter what source we go by. for tiers 0/1/2 on ffxidb we can check which columns come close to rate buckets and corroborate each other making our best guess. So if the TH0 column implies common but the TH2 column implies rare, I know one or both columns had some skew going on. Either imperfect sample sizes or other factors. (not sure what happens when in a party with a TH source - does the data collector FFXIDB uses know your party member had TH?)

tl;dr don't expect it to ever be perfect without a leak that we aren't supposed to look at for legal reasons,
