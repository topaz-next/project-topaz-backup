**Labels:**



<a href="https://github.com/nsabott"><img src="https://avatars0.githubusercontent.com/u/25453121?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [nsabott](https://github.com/nsabott)**
_Monday Oct 05, 2020 at 19:06:27_
_Originally opened as: project-topaz/topaz - Issue 1257_

----

1: ZilartStatus needs to be '257' not '255', because it started at 2 and 255 was added.
2: You need to re-get the char var when checking to start cutscene upon selecting the last Pedestal because it was added to, so the check looks at the old stored variable instead of the updated one.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Oct 06, 2020 at 06:19:48_

----

Hi! Welcome to the project and congrats on your first PR (so says GitHub)!

If you haven't already, please join us in discord:
https://discord.gg/nbYJfA5

I'll have time to review this properly in a few days, but at a quick glance it looks good 👍 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Oct 14, 2020 at 20:51:33_

----

It looks like the pedestals are already using a standard bitmask that starts at 1 with the Pedestal of Fire. Bitmask of 8 bits = 255.

[I don't see ZilartStatus being set to an initial value after the completion of the BCNM](https://github.com/project-topaz/topaz/blob/release/scripts/zones/Chamber_of_Oracles/bcnms/through_the_quicksand_caves.lua#L34-L36).
