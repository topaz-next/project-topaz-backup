**Labels:**

bug

crafting



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:28_
_Originally opened as: project-topaz/topaz - Issue 185_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Wiggo32](https://github.com/Wiggo32)**
_Friday Aug 25, 2017 at 00:13 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4016_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**30170728_2


**_Server Version_** (type `!revision` in game) **:**unknown


**_Source Branch_** (master/stable) **:**master


**_Additional Information_** (Steps to reproduce/Expected behavior) **:** Resale price for Bastore Bream is 582-615 gil. http://ffxiclopedia.wikia.com/wiki/Bastore_Bream
But, take it to the guild NPC Babubu who you're fishing right next to and she'll give you 6,264 per fish! Sounds fishy to me.





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:30_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 25, 2017 at 03:38 GMT_

----

Guild pricing depends on their stock level, can often get far more than regular shops. Or far less, if they are overstocked.

I'd need to see some retail data on the min and max guild pricing to know if this was off.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:31_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Friday Aug 25, 2017 at 04:07 GMT_

----

It's off. Your "retail data" will confirm. Trust me. I can catch 2 stacks of Bream in an hour. Then turn around and sell them to the NPC right behind me for 150,336 gil. That sound right to you? 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:32_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 25, 2017 at 04:21 GMT_

----

I don't have retail data for that "will confirm". So I "can't say" and its been so long since I gamed the guild NPCs on retail I don't know "whats sounds right" to me anymore. 😉 

**So someone more familiar than me will hafta do the fixin**, and hopefully make a good case for the "_yes I actually checked this_" part of it, ya know? 


Its easy to modify for server operators until then. There's an impossible to miss SQL table that holds guild pricing. Or can go the drastic route and disable the guild style shops (one line to comment out in npc script) and just add a regular shop containing what you want at fixed prices (see any non guild shop npc script ever).

Personally I'd just crush the max sell in the guild table. Can be done in one query, and players can just NPC stuff at non guilds if they hafta npc and guild price is "too low" after the change.

_Examples_ _:_
```sql
UPDATE guild_shops SET max_price = min_price WHERE max_price > min_price;
```
Would *bottom out* ***all*** the guild prices.
```sql
UPDATE guild_shops SET max_price = min_price*2 WHERE max_price > min_price*2;
```
Would clamp them all to 2 times the minimum.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:34_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Friday Aug 25, 2017 at 05:01 GMT_

----

I checked the "impossible to miss" SQL and in there are values for what the NPC sells the item for. Not what you can sell to the NPC. github/DarkstarProject/darkstar/blob/master/sql/guild_shops.sql am i looking in the wrong place?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:35_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 25, 2017 at 05:06 GMT_

----

You are "looking in the right place" but not understanding "how guild shops work".

Its the same base used for buy and sell. "And then math happens." Say the guild is selling at 300. Then its buying at 100 at the same stock amount. But then a new game day starts and now it has a lot more of that item from people selling it. Now it sells them for 30 and buys them at 10. Numbers pulled from my rear end for example purposes. The guild doesn't have values for a sell and a buy in its table - its has a "guild price". buy/sell and low stock/high stock modify that price.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:36_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Friday Aug 25, 2017 at 05:09 GMT_

----

`            PItem->setBasePrice(PItem->getMinPrice() + ((float)(PItem->getStackSize() - PItem->getQuantity()) / PItem->getStackSize()) * (PItem->getMaxPrice() - PItem->getMinPrice()));
`



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:37_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 25, 2017 at 05:12 GMT_

----

See? Maths.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:39_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Friday Aug 25, 2017 at 05:19 GMT_

----

I see. When I do that though, that means people will be able to buy the Bream for cheaper than normal prices also, Right?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:40_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 25, 2017 at 05:20 GMT_

----

my examples would cause a "cheap goods" situation. Do math unto the min and max as you see fit.

Until it is properly fixed.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:41_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Friday Aug 25, 2017 at 05:26 GMT_

----

Ok, I got it! I didn't realize that the guilds weren't meant to behave like retail. Now that I'm unconfused, I'll play with the prices. Thanks!



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:42_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Aug 25, 2017 at 05:31 GMT_

----

Oh they were "meant to" They just sorta aren't and we don't have everything we need to make it so. Sorry about that. We've had some previous complaints about it but they tended to start off with some nutty arguments, like talking about the AH value instead of the guild NPC. Another reason this is hard to get right is a lot of retail servers are just sorta..dead...So we can't really get the extremes of what retail does anymore, have to wing it. Best we can do is maintenance camp a retail guild to see what it starts off, then buy/sell a bit and see what our stock change did to it in a small time frame.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:44_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Friday Aug 25, 2017 at 05:39 GMT_

----

please use discord for discussing specifics like this

