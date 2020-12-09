**Labels:**

merge ready



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 07:32:45_
_Originally opened as: project-topaz/topaz - Issue 410_

----

Fixes https://github.com/project-topaz/topaz/issues/187

To apply this change, either run the `sql/item_basic.sql` file, or
just manually execute the following:

```
UPDATE item_basic SET BaseSell = 1319 WHERE name = "spool_of_wyrdstrand"
LIMIT 1
```

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 07:36:17_

----

I can put the command into a migration script if we felt that was necessary, but might be overkill for this since it's a non-destructive and non-structual change and can be updated by simply running the existing script again.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Mar 20, 2020 at 22:22:17_

----

I ended up holding this at the last meeting to make sure the sale price is based on a fame-less value and we're not accidentally introducing fame into this price. Will merge if the price given in the issue is the right one.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Mar 25, 2020 at 13:52:28_

----

I just checked by selling to mog garden (which should be fameless), and the value i have is 1360


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 25, 2020 at 14:49:38_

----

> I just checked by selling to mog garden (which should be fameless), and the value i have is 1360

wondering how/where the value of 1319 was captured now, or if mog garden is using an adoulin fame system rendering it non-neutral


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Mar 25, 2020 at 15:13:01_

----

ok, i made a new character and sent them wyrdstrand. value is 1319. mog garden is NOT fameless.
now to go back and recheck all these item_basic things ive done haha.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Mar 25, 2020 at 15:23:17_

----

_cries in mog garden with his lack of seekers knowledge_

NOOOOOOOOOOoooooooooooooooo a new fame area to add :sob: 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 25, 2020 at 16:51:55_

----

> ok, i made a new character and sent them wyrdstrand. value is 1319

Works for me!
