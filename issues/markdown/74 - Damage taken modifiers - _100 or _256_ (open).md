**Labels:**

improvement



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:20:59_
_Originally opened as: project-topaz/topaz - Issue 74_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Hozu](https://github.com/Hozu)**
_Monday Dec 28, 2015 at 20:14 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2537_

----

There was a pull not too long ago that converted everything to /100. Well, almost everything, there are some mob family modifiers that were unchanged, and Shell power was also unchanged (dat max Shellra V being -68% mdt).

The question is, wasn't /256 retail accurate? If so, why was this changed? And where will DSP go from here?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:21:00_

----

<a href="https://github.com/armouredking"><img src="https://avatars1.githubusercontent.com/u/16038428?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [armouredking](https://github.com/armouredking)**
_Thursday Dec 31, 2015 at 21:38 GMT_

----

[Wikia](http://ffxiclopedia.wikia.com/wiki/Calculating_Magic_Damage) used the /256 system for explanations. I've always heard it referred to that way. But even wiki says "appears to" and other vaguery texts so perhaps /100 is correct now or always was correct and the formulaes were wrong?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:21:01_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday Dec 31, 2015 at 23:38 GMT_

----

Well when it comes to mobs taking 1/8th damage, that's 12.5% so /100 in itself isn't entirely accurate... if DSP wants to go that way, /1000 should be sufficient? Depends on how it works out with Shell, particularly the different merit levels of Shellra V.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:21:03_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jan 04, 2016 at 00:10 GMT_

----

A quick google search gets multiple sources that actually did math rather than repeating either wiki's claims of 256, so I'm fairly confident saying retail uses fractions of 256. It all depends just how much precision Darkstar here wants to have on this. 

Both x/100 and x/1000 are less likely to get messed up by new editors (Haste and its 256 fraction is frequently done wrong when new gears are added) if being "perfectly retail" is seen as less important.

Just wanted to toss that out there, I don't really care which thing we do.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:21:05_

----

<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Monday Jan 11, 2016 at 16:51 GMT_

----

I'm confused, did you look at the code? That was my commit.

I did 256f \* literal %(ie, avalon body, 5% so 5) on the item / 256f, this should still work, no?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:21:06_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jan 11, 2016 at 16:59 GMT_

----

m241dan the confusion is over some modifier values being set differently than others, for the same modifier. The question is which one to change to the other.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:21:07_

----

<a href="https://github.com/m241dan"><img src="https://avatars3.githubusercontent.com/u/3581401?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [m241dan](https://github.com/m241dan)**
_Monday Jan 11, 2016 at 17:02 GMT_

----

I took care of all the items and I thought I did spells and abilities? Hmmm...




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:21:08_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jan 11, 2016 at 17:30 GMT_

----

Hozu ok, after chatting on irc with m241dan, the way things should be working is all the modifiers go with 0-100 scale and the core convert them to the correct fraction. Feel like PR'ing any that need corrected still?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:21:10_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Monday Jan 11, 2016 at 18:33 GMT_

----

Uh, there's those mob values and anything that applies Shell status, those are the ones I know of but there may be more. I'm not sure when I'll be able to handle changes since I'm a bit busy at the moment.

Also Protectra V/Shellra V can be casted by certain mobs (though none are currently coded) so right now their power is a bit lower than it should be due to not having merits.


