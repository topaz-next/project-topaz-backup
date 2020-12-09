**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:27_
_Originally opened as: project-topaz/topaz - Issue 20_

----

<a href="https://github.com/RwNigma"><img src="https://avatars3.githubusercontent.com/u/11567678?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [RwNigma](https://github.com/RwNigma)**
_Tuesday May 26, 2015 at 20:46 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 1480_

----

Darkstar Issue Darkstar Issue  This is the current damage modifier:

local dmg = 2 \* player:getRangedDmg() + player:getAmmoDmg() + player:getMod(MOD_QUICK_DRAW_DMG);

This doesn't check for Elemental Staffs, MAB, and Weather. MOD_QUICK_DRAW_DMG may account for these, but looking at that variable I don't see where these are applied.
Darkstar Issue Darkstar Issue  Damage according to The wiki page is as follows:

(I understand the Tricone isn't coded)
(2 \* (Gun base DMG + bullet base DMG + Corsair's Tricorne bonus)) \* (1 + (MAB / 100)) \* (Elemental Staff bonus) \* (Day/Weather Bonus) 
Darkstar Issue Darkstar Issue  I also noticed that the shots are giving improper status effects. These apply to all of them giving these types of status effects.

Wind Shot:
local effects = {};
    local counter = 1;
    local choke = target:getStatusEffect(EFFECT_CHOKE);
    if (choke ~= nil) then
        effects[counter] = choke;
        counter = counter + 1;
    end
Going to assume this gives the mob "Choke"? This gives a VIT debuff and lowers total HP?
Darkstar Issue Darkstar Issue  FFxiCyclo has Shots as listed:

Light Shot: Dia Defense Down+5%, Damage Over Time increase *
Dark Shot: Bio Attack Down+5%, Damage Over Time increase; Blind+10%
Earth Shot: Slow+10%
Wind Shot: Acid Bolt Defense Down+5%, Silence+10%, Gravity+10%
Ice Shot: Paralyze+10%, Bind+10%
Thunder Shot: Stun+10%
Water Shot: Poison Duration increase

Special Note about Dia/Bio: Quick Draw will upgrade Bio and Dia to their next spell tier. E.g. Dia II augmented by Light Shot becomes equivalent to Dia III and thus is not overwritten by Bio II. Presumably, Bio III and Dia III augmented by Quick Draw become equivalent to "Bio IV" and "Dia IV."Exclamation
Regardless of tier, the bonus provides a flat +3 DoT bonus.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:28_

----

<a href="https://github.com/RwNigma"><img src="https://avatars3.githubusercontent.com/u/11567678?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [RwNigma](https://github.com/RwNigma)**
_Tuesday May 26, 2015 at 20:54 GMT_

----

I am interested in Coding and have C++, Visual Basic, and Java under my belt. I wouldn't mind giving it a go and coding when I get settled after this week. I have talked to Nesstea before about it and I just need to get the files and start on things.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:29_

----

<a href="https://github.com/takhlaq"><img src="https://avatars1.githubusercontent.com/u/6381451?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [takhlaq](https://github.com/takhlaq)**
_Tuesday May 26, 2015 at 21:09 GMT_

----

hop on irc if you need anything (see github/DarkstarProject/darkstar/blob/master/README.md for info)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:31_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday May 26, 2015 at 22:08 GMT_

----

"This doesn't check for Elemental Staffs, MAB, and Weather."

sure it does.  it's actually on the very next line




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:32_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday May 26, 2015 at 22:11 GMT_

----

as for the chunk about choke, it doesn't actually do anything yet at that point, just checks if the mob has choke and saves the effect for later.  (later it checks the array of effects the target has, picks one, and augments it.  for this specific shot, it checks for choke and threnody)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:33_

----

<a href="https://github.com/RwNigma"><img src="https://avatars3.githubusercontent.com/u/11567678?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [RwNigma](https://github.com/RwNigma)**
_Wednesday May 27, 2015 at 02:08 GMT_

----

I see the earth staff under the player bonuses. Is the weather then under "params" within playerbonuses? Magic attack bouns I don't see within the code unless again it is within "params". I know that getlines(); tend to grab from almost anywhere, and from classes and books that its the easy way to do things.

Checks if it has choke...Shouldn't it check if it has Slow? Or this is just to apply extra damage to it if it has choke applied? First time with LUA, but it looks a lot like C++. Just wanting to get better at it. And I am not meaning to post things if it doesn't need to be fixed, but more to make sure I guess.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:34_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday May 27, 2015 at 02:10 GMT_

----

Slow is an earth spell, so wind shot would not check it (earth shot would, and does).

addBonusesAbility is in magic.lua, you can see everything for affinity (staff) and weather in there




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:35_

----

<a href="https://github.com/RwNigma"><img src="https://avatars3.githubusercontent.com/u/11567678?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [RwNigma](https://github.com/RwNigma)**
_Wednesday May 27, 2015 at 02:12 GMT_

----

Was looking in earth shot and was talking here still as I was looking at wind shot. 

So does wind shot actually give the mob gravity status, DEF down, and Silence?

magic.lua makes my head hurt haha.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:36_

----

<a href="https://github.com/dazusu"><img src="https://avatars0.githubusercontent.com/u/7009763?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dazusu](https://github.com/dazusu)**
_Wednesday May 27, 2015 at 14:21 GMT_

----

Note that the bonuses to Dia, Bio, Blind, Slow, Paralyze, Silence, Gravity, Stun ONLY occur if the spell/enfeeble is landed on the monster 2~3 seconds after the shot; kind of like a magic burst. This wasn't stated in the opening post, so adding it here.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:38_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday May 27, 2015 at 14:41 GMT_

----

er... no, that is not true at all.  it enhances it as long as the debuff is applied to the target when the quick draw is fired




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:39_

----

<a href="https://github.com/dazusu"><img src="https://avatars0.githubusercontent.com/u/7009763?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [dazusu](https://github.com/dazusu)**
_Wednesday May 27, 2015 at 15:15 GMT_

----

Maybe I'm remembering wrong; I thought the debuff was only amplified if the quickdraw shot landed a few seconds after the debuff was applied - but if it was too long after, the bonus didn't happen (I got the order the wrong way around in my other post).

I could easily be mistaken, it was a long time ago I did shit on retail that required a COR :)




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:40_

----

<a href="https://github.com/RwNigma"><img src="https://avatars3.githubusercontent.com/u/11567678?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [RwNigma](https://github.com/RwNigma)**
_Wednesday Jun 03, 2015 at 18:59 GMT_

----

Eh. No one needs a COR, but I really enjoy the job and was just making sure quick draw was working correctly. Can we confirm or deny the few seconds window because a lot of skill chains and magic bursts aren't working as intended. 




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:41_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Wednesday Jun 03, 2015 at 19:03 GMT_

----

The few seconds window is denied. If you are having problems timing
weaponskills or magic bursts, please open a new issue on it.




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:00:42_

----

<a href="https://github.com/RwNigma"><img src="https://avatars3.githubusercontent.com/u/11567678?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [RwNigma](https://github.com/RwNigma)**
_Wednesday Jun 03, 2015 at 19:08 GMT_

----

Awesome. Thanks teschnei. I will check some skill chains and get back on that.


