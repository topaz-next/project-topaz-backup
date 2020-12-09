**Labels:**

feature



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:34_
_Originally opened as: project-topaz/topaz - Issue 157_

----

<a href="https://github.com/ghost"><img src="https://avatars3.githubusercontent.com/u/10137?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [ghost](https://github.com/ghost)**
_Thursday Feb 23, 2017 at 05:55 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3744_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:**
version 30161227_1


**_Server Version_** (type `revision` in game) **:**
Unknown


**_Source Branch_** (master/stable) **:**
master


**_Additional Information_** (Steps to reproduce/Expected behavior) **:**
From BGWiki:
 https://www.bg-wiki.com/bg/Call_Wyvern

"While alive the Wyvern gives a variety of effects to the Dragoon.

    20% Attack Bonus
    20% Defense Bonus
    10% Job Ability Haste
...
Attack Bonus and Defense Bonus potency begins at 10% but increases by 2% each time the Wyvern's 'attributes increase' for a maximum of 20%, the Haste effect begins at 0% but likewise increases in increments of 2% until it reaches 10%.
Source: http://forum.square-enix.com/ffxi/threads/43912-dev1229-Job-Adjustments"

I could be really wrong about this, but it seems simple to do like addMod(MOD_ATTP) to player after call wyvern and delete them after dismiss/wyvern's death? Oh.. but the increments...hmm




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:36_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Feb 23, 2017 at 06:06 GMT_

----

It is as you think, fairly simple - the flat bonus would be added on summon
and deleted on dismissal, and the increments would be added when the wyvern
levels up, and then deleted when dismissed (of course, keeping track of the
number of times it levelled up)

On Wed, Feb 22, 2017 at 10:55 PM, soupcans <notificationsgithub.com> wrote:

> *I have:*
>
>    - searched existing issues (http://github.com/darkstarproject/darkstar/
>    issues/ <github/darkstarproject/darkstar - Issue >) to see
>    if the issue I am posting has already been addressed or opened by another
>    contributor
>    - checked the commit log to see if my issue has been resolved since my
>    server was last updated
>
> *Client Version* (type /ver in game) *:*
> version 30161227_1
>
> *Server Version* (type revision in game) *:*
> Unknown
>
> *Source Branch* (master/stable) *:*
> master
>
> *Additional Information* (Steps to reproduce/Expected behavior) *:*
> From BGWiki:
> https://www.bg-wiki.com/bg/Call_Wyvern
>
> "While alive the Wyvern gives a variety of effects to the Dragoon.
>
> 20% Attack Bonus
> 20% Defense Bonus
> 10% Job Ability Haste
>
> ...
> Attack Bonus and Defense Bonus potency begins at 10% but increases by 2%
> each time the Wyvern's 'attributes increase' for a maximum of 20%, the
> Haste effect begins at 0% but likewise increases in increments of 2% until
> it reaches 10%.
> Source: http://forum.square-enix.com/ffxi/threads/43912-dev1229-
> Job-Adjustments"
>
> I could be really wrong about this, but it seems simple to do like
> addMod(MOD_ATTP) to player after call wyvern and delete them after
> dismiss/wyvern's death? Oh.. but the increments...hmm
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 3744>, or mute the
> thread
> <github/notifications/unsubscribe-auth/ABGI_24SvP_8yI82YC5P6wPwPXi3mzAyks5rfR9vgaJpZM4MJk2Y>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:37_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Thursday Feb 23, 2017 at 16:25 GMT_

----

I believe those buffs are being applied to the wyvern itself, currently. I thought that's how it was supposed to be? Didn't think the buffs were to the player itself...



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:40:38_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Feb 23, 2017 at 17:00 GMT_

----

2014 change

On Feb 23, 2017 9:25 AM, "Hozu" <notificationsgithub.com> wrote:

> I believe those buffs are being applied to the wyvern itself, currently. I
> thought that's how it was supposed to be? Didn't think the buffs were to
> the player itself...
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 3744Darkstar Issue issuecomment-282042385>,
> or mute the thread
> <github/notifications/unsubscribe-auth/ABGI_xmVgGq8EpGogf17vrvWE4WDa1A2ks5rfbLigaJpZM4MJk2Y>
> .
>


