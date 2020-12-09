**Labels:**

bug

focus



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:31_
_Originally opened as: project-topaz/topaz - Issue 231_

----

<a href="https://github.com/Dynas13"><img src="https://avatars0.githubusercontent.com/u/36946058?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Dynas13](https://github.com/Dynas13)**
_Wednesday Jul 11, 2018 at 18:02 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5079_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
n/a

**_Source Branch_** (master/stable) **:** 
n/a

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

I've been using BLU a lot lately trying to figure out why certain spells aren't as good as they should be. The reason for this is partly because the code is using outdated info from ffxiclopedia instead of bg-wiki which is more current.

This is the citation in the code for where info is being copied 
 -- This data should match information on http://wiki.ffxiclopedia.org/wiki/Calculating_Blue_Magic_Damage

Instead it should use
https://www.bg-wiki.com/bg/Calculating_Blue_Magic_Damage

Examples of discrepancies:
Eyes on Me should be using a 40% CHR mod instead of 20%
Regurgitation has a 2.46 multiplier when used from behind that is completely absent
Mysterious Light uses a 30% CHR mod instead of 20%

Breath spells should be using Damage= D value + HP percentage instead of normal calculations.
For example Heat Breath is listed as having a 30% MND mod.
However, i'm not sure if what's listed was an attempt at an approximation.





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:33_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 11, 2018 at 18:12 GMT_

----

In addition to the above, many spells (particularly those that cannot be obtained until after lv 76+) are just plain guessed at with copy pasted code and values modified until someone thought the damage "felt right".

BG's data is more current, but even BG may be some and has a note about physical blue dmg calculations so anyone willing to do lots of math with large amounts of retail sampling will be greatly appreciated
> Note: Due to the July 9 2013 and the August 12, 2014 updates, the formula here is lacking in information or adjustments. This is mostly why the page has been flagged as outdated.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:34_

----

<a href="https://github.com/Dynas13"><img src="https://avatars0.githubusercontent.com/u/36946058?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Dynas13](https://github.com/Dynas13)**
_Thursday Jul 12, 2018 at 15:50 GMT_

----

The 2013 update includes this:
The damage of physical blue magic spells will now increase depending on the item equipped in the main weapon slot.
* This change applies to weapons equipped in the main weapon slot for which their item levels are displayed and have an attribute modified by a weapon skill.

The 2014 update added this line
The attack power of physical blue magic spells has been increased.
Job abilities, magic, food, and equipment that affect physical attack are now reflected in the attack power of physical blue magic spells.
* With regard to those effects that raise physical attacks by a percentage, the attack of physical blue magic spells will vary based on the strength of the weapon wielded in the main hand.

My assumption is that Base damage of your main hand weapon influences your physical blue magic spells. And this is easily testable for anyone with a retail copy of the game. Just go out test a spell with a low damage weapon then test it with a high damage weapon and voila. The other tests you could do is compare a single hit spell like say mandibular bite in retail then on private servers to see what the damage difference is since physical spells got their attack power buffed.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:35_

----

<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Thursday Jul 12, 2018 at 16:05 GMT_

----

Thats the way i have always believed it worked also. It you put a earth staff on you would miss alot as its acc. Was also fependent on main hand weapon amd the damage would drop



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:37_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 12, 2018 at 16:05 GMT_

----

That and or attack matters and I don't think thats used in current code



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:38_

----

<a href="https://github.com/Dynas13"><img src="https://avatars0.githubusercontent.com/u/36946058?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Dynas13](https://github.com/Dynas13)**
_Friday Jul 13, 2018 at 14:26 GMT_

----

Attack and hit rate are calculated in the offcratiomod of the code in bluemagic.lua around line 125. Accounts for pdif as well.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:40_

----

<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Friday Jul 13, 2018 at 14:30 GMT_

----

There still needs another ammendment to blu magic for breath spells. 
1. Physical spells
2. Magical spells
3. Breath spells



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:43_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 13, 2018 at 14:30 GMT_

----

> Attack and hit rate are calculated in the offcratiomod of the code in bluemagic.lua around line 125. Accounts for pdif as well.

k. I've been at work and not had time to delve to deeply into anything lately. if we're just missing using the wDmg, thats great means less needs done than I thought.

