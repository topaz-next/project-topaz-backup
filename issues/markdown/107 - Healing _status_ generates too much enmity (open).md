**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:10_
_Originally opened as: project-topaz/topaz - Issue 107_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Hozu](https://github.com/Hozu)**
_Thursday Mar 17, 2016 at 22:55 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2918_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30160203_0

**_Server Version_** (type `revision` in game) **:**
github/DarkstarProject/darkstar/commit/ff4a4e41d45fb7ed60035ecdb51c3f6028f2a339

**_Source Branch_** (master/stable) **:**
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
github/DarkstarProject/darkstar/blob/master/scripts/globals/effects/healing.luaDarkstar Issue L38

That was added due to an issue where resting next to a mob wasn't causing it to aggro, which was to break supertanking. It should be adding the player to the mob's hate list with 1 CE if they're not already on the list. Right now any mages resting next to a HNM would generate hate based on the HP they would have recovered, even if they're at full hp.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:11_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Saturday Mar 19, 2016 at 07:36 GMT_

----

The /heal command should put the mage on the mob's active hate list and generate ~~60 ve/sec~~ 10 ve/sec if they are within 12 yalms.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:12_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Saturday Mar 19, 2016 at 16:29 GMT_

----

60 VE/second? Where did that come from? Sounds strange because VE decays that fast... wouldn't that make resting with enmity+ gear make you gain VE over time?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:13_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Saturday Mar 19, 2016 at 17:58 GMT_

----

Comes from retail. 

Don't know if it was affected by enmity gear or not but I'd /heal in fire resist set at tiamat to keep capped hate till stoneskin broke. Years later there was a thread where SE came out said it was 60ve/sec for anyone in half of spell-casting range or something. I'm a little fuzzy on the details.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:14_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Saturday Mar 19, 2016 at 19:17 GMT_

----

citation needed




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:16_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Saturday Mar 19, 2016 at 20:21 GMT_

----

I found the enmity post that I was thinking back to talking about the half spellcasting range distance thing.

http://forum.square-enix.com/ffxi/threads/30629-Enmity-System-Explanation-and-Planned-Adjustments?p=402769&viewfull=1Darkstar Issue post402769

Will try to get into retail with a buddy of mine and run some current tests on /heal enmity, as they do not specify in that post.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:31:17_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Sunday Mar 27, 2016 at 00:18 GMT_

----

Control test: friend with 2CE has a mob. I use provoke wearing no enmity gear.
Expected result: mob will turn back to friend after 30 seconds
Actual result: mob turned back to friend after 30 seconds

Resting enmity test: friend with 2CE has mob. I use provoke and immediately heal with no enmity gear.
Expected result: mob will turn back to friend after a longer duration
Actual result: mob turned back to friend after 36 seconds
Conclusion: 36 seconds of healing generates 360 volatile enmity (or roughly 10 per second)

Resting enmity test 2 (testing enmity equips): I use provoke with no enmity gear and then put 17 enmity in gear on.
Expected result: Mob will turn back to friend after 36 sec if enmity gear not relevant, if enmity gear is relevant 37 seconds if it is.
Actual result: mob turned back to friend after 36 seconds, enmity gear appears to not factor.

Question: Does it resting put you on active hate list on retail?
Answer: this is a well documented yes, but currently not functioning correctly last I checked.

Question: Does resting build CE over time?
Answer: Probably not it is possible to /heal all day and you wont take the mob back

Question: How often does it calculate the 10/sec avg VE
Answer: Unknown, but my best guess is once per second. It did not appear to me to be tick based, nor did recovering actual hp or mp or not seem to affect the test.

It would appear my initial recollection of 60ve/sec was flat wrong. The forum provided stating that there is no hate gain until within half of spellcasting distance (my 12' comment) likely still applies.


