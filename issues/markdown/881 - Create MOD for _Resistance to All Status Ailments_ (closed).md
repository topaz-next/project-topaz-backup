**Labels:**

approved



<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [neuromancerxi](https://github.com/neuromancerxi)**
_Thursday Jul 23, 2020 at 22:16:02_
_Originally opened as: project-topaz/topaz - Issue 881_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Creates MOD 958 - STATUSRES for "Resistance to All Status Ailments".
Removes Death Resistance from Items with "All Status Ailments" (see: related BG Thread with justification - https://www.bluegartr.com/threads/108199-Random-Facts-Thread-Other?s=c66ef360f8f47cb9a568306781e9a045&p=6981981&viewfull=1#post6981981 )
Replaces Individual Resist MODS (240-255) on existing "All Status Ailment" Items with a single 958 with relevant value.
Adds math check in magic.lua to combine specific resistance values with the newly created All Status Ailments MOD.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Aug 17, 2020 at 06:33:42_

----

is this the MOD for the ribbon equipment? :smile: 


----
<a href="https://github.com/neuromancerxi"><img src="https://avatars0.githubusercontent.com/u/3996176?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [neuromancerxi](https://github.com/neuromancerxi)**
_Monday Aug 17, 2020 at 11:56:45_

----

> is this the MOD for the ribbon equipment? smile

Yep. Ribbons, Hearty Earring, and others with the "Resistance to All Status Ailments" listed on the item.
