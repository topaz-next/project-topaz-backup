**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Oct 25, 2020 at 15:06:15_
_Originally opened as: project-topaz/topaz - Issue 1433_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This PR corrects and adds the occurrences where the player receives or loses the Mysterious Amulet of Selh'teus and Prishe throughout Chains of Promathia missions.

1. COP 1-1: The player *receives* Selh'teus' fully charged amulet (was ok)
2. COP 2-1: The taru gang *steals* the amulet (loses it) from the player (was ok)
bg-wiki claims that you get your amulet back on this mission after zoning into Safehold, this is wrong
3. COP 2-4: Prishe inspects the amulet, it violently reacts and she *returns* it (obtains it) to the player (was missing)
From here on Selh'teus' amulet is now weaker than before
4. COP 3-5: Prishe becomes sick and loses her amulet. The player *lends* her (loses it) Selh'teus' amulet (was missing)
5. COP 7-5: Nag'molada violently takes Selh'teus' amulet from Prishe and *steals a random light* from the player (was missing)
6. COP 8-2: Prishe recovers the amulet from Nag'molada and later *hands* it (obtains it) to the player (was missing)
7. COP 8-4: Prishe tells the player to *return* the amulet (loses it) to her (was missing)

Thanks to ibm for his great captures. Watched tons of CoP for this.
All of these were tested working locally.
