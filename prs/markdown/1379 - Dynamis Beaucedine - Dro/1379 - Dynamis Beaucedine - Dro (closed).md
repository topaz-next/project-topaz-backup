**Labels:**



<a href="https://github.com/EpicTaru"><img src="https://avatars3.githubusercontent.com/u/26195580?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [EpicTaru](https://github.com/EpicTaru)**
_Friday Oct 16, 2020 at 19:12:26_
_Originally opened as: project-topaz/topaz - Issue 1379_

----

-- mob_droplist.sql: Added Attestation NM pop items to Hydra NMs with normalized drop rate of 10%

- Despot's Fortune Parchment - Item ID 3359, drops from Hydra Warrior, Hydra Paladin, Hydra Red Mage (DropID 1343)
- Sadist's Fortune Parchment - Item ID 3360, drops from Hydra Bard*, Hydra White Mage, Hydra Black Mage (DropID 1344)
- Villain's Fortune Parchment - Item ID 3361, drops from Hydra Monk, Hydra Ninja, Hydra Thief (DropID 1345)
- Deluder's Fortune Parchment - Item ID 3362, drops from Hydra Ranger, Hyra Samurai, Hydra Dark Knight (DropID 3145)
- Traitor's Fortune Parchment - Item ID 3363, drops from Hydra Beastmaster, Hydra Dragoon, Hydra Summoner (DropID 3146)

-- mob_groups.sql: Added/moved DropIDs to allow for above Hydra NMs to drop relevant Attestation NM pop item
- Hydra Bard was moved from existing DropID 1343 to 1344 (1344 also pre-existing but correct group for the drop of the pop item)
- Hydra Ranger, Hyra Samurai, Hydra Dark Knight were moved from pre-existing DropID 1343 to new DropID 3145 to NEW DropID 3145
- Hydra Beastmaster, Hydra Dragoon, Hydra Summoner were moved from pre-existing DropID 1343 to NEW DropID 3146

-- Added other items that also should drop from mobs in the two above new Drop IDs (copied from drop lists for the other Drop IDs)
-- Added commenting to denote which mobs were in each Drop ID as well as the Item Names for the items that already existed
-- Removed an unnecessary space in Item Description for Drop ID 3144 (it was bugging me!!!!!!)

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Friday Oct 16, 2020 at 19:35:44_

----

It's nice to see Dynamis moving! :-)


----
<a href="https://github.com/EpicTaru"><img src="https://avatars3.githubusercontent.com/u/26195580?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [EpicTaru](https://github.com/EpicTaru)**
_Saturday Oct 17, 2020 at 13:52:40_

----

https://github.com/project-topaz/topaz/issues/311
