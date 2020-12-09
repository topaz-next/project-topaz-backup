**Labels:**

bug

help wanted

research needed



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 07:10:35_
_Originally opened as: project-topaz/topaz - Issue 409_

----

Here's a list of all of the items that need to be updated:

[item_basic.xlsx](https://github.com/project-topaz/topaz/files/4316556/item_basic.xlsx)

```
select * from item_basic where BaseSell = 0 and NoSale = 0
```

Related issues: https://github.com/project-topaz/topaz/issues/187




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 11, 2020 at 07:13:32_

----

This is definitely going into my drawer for next free period, thanks!

Tagging: @project-topaz/researcher and @Wiggo32 


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 07:14:00_

----

Warning: there's more than 5500 items returned by this query. So it may take some time to update them all.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 07:14:59_

----

FFXIclopedia shows `Resale Price` under its items, however they may not be 100% accurate.

https://ffxiclopedia.fandom.com/


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Wednesday Mar 11, 2020 at 07:17:20_

----

That's definitely one issue I can look into for the next free campaign. I'll check my pricelog (thanks to ibm2431) data to compare for now. Thanks, mrhappyasthma.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Mar 18, 2020 at 04:47:50_

----

Just to check before I start trying to collect - I assume we need this data with 0 fame? and what goes in the nosale column?


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 18, 2020 at 15:33:07_

----

It seems like `NoSale` is set to 1 for `EX` items that cannot be sold.

So I believe we only need prices for items that are sellable (i.e. `NoSale = 0`).

I imagine `BasePrice` should be the 0 fame value. Although looking through the code, it does not look like we take fame into account at all (unless I just couldn't find where that happens). But it's something we could more easily apply to the base price by scaling it up by some factor.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Mar 20, 2020 at 16:17:08_

----

> I imagine BasePrice should be the 0 fame value. 

yes. in retail fame adds a small bit of extra gil to this value in areas where fame applies.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Monday Mar 23, 2020 at 18:10:20_

----

i started updating here - feel free to update:
https://docs.google.com/spreadsheets/d/1fPJAoyxn1JuHXWTLS9ccF_5Coe9cQTniOJRbZwg_9Zc/edit?usp=sharing
added a column for acquisition method, as many of these are inaccessible without gp or on certain times of the year 
for things that are rare/ex, im changing no sale to 1
