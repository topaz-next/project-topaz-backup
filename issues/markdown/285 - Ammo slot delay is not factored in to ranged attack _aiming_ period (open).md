**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:03:55_
_Originally opened as: project-topaz/topaz - Issue 285_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [isotor](https://github.com/isotor)**
_Tuesday Apr 23, 2019 at 06:14 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5885_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 30190328_2


**_Source Branch_** (master/stable) **:** master


<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

First tested with a few types of dart darts, grenades, and even an imperial egg - it is impossible to "move and interrupt your aim" *(even with the 999 delay egg)* indicating the delay is not being correctly factored into the ranged attack wind-up.

Different issue still affecting darts: [Darts still use the singing skill animation](github/DarkstarProject/darkstar - Issue 3630) *(this also applies to imperial egg)*



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:03:56_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Apr 23, 2019 at 14:17 GMT_

----

this is intentional, as sources indicated (at the time) that ranged weapon
delay is the "aiming" time, and ammo delay is the action cooldown after
it's shot/thrown

if you can show that this isn't the case, it's easy enough to change

On Tue, Apr 23, 2019 at 12:15 AM isotor <notificationsgithub.com> wrote:

> *I have:*
>
>    - searched existing issues (
>    http://github.com/darkstarproject/darkstar - Issue 
>    <github/darkstarproject/darkstar - Issue >) to see if the
>    issue I am posting has already been addressed or opened by another
>    contributor
>    - checked the commit log to see if my issue has been resolved since my
>    server was last updated
>
> *Client Version* (type /ver in game) *:* 30190328_2
>
> *Source Branch* (master/stable) *:* master
>
> *Additional Information* (Steps to reproduce/Expected behavior) *:*
>
> First tested with a few types of dart darts, grenades, and even an
> imperial egg - it is impossible to "move and interrupt your aim" *(even
> with the 999 delay egg)* indicating the delay is not being factored into
> ranged attack delay.
>
> Different issue still affecting darts: Darts still use the singing skill
> animation <github/DarkstarProject/darkstar - Issue 3630> *(this
> also applies to imperial egg)*
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 5885>, or mute the
> thread
> <github/notifications/unsubscribe-auth/AAIYR72GRJ65BU6EZHI2AULPR2SOJANCNFSM4HHU4GJQ>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:03:57_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Apr 23, 2019 at 17:22 GMT_

----

if its happening, the real bug would be not getting interrupted if your end of animation pos doesn't match the pos you started at (you can run around on retail as long as you stop where you started before it goes off - how this looks client side will depend heavily on your latency)



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:03:59_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [isotor](https://github.com/isotor)**
_Wednesday Apr 24, 2019 at 07:13 GMT_

----

TeoTwawki are you saying even with 0 delay the throw should only occur after the animation/wind up time? If so I can double check but pretty much confirm this isn't the case and the throw/damage is being triggered at the start as I was unable to interrupt on a local server with no latency.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:00_

----

<a href="https://github.com/isotor"><img src="https://avatars2.githubusercontent.com/u/43398624?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [isotor](https://github.com/isotor)**
_Wednesday Apr 24, 2019 at 08:01 GMT_

----

Confirmed on retail if you move during the animation/ wind-up time you receive the message 'You move and interrupt your aim".



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:01_

----

<a href="https://github.com/Vampric"><img src="https://avatars3.githubusercontent.com/u/49852760?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Vampric](https://github.com/Vampric)**
_Thursday Apr 25, 2019 at 02:14 GMT_

----

unless snapshot activates in which case next shot will have no delay or be shot immediately after I believe
mistake not snapshot >>> rapid shot correction



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:02_

----

<a href="https://github.com/Vampric"><img src="https://avatars3.githubusercontent.com/u/49852760?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Vampric](https://github.com/Vampric)**
_Thursday Apr 25, 2019 at 02:44 GMT_

----

confirmed ammo delay is being accounted for using Silver bullet Tp shot was 183, removed weapon to reset tp count changed to platinum bullet tp shot became 184 which confirms delay from 240 from silver bullet to delay of 249 platinum is being counted for. 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:03_

----

<a href="https://github.com/helixhamin"><img src="https://avatars1.githubusercontent.com/u/2202779?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [helixhamin](https://github.com/helixhamin)**
_Thursday Apr 25, 2019 at 03:34 GMT_

----

Vampric Is it possible to take a video on retail to show this? It would help the devs to make the corrections.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:05_

----

<a href="https://github.com/Vampric"><img src="https://avatars3.githubusercontent.com/u/49852760?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Vampric](https://github.com/Vampric)**
_Thursday Apr 25, 2019 at 11:07 GMT_

----

I am currently not on retail atm but will ask a friend of mine to see if I can get that recorded. my testing was done on a private server. 

