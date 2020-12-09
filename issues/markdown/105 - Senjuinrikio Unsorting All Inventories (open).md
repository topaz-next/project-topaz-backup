**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:32_
_Originally opened as: project-topaz/topaz - Issue 105_

----

<a href="https://github.com/djridgley"><img src="https://avatars2.githubusercontent.com/u/17796020?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [djridgley](https://github.com/djridgley)**
_Saturday Mar 12, 2016 at 20:21 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2902_

----

**_I have:_**
- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated

<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
30160203_0

**_Server Version_** (type `revision` in game) **:**
Shows as Unknown

**_Source Branch_** (master/stable) **:**
Not Sure, Nasomi Server

**_Additional Information_** (Steps to reproduce/Expected behavior) **:**

This is a bit of a weird one. When zoning with the Senjuinrikio Katana equipped in either hand it unsorts your inventory, safe, locker, and everything else. You can zone with it unequipped and there is no issue. I found a couple other NINs with unlcocked Senj with the same issue.

If you open up the inventory quickly after zoning you can see Senj hangs at the top for a second then everything else populates all jumbled. This could be happening on the other Crit Latent weapons but I don't have them to test it. 

It isn't a real serious issue but I wanted to throw it out there just in case it could potentially cause more serious issues I'm unaware of. It is however super annoying. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:33_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Sunday Mar 13, 2016 at 17:35 GMT_

----

edit your issue following the template (the text when you create a new issue)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:35_

----

<a href="https://github.com/djridgley"><img src="https://avatars2.githubusercontent.com/u/17796020?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [djridgley](https://github.com/djridgley)**
_Sunday Mar 13, 2016 at 23:33 GMT_

----

Sorry about that, updated to the best of my ability.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:36_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Mar 16, 2016 at 00:02 GMT_

----

This is likely because the WS points (part of the item extra data) is sent to the client when it shouldn't be anymore




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:37_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Saturday Mar 19, 2016 at 22:19 GMT_

----

WS points aren't sent to the client? I thought there was a plugin (latent checker) that would get the WS points on weapons like that. Does it not work on retail anymore?




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:38_

----

<a href="https://github.com/djridgley"><img src="https://avatars2.githubusercontent.com/u/17796020?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [djridgley](https://github.com/djridgley)**
_Saturday Mar 19, 2016 at 22:27 GMT_

----

Hopefully it's an easy fix for you guys. My friend told me he zoned with Senj equipped on accident a few mins ago. I told him he done got Senj'd.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:40_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Saturday Mar 19, 2016 at 22:29 GMT_

----

IIRC they used to be, and now they aren't

On Sat, Mar 19, 2016 at 4:27 PM, Arximiro notificationsgithub.com wrote:

> Hopefully it's an easy fix for you guys. My friend told me he zoned with
> Senj equipped on accident a few mins ago. I told him he done got Senj'd.
> 
> —
> You are receiving this because you commented.
> Reply to this email directly or view it on GitHub
> github/DarkstarProject/darkstar - Issue 2902Darkstar Issue issuecomment-198800172




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:41_

----

<a href="https://github.com/djridgley"><img src="https://avatars2.githubusercontent.com/u/17796020?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [djridgley](https://github.com/djridgley)**
_Saturday Apr 02, 2016 at 03:59 GMT_

----

Is this an easy fix or is it one of those things that can't be fixed without breaking it? I ask as I again forget to take off my Katana while zoning and proceed to bang my head on the desk.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:42_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Saturday Apr 02, 2016 at 04:00 GMT_

----

don't you just.. auto sort your inventory again after?

On Fri, Apr 1, 2016 at 9:59 PM, Arximiro notificationsgithub.com wrote:

> Is this an easy fix or is it one of those things that can't be fixed
> without breaking it? I ask as I again forget to take off my Katana while
> zoning and proceed to bang my head on the desk.
> 
> —
> You are receiving this because you commented.
> Reply to this email directly or view it on GitHub
> github/DarkstarProject/darkstar - Issue 2902Darkstar Issue issuecomment-204640803




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:44_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Saturday Apr 02, 2016 at 04:00 GMT_

----

the priority isn't very high because I assume it's not a very important bug

On Fri, Apr 1, 2016 at 9:59 PM, Tyler Schneider teschneigmail.com wrote:

> don't you just.. auto sort your inventory again after?
> 
> On Fri, Apr 1, 2016 at 9:59 PM, Arximiro notificationsgithub.com wrote:
> 
> > Is this an easy fix or is it one of those things that can't be fixed
> > without breaking it? I ask as I again forget to take off my Katana while
> > zoning and proceed to bang my head on the desk.
> > 
> > —
> > You are receiving this because you commented.
> > Reply to this email directly or view it on GitHub
> > github/DarkstarProject/darkstar - Issue 2902Darkstar Issue issuecomment-204640803




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:45_

----

<a href="https://github.com/djridgley"><img src="https://avatars2.githubusercontent.com/u/17796020?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [djridgley](https://github.com/djridgley)**
_Saturday Apr 02, 2016 at 04:01 GMT_

----

It's all inventories, safe, storage, bags, locker, etc. It's just super annoying to have to resort 7 inventories and hard to remember to take the damn thing off. ><




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:46_

----

<a href="https://github.com/Mizzguy"><img src="https://avatars1.githubusercontent.com/u/14020567?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Mizzguy](https://github.com/Mizzguy)**
_Tuesday Apr 12, 2016 at 14:56 GMT_

----

I've seen this issue on my server, with different weapons. Once they unequipped the weapon and zoned. The inventory didn't resort.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:47_

----

<a href="https://github.com/djridgley"><img src="https://avatars2.githubusercontent.com/u/17796020?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [djridgley](https://github.com/djridgley)**
_Tuesday Apr 12, 2016 at 17:11 GMT_

----

Is it just the latent crit weapons doing it or other weapons without unlockable latents? I haven't seen it with other weapons yet except Senj. but I don't have a test server to check the other crit weapons. 

On an unrelated note does anyone know if Senj crit is coded to work in both hands like a Fudo or just its own hits like retail? It's hard to test if its crit applies to wses when in offhand. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:48_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Apr 12, 2016 at 17:36 GMT_

----

Both. github/DarkstarProject/darkstar - Issue 2661




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:50_

----

<a href="https://github.com/Mizzguy"><img src="https://avatars1.githubusercontent.com/u/14020567?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Mizzguy](https://github.com/Mizzguy)**
_Tuesday Apr 12, 2016 at 17:46 GMT_

----

The player said, he had burtgang, aegis (with shield mastery aug., on it) and lamia bow +1. If that helps a bit more.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:51_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Apr 12, 2016 at 18:34 GMT_

----

If I were to guess, it'd be the item with the augment. Have him try to narrow down the item(s) if possible.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:52_

----

<a href="https://github.com/Mizzguy"><img src="https://avatars1.githubusercontent.com/u/14020567?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Mizzguy](https://github.com/Mizzguy)**
_Tuesday Apr 12, 2016 at 22:51 GMT_

----

Looks like augment items, two dif. Players 1 with aug. Shield, other with aug. Whitch hat. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:53_

----

<a href="https://github.com/djridgley"><img src="https://avatars2.githubusercontent.com/u/17796020?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [djridgley](https://github.com/djridgley)**
_Sunday May 01, 2016 at 02:51 GMT_

----

Any luck figuring out a way to fix this? Once fixed I can let Nasomi know so he can do a code pull. Thanks for all you guys do. Hope to take the time to learn Lua soon so I can contribute more than just reports.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:55_

----

<a href="https://github.com/personaone"><img src="https://avatars0.githubusercontent.com/u/8123295?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [personaone](https://github.com/personaone)**
_Monday Jan 28, 2019 at 19:05 GMT_

----

I can confirm that this one is still active, i couldn't figure out what was going on so this issue explains it



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:56_

----

<a href="https://github.com/personaone"><img src="https://avatars0.githubusercontent.com/u/8123295?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [personaone](https://github.com/personaone)**
_Friday Feb 01, 2019 at 18:34 GMT_

----

> I can confirm that this one is still active, i couldn't figure out what was going on so this issue explains it

Actually the same happens with the Heart Snatcher - another one of the latent Crit weapons



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:57_

----

<a href="https://github.com/zynjec"><img src="https://avatars3.githubusercontent.com/u/17911103?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zynjec](https://github.com/zynjec)**
_Friday Feb 01, 2019 at 18:41 GMT_

----

Does anyone have like, literally step by step repro on this? I've tried multiple times for months now, and never triggered this.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:58_

----

<a href="https://github.com/personaone"><img src="https://avatars0.githubusercontent.com/u/8123295?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [personaone](https://github.com/personaone)**
_Friday Feb 01, 2019 at 18:54 GMT_

----

> Does anyone have like, literally step by step repro on this? I've tried multiple times for months now, and never triggered this.

What works for me always is: I just equip an unlocked Senj or Heart snatcher to sub slot, sort inventory, then just zone to the next area, it will be unsorted



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:30:59_

----

<a href="https://github.com/zynjec"><img src="https://avatars3.githubusercontent.com/u/17911103?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zynjec](https://github.com/zynjec)**
_Friday Feb 01, 2019 at 19:04 GMT_

----

Okay, your update included a very important piece of information which changed repro from never to always.

It only happens when the weapon is completely unlocked and equipped.

