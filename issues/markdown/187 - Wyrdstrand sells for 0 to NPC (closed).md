**Labels:**

bug

feature

good first issue



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:50_
_Originally opened as: project-topaz/topaz - Issue 187_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Wiggo32](https://github.com/Wiggo32)**
_Thursday Aug 31, 2017 at 06:38 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4027_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**30170728_2


**_Server Version_** (type `!revision` in game) **:**unknown


**_Source Branch_** (master/stable) **:**master


**_Additional Information_** (Steps to reproduce/Expected behavior) **:** Spool of Wyrdstrand (item 3550) in the 'item_basic' table has '0' set for BaseSell. Here are 2 sites referencing similar NPC sell prices:
http://ffxiclopedia.wikia.com/wiki/Wyrdstrand
http://www.ffxiah.com/item/3550/wyrdstrand

The Wyrdweave is also set to '0' but I cannot find a reference price online.





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:52_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Aug 31, 2017 at 20:32 GMT_

----

> The Wyrdweave is also set to '0' but I cannot find a reference price online.

This is exactly why its zero. Zero is a placeholder for "we don't know yet". Also used when sites disagree and we don't want to guess which one is right.

A great many items have this problem. What is needed is someone to get on retail and check it, taking their fame modification to the price (if any) into account (or just selling someplace not modified by fame).



----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Monday Mar 09, 2020 at 21:25:47_

----

Hello. Both of them have a price documented now. As for the Wyrdstrand, my retail capture shows a price at 1319 gils (sold multiple of them).


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 07:01:33_

----

It's in `item_basic` table:

https://github.com/project-topaz/topaz/blob/master/sql/item_basic.sql

```
itemid, subid, name, sortname, stackSize, flags, aH, NoSale, BaseSell
'3550', '0', 'spool_of_wyrdstrand', 'wyrdstrand', '12', '4', '40', '1', '0'
```


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 07:03:04_

----

The captured `1319` is lower than the range specified in https://ffxiclopedia.fandom.com/wiki/Wyrdstrand

That claims `1,360~1,394 gil`. But I'm tempted to lean toward an actual capture over the data from the wiki, which could be stale.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 11, 2020 at 11:37:55_

----

> The captured `1319` is lower than the range specified in https://ffxiclopedia.fandom.com/wiki/Wyrdstrand
> 
> That claims `1,360~1,394 gil`. But I'm tempted to lean toward an actual capture over the data from the wiki, which could be stale.

‘Clopedia usually has outdated proces tbat ppl did not accurately gauge fame on so they guesstimated - wiki is rarely confirming these once someone adds one 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 11, 2020 at 11:38:55_

----

Selling an item in a non fame effected area on retail is the most accurate info we can get
