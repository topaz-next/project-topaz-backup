**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:33_
_Originally opened as: project-topaz/topaz - Issue 150_

----

<a href="https://github.com/Heepster03"><img src="https://avatars1.githubusercontent.com/u/8421725?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Heepster03](https://github.com/Heepster03)**
_Friday Jan 06, 2017 at 02:06 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3628_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30161206_3

**_Server Version_** (type `revision` in game) **:**
[c31bd6b](github/DarkstarProject/darkstar/commit/c31bd6b31708695f77d04eb089fa0a1dfe24ae93)

**_Source Branch_** (master/stable) **:**
Master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
Currently, San d'Oria is 2nd in the conquest and we have the quiver npc, Nokkhi Jinjahl, in Sandy when they shouldn't be. Secondly, this npc after trading 4 stacks of items for quivering, you get a client crash. After logging on, another trading attempt causes another crash, and so forth.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:34_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jan 06, 2017 at 07:10 GMT_

----

Bet it doesn't crash after the requires I just added reach yer server. But the conquest thing where she's only supposed to be in the nation "winning", that I did not touch. *Not it! -runs and hides-*



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:38:36_

----

<a href="https://github.com/metalfiiish"><img src="https://avatars1.githubusercontent.com/u/6957288?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [metalfiiish](https://github.com/metalfiiish)**
_Thursday Dec 14, 2017 at 00:10 GMT_

----

Looks like she should be spawned in Bastok and Sandy but not windurst (my home nation is being discriminated) according to the sql. It looks like the conquest system has a method to update NPC's based off conquest position but only by region, not per city. I might look to implement a similar function for the main cities to update these types of NPC's.

Listing other NPC's we should implement this behavior for: 
Besides Regional Merchants, the 1st place Allegiance will have the following NPCs available in its city: Nokkhi Jinjahl, Ominous Cloud, Valeriano, Mokop-Sankop, Cheh Raihah, Nalta and Dahjal. If there is a draw or a 1st place Alliance, those NPCs won't be available. 

http://ffxiclopedia.wikia.com/wiki/Category:Conquest

It does look like regional Merchants are coded so it would just be toggling status of the above NPC's.

