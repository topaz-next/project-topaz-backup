**Labels:**

reviewed



<a href="https://github.com/Nireya"><img src="https://avatars2.githubusercontent.com/u/17558211?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Nireya](https://github.com/Nireya)**
_Sunday Aug 30, 2020 at 19:01:02_
_Originally opened as: project-topaz/topaz - Issue 1043_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Previously this ability was wiping all shadows if the mob classified as an NM but that's not how it should work. Time Extensions also classify as "Notorious Monsters" so they were wiping all shadows with their Seismostomps. This fix corrects this and makes Seismostomp absorb either 1 or 2 shadows as shown in the video evidence below.

https://ffxiclopedia.fandom.com/wiki/Category:Simulacra
![Screenshot_184](https://user-images.githubusercontent.com/17558211/91667269-4d0d4080-ead1-11ea-84bb-00becb5b7239.png)

https://www.bg-wiki.com/bg/Mu%27Sha_Effigy
"Advisable for DDs to sub nin to absorb Seismostomp with Utsusemi as back to back use of this move can result in death" is on
most of the Dynamis statue NM pages. As well as the NM fought in the video evidence below.

Source video to show it absorbs 1-2 shadows randomly (watch the battle mod log with the NIN tank's shadows):
https://youtu.be/gEyhDflh_2g?t=1517

Thanks to Tankfest for help with this.







----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Sep 02, 2020 at 05:48:31_

----

Code looks good, I would maybe have left the shadows var so it's clear what's being passed into the damage calculation, but the end result is the same.

I'll let another staff look this over and confirm its OK

**EDIT:**

My point being is that it's much clearer to lay things out like this, even if it's a little redundant:
```lua
local shadows_removed = math.random(2)
local dmg = MobFinalAdjustments(info.dmg, mob, skill, target, tpz.attackType.PHYSICAL, tpz.damageType.BLUNT, shadows_removed)
```


----
<a href="https://github.com/Nireya"><img src="https://avatars2.githubusercontent.com/u/17558211?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Nireya](https://github.com/Nireya)**
_Thursday Sep 03, 2020 at 18:20:13_

----

I agree with you zach. I'll likely be looking over other mob abilities in the future and rewriting their shadow behavior to be more retail accurate like this one is now.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Sep 04, 2020 at 11:55:14_

----

> 
> 
> Code looks good, I would maybe have left the shadows var so it's clear what's being passed into the damage calculation, but the end result is the same.
> 
> I'll let another staff look this over and confirm its OK
> 
> **EDIT:**
> 
> My point being is that it's much clearer to lay things out like this, even if it's a little redundant:
> 
> ```lua
> local shadows_removed = math.random(2)
> local dmg = MobFinalAdjustments(info.dmg, mob, skill, target, tpz.attackType.PHYSICAL, tpz.damageType.BLUNT, shadows_removed)
> ```

@zach2good that was almost what I initially suggested before seeing the global variables for the shadows were literally just 1 and 2 and thought "if I say to do that someone is just going to go 'we don't need a variable for that why even do that Teo' "
which happens pretty much everytime I use a variable like that in chat on discord in my [example scripts](https://discordapp.com/channels/639659267003252746/639670779386134548/745785506633220216)




----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Saturday Sep 05, 2020 at 00:51:50_

----

> 
> 
> Code looks good, I would maybe have left the shadows var so it's clear what's being passed into the damage calculation, but the end result is the same.
> 
> I'll let another staff look this over and confirm its OK
> 
> **EDIT:**
> 
> My point being is that it's much clearer to lay things out like this, even if it's a little redundant:
> 
> ```lua
> local shadows_removed = math.random(2)
> local dmg = MobFinalAdjustments(info.dmg, mob, skill, target, tpz.attackType.PHYSICAL, tpz.damageType.BLUNT, shadows_removed)
> ```

"Hey that's something everyone can enjoy!"
