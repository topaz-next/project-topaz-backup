**Labels:**

bug

focus



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:40_
_Originally opened as: project-topaz/topaz - Issue 158_

----

<a href="https://github.com/Brierre"><img src="https://avatars3.githubusercontent.com/u/20527593?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Brierre](https://github.com/Brierre)**
_Monday Feb 27, 2017 at 19:17 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3751_

----

**_I have:_**

- [X] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [X] checked the commit log to see if my issue has been resolved since my server was last updated

Only blue magic issue I saw was Darkstar Issue 1281 dating back a long way. github/DarkstarProject/darkstar - Issue 1281

I've been having a discussion with some people about blue magic physical spell range.  The close ones (34 in the spell range column) seem to work at a reasonable (similar to melee) distance from small mobs, but when you get into end game, and start to fight large mobs, you spend a lot more time trying to get close enough, and many times wind up "in the mob's butt crack".  

Is there a way to set the spell range from the outer edge of the mob's personal space, rather than its center?  Maybe assigning mobs a radius from center, depending on mob size, and having the spell range start there?  Would it be a project worth the time it would take to do it?





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:41_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Monday Feb 27, 2017 at 19:21 GMT_

----

We already do that

On Feb 27, 2017 12:19 PM, "Brierre" <notificationsgithub.com> wrote:

> *I have:*
>
>    - searched existing issues (http://github.com/darkstarproject/darkstar/
>    issues/ <github/darkstarproject/darkstar - Issue >) to see
>    if the issue I am posting has already been addressed or opened by another
>    contributor
>    - checked the commit log to see if my issue has been resolved since my
>    server was last updated
>
> Only blue magic issue I saw was Darkstar Issue 1281
> <github/DarkstarProject/darkstar - Issue 1281> dating back a
> long way. Darkstar Issue 1281 <github/DarkstarProject/darkstar - Issue 1281>
>
> I've been having a discussion with some people about blue magic physical
> spell range. The close ones (34 in the spell range column) seem to work at
> a reasonable (similar to melee) distance from small mobs, but when you get
> into end game, and start to fight large mobs, you spend a lot more time
> trying to get close enough, and many times wind up "in the mob's butt
> crack".
>
> Is there a way to set the spell range from the outer edge of the mob's
> personal space, rather than its center? Maybe assigning mobs a radius from
> center, depending on mob size, and having the spell range start there?
> Would it be a project worth the time it would take to do it?
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 3751>, or mute the
> thread
> <github/notifications/unsubscribe-auth/ABGI_6EXAcdR3yq_Vn1O2LKZBhURwW1Iks5rgyE2gaJpZM4MNgmC>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:42_

----

<a href="https://github.com/Brierre"><img src="https://avatars3.githubusercontent.com/u/20527593?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Brierre](https://github.com/Brierre)**
_Monday Feb 27, 2017 at 19:23 GMT_

----

Hrmm...It feels like the 3.4 is from center on big things like Cerberus, etc. 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:43_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Feb 27, 2017 at 19:28 GMT_

----

If collision with the mobs model is making being close enough an issue, fix the mobs size to the correct value because its wrong. Its that simple.  _**Disclaimer**: preceding statement assumed "we already do that" was correct._

github/DarkstarProject/darkstar/blob/master/sql/mob_family_system.sqlDarkstar Issue L30  
(this one ffects range/distance)

and github/DarkstarProject/darkstar/blob/master/sql/mob_pools.sqlDarkstar Issue L44  
(only the first 3 of 32 bits, so flags 0x01, 0x02, and 0x04.. this one effects its physical size appearance in your client, and a ton of things 100% unrelated as well)





----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:44_

----

<a href="https://github.com/Brierre"><img src="https://avatars3.githubusercontent.com/u/20527593?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Brierre](https://github.com/Brierre)**
_Monday Feb 27, 2017 at 19:30 GMT_

----

Thanks!  I'll take a good look at those.  Should I just close this issue then?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:45_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Monday Feb 27, 2017 at 20:41 GMT_

----

We do have radius for monsters, but I don't know for sure if spells are
taking them into account

On Feb 27, 2017 12:30 PM, "Brierre" <notificationsgithub.com> wrote:

> Thanks! I'll take a good look at those. Should I just close this issue
> then?
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 3751Darkstar Issue issuecomment-282825983>,
> or mute the thread
> <github/notifications/unsubscribe-auth/ABGI_4GpMiLkzpAkATw6_rWvZTcl4E3Rks5rgyRpgaJpZM4MNgmC>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:46_

----

<a href="https://github.com/Brierre"><img src="https://avatars3.githubusercontent.com/u/20527593?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Brierre](https://github.com/Brierre)**
_Monday Feb 27, 2017 at 20:53 GMT_

----

The complaints seem to be saying that the physical spells require you to be closer than melee attacks.  Perhaps not.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:48_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Tuesday Feb 28, 2017 at 01:47 GMT_

----

Spells do not take monster size into account on DSP. Or at least, blue magic ones do not, but I'm going to make the assumption that they all don't. For Khimaira you have to get almost inside of the model to cast melee range spells.

There may be other things that aren't taking monster size into account like offensive JAs (bashes). I think WSs are fine though.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:49_

----

<a href="https://github.com/xipies"><img src="https://avatars3.githubusercontent.com/u/7948457?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [xipies](https://github.com/xipies)**
_Tuesday Mar 07, 2017 at 16:07 GMT_

----

Bashes definitely have this problem. For example, using Shield Bash on Behemoth. I have to "unlock" and move "inside" the mob's model to get in range.


