**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:04_
_Originally opened as: project-topaz/topaz - Issue 93_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Hozu](https://github.com/Hozu)**
_Monday Feb 22, 2016 at 21:04 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2797_

----

Client Version (type /ver in game) :
30160203_0

Server Version (type revision in game) :
5cfcf10

Source Branch (master/stable) :
master

Additional Information (Steps to reproduce/Expected behavior) :
BP is supposed to go off, and claim the mob. Right now nothing happens, but the cost still occurs. I didn't test with other pet jobs, however.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:05_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Feb 23, 2016 at 01:02 GMT_

----

I can't reproduce this.. walk up to unclaimed mob, predator claws, and it goes off like expected.  What were you using?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:06_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Feb 23, 2016 at 03:22 GMT_

----

I was using Grand Fall against an idle Fafnir.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:07_

----

<a href="https://github.com/ZirkPrime"><img src="https://avatars3.githubusercontent.com/u/17181229?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ZirkPrime](https://github.com/ZirkPrime)**
_Monday Feb 29, 2016 at 07:36 GMT_

----

Was your leviathan too far away from Fafnir for your BP to go off?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:09_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Monday Feb 29, 2016 at 07:56 GMT_

----

I don't remember now, I'd have to re-test this at some point.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:10_

----

<a href="https://github.com/ZirkPrime"><img src="https://avatars3.githubusercontent.com/u/17181229?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ZirkPrime](https://github.com/ZirkPrime)**
_Monday Feb 29, 2016 at 20:59 GMT_

----

I noticed the other day when fighting Steelfleece Baldarich that I was in range for melee attacks, but too far away to use the Steal job ability, so likely melee range being determined by mob perimeter but JA using mob center, creating mismatch for larger mobs. If leviathan only moved into melee range of Fafnir for BP, and BP also checks against mob center, then possible BP was too far away. (I suppose there could not be a distinction between mob perimeter and mob center, but for certain actions the allowable range is scaled by some MOB_SIZE value, scaling would occur for melee attack but not JA/spells, not sure if provisions made to distinguish between "melee" JA like steal and ranged JA like provoke)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:26:11_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Sep 26, 2017 at 04:27 GMT_

----

> I don't remember now, I'd have to re-test this at some point.

*nudges*

When you get the chance to, let us know so we can get this handled/closed



----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Sunday Mar 08, 2020 at 03:58:19_

----

Hello. Unable to reproduce this on master as of 03/07/2020. Feel free to reopen an issue if it still happens on your end. Thank you.
