**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:03_
_Originally opened as: project-topaz/topaz - Issue 236_

----

<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [KnowOne134](https://github.com/KnowOne134)**
_Monday Jul 23, 2018 at 02:08 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5136_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 


**_Source Branch_** (master/stable) **:** 
Master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
using automation in a instance zone can cause crashes. think its to do with status effects on the pet when deactivating and reactivateing.  Mostly happens with use of the whm puppet.
crash dump

https://www.dropbox.com/s/sqd0qed57adhhn8/crash_automation.rar?dl=0




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:05_

----

<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Monday Jul 23, 2018 at 02:10 GMT_

----

also it doesnt seem like the pet entities clear from memory as seen you can see all the pet dead names

![img_20180722_210843](https://user-images.githubusercontent.com/35616771/43053682-9cb27cb4-8df3-11e8-8bf0-60655868c9fc.png)



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:06_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Monday Jul 23, 2018 at 02:27 GMT_

----

Yes, pet memory is definitely not cleared.  Ref: github/DarkstarProject/darkstar - Issue 4549



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:08_

----

<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Monday Jul 23, 2018 at 10:52 GMT_

----

Except in an instance zone you can crash with a status effect active on it. Only seen with a automation so far



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:09_

----

<a href="https://github.com/rebeccaloran"><img src="https://avatars1.githubusercontent.com/u/4107800?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [rebeccaloran](https://github.com/rebeccaloran)**
_Monday Jul 23, 2018 at 19:10 GMT_

----

Do you mean automaton?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:10_

----

<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Monday Jul 23, 2018 at 19:18 GMT_

----

Yea pup pet automatron



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:56:12_

----

<a href="https://github.com/rebeccaloran"><img src="https://avatars1.githubusercontent.com/u/4107800?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [rebeccaloran](https://github.com/rebeccaloran)**
_Monday Jul 23, 2018 at 21:26 GMT_

----

lol a-u-t-o-m-a-t-o-n


On 07/23/2018 12:18 PM, KnowOne134 wrote:
>
> Yea pup pet automatron
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub 
> <github/DarkstarProject/darkstar - Issue 5136Darkstar Issue issuecomment-407170637>, 
> or mute the thread 
> <github/notifications/unsubscribe-auth/AD6uGJjq1xn-OLtjohjUOlDLf-fTYU_xks5uJiF3gaJpZM4VaQqB>.
>



