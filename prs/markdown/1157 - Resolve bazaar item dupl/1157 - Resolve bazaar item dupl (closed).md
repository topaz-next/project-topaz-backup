**Labels:**

exploit



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Friday Sep 18, 2020 at 17:42:20_
_Originally opened as: project-topaz/topaz - Issue 1157_

----

Thanks to @InoUno for pointing this out.

Explanation at a later date~!

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday Sep 18, 2020 at 18:06:23_

----

Already distributed this to the community, going straight in and will end up in canary tomorrow. Thanks! 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Oct 09, 2020 at 08:01:24_

----

**Bazaar Exploit Dupe:**
Basically, a check if a player can afford all quantity of a bazaar item - and then returning if they can't - was accidentally inserted on lines _after_ creating the item and giving it to the buyer. Purchase packet injection from there (to get around the client-side "you don't have enough gil" check).

But here's the video anyway, which is really just an excuse to show off a [FFXI remix album that I like](http://landofvanadiel.com/lov/):
https://www.youtube.com/watch?v=Tpc3sdQH4s0
