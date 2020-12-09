**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:10_
_Originally opened as: project-topaz/topaz - Issue 160_

----

<a href="https://github.com/nyczducky"><img src="https://avatars3.githubusercontent.com/u/20367923?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [nyczducky](https://github.com/nyczducky)**
_Tuesday Feb 28, 2017 at 14:52 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3757_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) 30170204_1


**_Server Version_** (type `revision` in game) 8b8a839


**_Source Branch_** (master/stable) master


**_Additional Information_** (Steps to reproduce/Expected behavior) 

http://ffxiclopedia.wikia.com/wiki/Beast_Affinity

Beast Affinity should increase the level cap of the monster past the level cap set by server.

Getting reports that it is not working properly.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:12_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Feb 28, 2017 at 16:47 GMT_

----

github/DarkstarProject/darkstar/blob/ca49d6169089d40dee318e8007c1a40790161180/src/map/utils/petutils.cppDarkstar Issue L1321

Looks fine to me... gets max level for the jug pet, adds the merits to that max, then caps it at the level of the master. Then applies the level randomization of - 0-2 levels (less Monster Gloves effect).



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:13_

----

<a href="https://github.com/nyczducky"><img src="https://avatars3.githubusercontent.com/u/20367923?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nyczducky](https://github.com/nyczducky)**
_Tuesday Feb 28, 2017 at 17:49 GMT_

----

Its not supposed to cap it at the master. It can exceed the master's cap.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:14_

----

<a href="https://github.com/nyczducky"><img src="https://avatars3.githubusercontent.com/u/20367923?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nyczducky](https://github.com/nyczducky)**
_Tuesday Feb 28, 2017 at 17:50 GMT_

----

Increases the level cap of pets summoned with Call Beast. For example: Courier Carrie had a cap of level 75, and with 5 merits into Beast Affinity the cap will be raised to lvl 85.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:15_

----

<a href="https://github.com/nyczducky"><img src="https://avatars3.githubusercontent.com/u/20367923?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nyczducky](https://github.com/nyczducky)**
_Tuesday Feb 28, 2017 at 17:51 GMT_

----

Would it be as simple as deleting github/DarkstarProject/darkstar/blob/ca49d6169089d40dee318e8007c1a40790161180/src/map/utils/petutils.cppDarkstar Issue L1323-L1327





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:16_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Feb 28, 2017 at 17:53 GMT_

----

Unless that was changed sometime after introduction of the merit category (ie. a changelog for the change exists) this should remain. Otherwise you'll run into the issue of the BST being unable to call a jug pet because it would kill EXP gain by having a pet of 10 levels above the rest of the party. Among other things.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:17_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Feb 28, 2017 at 17:56 GMT_

----

https://www.bg-wiki.com/bg/Beast_Affinity

"A pet's level cannot exceed the calling Beastmaster's level or main hand weapon item level (whichever is highest), but it can exceed the pet's normal cap. "



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:19_

----

<a href="https://github.com/nyczducky"><img src="https://avatars3.githubusercontent.com/u/20367923?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nyczducky](https://github.com/nyczducky)**
_Tuesday Feb 28, 2017 at 18:01 GMT_

----

Under that: This means a Jug Pet that caps at level 90 may reach 105 with 5/5 merits and Monster +2/Ankusa gloves and a main hand weapon that is ilvl 105+.

http://ffxi.allakhazam.com/forum.html?forum=262&mid=1298635397162868956&h=50&p=9Darkstar Issue 426



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:20_

----

<a href="https://github.com/nyczducky"><img src="https://avatars3.githubusercontent.com/u/20367923?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nyczducky](https://github.com/nyczducky)**
_Tuesday Feb 28, 2017 at 18:02 GMT_

----

Wouldn't that then have to say "may reach 99 with 5/5 merits."



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:21_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Feb 28, 2017 at 18:04 GMT_

----

It looks right to me.  We can't get a jug pet past 99 because there is no support for item level weapons yet.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:41:22_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Wednesday Mar 01, 2017 at 02:52 GMT_

----

Under that: This means a Jug Pet that caps at level 90 may reach 105 with 5/5 merits and Monster +2/Ankusa gloves and a main hand weapon that is ilvl 105+.

That's saying the pet will be level 105 with the listed gear and a ilvl 105 or higher weapon, because of the ilvl deeming you as level 105 for the calculation. If you're level 99 it will be capped at 99 despite having a total of +15 levels to the pet.



----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Mar 25, 2020 at 04:36:35_

----

related to #322 and solved by #415 
