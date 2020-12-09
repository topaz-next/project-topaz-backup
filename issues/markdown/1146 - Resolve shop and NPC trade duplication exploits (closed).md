**Labels:**

approved

exploit

reviewed



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Thursday Sep 17, 2020 at 03:30:42_
_Originally opened as: project-topaz/topaz - Issue 1146_

----

_Reported_ exploits will be investigated and resolved. Fixes will be shared with the entire community - we're not the type to hoard exploit knowledge/fixes.

Two exploits, two resolutions, two commits. I'll post a summary, exact replication steps, and videos later.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Sep 17, 2020 at 03:31:02_

----

Some people may have gotten an earlier version of the NPC trade fix. You'll _probably_ want this version which is a _touch_ more permissive and lets players use the remaining stack of items after using it in a trade. 😉 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Sep 17, 2020 at 03:34:41_

----

Yeah, I was pretty hasty in getting the earlier version into people's hands, that's on me 😅


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Sep 30, 2020 at 20:21:50_

----

**Shop Duplication exploit:**
When an item is appraised by an NPC vendor to potentially be sold, it's added as the last item to the trade container (I'm guessing this was due to difficulties in how the shop appraise/sell packet flow works). Back when shops were limited to 16 items, this item was added in a hardcoded slot (slot 16, so the 17th item), and there was a hardcoded check to prevent purchases from slots > 15. But when shops were expanded to allow more than 16 items, the check was changed to disallow purchase of items in slots higher than the container's size. This unfortunately no longer prevented the exploiter from injecting a packet to buy the items they've placed in the container (by appraising them), as the size of the container was dynamic. Items purchased in this manner would be "bought from" the shop for 1 gil.

<https://www.youtube.com/watch?v=ZojTUBQKIPw>

I attacked this by adding setExSize and getExSize. When vendor shops are generated from lua, the shop will save its original size to the container. Purchases from slots higher than this size are ignored.

**NPC Trade Replication exploit:**
Unlike player-to-player trade windows, the "trade to NPC" window doesn't send intermediary packets when each item is placed in a trade slot. The only time the client sends any packet regarding a "to NPC" trade is when the entire trade window is sent. This packet contains 8 fields for inventory slot IDs, and 8 fields for the quantity being traded. Previously, the only check was to see if the quantity of the item in that inventory slot was enough for the quantity the player claimed to be trading.

The exploit worked by injecting a packet with the same inventory slot ID across multiple trade slots, producing "shadow clones" of the single item you're replicating. This could be used to make NPCs think you're giving them more than you actually are, so an exploiter could complete quests with less than the required items, or inflate the amount of beastmen seals/currency they're trading in.

<https://www.youtube.com/watch?v=wUL6qHc-rg4>

The original solution (in this PR) was to place a lock on items being traded when the trade packet was being processed (when stepping through the trade slots), and then reject the trade if it detected a locked item was being traded (ie: someone trying to use the same slot twice). This turned out to be too extreme (mainly with how some NPCs gave items _back_ to the player), so it was changed to set and check reserves in #1196 


----
<a href="https://github.com/ghost"><img src="https://avatars3.githubusercontent.com/u/10137?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ghost](https://github.com/ghost)**
_Thursday Oct 01, 2020 at 19:54:38_

----

Why surely you are mistaken. I saw you ask for people to actually report bugs first, which is obviously the same as saying there are no bugs. So you fixing this is imagined because topaz is bug free. I saw it said on the internets so it must be true.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Oct 01, 2020 at 20:05:53_

----

Fuck off, Wuku.


----
<a href="https://github.com/zircon-tpl"><img src="https://avatars0.githubusercontent.com/u/60901633?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zircon-tpl](https://github.com/zircon-tpl)**
_Thursday Oct 01, 2020 at 20:23:54_

----

ibm2431 has said all there is to say on this subject.

The discussion is now closed.
