**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:01_
_Originally opened as: project-topaz/topaz - Issue 268_

----

<a href="https://github.com/ababyduck"><img src="https://avatars3.githubusercontent.com/u/9102794?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [ababyduck](https://github.com/ababyduck)**
_Sunday Mar 24, 2019 at 22:24 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5805_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
N/A

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
The game server fails to compile if the Windows system locale is set to Japanese. (Windows 10, VS Community 2017) Setting the locale back to English resolves this issue, but also prevents Japanese input from being used in FFXI.

This appears to be related to non-unicode characters in the following files:
- char_update.cpp
- packet_system.cpp
- battleutils.cpp
- synthutils.cpp

...although I was *not* able to resolve the issue simply by saving these files in UTF-8 encoding.

Full compile output looks like this:
https://gist.github.com/ababyduck/fcf5f2313a85743b862ac0b9616fc652

To set system locale in Windows 10:
Region & Language Settings > Administrative Language Settings > Change System Locale... > Japanese (Japan) > OK



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:02_

----

<a href="https://github.com/zynjec"><img src="https://avatars3.githubusercontent.com/u/17911103?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zynjec](https://github.com/zynjec)**
_Sunday Mar 24, 2019 at 22:29 GMT_

----

More a Visual Studio issue than project issue, the files are already UTF-8 despite what VS claims.

It's caused by the comments all in cyrillic, remove them locally or PR translations I guess.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:00:04_

----

<a href="https://github.com/ababyduck"><img src="https://avatars3.githubusercontent.com/u/9102794?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ababyduck](https://github.com/ababyduck)**
_Monday Mar 25, 2019 at 05:25 GMT_

----

Thanks zynjec. I found a few outlying non-ascii characters that were contributing to the issue, but as you said, it's mostly the cyrillic comments. I collected a list of the lines and text that need translation here:

https://gist.github.com/ababyduck/34b3f640e11a3d7b13c26d6ef82f2d8a

Google Translate does an ok job for some of it, but certain things are out of context (e.g. using the word "value" when describing the price of an item, which obviously has a different meaning when discussing code). If a native speaker would like to translate these, I suspect it would be helpful.

Alternatively, I was able to solve the issue by adding `/source-charset:IBM437` to Solution Browser > DSGame-server > Properties > Configuration Properties > C/C++ > Command Line > Additional Options. This forces the project to build with an English code page regardless of the system locale. Is it worth PRing this, or would a translation be preferable?

edit: Setting charset to utf-8 rather than IBM437 works as well.



----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Thursday Mar 19, 2020 at 13:51:23_

----

Hello. I'm unable to reproduce this issue on canary as of 03/19/2020, tested with Visual Studio Community 2019 16.5.0. Feel free to reopen an issue if you come across something new regarding this. Thank you.
