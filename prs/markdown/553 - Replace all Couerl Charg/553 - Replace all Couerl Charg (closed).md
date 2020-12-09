**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Thursday Apr 30, 2020 at 06:04:07_
_Originally opened as: project-topaz/topaz - Issue 553_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

3416 is Dragon Kick.  All couerls need 483.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Apr 30, 2020 at 06:16:22_

----

It should be noted somewhere that 3416 is indeed dragon kick, and it needs to be changed in the sql file.  I don't have the capture info to update the parameters for the entire entry.

Also cocosolos theorized that a second charged whisker skill ID may have been shifted by SE, and it had a shorter CD time (i assume for NM use?).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Apr 30, 2020 at 11:40:00_

----

These are all the mob versions of Charged Whisker in the client:
483  (00227+256)	Charged Whisker
2407 (02151+256)	Charged Whisker
3912 (03656+256)	Charged Whisker
(+256 because we offset for formor and other mobs that use player ws)
We may or may not need the other 2 for some mob(s) someday. In a lot of cases we can use scripting to do the special things (like an extra effect or higher dmg) without using a new ID, usually need a new one for animation differences or CD  like you said.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Apr 30, 2020 at 23:25:14_

----

Good to know.  I think in this case it wasn't a difference in cooldown, rather a difference in cast time, which also seems like it's skill ID specific.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday May 01, 2020 at 01:16:20_

----

I knew what you meant I was just trying to use the same term you did for it.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday May 06, 2020 at 13:38:07_

----

so i've fought sekhmet twice now, for 60 mins total with it sitting under 25%, and the mob does not  use any weaponskills at all. while wiki mentions charged whisker can be used, my only guess is it is used during lightningsday or the wiki is just wrong. will continue to test and just submit a new pr for sekhmet and dragon kick changes. 
