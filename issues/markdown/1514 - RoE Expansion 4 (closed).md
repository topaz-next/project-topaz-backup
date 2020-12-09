**Labels:**



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Saturday Nov 14, 2020 at 02:31:30_
_Originally opened as: project-topaz/topaz - Issue 1514_

----

<p>Adds another 60 or so records, but more importantly this new logic should cover a **huge** number of the remaining records. Those contributors who have expressed an interest in adding to the list of available records, now would be a great time as there are easily hundreds which can be implemented. If interested, please message me on the Discord (Kreidos) and let me know what sections you'd like so we can all work together to avoid duplication of effort. :smiley: </p>
<p>To whoever reviews & merges might not be a bad plan to give this a feature branch and canary time, as there is new logic as well as a potential future landrush for new records that could probably benefit from some testing.</p>

New:
- Heal + Buff Ally Records (Combat + Daily Categories now 100%)
- Physical/Magical kill timed records (Timed schedule now 100%)
- Achievements -> Job Levels I Records
- Tutorial -> Level Cap Increase Records
- Tutorial -> Storage Expansion Records
- Early Tutorial -> Bastok Rank records (Mostly as examples)

Core work + Fixes:
- Proper handling for Inventory Full on RoE Completion
- 5 new core RoE Triggers + logic (Levelup, QuestComplete, MissionComplete, BuffAlly + HealAlly)
- Core work for retroactively claimable RoE Records
- Migrate datagrams to use std::variant

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Nov 14, 2020 at 09:47:23_

----

I've removed the references to pepe the frog from this PR. While _obviously_ not meant that way here, that meme has a lot of linkage to very hateful things and I don't want it anywhere near the project.

Targetting a new feature branch, will do proper review tomorrow. (and I'll hold off on making a release until tomorrow so this has a chance to make it in)
