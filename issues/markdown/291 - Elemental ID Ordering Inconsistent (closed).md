**Labels:**

improvement



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:28_
_Originally opened as: project-topaz/topaz - Issue 291_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Friday May 10, 2019 at 17:22 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6002_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** n/a


**_Source Branch_** (master/stable) **:** master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

I am presenting the can of worms. A lot of us already know this, but I couldn't find it reported as an Issue.

[Days of the week go in an order inconsistent with retail's elemental wheel](github/DarkstarProject/darkstar/blob/master/src/map/vana_time.hDarkstar Issue L36-L46). The fault is on SE here, and our ordering of the days is correct.

However, in many locations [our ordering of elements follows the days of the week instead of retail's wheel.](github/DarkstarProject/darkstar/blob/master/scripts/globals/magic.luaDarkstar Issue L16-L28)

[It causes people to try to use the subEffect table to represent an elemental spirit instead of the magical element, using a family bridge to link family to the subEffect.](github/DarkstarProject/darkstar/blob/c8c9564ae5863d4c489567b8df7d3723086badee/scripts/globals/pets/avatar.luaDarkstar Issue L156-L171) This is because despite how the [spirit pacts spells follow the elemental wheel](github/DarkstarProject/darkstar/blob/5e04622f60dfd196dc1630d603f24d2ec8403383/sql/spell_list.sqlDarkstar Issue L345-L352) (as do [our elements for the spirits](github/DarkstarProject/darkstar/blob/master/sql/mob_family_system.sqlDarkstar Issue L164-L171)) our elemental table in Lua doesn't.

But we can't simply replace the values in the Lua table, because [our element column for spells uses the day of the week values](github/DarkstarProject/darkstar/blob/master/sql/spell_list.sqlDarkstar Issue L202-L231). This also causes our element columns to not increase in a linear order with our spell lists.

This inconsistency makes [our elemental modifiers not go in the same order](github/DarkstarProject/darkstar/blob/3e46a535c9fe3ab405a829d4de117c638c44493a/src/map/modifier.hDarkstar Issue L51-L58) as our elemental listing. (The modifiers go in the correct order, the inconsistency is with our element tables).

It causes [our Damage Types](github/DarkstarProject/darkstar/blob/2924080116c08539ab245f2a8947f1d448237bdf/src/map/entities/battleentity.hDarkstar Issue L255-L262) to not go in the same order as the [Subeffects _just 20 lines below_ the type definition](github/DarkstarProject/darkstar/blob/2924080116c08539ab245f2a8947f1d448237bdf/src/map/entities/battleentity.hDarkstar Issue L286-L296), or the [order of the elements in queries for resistances](github/DarkstarProject/darkstar/blob/09b3ddfe5f24190203a2ceb225c479bcc699d045/src/map/instance_loader.cppDarkstar Issue L105-L111).

For fun, before [seeing the order our Enspells go in, try to guess what it is](github/DarkstarProject/darkstar/blob/2d0add60f09a79bc03a8ffd0ede33d408ec77f3e/src/map/utils/battleutils.hDarkstar Issue L48-L55). Then give [COR shots](github/DarkstarProject/darkstar/blob/2d0add60f09a79bc03a8ffd0ede33d408ec77f3e/src/map/ability.hDarkstar Issue L159-L166) and [PUP Maneuvers](github/DarkstarProject/darkstar/blob/2d0add60f09a79bc03a8ffd0ede33d408ec77f3e/src/map/ability.hDarkstar Issue L175-L182) a guess. How about [Avatar perpetuation reduction](github/DarkstarProject/darkstar/blob/5e04622f60dfd196dc1630d603f24d2ec8403383/src/map/utils/charutils.cppDarkstar Issue L4404-L4414)?

It causes our [internal crystal elements](github/DarkstarProject/darkstar/blob/09b3ddfe5f24190203a2ceb225c479bcc699d045/src/map/utils/synthutils.hDarkstar Issue L39-L49) to be misaligned with the item IDs for those crystals:
```sql
INSERT INTO `item_basic` VALUES (4096,0,'fire_crystal','fire_crystal',12,516,35,0,13);
INSERT INTO `item_basic` VALUES (4097,0,'ice_crystal','ice_crystal',12,516,35,0,30);
INSERT INTO `item_basic` VALUES (4098,0,'wind_crystal','wind_crystal',12,516,35,0,14);
INSERT INTO `item_basic` VALUES (4099,0,'earth_crystal','earth_crystal',12,516,35,0,13);
INSERT INTO `item_basic` VALUES (4100,0,'lightning_crystal','lightng._crystal',12,516,35,0,30);
INSERT INTO `item_basic` VALUES (4101,0,'water_crystal','water_crystal',12,516,35,0,15);
INSERT INTO `item_basic` VALUES (4102,0,'light_crystal','light_crystal',12,516,35,0,80);
INSERT INTO `item_basic` VALUES (4103,0,'dark_crystal','dark_crystal',12,516,35,0,77);
```
Which results in [additional effort in mapping the item ID to the correct element](github/DarkstarProject/darkstar/blob/master/src/map/utils/synthutils.cppDarkstar Issue L722-L764).

It causes you to, upon reading the comment ["We are able to get the correct elemental mod here by adding the element to it since they are in the same order"](github/DarkstarProject/darkstar/blob/master/src/map/utils/synthutils.cppDarkstar Issue L630-L631) to go verify [what that order mods for "reduce fail rate when using ELEMENT crystal" go in](github/DarkstarProject/darkstar/blob/3e46a535c9fe3ab405a829d4de117c638c44493a/scripts/globals/status.luaDarkstar Issue L1490-L1497). It works out in the end, but you had to go confirm to make sure. [What about Moghancements](github/DarkstarProject/darkstar/blob/186cbafb2d091b8f1c37ea1e17f4401604cc246a/src/map/items/item_furnishing.hDarkstar Issue L35-L42)?

I'll spare a treatise about everything relating to, or depending on, weather, and/or days of the week.

I doubt it'd be _too_ controversial to say that the only thing that should follow SE's days of the week order is our definition of days of the week. _Everything else_ should be using the elemental wheel which SE uses for everything besides week days.

Now, if there were a "Hard Fix" tag, this would earn it due to how pervasive these inconsistencies are throughout the project. _I_ certainly have no plans to open the worm can and start digging through it. But if someone feels _particularly_ ambitious, here's something you can look into.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:29_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday May 10, 2019 at 17:29 GMT_

----

Yep this has been brought up before. Nobody has fixed it because nobody wants to be responcible for defending it against people “fixing” the fix when they inevitably get confused from there being multiple different elemental orders.

