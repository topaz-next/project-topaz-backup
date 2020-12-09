**Labels:**

improvement



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:10_
_Originally opened as: project-topaz/topaz - Issue 288_

----

<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [ShelbyZ](https://github.com/ShelbyZ)**
_Friday Apr 26, 2019 at 04:47 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5895_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] _looked code way later than I should have_

In both Database_xxx.bat scripts there are direct references to path for Program Files.  Depending on the install and target system this could be either **Program Files** or **Program Files (x86)**.  To remove the need for a user to change this file we can use environment variables and check both locations.  Setting a variable when we find that option.

Database_initial_setup.bat
github/DarkstarProject/darkstar/blob/d0bc0d2cd3a6cb874c279b96811aebb692b3bbd6/tools/Database_initail_setup.batDarkstar Issue L33-L34

Database_update.bat
github/DarkstarProject/darkstar/blob/d0bc0d2cd3a6cb874c279b96811aebb692b3bbd6/tools/Database_update.batDarkstar Issue L33

Sample
```batch
if exist %ProgramFiles\MySQL\MySQL Server 5.7\bin (
    set mysql="..."
)

if not defined mysql (
    if exist %ProgramFiles(x86)\MySQL\MySQL Server 5.7\bin (
        set mysql="..."
    )
)
```



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:11_

----

<a href="https://github.com/ShelbyZ"><img src="https://avatars0.githubusercontent.com/u/1033099?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ShelbyZ](https://github.com/ShelbyZ)**
_Friday Apr 26, 2019 at 04:48 GMT_

----

KnowOne134 food for thought



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:12_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Apr 26, 2019 at 07:23 GMT_

----

What if we're a weirdo and use MariaDB? :anguished: 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:13_

----

<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Friday Apr 26, 2019 at 10:53 GMT_

----

Manually edit the line?

On Fri, Apr 26, 2019, 2:23 AM ibm2431 <notificationsgithub.com> wrote:

> What if we're a weirdo and use MariaDB? 😧
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 5895Darkstar Issue issuecomment-486955424>,
> or mute the thread
> <github/notifications/unsubscribe-auth/AIPXQA7YSSQXWHFH5HT7RF3PSKUYPANCNFSM4HISO4TA>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:04:15_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Apr 26, 2019 at 13:10 GMT_

----

```
if exist %ProgramFiles\MariaDB 10.2\bin (
    set mysql="..."
)
```
Don't forget Maria!

