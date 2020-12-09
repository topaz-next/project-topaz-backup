**Labels:**

reviewed



<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [NassirAlawar](https://github.com/NassirAlawar)**
_Thursday Oct 22, 2020 at 05:10:46_
_Originally opened as: project-topaz/topaz - Issue 1407_

----

Too much changed to go into detail here. I have summarized changes in each commit and my code is packed full of comments and links to references and research.

Super short summary: 
Updated battleutils and summon.lua with equations for pDIF, fSTR, Hit Rate, Level Correction.
I have updated the base weapon computation for avatars.
I have updated how crit rate from dex works.
Level correction is not computed for newer zones/content since the release of SoA.
Some minor bug fixes.

Note: I have not updated the BP damage equations and plan to tackle those in the future, likely one avatar per PR or maybe even one BP per PR.

Note: I have not added the Damage Limit+ trait or "Physical Damage +%" to the computations as I do not believe the project supports them yet. I have noted how they were and where they need to be added once they are implemented.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 22, 2020 at 09:49:05_

----

No need for double line breaks here


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 22, 2020 at 09:52:18_

----

This cast can still produce `nullptr`, which will get used by `targ_weapon->isTwoHanded();` later, you can change that to:
`bool isTwoHanded = targ_weapon && targ_weapon->isTwoHanded();` to make it safe


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 22, 2020 at 09:54:05_

----

Floats should be marked as `0.0f` or else they'll be created as doubles and then converted. I'm sure the compiler probably handles this, but better to be clear


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 22, 2020 at 09:55:09_

----

Same here, you're going to be using `targ_weapon` later and there isn't a guarantee that it'll be populated, so either bail all of those checks if this is nullptr or put a nullptr check inline with each of those down below


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 22, 2020 at 09:56:05_

----

Can be changed to:
```cpp
if (CPetEntity* petEntity = dynamic_cast<CPetEntity*>(PAttacker))
{
    ...
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 22, 2020 at 09:57:18_

----

petEntity can be nullptr here
```cpp
if (CPetEntity* petEntity = dynamic_cast<CPetEntity*>(PAttacker))
{
    isAvatar = petEntity->getPetType() == PETTYPE_AVATAR;
}
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 22, 2020 at 09:57:44_

----

Use `static_cast` instead of C-Style casts please


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Oct 22, 2020 at 14:33:32_

----

[Should throw in the source for this](https://www.bg-wiki.com/bg/PDIF#Level_Correction_Function_.28cRatio.29), because I was gearing up to fight it. 😉 

Although we should probably be setting up and using a new zone flag instead of checking hardcoded zone IDs.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Oct 22, 2020 at 14:59:22_

----

Let's give/use a mod for the Crit Bonus via trait~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Oct 22, 2020 at 15:08:42_

----

Problem with the `finaldmg < targetHP` check is that `AvatarPhysicalMove` is called _before_ defense adjustments for the defender `AvatarFinalAdjustments`, which can cause these cycles to break out early under the assumption the mob will be dead.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Oct 22, 2020 at 15:12:26_

----

I know this was here before, but waking up targets is now baked into lua_baseentity:takeDamage(); you can remove it from the raw damage calculation step.


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Thursday Oct 22, 2020 at 15:48:54_

----

Oh interesting okay, maybe down the road we need a final display damage and an internal total damage. Good catch 👍 


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Thursday Oct 22, 2020 at 15:54:34_

----

lol sure I'll add it, I left out the link because I'd been linking to pDIF so often. I thought I was safe!
I would agree with a zone flag, the first place I looked was the DB to see if there was any flag per expansion and or anything else I could use. Luckily they're all clumped together except for Legion A


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Thursday Oct 22, 2020 at 15:55:35_

----

Sure, I'll look into doing that


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 22, 2020 at 09:49:05_

----

No need for double line breaks here


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 22, 2020 at 09:52:18_

----

This cast can still produce `nullptr`, which will get used by `targ_weapon->isTwoHanded();` later, you can change that to:
`bool isTwoHanded = targ_weapon && targ_weapon->isTwoHanded();` to make it safe


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 22, 2020 at 09:54:05_

----

Floats should be marked as `0.0f` or else they'll be created as doubles and then converted. I'm sure the compiler probably handles this, but better to be clear


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 22, 2020 at 09:55:09_

----

Same here, you're going to be using `targ_weapon` later and there isn't a guarantee that it'll be populated, so either bail all of those checks if this is nullptr or put a nullptr check inline with each of those down below


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 22, 2020 at 09:56:05_

----

Can be changed to:
```cpp
if (CPetEntity* petEntity = dynamic_cast<CPetEntity*>(PAttacker))
{
    ...
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 22, 2020 at 09:57:18_

----

petEntity can be nullptr here
```cpp
if (CPetEntity* petEntity = dynamic_cast<CPetEntity*>(PAttacker))
{
    isAvatar = petEntity->getPetType() == PETTYPE_AVATAR;
}
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Oct 22, 2020 at 09:57:44_

----

Use `static_cast` instead of C-Style casts please


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Oct 22, 2020 at 14:33:32_

----

[Should throw in the source for this](https://www.bg-wiki.com/bg/PDIF#Level_Correction_Function_.28cRatio.29), because I was gearing up to fight it. 😉 

Although we should probably be setting up and using a new zone flag instead of checking hardcoded zone IDs.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Oct 22, 2020 at 14:59:22_

----

Let's give/use a mod for the Crit Bonus via trait~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Oct 22, 2020 at 15:08:42_

----

Problem with the `finaldmg < targetHP` check is that `AvatarPhysicalMove` is called _before_ defense adjustments for the defender `AvatarFinalAdjustments`, which can cause these cycles to break out early under the assumption the mob will be dead.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Oct 22, 2020 at 15:12:26_

----

I know this was here before, but waking up targets is now baked into lua_baseentity:takeDamage(); you can remove it from the raw damage calculation step.


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Thursday Oct 22, 2020 at 15:48:54_

----

Oh interesting okay, maybe down the road we need a final display damage and an internal total damage. Good catch 👍 


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Thursday Oct 22, 2020 at 15:54:34_

----

lol sure I'll add it, I left out the link because I'd been linking to pDIF so often. I thought I was safe!
I would agree with a zone flag, the first place I looked was the DB to see if there was any flag per expansion and or anything else I could use. Luckily they're all clumped together except for Legion A


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Thursday Oct 22, 2020 at 15:55:35_

----

Sure, I'll look into doing that


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Oct 22, 2020 at 11:30:02_

----

> And maybe an excuse to introduce a new rule:
In lua you're leaving a space after starting a comment: -- Comment
Can you do the same with C++: // Comment instead of //Comment

new? that was always a rule. I know coz it was my rule before topaz happened. :stuck_out_tongue: 


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Thursday Oct 22, 2020 at 14:56:22_

----

Sure, I'll fix these today 👍 
Just to be clear on the thread name: "General combat calculation improvements for Avatars"
This will impact players as well, I started with the summon.lua but then that drifted into the general combat equations for the melee hits.


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Friday Oct 23, 2020 at 00:59:26_

----

I believe all the noted issues have been fixed and I have merged and retested


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Sunday Oct 25, 2020 at 04:27:05_

----

Just realized I forgot to implement the request to give avatars crit att bonus from db and get rid of the hard coding. Will try to get that done in a day or two


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Sunday Oct 25, 2020 at 18:41:24_

----

Changed the crit bonus to a modifier and added the modifier logic to summon.lua as well

I have retested and confirmed I see no issues. As always, let me know if there's anything else 👍 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Nov 12, 2020 at 06:07:32_

----

We were talking about this PR yesterday; Avatars will eventually need a full rewrite, but this lays out a well-researched framework for when that happens 👍 


----
<a href="https://github.com/NassirAlawar"><img src="https://avatars1.githubusercontent.com/u/22628472?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [NassirAlawar](https://github.com/NassirAlawar)**
_Thursday Nov 12, 2020 at 06:14:30_

----

Let me know if there's anything I can do to help regarding avatars or if there's anything you'd prefer to have prioritized. My next plan was to move onto blood pact equations including modifiers. I have been collecting some Pet: DEX+/STR+ gear for math stuff on retail.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Nov 12, 2020 at 06:23:03_

----

I honestly know nothing about combat balancing and rely on the others for sanity checking, but if you continue testing things and documenting your sources, we'll have all of that available when someone "fixes" avatars 👍 
