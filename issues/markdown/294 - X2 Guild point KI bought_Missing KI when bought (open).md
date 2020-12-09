**Labels:**

bug

crafting



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:34_
_Originally opened as: project-topaz/topaz - Issue 294_

----

<a href="https://github.com/AppleCrumble1"><img src="https://avatars3.githubusercontent.com/u/45308457?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [AppleCrumble1](https://github.com/AppleCrumble1)**
_Friday May 17, 2019 at 11:45 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6012_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_**   31090328_2 


**_Source Branch_** (master/stable) **:**  master


<!-- Demiurge Server. -->

**_Additional Information_** 

I had 20k Guild points for smithing guild, I wanted to buy Chainwork and Sheeting KI's both 10k guild points each. I bought Sheeting KI and spenk 10k guild points and then Chainwork vanished from the KI list but Sheeting remained, Thought maybe it was a text id bug so tried to buy the second Sheeting hoping it would give Chainwork. It took the remaining 10k guild points and gave me Sheeting again. Checked my perm KI list and only showed sheeting once. Was rectified by GM to give Chainwork in game 





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:35_

----

<a href="https://github.com/AppleCrumble1"><img src="https://avatars3.githubusercontent.com/u/45308457?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [AppleCrumble1](https://github.com/AppleCrumble1)**
_Friday May 17, 2019 at 11:49 GMT_

----

We run Master Source Branch so Teo just informed me.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:36_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday May 19, 2019 at 08:08 GMT_

----

Saving people some time:
github/DarkstarProject/darkstar/blob/dbaaa7710698a4e41e3175b6f3e80fc59e671d98/scripts/globals/keyitems.luaDarkstar Issue L1982-L1983
(These IDs checked out when I used `!addkeyitem 1994` and `!addkeyitem 1995`)

github/DarkstarProject/darkstar/blob/dbaaa7710698a4e41e3175b6f3e80fc59e671d98/scripts/zones/Metalworks/npcs/Lorena.luaDarkstar Issue L22-L31

github/DarkstarProject/darkstar/blob/dbaaa7710698a4e41e3175b6f3e80fc59e671d98/scripts/zones/Northern_San_dOria/npcs/Macuillie.luaDarkstar Issue L22-L31

Suspect the issue might be in here (maybe mismatched bit-shifting), but I don't know how this menu is supposed to work:
github/DarkstarProject/darkstar/blob/dbaaa7710698a4e41e3175b6f3e80fc59e671d98/scripts/globals/crafting.luaDarkstar Issue L243-L253
While fixing this, should probably also add a safety check that the player doesn't already possess the KI before trying to give it to them.

