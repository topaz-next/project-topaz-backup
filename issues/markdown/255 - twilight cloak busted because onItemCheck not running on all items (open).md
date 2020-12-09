**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:03_
_Originally opened as: project-topaz/topaz - Issue 255_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jan 27, 2019 at 17:34 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5660_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
n/a

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
github/DarkstarProject/darkstar/commit/7a160120a7b7313cbfc1b5483627cebc24776adaDarkstar Issue diff-aae988c514ff0e269bae6cbe94203ba0R3

_edit: that link may take a long time to load. its one of the earliest commits to the repository, and was a lot of junk at once_

that doesn't work anymore, looks like its only firing for items that are usable, used to run on every item (which was bad behavior anyway?)

other: 
1. Missing the return.
2. That should be a mod to generically add a spell anyway in case SE ever adds another item granting a spell.. with a safety check to see if the player already has the spell native (the above script would remove it even if player had it without the equip, if the script was working)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:04_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Sunday Jan 27, 2019 at 17:52 GMT_

----

it's supposed to run on any item with the script flag set as a response to
certain things.  Twilight Cloak does have SCRIPT_EQUIP set, but since we
just got another bug saying the dusk/dawn part of NIN AF isn't working
(which uses the same flag) then there might be something wrong with the
actual Lua call

On Sun, Jan 27, 2019 at 10:34 AM TeoTwawki <notificationsgithub.com> wrote:

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
> *Client Version* (type /ver in game) *:*
> n/a
>
> *Source Branch* (master/stable) *:*
> master
>
> *Additional Information* (Steps to reproduce/Expected behavior) *:*
> 7a16012Darkstar Issue diff-aae988c514ff0e269bae6cbe94203ba0
> <github/DarkstarProject/darkstar/commit/7a160120a7b7313cbfc1b5483627cebc24776adaDarkstar Issue diff-aae988c514ff0e269bae6cbe94203ba0>
>
> that doesn't work anymore, looks like its only firing for items that are
> usable, used to run on every item (which was bad behavior anyway?)
>
> other:
>
>    1. Missing the return.
>    2. That should be a mod to generically add a spell anyway in case SE
>    ever adds another item granting a spell.. with a safety check to see if the
>    player already has the spell native (the above script would remove it even
>    if player had it without the equip, if the script was working)
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 5660>, or mute the
> thread
> <github/notifications/unsubscribe-auth/ABGI_21gq2NOooCILSacO7savXa4ulvjks5vHeMogaJpZM4aU1q1>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:06_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jan 27, 2019 at 17:53 GMT_

----

ah ok, makes sense



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:59:07_

----

<a href="https://github.com/zynjec"><img src="https://avatars3.githubusercontent.com/u/17911103?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zynjec](https://github.com/zynjec)**
_Monday Jan 28, 2019 at 19:25 GMT_

----

> but since we just got another bug saying the dusk/dawn part of NIN AF isn't working (which uses the same flag) then there might be something wrong with the actual Lua call

Unrelated, the haste was just getting floored to 0% after being missed in the haste rewrite.

