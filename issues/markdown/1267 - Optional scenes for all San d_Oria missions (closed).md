**Labels:**

reviewed



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 06, 2020 at 23:50:36_
_Originally opened as: project-topaz/topaz - Issue 1267_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

I apologize for the size of this commit but I'm positive it's very well structured  and commented just the right amount to not be a burden to review.

**This commit adds all missing optional dialogues and cut-scenes to the San d'Oria mission line.**
*(Because San d'Oria is epic, and now it's even more!)*
It additionally cleans up a large amount of code and fits it to the style guide.
Some quests were re-arranged for better prioritization: (RDM AF over Savage Blade WS quest e.g.)
Nesting was added for less condition checks where possible and sensible.
A lot of operators have been reduced/optimized and conditions were generally reviewed for effectiveness.
Two of the optional cut-scenes that were already there but in series have been re-written in parallel so that the viewing order doesn't matter (Trion's & Pieuje's doors).

Missions directly affected by this change are
- 5-1 The Ruins of Fei'Yin
- 5-2 The Shadow Lord
- 8-2 Lightbringer
- 9-1 Breaking Barriers
- 9-2 The Heir to the Light
- New: Epilogue

*Some other missions have not been altered in the sense of the script but were also affected by the clean up.*

NPCs affected by this change in Chateau d'Oraguille are Halver, Curilla, Rahal, Aramaviont, Milchupain, Nachou, Perfaumand, _6h0 (Trion), _6h1 (Pieuje), _6h4 (Great Hall) and in Northern San d'Oria _6fc (Papal Chambers).

Given the rather large scope of this commit I tested this very thoroughly during two days.
- [x] **I tested all missions from 1-1 to 9-2 and Epilogue several times with debugging commands and once without.**
- [x] **I tested all the quests that are not missions but are also affected by this commit:**
  - Lure of the wildcat
  - General's Secret
  - Enveloped in Darkness
  - Peace for the Spirit
  - Savage Blade quest
  - A Boy's Dream
  - Under Oath
- [x] **I re-viewed code several times**

If despite all the above, and me being very positive about the correctness of this commit, someone should find a bug, a failing condition or just spelling mistakes I apologize in advance and if called out directly in this commit I'll fix it as soon as possible.



----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Oct 11, 2020 at 00:51:10_

----

d5690fc49ad1e4d3b26be662bab1b28664962cba adds two more very short additional dialogues to the gate guards in front of the Great Hall in Chateau d'Oraguille as mentioned in #1311 
That issue would therefore be closed with this PR.
