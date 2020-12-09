**Labels:**

feature



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:17_
_Originally opened as: project-topaz/topaz - Issue 260_

----

<a href="https://github.com/EpicTaru"><img src="https://avatars3.githubusercontent.com/u/26195580?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [EpicTaru](https://github.com/EpicTaru)**
_Wednesday Feb 06, 2019 at 18:18 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5714_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [X] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [X] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
30181222_1

**_Source Branch_** (master/stable) **:** 
Master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Armor item Karura Hachigane (ItemID is 16154) is missing mods to reduce perpetuation cost for avatar Garuda, as well as to give Attack/Defense bonuses to that specific avatar.  Item was included in June 2008 retail update and drops from ZNM Vulpangue on retail as well as on DSP (DropID is 4035).

Are these mods not added to this item due to there not being support yet in DSP for an item to have mods for only if a specific avatar is summoned?

Please advise and thanks in advance for any insight that is lent regarding this!

Sources for info on item:
https://www.bg-wiki.com/bg/Karura_Hachigane
https://www.bg-wiki.com/bg/June_2008_Version_Update_Changes



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:19_

----

<a href="https://github.com/whasf"><img src="https://avatars3.githubusercontent.com/u/6373706?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [whasf](https://github.com/whasf)**
_Wednesday Feb 06, 2019 at 18:32 GMT_

----

Probably just never added, i'm pretty sure -perpetuation is implemented for other avatars (like carbuncle)



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:20_

----

<a href="https://github.com/zynjec"><img src="https://avatars3.githubusercontent.com/u/17911103?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zynjec](https://github.com/zynjec)**
_Wednesday Feb 06, 2019 at 18:35 GMT_

----

Carbuncle Mitts have a very poorly written hack to work, there is no proper system setup for avatar-specific mods.

github/DarkstarProject/darkstar/blob/361ab1f03bcb008af3dc91bb34ae755df96afc94/src/map/status_effect_container.cppDarkstar Issue L1484-L1487



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:21_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Feb 06, 2019 at 18:41 GMT_

----

Carbuncle Mitts have a hack because it halves perpetuation instead of a flat decrease.  There is a latent effect for a specific PETID, which should work fine for this



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:22_

----

<a href="https://github.com/EpicTaru"><img src="https://avatars3.githubusercontent.com/u/26195580?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [EpicTaru](https://github.com/EpicTaru)**
_Wednesday Feb 06, 2019 at 20:30 GMT_

----

OK, so I found this in item_latents.sql:
<code>INSERT INTO `item_latents` VALUES(16154, 346, 2, 9, 13);</code>
which satisfies the Garuda perpetuation cost reduction, but not finding the other mods that this item does.  I'll do a PR to get those added.

Thanks y'all for your help!



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:24_

----

<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Wednesday Feb 06, 2019 at 20:57 GMT_

----

Look in item_pet_mods?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:24_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Feb 06, 2019 at 21:00 GMT_

----

For the ATK/DEF, I don't think we have a way to add them to a specific petid. item_latents can only add mods to the player when using a specific pet, and item_pet_mods can only add mods to the pet when using a specific pet *type*.

item_pet_mods probably should have just been a latent effect and latent effects updated to be able to apply to pets



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:26_

----

<a href="https://github.com/EpicTaru"><img src="https://avatars3.githubusercontent.com/u/26195580?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [EpicTaru](https://github.com/EpicTaru)**
_Wednesday Feb 06, 2019 at 21:38 GMT_

----

Ok, all that is good to know! I'm standing down for the time being then, lol. 

