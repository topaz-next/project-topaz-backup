**Labels:**

WIP



<a href="https://github.com/helixhamin"><img src="https://avatars1.githubusercontent.com/u/2202779?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [helixhamin](https://github.com/helixhamin)**
_Tuesday Jul 07, 2020 at 02:08:40_
_Originally opened as: project-topaz/topaz - Issue 819_

----

under item ID 20000.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

@TeoTwawki I am doing an early commit, so keeping as WIP. Can you help check my submissions for itemid 16404-16582?
Just want to make sure I am doing this properly before I do the next (lots...).

If I am on the right path,  I will finish up to itemid 20000.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 17:16:56_

----

need 
```sql
ITEM_ADDEFFECT_ELEMENT  = 950, -- Element of the Additional Effect or Spikes, for resist purposes
```
so that the script knows to check against fire resists when this damage is dealt, otherwise your 30 damage set  here will never have any resists


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 17:17:25_

----

same is true for all add effects that deal elemental damage


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 17:20:36_

----

these 3 are missing the other mods for status effects. the weaken and the stun both needs same kind of info you gave poison. I.E. "How potent is the effect of def down? How long does it last?"


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 17:21:53_

----

I'm not fond of us just repeating the same comment, it doesn't aid anyone in knowing what the line does. Thats why i was writing my examples the way I did: it told you exactly what that line did, by itself


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 17:23:31_

----

HP drain is type 4 instead of type 1, and otherwise needs all the same mods an elemental damage effect would get. Element is darkness.

(I know you said to 16582, but I didn't see any that weren't type 1 in the range you specified and wanted to be sure you know how drains will work)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 17:24:20_

----

these 3 lines required no change, this is a pure whitespace difference.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 17:16:56_

----

need 
```sql
ITEM_ADDEFFECT_ELEMENT  = 950, -- Element of the Additional Effect or Spikes, for resist purposes
```
so that the script knows to check against fire resists when this damage is dealt, otherwise your 30 damage set  here will never have any resists


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 17:17:25_

----

same is true for all add effects that deal elemental damage


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 17:20:36_

----

these 3 are missing the other mods for status effects. the weaken and the stun both needs same kind of info you gave poison. I.E. "How potent is the effect of def down? How long does it last?"


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 17:21:53_

----

I'm not fond of us just repeating the same comment, it doesn't aid anyone in knowing what the line does. Thats why i was writing my examples the way I did: it told you exactly what that line did, by itself


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 17:23:31_

----

HP drain is type 4 instead of type 1, and otherwise needs all the same mods an elemental damage effect would get. Element is darkness.

(I know you said to 16582, but I didn't see any that weren't type 1 in the range you specified and wanted to be sure you know how drains will work)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 17:24:20_

----

these 3 lines required no change, this is a pure whitespace difference.
