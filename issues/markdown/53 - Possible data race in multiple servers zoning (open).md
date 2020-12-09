**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:11_
_Originally opened as: project-topaz/topaz - Issue 53_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [teschnei](https://github.com/teschnei)**
_Wednesday Oct 07, 2015 at 17:49 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 2202_

----

Scenario: Player zones from server A to server B
Expected sequence of events:
1 - (Server A) informs player of new server's IP/port
2 - (Player) sends 0x0D to Server A to inform of zone departure
3 - (Server A) receives 0x0D from player, saves character information, destroys character storage in memory
4 - (Player) sends 0x0A to Server B to inform of zone arrival
5 - (Server B) loads character information and creates character storage in memory

Exception case: there is no guarantee that 3 is executed before 5 - especially in the case of where server A is performing more slowly than server B.  This means that the character may lose data when zoning.  Probable fix: move saving of character information to step 1.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:12_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Oct 07, 2015 at 17:52 GMT_

----

Note: this is the same problem that demolish found where the zone wouldn't be updated when the player zoned in to server B.  I didn't realize at that time that the problem would apply to everything rather than just zoning (and the probable fix is what I did to fix that)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:13_

----

<a href="https://github.com/nasomi"><img src="https://avatars0.githubusercontent.com/u/6567800?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nasomi](https://github.com/nasomi)**
_Wednesday Oct 07, 2015 at 17:53 GMT_

----

Heres a dump for it:
https://www.dropbox.com/s/if0o81c2j2nr6u1/nonmuteable%20string.7z?dl=0




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:14_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Wednesday Oct 07, 2015 at 17:53 GMT_

----

i did have some fixes for this on dev branch, which i tested locally and wasn't able to reproduce but apparently it didn't fix it for legion
(by fixes i mean preventing any data being written to char/accounts_sessions tables for that char after client sends 0x0D, as well as preventing writing to the db on logging)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:15_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Wednesday Oct 07, 2015 at 19:21 GMT_

----

see github/DarkstarProject/darkstar - Issue 1796 for more info




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:17_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Oct 08, 2015 at 02:32 GMT_

----

appears that the only thing saved in 0x0D is exp/stats, so it's not as critical as I initially thought




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:18:18_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Sunday Nov 15, 2015 at 12:28 GMT_

----

need someone with a populated server to pull and build github/DarkstarProject/darkstar - PR 2417

reimport triggers.sql too


