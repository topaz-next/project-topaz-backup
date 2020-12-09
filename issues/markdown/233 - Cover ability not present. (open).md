**Labels:**

feature



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:46_
_Originally opened as: project-topaz/topaz - Issue 233_

----

<a href="https://github.com/Dynas13"><img src="https://avatars0.githubusercontent.com/u/36946058?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [Dynas13](https://github.com/Dynas13)**
_Tuesday Jul 17, 2018 at 01:51 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 5095_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
all

**_Source Branch_** (master/stable) **:** 
master

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

The status effect exists, the animation works, the necessary elements to make it happen are there but there's no development on making Cover.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:47_

----

<a href="https://github.com/Dynas13"><img src="https://avatars0.githubusercontent.com/u/36946058?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Dynas13](https://github.com/Dynas13)**
_Tuesday Jul 17, 2018 at 01:59 GMT_

----

```lua

-- Ability: Cover
-- Allows you to protect party members by placing yourself between them and the enemy.
-- Obtained: Paladin Level 35
-- Recast Time: 3:00
-- Duration: 0:15-0:30
-----------------------------------
require("scripts/globals/settings");
require("scripts/globals/status");
require("scripts/globals/msg");
-----------------------------------
```

```lua
function onAbilityCheck(player,target,ability)
    if (target == nil or target:getID() == player:getID() or not target:isPC()) then
        return dsp.msg.basic.CANNOT_ON_THAT_TARG, 0;
    else
        return 0, 0;
    end
end;

function onUseAbility(player,target,ability)
    target:addStatusEffect(player,dsp.effect.COVER,1,0,15)
end;
```

I'm know this is extremely basic and wrong in some points but something like this would be where I would start personally.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:49_

----

<a href="https://github.com/davismj"><img src="https://avatars2.githubusercontent.com/u/3845823?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [davismj](https://github.com/davismj)**
_Tuesday Jul 17, 2018 at 02:33 GMT_

----

Do you know how to submit a PR?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:50_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Tuesday Jul 17, 2018 at 03:04 GMT_

----

i don't think any of the necessary stuff to make it work are implemented
yet (ie, the checks when being attacked for the effect)

On Mon, Jul 16, 2018 at 7:51 PM Dynas13 <notificationsgithub.com> wrote:

> *I have:*
>
>    - searched existing issues (
>    http://github.com/darkstarproject/darkstar - Issue 
>    <github/darkstarproject/darkstar - Issue >) to see if the
>    issue I am posting has already been addressed or opened by another
>    contributor
>    - checked the commit log to see if my issue has been resolved since my
>    server was last updated
>
> *Client Version* (type /ver in game) *:*
> all
>
> *Source Branch* (master/stable) *:*
> n/a
>
> *Additional Information* (Steps to reproduce/Expected behavior) *:*
>
> The status effect exists, the animation works, the necessary elements to
> make it happen are there but there's no development on making Cover.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <github/DarkstarProject/darkstar - Issue 5095>, or mute the
> thread
> <github/notifications/unsubscribe-auth/ABGI_y6LvlscOOyhSOA0X3iv7caIx0Ynks5uHUMqgaJpZM4VSDfw>
> .
>




----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:52_

----

<a href="https://github.com/Dynas13"><img src="https://avatars0.githubusercontent.com/u/36946058?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Dynas13](https://github.com/Dynas13)**
_Tuesday Jul 17, 2018 at 03:22 GMT_

----

> Do you know how to submit a PR?

I do, but my code is missing too much for me to submit it properly. Doesn't calculate half the things that are apart of cover like the VIT formula and enmity added to paladin and subtracted from target.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:53_

----

<a href="https://github.com/Wiggo32"><img src="https://avatars2.githubusercontent.com/u/30469395?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Wiggo32](https://github.com/Wiggo32)**
_Tuesday Jul 17, 2018 at 14:11 GMT_

----

also something to consider whenever someone starts working on this:
-the case of 2 or more PLD's in a party, being able to determine which PLD the active cover effect belongs to



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:55_

----

<a href="https://github.com/Dynas13"><img src="https://avatars0.githubusercontent.com/u/36946058?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Dynas13](https://github.com/Dynas13)**
_Wednesday Jul 18, 2018 at 13:58 GMT_

----

I've done a lot of digging around trying to figure a way for damage transfer to work. There's stuff like transferEnmity which is for accomplice and collaborator. Or trickattackPartner which lets the code know who's receiving enmity. What I can't wrap my head around is how damage is received. I'm sure it's buried somewhere but if we could say something like

```lua
--Pseudocode------------------------------
while ability is active then
  player receives targets damage
  if damage >= 0 then
    player.addMod(dsp.mod.Enmity, +200)
    target:lowerEnmity(target, 10)
elseif gallant coronet equipped then
  transfer magical damage to player
elseif valor surcoat equipped then
  20% of damage transferred converted to mp.
end
-------------------------------------------------------
function onUseAbility(player,target,ability)
--formula from https://www.bg-wiki.com/bg/Cover
local baseDuration = 15;
local bonusTime = utils.clamp(math.floor((player:getMod(dsp.mod.VIT) + player:getMod(dsp.mod.MND) - target:getMod(dsp.mod.VIT) * 2) / 4), 0, 15)
local duration = baseDuration + bonusTime;

player:addStatusEffect(player,dsp.effect.COVER,0,0,duration)

  if target:physicalDmgTaken >= 0 then
    player.addMod(dsp.mod.Enmity, +200)
    target:lowerEnmity(target, 10)
  end
end;
```
I assume Gallant Coronet and Surcoat are handled within their own files instead of the ability file, if so, that wont be needed here.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 14:55:56_

----

<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Jul 18, 2018 at 14:00 GMT_

----

Dynas13 I code tagged your post, click edit and you can see how that was done for next time :-)

