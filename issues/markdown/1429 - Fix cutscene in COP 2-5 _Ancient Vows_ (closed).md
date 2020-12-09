**Labels:**

reviewed



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Oct 25, 2020 at 03:01:31_
_Originally opened as: project-topaz/topaz - Issue 1429_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

_ Fixes a wrong cutscene ( #1420  ) after entering through the Dilapidated Gate in Misareaux Coast (F-7) and clicking the Spacial Displacement
_ This affected mission 4-2 (csid 8) so I added one optional dialogue and a new default dialogue there while at it
_ Minor style guide clean up for the Dilapidated Gate (4383c20098a31dcbfd507bd758f228c0568b1c97)

Captures used for this PR:
[Missions: COP 2-4 (An Eternal Melody) ~ COP 2-5 (Ancient Vows)](https://www.youtube.com/watch?v=xHDoAEIQ7_Y&feature=youtu.be)
[Chains of Promathia: COP 4-1 (Sheltering Doubt)](https://www.youtube.com/watch?v=TyOlnk3c_Po&feature=youtu.be)
[Chains of Promathia: COP 4-2 (The Savage)](https://www.youtube.com/watch?v=jIVHFjG1kS0&feature=youtu.be)



----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Friday Nov 06, 2020 at 14:35:56_

----

Please check Despechiaire again, I cleaned that one up too, structured it a little to make it legible and added comments.
The "Sheltering Doubt" optional dialogue needed a missionStatus condition or else it would trigger after going to Bastok.
I moved the event references to the bottom; wouldn't want to delete those, somebody put in effort to pick them, but they shouldn't clutter the functions.

(Force Push fixed a missing Unix (LF) line end)
