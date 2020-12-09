**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:54_
_Originally opened as: project-topaz/topaz - Issue 189_

----

<a href="https://github.com/ababyduck"><img src="https://avatars3.githubusercontent.com/u/9102794?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [ababyduck](https://github.com/ababyduck)**
_Sunday Sep 24, 2017 at 06:46 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4094_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated



<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30161227_1 


**_Server Version_** (type `!revision` in game) **:** 21ce4ef05b5cf78ca97a6d778b4d392fe5334189 _(Note: this commit link will take you to my testing fork, but all that's been modified there at this point are some NPC scripts and TextIDs.)_


**_Source Branch_** (master/stable) **:** master


**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
1) Equip a weapon (tested with Sapara of Trials, 17654)
2) Place a different weapon in Mog Wardrobe (tested with Kodachi of Trials, 17773), make sure no other items of that type are in player's (non-storage) inventory.
3) Call !delitem on the equipped weapon
-- Weapon is deleted.
4) Move the other weapon from wardrobe into your inventory
-- Other weapon is equipped, even if player does not meet the requirements for it.
**Attempting to attack at this point causes the map server to crash with the following error:** 
> ([Fatal Error] --- gdb backtrace ---)

- Was able to equip a katana that requires 71 NIN, as a 75 WAR. 
- Works with armor too, but player does not benefit from armor stats.
- Items are unequipped on changing zones.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:56_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Sunday Sep 24, 2017 at 16:05 GMT_

----

That's uh... interesting. When I wrote the command I merely saw that an equipped item was visually removed (ie. no longer showing as equipped in the slot), so I never bothered to try anything else. At the time the only other use of the delItem binding was for COR Quick Draw deleting cards, so I wasn't quite sure how this would work out.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:57_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Sunday Sep 24, 2017 at 16:32 GMT_

----

If the only way to trigger this is with a gm command, then it's not really
a big problem

On Sep 24, 2017 10:05 AM, "Hozu" <notificationsgithub.com> wrote:

That's uh... interesting. When I wrote the command I merely saw that an
equipped item was visually removed (ie. no longer showing as equipped in
the slot), so I never bothered to try anything else. At the time the only
other use of the delItem binding was for COR Quick Draw deleting cards, so
I wasn't quite sure how this would work out.

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub
<github/DarkstarProject/darkstar - Issue 4094Darkstar Issue issuecomment-331719697>,
or mute the thread
<github/notifications/unsubscribe-auth/ABGI_xyJr26rZPTBKSSjsJQIqTRX26p1ks5sln3egaJpZM4Phy5I>
.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:45:58_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Sep 24, 2017 at 18:12 GMT_

----

we could prolly just force unequip the item in the command script just before deleting it though without any hassle..leave it to the minions to pr.

