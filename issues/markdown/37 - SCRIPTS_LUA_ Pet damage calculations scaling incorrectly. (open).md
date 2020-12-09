**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:41_
_Originally opened as: project-topaz/topaz - Issue 37_

----

<a href="https://github.com/Kthulupwns"><img src="https://avatars1.githubusercontent.com/u/11568537?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Kthulupwns](https://github.com/Kthulupwns)**
_Friday Jul 31, 2015 at 04:14 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 1831_

----

The issue specifically impacts pet damage on higher vit/defense mobs. For example I can use predators claw on a VT+mob in sea for 1300 (which is low for 75 cap) and then go and do predator claws to tiamat for less then 300, when predator claws could do 1800-2400 to tiamat on retail 75 cap. The problem seems to be the way that fStr Calculates against mVit/def. As far as correcting the formula i'd be open to any and all input since i don't know how to write that code




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:42_

----

<a href="https://github.com/Turttle"><img src="https://avatars0.githubusercontent.com/u/10113722?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Turttle](https://github.com/Turttle)**
_Sunday Aug 02, 2015 at 23:45 GMT_

----

github/DarkstarProject/darkstar/blob/master/scripts/globals/weaponskills.luaDarkstar Issue L52

--get fstr
    local fstr = fSTR(attacker:getStat(MOD_STR),target:getStat(MOD_VIT),attacker:getWeaponDmgRank());


