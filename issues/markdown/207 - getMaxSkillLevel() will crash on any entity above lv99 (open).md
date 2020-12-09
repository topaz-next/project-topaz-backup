**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:06_
_Originally opened as: project-topaz/topaz - Issue 207_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jan 31, 2018 at 22:09 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 4526_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
n/a

**_Server Version_** (type `!revision` in game) **:** 
273806765b5cbcd82db1fa2e60395fb10abaf001

**_Source Branch_** (master/stable) **:** 
master

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
Make a monster lv 120 or so, have it cast meteor, watch server crash




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:08_

----

<a href="https://github.com/hilts-vaughan"><img src="https://avatars0.githubusercontent.com/u/1079207?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [hilts-vaughan](https://github.com/hilts-vaughan)**
_Monday Feb 19, 2018 at 00:05 GMT_

----

Looks like this is because of an out-of-bounds access on the `battleutils.cpp` (it stops at 99) See: `GetMaxSkill` trying to access the `g_SkillTable` but there are only entries up to 99 on the actual skill table SQL. 

Should we put a guard in place here? And what should we put for these values? Do we have new values to put here?

Also, hi. New person looking to contribute here. :) 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:09_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Feb 19, 2018 at 00:08 GMT_

----

Yes. 

Which is pretty much because we don't really have any post 99 support yet. Which needs to eventually change. In my opinion should be capable of monster levels clear to 255 just in case of any future higher level monsters. I think retail has some above 130 now, I don't know exactly. Oldschool I think highest lv mobs were lv95 wyrms.

Maybe in the meantime we could treat above 99 as if it is exactly 99.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:10_

----

<a href="https://github.com/hilts-vaughan"><img src="https://avatars0.githubusercontent.com/u/1079207?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [hilts-vaughan](https://github.com/hilts-vaughan)**
_Monday Feb 19, 2018 at 00:10 GMT_

----

A quick `grep` through the source code seems to indiciate that you guys already treat above `99` as the max level, since there are some checks elsewhere that do `if level > 99, clamp to 99` so that seems like a reasonable thing to do.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:11_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Feb 19, 2018 at 04:44 GMT_

----

We do that elsewhere. We just didn't do it *here* yet. We should, and then later put some actual care into making non oldschool situations accurate. But that'll probably be long ways into the future. I kept forgetting this existed so I tossed it into the tracker so it wouldn't get lost (_also "maybe someone else will fix it before I get around to it" Pull Requests welcome_).



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:12_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Monday Feb 19, 2018 at 05:17 GMT_

----

I think retail just caps it at 99 as well and then tack on extra stats.
Kind of like item level in Adoulin gear

On Sun, Feb 18, 2018 at 9:44 PM, TeoTwawki <notificationsgithub.com> wrote:

> We do that elsewhere. We just didn't do it *here* yet. We should, and
> then later put some actual care into making non oldschool situations
> accurate. But that'll probably be long ways into the future. I kept
> forgetting this existed so I tossed it into the tracker so it wouldn't get
> lost (*also "maybe someone else will fix it before I get around to it"
> Pull Requests welcome*).
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 4526Darkstar Issue issuecomment-366587692>,
> or mute the thread
> <github/notifications/unsubscribe-auth/ABGI_8eOhICBmuGwCHKwEGRrdr_8LmO5ks5tWPwmgaJpZM4R0uqK>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:51:13_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Feb 19, 2018 at 05:20 GMT_

----

I've seen packets where the level field was populated as "120". That could still be from being an "effective" level though, for exp purposes, I guess we could see wtf happens to level correction'd things on a high enough mob and tha'd give us an idea of what retail does.

