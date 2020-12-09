**Labels:**

approved

reviewed



<a href="https://github.com/triple-lariat"><img src="https://avatars1.githubusercontent.com/u/30502556?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [triple-lariat](https://github.com/triple-lariat)**
_Saturday Aug 29, 2020 at 18:14:18_
_Originally opened as: project-topaz/topaz - Issue 1035_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

All implemented behavior for Provoker is based on the capture and noted behavior by Jimmayus: https://youtu.be/0fSKlDz5bWU
There didn't seem to be any apparent way to add a dummy ability for its elemental affinity change aside from using the existing "vulture_1" mob skill, so I put those changes in as well.

For the most part, Provoker's behavior matches the elemental affinity change of Kam'lanaut, so its script is largely adapted from Kam'lanaut's.

Furthermore, though Provoker has Enspells currently in Topaz, the capture indicates that Provoker's enspell effect comes from its current elemental affinity. 

Lastly, the double attack and accuracy boost are based on observations that Provoker had a fairly high accuracy against a 75 RDM and double attacked fairly often. 



----
<a href="https://github.com/triple-lariat"><img src="https://avatars1.githubusercontent.com/u/30502556?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [triple-lariat](https://github.com/triple-lariat)**
_Wednesday Sep 02, 2020 at 17:15:20_

----

It absolutely slipped my mind! Thanks for letting me know!



----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 03, 2020 at 18:39:01_

----

Merging this into it's own feature branch means that it'll get merged into `canary` in the next update (in a few days maybe). It'll then get battle tested for _some length of time_ and then snuck into `release`. Congrats on your first PR!
