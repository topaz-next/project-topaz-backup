**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:44:18_
_Originally opened as: project-topaz/topaz - Issue 181_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Deadwing888](https://github.com/Deadwing888)**
_Wednesday Jul 05, 2017 at 22:40 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 3928_

----

<!-- remove space and mark with 'x' between [] -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **not a client issue**


**_Server Version_** (type `revision` in game) **I looked at the sql files**


**_Source Branch_** (master/stable) **:**


**_Additional Information_** (Steps to reproduce/Expected behavior) **:**


EDIT: issue completely re-written:

The rune weapons have a latent param for LATENT_WEAPON_DRAWN_MP_OVER which lets them function correctly. There is no LATENT_WEAPON_DRAWN_HP_OVER latent which would be a necessary check for the Berserker's Torque to not kill the player. (The latent param in this case would be 50)



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:44:20_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Jul 05, 2017 at 22:47 GMT_

----

I think I understand what you are saying (when you give the Rune Chopper example, I assume you mean that's how it works on retail - the post isn't very clear and I'm not familiar with the weapon).

Both proposed solutions have their own problems, though.  The first one can explode in complexity in a bad way if it's not careful.  For the second one, I don't want to add any more bindings unless we really need it for a core mechanic.  I don't really see how it would fix the problem though (adding an mp drain latent when weapon is drawn?  It seems not very intuitive, compared to the rest).



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:44:21_

----

<a href="https://github.com/Deadwing888"><img src="https://avatars0.githubusercontent.com/u/12477635?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Deadwing888](https://github.com/Deadwing888)**
_Wednesday Jul 05, 2017 at 22:58 GMT_

----

I'll try to clarify:

~~The way the latent effects are currently setup, rune weapons will give positive effects as long as the weapons are drawn. On retail to achieve this effect you would have had to have refresh of some sort active because the positive effects checked both MP >0 and "Is Weapon Drawn?".~~

~~I agree neither solution is great. I think the first solution may be superior as it would only take I believe two additional latent effect types (one where latentparam checks mp for rune weapons, one where latentparam checks hp for Berserker's Torque).~~

~~The second solution could handle it by means of:~~

~~--item Berserker's Torque
function onWeaponEngage(target)
    if (target:getHP()> 50) then
        target:addMod(MOD_REGAIN, 10)
        target:addMod(MOD_REGEN, -50)
    end
end;~~


~~I guess you might need a second function for onWeaponDisengage to delete the effects?  I'm not sure this would handle all instances such as dieing, zoning, deleveling and losing weapon etc. Probably makes this the inferior solution.~~

~~Edit: Maybe the function would have to check it each tick like onmobfight and just not give any effects otherwise?~~

Edit 2: I'm an idiot, they work fine outside of the .9 haste instead of 9 haste on rune chopper. Berserker's torque issue still at large



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:44:23_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Jul 05, 2017 at 23:02 GMT_

----

Well, it would also have the exact same problem that you're reporting here, so it's definitely the inferior one :)

on tick checking is going to be bad, too.

Ideally - a way to compose latent effect trigger conditions such that a stat can require multiple conditions to be met before being active.  Probably not that hard to implement, either, now that I think about it.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:44:24_

----

<a href="https://github.com/KnowOne134"><img src="https://avatars3.githubusercontent.com/u/35616771?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [KnowOne134](https://github.com/KnowOne134)**
_Wednesday Jul 10, 2019 at 20:56 GMT_

----

from wiki it says it can kill you
"Drains 50 Hit Points in exchange for 10 TP each tick.
This effect will cause death if HP is at or below 50 while the effect is active."

https://ffxiclopedia.fandom.com/wiki/Berserker's_Torque



----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Monday Mar 09, 2020 at 21:33:27_

----

Hello. As KnowOne stated, this is working as intended. Closing. Thank you.

Edit:

Came across a related issue while testing: while the Torque works as intended when you first draw your Weapon (it will kill you), **the latent is still working after being raised without being engaged**, putting you in a dying loop.

Tested while being a GM, used the !raise power Name command multiple times.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Mar 09, 2020 at 22:01:23_

----

A new entry in one million and one ways to die in ffxi!
- [x] _Death by animation delay **during reraise**._

