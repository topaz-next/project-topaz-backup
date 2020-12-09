**Labels:**

good first issue



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Monday Oct 26, 2020 at 03:03:47_
_Originally opened as: project-topaz/topaz - Issue 1435_

----

https://github.com/project-topaz/topaz/blob/b0de87cf6a892f7625aef5af1bede1d078f5a2de/scripts/zones/Windurst_Woods/npcs/Wetata.lua#L31

they seem to lack an else statement with a CS as it's only checking if the quest is available but not when it's completed or accepted.

This applies also to clarion star and the other dood in sandoria (never memorized their names cuz com on wind pipes)


----
<a href="https://github.com/RAIST5150"><img src="https://avatars0.githubusercontent.com/u/73744368?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [RAIST5150](https://github.com/RAIST5150)**
_Saturday Oct 31, 2020 at 13:17:10_

----

To better clarify, this may be isolated to players that completed first trusts for nations before the key items issue was addressed.  No key item (colored card or permit) exists but they have gotten the first trust so the quest is not flagged as available.
