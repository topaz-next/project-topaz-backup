**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:39:59_
_Originally opened as: project-topaz/topaz - Issue 152_

----

<a href="https://github.com/sisternERA"><img src="https://avatars3.githubusercontent.com/u/7881651?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [sisternERA](https://github.com/sisternERA)**
_Tuesday Jan 24, 2017 at 19:38 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3666_

----

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) *30161227_1


**_Server Version_** (type `revision` in game) e0c8a5d


**_Source Branch_** (master/stable) master


**_Additional Information_** (Steps to reproduce/Expected behavior) 
Any of the race specific gear you can equip it to any char as long as you use equipset macro
example as a taru you can use the galka rse to increase your mp pool to huge levels





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:00_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Jan 24, 2017 at 21:06 GMT_

----

You can also do this by sending the packet directly, which is what various gear management plugins do.

IIRC you can also do this on retail via a cosmetic race-changing plugin to bypass the client-side restriction. Well, that was the case years ago. And doing that would probably get you reported to a GM. The question is, can it still be done on retail? If so, it's technically proper behaviour.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:01_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Jan 24, 2017 at 21:26 GMT_

----

It can, SE hasn't fixed yet. I think we should anyway. Equipset allows more exploits than just race bypass.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:02_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Jan 24, 2017 at 21:45 GMT_

----

Race data is already in the db, isn't it?

On Jan 24, 2017 2:26 PM, "TeoTwawki" <notificationsgithub.com> wrote:

> It can, SE hasn't fixed yet. I think we should anyway. Equipset allows
> more exploits than just race bypass.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 3666Darkstar Issue issuecomment-274943722>,
> or mute the thread
> <github/notifications/unsubscribe-auth/ABGI_1L8U6By7Mt10a-4Q1BeO5xifI_eks5rVmxqgaJpZM4LssYm>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:04_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Jan 24, 2017 at 22:20 GMT_

----

Doesn't look like it. I don't see it in item_armor.sql. 

I suppose this means that gender-locked gear can be equipped by the wrong gender via /equipset as well.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:05_

----

<a href="https://github.com/sisternERA"><img src="https://avatars3.githubusercontent.com/u/7881651?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [sisternERA](https://github.com/sisternERA)**
_Tuesday Jan 24, 2017 at 22:29 GMT_

----

i thought gender was called out but havent found anything that can call out race for equiping items



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:06_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Wednesday Jan 25, 2017 at 00:15 GMT_

----

Different genders of the same race are technically different races - ie. Hume M and Hume F are different races from each other. It would probably be better to handle gender in the same way as races would be done.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:08_

----

<a href="https://github.com/sisternERA"><img src="https://avatars3.githubusercontent.com/u/7881651?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [sisternERA](https://github.com/sisternERA)**
_Wednesday Jan 25, 2017 at 00:37 GMT_

----

i know the belts dont call on what gender the race is



----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Monday Mar 09, 2020 at 21:29:31_

----

Hello. This is a duplicate of https://github.com/project-topaz/topaz/issues/183 but since the most recent one is more duplicated, I'm going to close this one. Thank you.
