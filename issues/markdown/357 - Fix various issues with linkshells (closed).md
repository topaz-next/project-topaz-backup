**Labels:**



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Wednesday Feb 19, 2020 at 22:09:36_
_Originally opened as: project-topaz/topaz - Issue 357_

----

This adds several features to make linkshells match retail behavior. The biggest change is using the 9th byte of a linkshell items extra data to hold the linkshell type, rather than using an offset of the item id as is currently done (this appears to be how retail does it). Also added is the ability to change /lsmes privilege level to LS holder only, pearlsack holders, or everyone. These changes should require no input to existing shells for compatibility. Breaking the linkshell group has also been added. This will kick and break the pearls/sacks of all equipped members, then set the linkshell as broken in the database. Any offline or unequipped members will receive a message when they next try equipping which will then break the item. There has been a !breaklinkshell command added for GMs to break any linkshell group. ***This change DOES require that you add a column to the linkshells table.***

* break linkshell and all pearls/sacks by dropping linkshell or with gm command
* pearlsack kick breaks equipped pearl, linkshell kick breaks all pearls/sacks in all inventories
* lsmes privilege (/lsmes level ls, /lsmes level ps, /lsmes level all, /lsmes clear)
* equipable from any local inventory (inventory, satchel, sack, case)

Fixes pretty much everything in #78 except trading pearls.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Saturday Feb 22, 2020 at 17:43:17_

----

tested, all works as long as its equipped in LS slot 1, you can promote demote and kick players that have pearl equipped in slot 2. all other tested worked out
