**Labels:**

merge ready



<a href="https://github.com/hooksta4"><img src="https://avatars0.githubusercontent.com/u/13935086?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [hooksta4](https://github.com/hooksta4)**
_Wednesday Apr 01, 2020 at 22:03:13_
_Originally opened as: project-topaz/topaz - Issue 459_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Wednesday Apr 01, 2020 at 23:38:54_

----

Please don't keep deleting and recreating your fork and PRs.  You only need to fork once, ever, and you only need to create one PR from your branch.  This is your current open PR, so it shouldn't be deleted until it's finished.  Everything that gets messy is fixable without deleting; just have patience and ask for help when needed.  Otherwise you end up leaving a bunch of garbage in the project's commit or PR history.

If you have time this evening, ping me on Discord and I'll help you neaten this PR up.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Apr 14, 2020 at 13:00:48_

----

Notes from the latest commit

### General changes:

* Some style stuff (tabs -> spaces, fix indendation, add newline at bottom of files)
* Some missing includes
* Some post-quest-stage NPC dialog

### Shadows of the Departed:

* Quest now requires player to have finished Awakening
* Fixed default message on Memory Fluxes
* Fixed Memory Fluxes in Promyvion-Mea to match retail captures
* Added post-event message to "trade in three slivers" event

### Apocalypse Nigh:

* Rename Transcendental Radiance script
* Reordered Kam'lanaut and Eald'narch pools and lists
* Reassigned skill and spell lists
* Removed ancient magic from Eald'narch's spell list
* Set levels and immunities.
* Eald'narch now teleports
* Kam'lanaut now uses en-element weapon skills
* Apoc Nigh now progresses and warps characters who are on the correct stage of quest
* Midnight wait happens on Gilgamesh's door, rather than on Gilgamesh.
* Fixed options and parameters on "get earring" events
* Memory Reset NPC now sets progress so that it matches retail capture

### What's left to do:

* Kam'lanaut and Eald'narch are facing the wrong way when players enter arena.
* Kam'lanaut "Can perform three TP attacks upon reaching 100%+ TP, giving very little rest for healers. He can do 3 Great Wheels in a row, devastating any melee jobs in range."
* Kam'lanaut has trait "When using enspell TP moves, nukes of the matching element heal him."
* Eald'narch is "Highly evasive. Sushi and/or Madrigal recommended."
* Eald'narch has "Very high magic defense (e.g., Thunder IV ~65 dmg)."

Once these points are addressed, I think we can toggle the battlefield on in bcnm.lua.

Otherwise, I believe the rest of the questline is working/retail accurate and could merge into Topaz.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 14, 2020 at 15:20:31_

----

Thanks for the assist, Wren! 👍 

(I'm embarrassed I spaced checking and handling Zilart progress)

Pushed a small commit with my final nitpicks:
- Commented Ealdnarche 2's moves since the file diff from your rename brought them up. Saw he had the skills "ark_guardian_tarutaru" (936) and "tarutaru_warp_ii" (962). Went out on a limb and assumed it was someone trying to handle warping by copying TT and removed the skills now that there's Warp In and Warp Out.
- On that note, Ealdnarche's skill list was the only one using those two skills, so they are now orphaned.
- Cleared the var after the midnight wait between Shadows of the Departed and Apocalypse Nigh
- Overly pick spell list order correction
