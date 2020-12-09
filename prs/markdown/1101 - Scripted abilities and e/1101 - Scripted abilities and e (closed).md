**Labels:**

hold

reviewed



<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 01:51:30_
_Originally opened as: project-topaz/topaz - Issue 1101_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Tested abilities on the deoffset abilities. recreated sql to have offset. more information is in the deoffset list which i have saved for when ever that is pushed to branches. I have tested these in game only issues ive come across are with a few of the animations. May want to create or pull into a testing branch incase my server missed something.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 03:36:40_

----

A couple of these scripts have improper indentation, the ones I see right now are this one and asylum.lua


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 03:38:16_

----

Minor inconsistency in the comments: description is on the same line as the effect name.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 03:40:11_

----

Several of the scripts have ( )s around "if" conditional statements that need to be purged.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 03:43:19_

----

typo


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 03:48:20_

----

i didn't actually check if these all match up to an ability/effect you added, but adding this to the database without the appropriate script will cause it to show up in the player's skill list, but do nothing when activated


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 03:55:16_

----

style issue


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 04:00:48_

----

mjob called once in this script, it can likely be removed and this if check replaced with 
``if player:getMainJob() == 19 then``


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 14:07:55_

----

removed this


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 14:10:57_

----

fixed style issue


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 14:14:15_

----

fixed typo


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 14:17:20_

----

purged extra ( )


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 14:19:10_

----

removed note from descrip


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 14:21:54_

----

reformatted indentation


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 14:27:30_

----

Commited out immanence, I did not script it thanks for the find!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Sep 12, 2020 at 20:15:01_

----

there is no job ID 83 (and we'd use the human readable name from status.lua anyway) so what is the intent here?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Sep 12, 2020 at 20:18:17_

----

Not `== 19` never use the number.

Use `== tpz.job.DNC` instead see https://github.com/project-topaz/topaz/blob/release/scripts/globals/status.lua#L54 for further info


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 21:58:06_

----

Oh Man was I so dumb this morning looking at this I was tryin to rush n not really look... lol .... sorry will fix when I’m back at the pc

alright all set used tpz.job.DNC


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 22:00:28_

----

I was in a rush this morning and wasn’t really thinking as I put the number for the job n dumb me was thinking about what lvl it unlocked at... will fix in a little bit.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:24:47_

----

I feel like this can be cleaned up, since:
```lua
    EFFECT_FINISHING_MOVE_1         = 381,
    EFFECT_FINISHING_MOVE_2         = 382,
    EFFECT_FINISHING_MOVE_3         = 383,
    EFFECT_FINISHING_MOVE_4         = 384,
    EFFECT_FINISHING_MOVE_5         = 385,
```
We can
```lua
for move = tpz.effect.FINISHING_MOVE_1, tpz.effect.FINISHING_MOVE_5 do
    player:delStatusEffect(move )
    player:addStatusEffect(tpz.effect.CLIMACTIC_FLOURISH, 3, 0, 60, 0, player:getMerit(tpz.merit.CLIMACTIC_FLOURISH_EFFECT))
end
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:26:49_

----

Can you add whatever this base message is to `tpz.msg.basic` please? I've seen this used elsewhere like this: `ability:setMsg(tpz.msg.basic.DOUBLEUP_BUST)`


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:27:58_

----

I don't think an automated tool will handle this sort of thing, but simple logic statements can just be `if condition then` without any additional parens


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:28:33_

----

I didn't know we could check like this, nice!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:31:08_

----

(I've never played DNC, so I don't know the specifics)

There is a lot of repetition with all of this DNC stuff, is there anything logical we can take advantage of?
Loopifying things, breaking out early wherever possible, (nuclear option) a bunch of status_type or grouping flags so we can hand off this repetition to core etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:31:25_

----

Sneaky tab


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:32:47_

----

I've never dug into damage calcs, @59blargedy could you focus in on this when you get time?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:33:34_

----

Titles please


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Sunday Sep 13, 2020 at 17:07:08_

----

Just to throw this out there, I took a different jump lua and edited it, I believe the edit was just to shed the right amount of enmity.


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Sunday Sep 13, 2020 at 17:09:33_

----

So I looked thru older stuff and all seems basically the same. I wish I knew a way to get it to look neater but everything I’ve tried other than the way it is hasn’t worked or didn’t take away/add the right amount of steps or daze/effect 


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Sunday Sep 13, 2020 at 23:04:45_

----

alright I set it up like that


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Sunday Sep 13, 2020 at 23:06:24_

----

took care of it and went thru others to make sure no more sneaky tabs showed up


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Sunday Sep 13, 2020 at 23:07:10_

----

got all the missing titles in there


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Sunday Sep 13, 2020 at 23:17:27_

----

So I'm going to sound dumb here but I have no idea how to add something like setMsg(tpz.msg.basic.DOUBLEUP_BUST) >_>`'


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Monday Sep 14, 2020 at 00:33:35_

----

took care of this among others


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Sep 14, 2020 at 00:53:09_

----

should be delmod matching the addmod above, not a 2nd addmod with a negative amount


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Sep 14, 2020 at 00:53:51_

----

delmod with 100, not addmod -100

admod and delmod belong paired


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Monday Sep 14, 2020 at 18:22:37_

----

changed to delmod 100 not addmod -100


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Monday Sep 14, 2020 at 18:24:05_

----

changed to delmod 100 not addmod -100


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 03:36:40_

----

A couple of these scripts have improper indentation, the ones I see right now are this one and asylum.lua


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 03:38:16_

----

Minor inconsistency in the comments: description is on the same line as the effect name.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 03:40:11_

----

Several of the scripts have ( )s around "if" conditional statements that need to be purged.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 03:43:19_

----

typo


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 03:48:20_

----

i didn't actually check if these all match up to an ability/effect you added, but adding this to the database without the appropriate script will cause it to show up in the player's skill list, but do nothing when activated


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 03:55:16_

----

style issue


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 04:00:48_

----

mjob called once in this script, it can likely be removed and this if check replaced with 
``if player:getMainJob() == 19 then``


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 14:07:55_

----

removed this


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 14:10:57_

----

fixed style issue


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 14:14:15_

----

fixed typo


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 14:17:20_

----

purged extra ( )


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 14:19:10_

----

removed note from descrip


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 14:21:54_

----

reformatted indentation


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 14:27:30_

----

Commited out immanence, I did not script it thanks for the find!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Sep 12, 2020 at 20:15:01_

----

there is no job ID 83 (and we'd use the human readable name from status.lua anyway) so what is the intent here?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Saturday Sep 12, 2020 at 20:18:17_

----

Not `== 19` never use the number.

Use `== tpz.job.DNC` instead see https://github.com/project-topaz/topaz/blob/release/scripts/globals/status.lua#L54 for further info


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 21:58:06_

----

Oh Man was I so dumb this morning looking at this I was tryin to rush n not really look... lol .... sorry will fix when I’m back at the pc

alright all set used tpz.job.DNC


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Saturday Sep 12, 2020 at 22:00:28_

----

I was in a rush this morning and wasn’t really thinking as I put the number for the job n dumb me was thinking about what lvl it unlocked at... will fix in a little bit.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:24:47_

----

I feel like this can be cleaned up, since:
```lua
    EFFECT_FINISHING_MOVE_1         = 381,
    EFFECT_FINISHING_MOVE_2         = 382,
    EFFECT_FINISHING_MOVE_3         = 383,
    EFFECT_FINISHING_MOVE_4         = 384,
    EFFECT_FINISHING_MOVE_5         = 385,
```
We can
```lua
for move = tpz.effect.FINISHING_MOVE_1, tpz.effect.FINISHING_MOVE_5 do
    player:delStatusEffect(move )
    player:addStatusEffect(tpz.effect.CLIMACTIC_FLOURISH, 3, 0, 60, 0, player:getMerit(tpz.merit.CLIMACTIC_FLOURISH_EFFECT))
end
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:26:49_

----

Can you add whatever this base message is to `tpz.msg.basic` please? I've seen this used elsewhere like this: `ability:setMsg(tpz.msg.basic.DOUBLEUP_BUST)`


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:27:58_

----

I don't think an automated tool will handle this sort of thing, but simple logic statements can just be `if condition then` without any additional parens


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:28:33_

----

I didn't know we could check like this, nice!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:31:08_

----

(I've never played DNC, so I don't know the specifics)

There is a lot of repetition with all of this DNC stuff, is there anything logical we can take advantage of?
Loopifying things, breaking out early wherever possible, (nuclear option) a bunch of status_type or grouping flags so we can hand off this repetition to core etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:31:25_

----

Sneaky tab


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:32:47_

----

I've never dug into damage calcs, @59blargedy could you focus in on this when you get time?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:33:34_

----

Titles please


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Sunday Sep 13, 2020 at 17:07:08_

----

Just to throw this out there, I took a different jump lua and edited it, I believe the edit was just to shed the right amount of enmity.


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Sunday Sep 13, 2020 at 17:09:33_

----

So I looked thru older stuff and all seems basically the same. I wish I knew a way to get it to look neater but everything I’ve tried other than the way it is hasn’t worked or didn’t take away/add the right amount of steps or daze/effect 


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Sunday Sep 13, 2020 at 23:04:45_

----

alright I set it up like that


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Sunday Sep 13, 2020 at 23:06:24_

----

took care of it and went thru others to make sure no more sneaky tabs showed up


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Sunday Sep 13, 2020 at 23:07:10_

----

got all the missing titles in there


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Sunday Sep 13, 2020 at 23:17:27_

----

So I'm going to sound dumb here but I have no idea how to add something like setMsg(tpz.msg.basic.DOUBLEUP_BUST) >_>`'


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Monday Sep 14, 2020 at 00:33:35_

----

took care of this among others


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Sep 14, 2020 at 00:53:09_

----

should be delmod matching the addmod above, not a 2nd addmod with a negative amount


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Sep 14, 2020 at 00:53:51_

----

delmod with 100, not addmod -100

admod and delmod belong paired


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Monday Sep 14, 2020 at 18:22:37_

----

changed to delmod 100 not addmod -100


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Monday Sep 14, 2020 at 18:24:05_

----

changed to delmod 100 not addmod -100


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 12, 2020 at 20:29:06_

----

I'm gonna put a hold tag on this until I can sit down and give this a really thorough review. This is good stuff, there's just loads of it. 


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 12, 2020 at 23:08:33_

----

I spent 30 minutes looking over this PR last night and I barely feel I've scratched the surface lol


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Sep 13, 2020 at 06:15:29_

----

Specifically _because_ this is such a massive PR, I would ask you to set up your editor to honour our editorconfig file (https://github.com/project-topaz/topaz/blob/release/.editorconfig).

If you're like me and you edit your Lua in VSCode, `Lua Helper` formats everything nicely (I'm not sure if it's using the editorconfig file, but the output looks good).

This'll handle: spacing out args, newline at end of file, indentation, etc. etc. etc.

I'm not gonna comment on style until you've ran a tool over everything, because I'm a human and I'll let mistakes through!


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Sunday Sep 13, 2020 at 17:01:18_

----

I grabbed a styling tool and ran it over all my changes. Looks good now thanks, I had no idea there was one and it makes life much easier!

I still need to check everywhere for extra sets of parens where they aren't needed.

I checked all of the comments at the top and adjusted where necessary.

I don't really like DNC part either I went thru what was already scripted for flourish n step abilities to get them to do what they should. They test ok in game just still trying to get animations found.


----
<a href="https://github.com/illzbee"><img src="https://avatars3.githubusercontent.com/u/65986311?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [illzbee](https://github.com/illzbee)**
_Sunday Sep 13, 2020 at 23:12:27_

----

I think I took care of all the extra sets of parens where they aren't needed


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Tuesday Sep 15, 2020 at 06:13:44_

----

Thanks for all your hard work tidying this up! I promise I'll sit down this weekend and in-depth review everything 👍 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Sep 19, 2020 at 12:21:43_

----

I've sat down and done about 5 partial reviews of this this week, and I think it's totally fair to drop this into a feature branch and into canary since it's 99.9% additive. It isn't going to break anything that wasn't already broken 👍 

Thanks for the gargantuan effort!
