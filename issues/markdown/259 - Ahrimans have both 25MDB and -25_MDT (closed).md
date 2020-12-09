**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:15_
_Originally opened as: project-topaz/topaz - Issue 259_

----

<a href="https://github.com/TrueSalmon"><img src="https://avatars1.githubusercontent.com/u/16270541?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TrueSalmon](https://github.com/TrueSalmon)**
_Thursday Jan 31, 2019 at 18:02 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5692_

----

**_Issue_**
I was learning about elemental nuke damage and found that Ahrimans take a lot less damage. Turns out, after a lot of searching, that they have both -25MDT and 25MDB. They should only have one of those according to the wikis. Other mobs like Weapons or Magic pots have one of those, not both.

You can check that here: github/DarkstarProject/darkstar/blob/dee2b4c2925922c1657824e949341c0a256fb154/sql/mob_family_mods.sql
Where you search for **VALUES (4,** and you can see that they possess the 29 (mdb) and 389 (mdt) traits.

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
version 30181222_1

**_Source Branch_** (master/stable) **:** 
master/stable

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Supernova





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:16_

----

<a href="https://github.com/TrueSalmon"><img src="https://avatars1.githubusercontent.com/u/16270541?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TrueSalmon](https://github.com/TrueSalmon)**
_Thursday Jan 31, 2019 at 22:30 GMT_

----

It's the same for Cardians, Corse and some others.

