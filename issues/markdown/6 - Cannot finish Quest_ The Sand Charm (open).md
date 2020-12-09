**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:03_
_Originally opened as: project-topaz/topaz - Issue 6_

----

<a href="https://github.com/Fiocitrine"><img src="https://avatars1.githubusercontent.com/u/7704601?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Fiocitrine](https://github.com/Fiocitrine)**
_Monday Jan 05, 2015 at 09:47 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 753_

----

I cannot finish quest because NPC Celestina (github/DarkstarProject/darkstar/blob/master/scripts/zones/Mhaura/npcs/Celestina.lua) needs rare/ex item Sand Charm (ID 13095) that drops from Crossbones (ID 17707020), which do not spawn on the Mhaura/Selbina Ferry.  So the issue is, I need those mobs to spawn on the boat.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:04_

----

<a href="https://github.com/gedads"><img src="https://avatars1.githubusercontent.com/u/5845173?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [gedads](https://github.com/gedads)**
_Monday Jan 05, 2015 at 17:12 GMT_

----

yes... there's 2 area (actually 4) mhaura - selbina 2 normal 2 with pirates attack.
Pirate attacks isn't working so... no pirates no drop no quest




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:06_

----

<a href="https://github.com/Fiocitrine"><img src="https://avatars1.githubusercontent.com/u/7704601?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Fiocitrine](https://github.com/Fiocitrine)**
_Monday Jan 05, 2015 at 19:59 GMT_

----

I checked the sql and found both the mob and the item in database. Is there a way to just make the mob spawn on the boat? Or, does the event need to work for the mob to spawn?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:07_

----

<a href="https://github.com/gedads"><img src="https://avatars1.githubusercontent.com/u/5845173?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [gedads](https://github.com/gedads)**
_Tuesday Jan 06, 2015 at 10:03 GMT_

----

DSP's goal is to mimick retail, making the pirates just spawn is more like a custom feature.
retail choose the zone you're sent in (pirates or not pirates) then the pirate ship comes, 3 npcs come out from behind crates and start summoning mobs -> the pirates and eventually, they'll summon the nm. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:08_

----

<a href="https://github.com/Fiocitrine"><img src="https://avatars1.githubusercontent.com/u/7704601?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Fiocitrine](https://github.com/Fiocitrine)**
_Tuesday Jan 06, 2015 at 13:56 GMT_

----

I understand that DSP's goal is to mimick retail. I'm not looking for short ways around. But, scripting the pirate fight is way beyond my scope and knowledge. I figured something is better than nothing, until it's fully scripted.

Cheers




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:09_

----

<a href="https://github.com/Scavenge"><img src="https://avatars2.githubusercontent.com/u/9778206?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Scavenge](https://github.com/Scavenge)**
_Friday Jan 09, 2015 at 01:27 GMT_

----

Musashi on our server was playing with the pirate attacks on his own time and was able to get almost the entire process to work, except for the mages that stand on the opposite boat and summon the skeletons.  he said it's all in there already he just had to trigger them, and i think the mages could be done by using npcs that have hidden names and untargetable.  but priorities may not lie in pirate attacks at the moment.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:10_

----

<a href="https://github.com/Fiocitrine"><img src="https://avatars1.githubusercontent.com/u/7704601?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Fiocitrine](https://github.com/Fiocitrine)**
_Friday Jan 09, 2015 at 18:08 GMT_

----

I just wanted it to be able to finish this quest and move onto the next quest, which seems fully scripted (weird).




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:11_

----

<a href="https://github.com/JoeCT"><img src="https://avatars1.githubusercontent.com/u/10385544?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [JoeCT](https://github.com/JoeCT)**
_Wednesday Jan 28, 2015 at 00:51 GMT_

----

Scavenge - Any chance of my getting hands on the scripts you have for the pirate attack?  I'd like to take a look at them.




----
<a href="https://github.com/jarmengaud"><img src="https://avatars3.githubusercontent.com/u/52013132?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jarmengaud](https://github.com/jarmengaud)**
_Tuesday Aug 25, 2020 at 19:07:19_

----

Actually this is no longer the case: you can get on the pirate ship and kill skeletons and get sand charm.
(thanks to whoever made the workaround!)
