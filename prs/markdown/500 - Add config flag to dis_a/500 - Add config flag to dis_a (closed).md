**Labels:**

merge ready



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Wednesday Apr 15, 2020 at 17:25:17_
_Originally opened as: project-topaz/topaz - Issue 500_

----

There are surely people hosting private servers for themselves or their friends who would prefer not have open registrations. True, the chance of someone port scanning you, finding your server, and logging in is minimal but most server emulators offer an option to disable registration entirely. This PR adds that capability.

Adds new flag "account_creation" (true/false) in login.conf file which permits new accounts to be created. Defaults to true. A one-line warning will also show at topaz_connect startup if this flag is set False, as this could be a cause of issues or confusion if someone had done so inadvertently or had forgotten they'd done so.

Considerations:
If account creation is disabled, topaz_connect will always return 0x04 ERROR_CREATE when receiving a new account request, which is visibly shown as "Username is taken" in xiloader. This is of course not **entirely** accurate, but as xiloader only recognizes a few return codes, this was the most suitable available.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 18, 2020 at 20:45:03_

----

[Looks like strings are already being escaped before the switch starts up at L103 and L104](https://github.com/project-topaz/topaz/blob/7e139a4645911acfca0712bd43a2a7a4efbe3041/src/login/login_auth.cpp#L102-L106).


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Saturday Apr 18, 2020 at 20:53:47_

----

Totally was. Can be removed.

Fixed.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 19, 2020 at 04:02:21_

----

maybe rephase to specify that creation via the loader/lobby is what is disabled.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Apr 19, 2020 at 04:14:10_

----

Is there another method for account creation? I know in theory they can be added to the database directly, linking into some web front-end but that wouldn't involve the server and I assume anyone doing that level of integration wouldn't be confused by the comment here.

I was aiming for it to be simple for newer users who may not know whether they're missing another setting somewhere to disable any theoretical "other types" of account creation methods. Do you have a specific phrase you'd prefer?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 19, 2020 at 04:31:47_

----

Answered your own question: I was thinking people might mistake it for preventing any new accounts, when in reality it will be used mainly to steer people toward one of those webpage signups you just referenced.

> I assume anyone doing that level of integration wouldn't be

haha oh man...If you only knew the things I've had to explain :(


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 19, 2020 at 04:34:20_

----

I guess I'll suggest:
`#Allow account creation via the loader (true/false)`


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Apr 19, 2020 at 04:38:15_

----

Sounds clear enough, I like it. 

Changed.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Apr 18, 2020 at 20:45:03_

----

[Looks like strings are already being escaped before the switch starts up at L103 and L104](https://github.com/project-topaz/topaz/blob/7e139a4645911acfca0712bd43a2a7a4efbe3041/src/login/login_auth.cpp#L102-L106).


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Saturday Apr 18, 2020 at 20:53:47_

----

Totally was. Can be removed.

Fixed.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 19, 2020 at 04:02:21_

----

maybe rephase to specify that creation via the loader/lobby is what is disabled.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Apr 19, 2020 at 04:14:10_

----

Is there another method for account creation? I know in theory they can be added to the database directly, linking into some web front-end but that wouldn't involve the server and I assume anyone doing that level of integration wouldn't be confused by the comment here.

I was aiming for it to be simple for newer users who may not know whether they're missing another setting somewhere to disable any theoretical "other types" of account creation methods. Do you have a specific phrase you'd prefer?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 19, 2020 at 04:31:47_

----

Answered your own question: I was thinking people might mistake it for preventing any new accounts, when in reality it will be used mainly to steer people toward one of those webpage signups you just referenced.

> I assume anyone doing that level of integration wouldn't be

haha oh man...If you only knew the things I've had to explain :(


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Apr 19, 2020 at 04:34:20_

----

I guess I'll suggest:
`#Allow account creation via the loader (true/false)`


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Apr 19, 2020 at 04:38:15_

----

Sounds clear enough, I like it. 

Changed.
