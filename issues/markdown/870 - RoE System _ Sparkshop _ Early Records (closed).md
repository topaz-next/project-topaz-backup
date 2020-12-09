**Labels:**



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Sunday Jul 19, 2020 at 15:57:28_
_Originally opened as: project-topaz/topaz - Issue 870_

----

From the team that brought you [Magian](https://github.com/project-topaz/topaz/pull/802) and "[That other feature nobody cares about](https://github.com/project-topaz/topaz/pull/645)", we present Records of Eminence. This is a complete base from which the rest of the records may be built. Thanks and credit goes to @Apocarypse for his packet captures, deciphering assistance, supplying the Spark shop and the NPC/Lua helpers. 

### What's in here?
- All UI elements and interactions.
- Taking/Dropping/Progressing/Completing records
- The Spark Shop + Eminence NPC scripts / CS.
- Persistence of all eminence data per player
- C++ / Lua hooks for interacting with the Eminence system
- Early records fully complete-able
- Migrations for existing DBs

### Which records work?
All Topaz-available content from `Tutorial->Basics`, plus one repeatable "Vanquish Multiple Enemies I".
> First Step Forward
Undertake a FoV Training Regime
Heal Without Using Magic
Vanquish One Enemy
Undertake a GoV Training Regime
Vanquish Multiple Enemies I

### What's comes next?
This base is essentially, wholly complete and these records serve as an example of how the system works, as well as an appetizer for players to sink their teeth into. Next steps would be getting the Records implemented. The vast majority of records could be fully realized using only the hooks provided here, but it would be messy. The next course will be to consider a paradigm for how the nearly 1300+ records will be checked. Whether those checks will be in Core or Lua, and what shape such a system would take. Discussion on this would be welcomed in Discord channels, but is technically out of the scope of this PR.

#### Considerations:
- This adds a new column to the `chars` table for eminence data. New sql file + migration python script is provided. The migration **should** be run on all existing databases. 
- The 6 records which are done here should be considered example *teaser* records only. As detailed above, a more comprehensive handling system for records would be the next phase. There are 1300+ records, and there's no expectation that they'd all be handled like the examples here. :)
- All standard records can be taken by a player, even if no logic exists to progress them. In part due to the current lack of a comprehensive check system as well as in the interests of testing. The client controls which records are shown, and there's no way to hide unimplemented records from the server end; please refer to the above list of working records.
<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Jul 19, 2020 at 17:20:59_

----

> Looks ~good~ _freaking awesome_ to me. Only thing sticks out to me is copyright notice

100%. They were copy-pasted without realizing it. Staff will advise regarding their replacement, I'd prefer the new source files go under AGPL if possible but either way that will be changed. :)


----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Sunday Jul 19, 2020 at 17:28:59_

----

other than tabling the rewards as we discussed, this looks awesome


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Jul 19, 2020 at 17:31:06_

----

> other than tabling the rewards as we discussed, this looks awesome

Thanks Xaver! For sure. As we discussed, the 6 records here should be considered as functioning examples only since a proper record-handling system would be phase 2. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jul 19, 2020 at 17:35:34_

----

there are a few things we can optimize here later, but everything is gewd :+1: 


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Tuesday Aug 18, 2020 at 05:33:20_

----

I have chosen to rebase due to conflicts introduced by `release` commits over the last month since I opened the PR. I've also changed the base back to `release` for the time being, since the roe branch is stale; this way diffs and reviews can still be made accurately. 


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Aug 20, 2020 at 03:44:42_

----

@project-topaz/developer @project-topaz/reviewer this one could use some review love post fixes. 
