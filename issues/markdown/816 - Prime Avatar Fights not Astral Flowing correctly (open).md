**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Jul 07, 2020 at 00:01:24_
_Originally opened as: project-topaz/topaz - Issue 816_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

I have done all lv 65 prime fights and avatars dont seem to be astral flowing, only got astral flowed by garuda once, then the second time she had this weird behavior as if she was using chain spell, where she started casting her claws 3 times in a row followed by Wind IV


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jul 07, 2020 at 03:20:13_

----

The diff versions of the avatars need split up and renamed, its on my todo list - right now they all try and use one script with a conditional check to figure out which battlefield it is. One version of them is meant to astral flow repeatedly and that code can go active after several of the thresholds resulting in multiple astrals back to back.


----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Thursday Jul 09, 2020 at 10:02:32_

----

I think for the normal prime fight, AF should be the next move when avatar goes below 50% (and should not be repeated)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Jul 09, 2020 at 18:36:40_

----

its not always 50% in retail (I have seen them go at 66% ish, and as low as 10% rarely) but yeah, one time for the normal fights. The multiples thing is specifically for an ASA mission version of them, Presently they share a single script and the conditional check to tell which version you are fighting fails.
