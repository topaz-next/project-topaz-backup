**Labels:**



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Friday Apr 03, 2020 at 06:46:49_
_Originally opened as: project-topaz/topaz - Issue 463_

----

`checkItemChestIsEmpty` [only takes an argument of `npc`; after dealing with some not-lua-local vars, it then calls `removeChest` on this first argument](https://github.com/project-topaz/topaz/blob/release/scripts/globals/caskets.lua#L421-L428).

[At which point the chest tries to disappear the player.](https://github.com/project-topaz/topaz/blob/release/scripts/globals/caskets.lua#L338)

To be fair, it does technically succeed in this endeavor. Unfortunately, it disappears the rest of the server in addition to the intended victim.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Apr 03, 2020 at 07:00:40_

----

I've kicked Travis twice now and it's still acting up. AppVeyor checks out, so I am utilizing my almighty write-access to ignore Travis this time.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Apr 03, 2020 at 11:52:11_

----

> Unfortunately, it disappears the rest of the server in addition to the intended victim.

Casket: and for my next trick, ima pull a hat out of this rabbit!

Rabbit: _readies whirls claws_
