**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 13, 2020 at 23:00:02_
_Originally opened as: project-topaz/topaz - Issue 1354_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This PR would successfully activate Ro'Maeve's bridges, gates and the fountain not only at exactly 6pm but at any hour that hits full moon between 6pm and (not including) 6am for the remaining amount of time until 6am. The current logic in release only once can activate the whole area at exactly 6pm not thereafter. This is not desirable.
~~It also adds the missing weather condition. The area must have no weather for the full moon to affect the mentioned objects.~~
Furthermore when cleaning up at 6am only the two Moongates should become targetable again.

This was a bummer to debug and test cause the !time command apparently throws off the sync between the in-game shown /clock and the server clock, but nonetheless:
- [x] Tested working locally at several hours, moon phases and weather conditions.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 13, 2020 at 23:26:16_

----

~~Please don't merge yet, I think I have a typo.~~


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Oct 13, 2020 at 23:31:00_

----

We used to have the weather requirement coded, but removed it; I thought this was because specific weather was no longer required in retail.
https://github.com/DarkstarProject/darkstar/issues/3957


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 13, 2020 at 23:49:19_

----

~~Took out the weather check (makes me sad) and removed `math.abs()` from one of the calculations cause not necessary. The subtraction will reliably always be negative, so just multiply by negative.~~ Outdated, see below.

Maybe I can raise awareness for https://github.com/project-topaz/topaz/issues/480 which is related to the content of this PR but not affected by it.
