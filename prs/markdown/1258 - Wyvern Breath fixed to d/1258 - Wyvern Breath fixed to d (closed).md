**Labels:**



<a href="https://github.com/nsabott"><img src="https://avatars0.githubusercontent.com/u/25453121?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [nsabott](https://github.com/nsabott)**
_Monday Oct 05, 2020 at 19:11:38_
_Originally opened as: project-topaz/topaz - Issue 1258_

----

Wyvern breaths should be coded using the ability name not hard coded with the number, as this causes it to be mismatched if the ability values change

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Monday Oct 05, 2020 at 23:17:33_

----

Haven't tested this code, but have some styling notes.  (See style guide for contributions [here](https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md).)

Set editor to use 4 spaces for indentation, rather than tabs.  Tabs muck up the indentation for reviewers in github.



----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Monday Oct 05, 2020 at 23:19:04_

----

per style guide, table braces on new line, spaces for indentation

```lua
breaths =
{
    tpz.jobAbility.FLAME_BREATH,
    tpz.jobAbility.FROST_BREATH,
    tpz.jobAbility.GUST_BREATH,
    tpz.jobAbility.SAND_BREATH,
    tpz.jobAbility.LIGHTNING_BREATH,
    tpz.jobAbility.HYDRO_BREATH,
}
```


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Monday Oct 05, 2020 at 23:19:21_

----

LF at end of file


----
<a href="https://github.com/NTSabott"><img src="https://avatars3.githubusercontent.com/u/71192266?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NTSabott](https://github.com/NTSabott)**
_Monday Oct 05, 2020 at 23:26:17_

----

Gotcha, okay, I'll use 4 spaces going forward :+1: 


----
<a href="https://github.com/NTSabott"><img src="https://avatars3.githubusercontent.com/u/71192266?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NTSabott](https://github.com/NTSabott)**
_Monday Oct 05, 2020 at 23:26:29_

----

sounds good :+1:  thanks


----
<a href="https://github.com/NTSabott"><img src="https://avatars3.githubusercontent.com/u/71192266?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NTSabott](https://github.com/NTSabott)**
_Monday Oct 05, 2020 at 23:27:09_

----

Not quite sure what this is?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Oct 06, 2020 at 11:21:57_

----

LF = LineFeed. Unix line endings.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Monday Oct 05, 2020 at 23:17:33_

----

Haven't tested this code, but have some styling notes.  (See style guide for contributions [here](https://github.com/project-topaz/topaz/blob/release/CONTRIBUTING.md).)

Set editor to use 4 spaces for indentation, rather than tabs.  Tabs muck up the indentation for reviewers in github.



----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Monday Oct 05, 2020 at 23:19:04_

----

per style guide, table braces on new line, spaces for indentation

```lua
breaths =
{
    tpz.jobAbility.FLAME_BREATH,
    tpz.jobAbility.FROST_BREATH,
    tpz.jobAbility.GUST_BREATH,
    tpz.jobAbility.SAND_BREATH,
    tpz.jobAbility.LIGHTNING_BREATH,
    tpz.jobAbility.HYDRO_BREATH,
}
```


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Monday Oct 05, 2020 at 23:19:21_

----

LF at end of file


----
<a href="https://github.com/NTSabott"><img src="https://avatars3.githubusercontent.com/u/71192266?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NTSabott](https://github.com/NTSabott)**
_Monday Oct 05, 2020 at 23:26:17_

----

Gotcha, okay, I'll use 4 spaces going forward :+1: 


----
<a href="https://github.com/NTSabott"><img src="https://avatars3.githubusercontent.com/u/71192266?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NTSabott](https://github.com/NTSabott)**
_Monday Oct 05, 2020 at 23:26:29_

----

sounds good :+1:  thanks


----
<a href="https://github.com/NTSabott"><img src="https://avatars3.githubusercontent.com/u/71192266?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NTSabott](https://github.com/NTSabott)**
_Monday Oct 05, 2020 at 23:27:09_

----

Not quite sure what this is?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Oct 06, 2020 at 11:21:57_

----

LF = LineFeed. Unix line endings.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Oct 06, 2020 at 06:21:47_

----

Hey! Please co-ordinate with @rude-jerk to make sure you don't trample eachothers work :)
https://github.com/project-topaz/topaz/pull/1263


----
<a href="https://github.com/rude-jerk"><img src="https://avatars0.githubusercontent.com/u/9592857?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [rude-jerk](https://github.com/rude-jerk)**
_Tuesday Oct 06, 2020 at 15:20:09_

----

If someone merges this after the requested changes I'll handle resolving the conflict on my PR. 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 08, 2020 at 04:55:20_

----

Since there is only a little formatting to do, I'm going to merge this and then ninja in the formatting so @rude-jerk can continue with what he's doing. Thanks for the contribution! 👍 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 08, 2020 at 05:02:31_

----

Style changes here:
https://github.com/project-topaz/topaz/commit/9b72cd2192efa1a5b4ffcaac3b7629177a9eda0e


----
<a href="https://github.com/nsabott"><img src="https://avatars0.githubusercontent.com/u/25453121?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [nsabott](https://github.com/nsabott)**
_Thursday Oct 08, 2020 at 09:07:23_

----

Sorry, I've been trying to get back to fixing this up, just got swamped with class work and haven't got the chance to fix up the formatting, my apologies :(.
