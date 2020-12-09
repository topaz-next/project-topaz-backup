**Labels:**

approved



<a href="https://github.com/rude-jerk"><img src="https://avatars0.githubusercontent.com/u/9592857?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [rude-jerk](https://github.com/rude-jerk)**
_Thursday Aug 06, 2020 at 01:41:57_
_Originally opened as: project-topaz/topaz - Issue 925_

----

…skill damage calculation

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

* Moved aftermath application above weaponskill damage calculation
* Removed 0 damage check for aftermath application 

Aftermath currently (and has always) applies even for aftermath-applying weaponskills that do no damage. Aftermaths are also always taken into effect for the weaponskill that caused them. 
