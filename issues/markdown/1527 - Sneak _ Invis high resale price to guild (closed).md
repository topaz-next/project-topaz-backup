**Labels:**



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Nov 24, 2020 at 02:00:02_
_Originally opened as: project-topaz/topaz - Issue 1527_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

This was reported on Canaria by RedQueen, you can abuse buying the items from curio vendor moogle and resale them to guildshop for profit.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Nov 24, 2020 at 02:47:51_

----

Please confirm this issue exists yourself.

We require exact items and sale process.

As currently reported, this should not be possible.

<https://github.com/project-topaz/topaz/blob/release/src/map/items/item_shop.cpp#L89-L98>
```sql
INSERT INTO `item_basic` VALUES (4164,0,'pinch_of_prism_powder','prism_powder',12,1540,33,0,350);
INSERT INTO `item_basic` VALUES (4165,0,'pot_of_silent_oil','silent_oil',12,1540,33,0,300);
```


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Nov 24, 2020 at 10:43:46_

----

I'm giving someone an opportunity to convince me to _not_ just set sell prices to 0 across the board. These guild shops are incredibly broken, I'm sick of hearing about them, and I'm not planning to spend further time on them.

<https://github.com/project-topaz/topaz/blob/release/src/map/utils/guildutils.cpp#L110>

<https://github.com/project-topaz/topaz/blob/release/sql/guild_shops.sql#L569-L570>
