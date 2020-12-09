**Labels:**

approved

exploit

reviewed



<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [ibm2431](https://github.com/ibm2431)**
_Wednesday Oct 21, 2020 at 02:34:59_
_Originally opened as: project-topaz/topaz - Issue 1402_

----

⚠️ **Highly recommended reading: http://wiki.project-topaz.com/Spatial-Orientation-and-Relative-Positions**

^ No really, you don't stand a chance of understanding the changes in this PR until you have~!

Currently, everything relating to positions will encounter issues at Rotation 0 (due East). This all stems from one [little lie told in the documentation for `getangle`](https://github.com/project-topaz/topaz/blob/37e22e0e9f648043e55158716c52631dde4f376a/src/map/lua/lua_baseentity.cpp#L2384-L2402):
```cpp
*  Function: getAngle()
*  Purpose : Returns the angle between two entities relative to front
*  Example : player:getAngle(target)
*  Notes   : 0 degrees front; 180 behind
```
That is [not what getAngle did at all](https://github.com/project-topaz/topaz/blob/37e22e0e9f648043e55158716c52631dde4f376a/src/common/utils.cpp#L140-L145).

What `getangle` was returning was the "world angle" between two entities - _not_ a facing angle. It was also using a different scale than advertised. This leads to some problems:
![current_function](https://user-images.githubusercontent.com/13112942/96661875-a9a41380-133c-11eb-9fbd-596555d5ed20.png)

We also had places which weren't even using getangle - [but instead subtracting two raw rotations from each other - **which caused them to suffer from the "rotation overflow" problem** above](https://github.com/project-topaz/topaz/blob/37e22e0e9f648043e55158716c52631dde4f376a/src/map/utils/battleutils.cpp#L2272-L2274).
```
Entity A: Rotation 255 (East), Entity B: Rotation 1 (East)
255 - 1 = 254, which isn't less than 64
```
(**Note**: This was reported in https://github.com/DarkstarProject/darkstar/issues/6415)

Naturally, this is all very no bueno. So I made `getangle` into the more specific `getWorldAngle`, which serves the same functional purpose that `getangle` _actually did_. As a nice bonus I threw in, it now lets you optionally pass in a custom number of degrees to scale to, provided that they're a multiple of 4.

**BOLD FOR EMPHASIS: You can now get the world angle between two entities on a custom scale. 4 = NESW, 8 adds NE, SE, SW, and SE. Increase for additional cardinal axis. This means _you_, Ballista Rooks, VWNMs, and [Geomancer](https://github.com/project-topaz/topaz/pull/723#discussion_r443180935)!**

Afterwards I added `getFacingAngle` to do what the previous `getangle` _advertised_, and several positioning arc functions like `isInfront`, `isBeside`, and `isBehind`. Each of the positioning functions can take a custom angle (_always 256 scaled_), but will otherwise use a default of 64 (equivalent to 90 degrees on "360 scale").

**So then came changes to conal attacks**. Wikis claim that damage drops from the center line of the cone. So I wrote a new lua utility function to handle that. It takes a "minimum percentage" argument, which is, well, **the minimum damage you'll take if you're hit with that breath attack at its farthest end. The closer you are to the damage line of the attack, the closer you'll get to taking the passed-in max damage**.

I couldn't find any sources on how this "damage reduction if you're farther away" is calculated. I'm a skeptic, so at the moment I'm not convinced it's real. So **I set all dragon breath attacks to have a minimum percentage of 90%** because I'd rather damage be overtuned than undertuned! _Normally_ in this circumstance I'd keep it at 100%, but I wanted to illustrate that the damage adjustment function works and how. Servers can set each breath's minimum percentages to their taste.

Due to what has been ingrained in all of us - "stand on the paws" - there were some questions to how these breaths worked. _Why_ are we standing on the paws? Do we dodge damage? Do we reduce damage? Hopefully by now everyone knows the **dangers of myths**. @zach2good and @UynGH did a video test on retail, and they produced this one beautiful image which shows a lot.
![breath3](https://user-images.githubusercontent.com/13112942/96663970-53859f00-1341-11eb-8d51-7b32b38a1acf.jpg)
That's Nyu, who had hate, getting hit with Dragon Breath while almost 90 degrees ("360 scale") to Fafnir's right. You can see it targeting _him_ in Zach's log, _and_ Nyu _being on fire_ from the animation. Also notice that Zach _wasn't_ hit.

**Dragon Breath can be used on someone so long as they're within the front 180 degrees ("360 scale") of the mob.** ~~Additional targets are based on the conal fan from the _primary_ target - not the mob's face. This [matches a TODO in targetfind's findWithinCone](https://github.com/project-topaz/topaz/blob/37e22e0e9f648043e55158716c52631dde4f376a/src/map/ai/helpers/targetfind.cpp#L168-L174).~~

(There is a video of this, but I won't publicly link it here. You might be able to ask Zach on Discord if you don't believe me.)

~~With the help of a new additional utility function (`relativeAngle`), **targets are now hit based on the primary target** instead of where the mob is facing.~~

(**Edit:** See later comments; I reverted the above back to additional targets from the mob's face.)

[This presented a problem for breath damage reduction, which will need to be solved later](https://github.com/ibm2431/topaz/blob/0bd3bad899d48dfb4d2785d331bbc36d073f707f/scripts/globals/utils.lua#L106-L111). It'd require a pretty massive restructuring of how mob skills work. When targets get hit with a skill, the lua script is executed individually on each one, with no methods of storing arbitrary data about what the skill did to others - like the primary target's world angle. **So while the targets hit are correctly selected, the "center damage line" used for breath damage reduction is unfortunately still the mob's face**. Keep this in mind when adjusting minimum damage percentages.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Oct 21, 2020 at 04:25:09_

----

![image](https://user-images.githubusercontent.com/1389729/96673161-8abe7500-136e-11eb-8ae1-63649e59a08d.png)



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Oct 21, 2020 at 05:24:44_

----

>(feel free to post the video on the PR)

Hitting target at almost 90 degrees to the right ("360 scale"):
https://www.youtube.com/watch?v=j8m3xFQXQFo&t=2m35s

Exact cone angle (two Dragon Breaths back-to-back):
https://www.youtube.com/watch?v=j8m3xFQXQFo&t=15m52s


----
<a href="https://github.com/InoUno"><img src="https://avatars3.githubusercontent.com/u/774909?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [InoUno](https://github.com/InoUno)**
_Wednesday Oct 21, 2020 at 05:33:20_

----

Nice stuff!
I also started looking into fixing conal attacks some time ago, since they are all kinds of wrong in DSP/topaz. I had to prioritize other things though, so I had to drop it for a while, but I did manage to gather a bunch of retail evidence before that. I'll gladly share my notes and findings, since you guys are looking into it now too.

> Additional targets are based on the conal fan from the primary target - not the mob's face.

I'm not sure if this is different for each type of breath attack, or maybe it's a difference based on if it's a mob conal vs a player conal, but I tested this extensively with BLU spells, and found that the cone **does** have its center at the face of the caster -- not the primary target like you have concluded. I'd love to compare notes and go through the data together!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Oct 21, 2020 at 05:38:23_

----

Looking like we'll have to define and use flags to determine the center of a cone~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Oct 21, 2020 at 07:14:08_

----

After talking it over with Ino a bit (and seeing a very illuminating video), I've set conal centers back to be mob facing. They'll **still hit off-face primary targets** like in the Fafnir video, but **additional targets will treat the mob's rotation as the center**.

More Fafnir testing may be in the future.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 00:16:28_

----

I wanted to open this as a Pull Request to have more eyes on checking it. But what I haven't mentioned until now is that the explicit purpose of this rework was initially to resolve an exploit in which players could cause HNM wyrms to deal almost no damage from breaths.

According to wikis, breath attacks are supposed to deal less damage depending on the target's distance from the center of the cone. These breaths were previously implemented like so:
```lua
    local angle = mob:getAngle(target)

    angle = mob:getRotPos() - angle
    dmgmod = dmgmod * ((128-math.abs(angle))/128)
    dmgmod = utils.clamp(dmgmod, 50, 1600)
```

Let's take a step though this, referencing [the image on the old getangle above](https://user-images.githubusercontent.com/13112942/96661875-a9a41380-133c-11eb-9fbd-596555d5ed20.png).

[Remember that rotations start at 0 and wrap around back to zero at 255, going clockwise.](http://wiki.project-topaz.com/Spatial-Orientation-and-Relative-Positions) So let's say that you're fighting Fafnir, and knowing this exploit, you cause Fafnir to face roughly due E (rotation zero). This can be precisely rotation zero, but for safety you can have it be a little south, so let's say rotation 1. If you then stand slightly north of due east, relative to Fafnir, you'll be at angle 255, since the return of `getangle` was absolutely world aligned instead of facing aligned.

Fafnir is facing 1, you're at 255.
1 - 255 = 254. Congratulations, you're 254 degrees away from Fafnir's damage source!
damage = damage * ((128 - 254)/128)
damage = damage * -0.98

Well, that's bad. Fafnir is going to be _healing_ you for just about the full amount of damage it's trying to do!

We're "saved" by the clamp though:
`utils.clamp(dmgmod, 50, 1600)`

So instead of outright healing you - and being a much more obvious bug - Dragon Breath instead does only 50 damage. I know players encourage Dragon Breaths instead of Spike Flails, but this isn't _quite_ the reason why. 😉

Public server operators should have been informed that this was an exploit fix. If you're a public server operator who didn't know this comment was coming, get in touch with either zach2good or myself on Discord.
