**Labels:**

reviewed



<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Omnione](https://github.com/Omnione)**
_Sunday Apr 19, 2020 at 16:53:46_
_Originally opened as: project-topaz/topaz - Issue 507_

----

CE and VE values to reflect retail values

I updated all that i could to known retail values, any that are unknown or need work are noted.

_Still not known values and notes_:

- **Overdrive**:  CE ??? VE ???.

- **Repair**: CE and VE needs to be added to the lua as updateFromCure for the recovery potency.

- **Retrieve**: CE ??? VE ???, probly 0.

- **Deep Breathing**: CE ??? VE ???, probly 0.

- **Role Reversal**: CE ??? VE ???, not sure on this one as it swaps HP and MP but probly dont add CE or VE.

- **Healing Waltz**: CE and VE values should be probly be set in lua per effect removed, left as is for now.

- **Double Shot**: CE and VE should be calculated from dmg delt, reduced this to CE 1 and VE 80.

- **hagakure**: lowered the VE on this as its unkown but as it does not directly affect the mob it feels like it should be 80 rather than 300.

- **Bully**:  VE was too low for an ability against a mob, raised to 300.

- **Maintenance**: CE and VE values should be probly be set in lua per effect removed, left as is for now.

- **Lunge**: CE and VE values need to be calculated based on dmg delt in lua.

- **Vivacious Pulse**: CE and VE needs to be added to the lua as updateFromCure for the recovery potency.

<!-- place 'x' mark between square [X] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday Apr 19, 2020 at 17:08:31_

----

These are a from BG and various other sources and cross checked as much as possible.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday Apr 19, 2020 at 17:13:51_

----

Not really much around for the CE and VE values, although 99% of these are from BG, i found a few disscutions on FFXIAH and google to help cross reference these as much as i could.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Apr 19, 2020 at 17:39:55_

----

whats CE and VE? (sorry for my ignorance)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 19, 2020 at 18:42:15_

----

> whats CE and VE? (sorry for my ignorance)

[Cumulative Enmity and Volatile Enmity](https://www.bg-wiki.com/index.php?curid=11855)

 - Cumulative Enmity (CE): Diminishes as a player takes damage or is the target of certain offensive actions  
 - Volatile Enmity (VE): Diminishes as time passes.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Apr 23, 2020 at 21:38:37_

----

I'm okay with the increases pending more retail testing. Absent concrete reason to believe the abilities are 0 enmity (ie: a source saying so definitively, not just having blank fields), bringing the self-target abilities from 0 up to the same values as abilities like Convert, Penury, Footwork, Spontaneity, etc doesn't sound too crazy. We can always adjust them _higher_ if there are later sources saying as such.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Apr 24, 2020 at 02:31:34_

----

Nyu and I created a merge conflict for this earlier today. So I did the rebase and force-push to your branch so I can merge! Hope you don't mind~!
