**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:46:21_
_Originally opened as: project-topaz/topaz - Issue 197_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Wiggo32](https://github.com/Wiggo32)**
_Saturday Nov 18, 2017 at 00:51 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4240_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30170905_5


**_Server Version_** (type `!revision` in game) **:** unknown


**_Source Branch_** (master/stable) **:** master


**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

Just tested out retail BST here are some issues needing addressing for dsp:

1. When pets 'uncharm' they should come completely off the enmity list of the mob which they were attacking. The 'attacked' mob does not retain memory of enmity toward a mob that was once charmed.

2. a BST and his PET cannot both hold claim on their own mob. Only 1 mob can be claimed between the two of them. How I watched this working was: BST attacking a mob while PET attacking a different mob, when the pet hit the mob it turned red and the BST mob turned yellow, when the BST hit, his mob turned red and the PET's mob turned yellow. There was never two mobs red at the same time even for a split second. 

3. PET has its own enmity list and acts off of it according to which mob generates the most enmity. 
 - first scenerio: PET ordered to fight a mob, then ordered to fight a different mob, pet would switch focus between the two mobs depending on who hit the hardest or generated the most enmity basically. and still only 1 mob could be red at a time.
- second scenerio: PET ordered to fight a mob, then was attacked by a link without any other provocation. as linked mob generated enough enmity it caused PET to switch focus from the originally attacked mob to the linked mob. and still only 1 mob could be red at a time.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:46:22_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Nov 18, 2017 at 00:59 GMT_

----

fixing no.2 may require taking care of the issues with claiming extant elsewhere as well. per issue Darkstar Issue 2109 right now one player can have multiple claims, which is also wrong. so anyone tackling this keep that in mind.

