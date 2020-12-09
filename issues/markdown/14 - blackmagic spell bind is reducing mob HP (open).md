**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 13:59:59_
_Originally opened as: project-topaz/topaz - Issue 14_

----

<a href="https://github.com/lichtl"><img src="https://avatars2.githubusercontent.com/u/1228155?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [lichtl](https://github.com/lichtl)**
_Thursday Apr 02, 2015 at 17:52 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 1213_

----

It seems that on various mobs bind will cause an HP reduction of approx 3-7%. This also seem to not apply to all mob types or jobs (I've just even confirmed that the same mob type different mobs might be affected while others not)

Zone: Mount Zhayolm
Ebony Pudding: 100%
Sweeping Cluster:  95%

Zone: Batallia Downs
Sabertooth Tiger: 97% / another stays at 100%
Mauthe Doog: 100% / another went down to 97%
Wight: 97%




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:00_

----

<a href="https://github.com/maxtherabbit"><img src="https://avatars3.githubusercontent.com/u/6538577?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [maxtherabbit](https://github.com/maxtherabbit)**
_Saturday Apr 04, 2015 at 13:45 GMT_

----

I haven't yet investigated the cause, but I don't think it's exclusive to bind. I've seen it happen with other non-damage spells as well




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:01_

----

<a href="https://github.com/xipies"><img src="https://avatars3.githubusercontent.com/u/7948457?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [xipies](https://github.com/xipies)**
_Tuesday Apr 28, 2015 at 01:48 GMT_

----

I've logged in before to zones and seen mobs that started out with ~95-98% hp. Maybe two different hp values being sent to client and the actual hp is making it appear less than 100%.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:02_

----

<a href="https://github.com/nesstea"><img src="https://avatars0.githubusercontent.com/u/1483915?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [nesstea](https://github.com/nesstea)**
_Wednesday Apr 29, 2015 at 22:30 GMT_

----

Happens with paraylze II as well :)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:03_

----

<a href="https://github.com/lichtl"><img src="https://avatars2.githubusercontent.com/u/1228155?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [lichtl](https://github.com/lichtl)**
_Saturday May 16, 2015 at 15:31 GMT_

----

Maybe this can bring some more light into it. It seems that the Mob HP is somewhere being recalculated after it is being claimed.

Dave : scan
----== SystemMessage ==----
Sweeping_Cluster HP: 4045/4045 MP: 0/0 TP: 0 ACC: 288 EVA: 236
STR: 72 DEX: 75 VIT: 55 AGI: 75 MND: 66 CHR: 
The Sweeping Cluster is out of range.
The Sweeping Cluster is out of range.
Dave starts casting Bind on the Sweeping Cluster.
The Sweeping Cluster is out of range.
Unable to see the Sweeping Cluster.
Dave : scan
----== SystemMessage ==----
Sweeping_Cluster HP: 4045/4285 MP: 0/0 TP: 0 ACC: 288 EVA: 236
STR: 72 DEX: 75 VIT: 55 AGI: 75 MND: 66 CHR: 
Unable to see the Sweeping Cluster.
Dave casts Bind.The Sweeping Cluster is bound.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:05_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Saturday May 16, 2015 at 16:50 GMT_

----

github/DarkstarProject/darkstar/blob/master/src/map/lua/lua_baseentity.cppDarkstar Issue L264
github/DarkstarProject/darkstar/blob/master/src/map/entities/battleentity.cppDarkstar Issue L448

have fun


