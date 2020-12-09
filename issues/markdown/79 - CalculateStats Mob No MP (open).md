**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:25:04_
_Originally opened as: project-topaz/topaz - Issue 79_

----

<a href="https://github.com/armouredking"><img src="https://avatars1.githubusercontent.com/u/16038428?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [armouredking](https://github.com/armouredking)**
_Thursday Jan 07, 2016 at 15:28 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2572_

----

This is from DSP server logs; I started the server last night at this point:

```
[0m[1;32m[Status][0m Memory manager initialised: [1;37mlog/DSP.leaks[0m
[1;37m[Info][0m DarkStar - Git Revision Hash: [1;37mdd6c854c182a8bedfde88c96ec5f1d057897aae7[0m.
[1;32m[Status][0m do_init: begin server initialization...
[06/Jan] [20:17:23][1;37m[Info][0m Console Silent Setting: 0           - [1;32m[OK][0m
[06/Jan] [20:17:23][1;32m[Status][0m do_init: map_config is reading        - [1;32m[OK][0m
[06/Jan] [20:17:23][1;32m[Status][0m luautils::init:lua initializing...        - [1;32m[OK][0m
[06/Jan] [20:17:23][1;32m[Status][0m do_init: sqlhandle is allocating          - [1;32m[OK][0m
[06/Jan] [20:17:23][1;32m[Status][0m do_init: zlib is reading              - [1;32m[OK][0m
[06/Jan] [20:17:23][1;32m[Status][0m do_init: loading items            - [1;32m[OK][0m
[06/Jan] [20:17:24][1;32m[Status][0m do_init: loading spells           - [1;32m[OK][0m
[06/Jan] [20:17:25][1;36m[Debug][0m [1;36mUpdateGuildPointsPattern is finished. New pattern: 5
[0m[06/Jan] [20:17:25][1;32m[Status][0m do_init: loading zones            - [1;32m[OK][0m
[06/Jan] [20:20:22][1;32m[Status][0m do_init: server is binding with port 54230    - [1;32m[OK][0m
[06/Jan] [20:20:24][1;36m[Debug][0m [1;36mInitializeWeather Finished
[0m[06/Jan] [20:20:24][1;32m[Status][0m The map-server is [1;32mready[0m to work...
 =======================================================================
[06/Jan] [20:20:24][1;36m[Debug][0m [1;36m[Lua] Garbage Collected. Current State Top: 0
```

I played for a while, bla bla, I left the server running when I went to bed. I started getting these:

```
[06/Jan] [21:16:49][1;31m[Error][0m mobutils::CalculateStats Mob (17969333) has no mp for casting spells!
[06/Jan] [21:16:49][1;31m[Error][0m mobutils::CalculateStats Mob (17969334) has no mp for casting spells!
[06/Jan] [21:16:49][1;31m[Error][0m mobutils::CalculateStats Mob (17969335) has no mp for casting spells!
[06/Jan] [21:16:49][1;31m[Error][0m mobutils::CalculateStats Mob (17969340) has no mp for casting spells!
[06/Jan] [21:16:49][1;31m[Error][0m mobutils::CalculateStats Mob (17969341) has no mp for casting spells!
[06/Jan] [21:16:49][1;31m[Error][0m mobutils::CalculateStats Mob (17969344) has no mp for casting spells!
[06/Jan] [21:16:49][1;31m[Error][0m mobutils::CalculateStats Mob (17969345) has no mp for casting spells!
[06/Jan] [21:16:49][1;31m[Error][0m mobutils::CalculateStats Mob (17969362) has no mp for casting spells!
[06/Jan] [21:16:49][1;31m[Error][0m mobutils::CalculateStats Mob (17969363) has no mp for casting spells!
[06/Jan] [21:16:49][1;31m[Error][0m mobutils::CalculateStats Mob (17969490) has no mp for casting spells!
[06/Jan] [21:16:49][1;31m[Error][0m mobutils::CalculateStats Mob (17969491) has no mp for casting spells!
[06/Jan] [21:16:49][1;31m[Error][0m mobutils::CalculateStats Mob (17969494) has no mp for casting spells!
[06/Jan] [21:16:49][1;31m[Error][0m mobutils::CalculateStats Mob (17969500) has no mp for casting spells!
[06/Jan] [21:16:49][1;31m[Error][0m mobutils::CalculateStats Mob (17969501) has no mp for casting spells!
[06/Jan] [21:16:49][1;31m[Error][0m mobutils::CalculateStats Mob (17969504) has no mp for casting spells!
[06/Jan] [21:16:50][1;31m[Error][0m mobutils::CalculateStats Mob (17969507) has no mp for casting spells!
[06/Jan] [21:16:50][1;31m[Error][0m mobutils::CalculateStats Mob (17969510) has no mp for casting spells!
[06/Jan] [21:16:51][1;31m[Error][0m mobutils::CalculateStats Mob (17969333) has no mp for casting spells!
[06/Jan] [21:16:51][1;31m[Error][0m mobutils::CalculateStats Mob (17969334) has no mp for casting spells!
[06/Jan] [21:16:51][1;31m[Error][0m mobutils::CalculateStats Mob (17969335) has no mp for casting spells!
[06/Jan] [21:16:51][1;31m[Error][0m mobutils::CalculateStats Mob (17969340) has no mp for casting spells!
[06/Jan] [21:16:51][1;31m[Error][0m mobutils::CalculateStats Mob (17969341) has no mp for casting spells!
[06/Jan] [21:16:51][1;31m[Error][0m mobutils::CalculateStats Mob (17969344) has no mp for casting spells!
[06/Jan] [21:16:51][1;31m[Error][0m mobutils::CalculateStats Mob (17969345) has no mp for casting spells!
[06/Jan] [21:16:51][1;31m[Error][0m mobutils::CalculateStats Mob (17969362) has no mp for casting spells!
[06/Jan] [21:16:51][1;31m[Error][0m mobutils::CalculateStats Mob (17969363) has no mp for casting spells!
[06/Jan] [21:16:51][1;31m[Error][0m mobutils::CalculateStats Mob (17969490) has no mp for casting spells!
[06/Jan] [21:16:51][1;31m[Error][0m mobutils::CalculateStats Mob (17969491) has no mp for casting spells!
[06/Jan] [21:16:52][1;31m[Error][0m mobutils::CalculateStats Mob (17969494) has no mp for casting spells!
[06/Jan] [21:16:52][1;31m[Error][0m mobutils::CalculateStats Mob (17969500) has no mp for casting spells!
[06/Jan] [21:16:52][1;31m[Error][0m mobutils::CalculateStats Mob (17969501) has no mp for casting spells!
[06/Jan] [21:16:52][1;31m[Error][0m mobutils::CalculateStats Mob (17969504) has no mp for casting spells!
[06/Jan] [21:16:52][1;31m[Error][0m mobutils::CalculateStats Mob (17969507) has no mp for casting spells!
[06/Jan] [21:16:52][1;31m[Error][0m mobutils::CalculateStats Mob (17969510) has no mp for casting spells!
```

After this block of messages occurs, it would reoccur every hour-ish afterwards. The next sets are at 2214, 2312, 0009, 0107, 0204, 0302, 0400, 0457, 0555, 0652, 0750. I shut down the server when I woke up this morning to rebuild it to fix Darkstar Issue 2571 . What's curious to me is that, these errors are happening _very_ regularly and always the same numbers / ids. Noone else is playing on the server.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:25:05_

----

<a href="https://github.com/bendangelo"><img src="https://avatars3.githubusercontent.com/u/674090?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [bendangelo](https://github.com/bendangelo)**
_Thursday Jan 07, 2016 at 15:32 GMT_

----

Mobs cast spells as they roam around. It looks like they are not restoring mp like they should be.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:25:06_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Saturday Jan 09, 2016 at 02:27 GMT_

----

bunch of WAR/WAR mobs in reisenjima with spell lists, gonna leave this for gedads


