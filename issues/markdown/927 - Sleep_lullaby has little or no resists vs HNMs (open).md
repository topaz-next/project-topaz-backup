**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Thursday Aug 06, 2020 at 07:19:09_
_Originally opened as: project-topaz/topaz - Issue 927_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Reported from multiple players on Gold Saucer: "sleep/lullaby are -READILY- landing on NMs it shouldnt be (Behemoth, Ancient Goobbue, Serket... and presumably many more)"

Further testimony: "Lullaby needs to be tested further on HNMs for accuracy.  [A] level ~67? bard was 100% landing lullabies on Behemoth."


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 06, 2020 at 11:28:10_

----

Likely a symptom of the existing problem of the resists system being wonky - things tend to land at the extreme ranges, if you something doesn't have enough resistance to resists pretty much always, then it will resists pretty much never. Instead of falling into the discreet tiers retail would. Retail also has multiple types of resistance checked _separately_ (status res, element res, status by trait) where the current system jams them all into one combined magic evasion value.

We're also missing tons of immunities on mobs, which you can tell apart from resists on retail because they will use a different message when the effect fails to land.
