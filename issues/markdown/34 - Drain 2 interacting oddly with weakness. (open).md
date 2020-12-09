**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:11_
_Originally opened as: project-topaz/topaz - Issue 34_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Hozu](https://github.com/Hozu)**
_Friday Jul 24, 2015 at 06:00 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 1790_

----

When Drain 2 grabs the max hp to calculate how much of a max HP boost it should give, it's using the unweakened HP value instead of the weakened value. I don't know how HP%/MP% boosts/penalties are supposed to interact with weakness so I'm not sure how do go about a fix. If you get say, 25% HP reduction via curse while weakened, is it supposed to be -25% of weakened max HP or unweakened max HP? If it's the latter, a simple fix in the drain 2 script to check for weakness would be fine. If it's the latter, I think there would need to be a new mod to handle the HP/MP weakness penalty separate from the other HP%/MP% mods.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:12_

----

<a href="https://github.com/Kthulupwns"><img src="https://avatars1.githubusercontent.com/u/11568537?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Kthulupwns](https://github.com/Kthulupwns)**
_Friday Jul 31, 2015 at 08:37 GMT_

----

local leftOver = (caster:getHP() + dmg) - caster:getMaxHP();

Could probably just add the var there.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:11:13_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Friday Jul 31, 2015 at 16:05 GMT_

----

I would if I knew how other forms of HP/MP % boosts/penalties are supposed to with weakness. :/


