**Labels:**

WIP

hold



<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Omnione](https://github.com/Omnione)**
_Tuesday Apr 14, 2020 at 20:00:03_
_Originally opened as: project-topaz/topaz - Issue 494_

----

<!-- place 'x' mark between square [X] brackets to affirm: -->
**_I affirm:_**
- [X] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [X] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This PR adds the basic functions for geo, including the auras or bubbles as some like to call them.
only spells available are as follows:
• indi-regen
• indi-poison
• indi-refresh
• geo-regen
• geo-posion
• geo-refresh

Abilities:
• Full Circle returns a fraction of mp based on the intial cost of the geo spell and luopans remaing HP

This is a WIP so feel free to test and make changes accordingly.

Credit to zach2good for making this possible and to actually move ahead.

NOTE: the animations when casting will look odd untill the mID for the bells are added if they are not added already.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:51:16_

----

Please update with text and info for Full Circle


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:53:32_

----

Now would be a good time to make `tpz.allegiance = {}` in `status.lua` and use that here
https://github.com/project-topaz/topaz/blob/release/scripts/globals/status.lua#L2159

EDIT: Ah, they are available already! Please use those


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:54:19_

----

I feel like this should be done in Core


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:54:35_

----

This is sneaky, I like it


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:54:49_

----

Typo


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:55:26_

----

These prints can probably be removed now. I can only _assume_ this script will be needed for something later on.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:56:01_

----

Should this be one of the new messages? `LUOPAN_ALREADY_PLACED` etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:56:31_

----

This is probably fine for now, but it might be worth moving these calcs into the geo helper later on


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:57:49_

----

~~(Not for now, but)
I guess it must be possible to be under the effect of more than one aura right? So we'll have to jiggle some things around to allow that (later)~~

**EDIT:** I forgot that the aura is the thing that distributes the effect, so you can be under multiple effects, but probably only holding a single aura. Ignore me.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:59:29_

----

Still some leftovers from the GEO quest branch


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:59:49_

----

Leftovers from your RUN work?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 06:02:01_

----

I think these are OK for now given the scope of this PR, but afterwards, it would be good to make up some kind of utility that allows you to filter by allegiance, instead of this or my plan of iterating over all the spawn lists


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 06:03:18_

----

I don't remember if this is even used anymore, I think we discovered that the Luopan takes up the pet slot, so it can't be used with other pets (mobs, jugs, fellows, wyverns etc.). Probably best to check that though


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 06:04:14_

----

Would be good to uncomment/update/remove any break_if's where the conditions have changed


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 06:04:56_

----

We have some leftover tabs floating around here (probably from my poor copy-pasting), please replace with 4xspaces


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 06:06:00_

----

Please wrap up these conditions with braces:
```
if (condition)
{
... stuff
}
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 06:07:10_

----

This is the main chunk right here, anyone else reviewing: This is the bit that needs the most scrutiny, as this is the part that will affect performance. (Along with getAllInRange, but not that one so much)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 06:07:33_

----

Later we'll handle this better, but for now this is good


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 12:42:06_

----

This is gonna be changed in the next push i do and will get rid of all this.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 13:00:29_

----

Done ✔


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 13:01:50_

----

I'd like to aswell but not really sure the best way yet, ill look into it and update accordingly.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 13:02:56_

----

Done ✔


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 13:08:59_

----

This was a boo boo made by me testing early on, fixed now ✔


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 13:10:00_

----

All Done ✔


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:36:04_

----

reserved for a reason do not steal the ID!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:36:23_

----

look at the next line


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:36:32_

----

```sql

INSERT INTO `pet_list` VALUES (69, 'HarlequinFrame', 5124, 1, 99, 0, 0);
INSERT INTO `pet_list` VALUES (70, 'ValoredgeFrame', 5125, 1, 99, 0, 0);
INSERT INTO `pet_list` VALUES (71, 'SharpshotFrame', 5126, 1, 99, 0, 0);
INSERT INTO `pet_list` VALUES (72, 'StormwakerFrame', 5127, 1, 99, 0, 0);
-- INSERT INTO `pet_list` VALUES (73, 'AdventuringFellow', 0, 1, 99, 0, 0);
-- 74 is Chocobo in the enum..
```
like I've been saying for a long long time now, pet list core code needs changed to not rely on its size and just get the highest ID as the "top" of it so that gaps in the list do not cause issues. 73 was earmarked for the NPC fellow, but nobody commented it in the lua side of things.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:41:16_

----

should not even need any dummy effects to do this on the Geo. may -possibly- still need addStatusEffectEx to hide the icon if the loupan itself doesn't have one when targeted. The COLURE_ACTIVE status can hand out the status ID passed to it in its regular addStatusEffect() arguments (the only thing ex is adding is an argument for the icon separate from the actual status, allowing you to make any status say it is anything else-or- use zero for no icon).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:44:52_

----

It says you already have a pet if you try to cast an avatar, and very obviously uses the same placement for the loupans HP bar, so yeah.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:49:11_

----

unrelated to this PR but: at some point we need to see what exactly happens if we go above this max index the dat has - will the packet even support higher values? will the client use them if given?

We have limited real estate for user, and we have to make use of it cautiously, but we may have more headroom if we can exceed the 1023 "slots" allotted by the dat file.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:51:29_

----

>  will get rid of all this.

:+1: 
was gonna ask why you were checking the status instead of what spell cast it rode in on (which has an element you can switch case).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:53:21_

----

at no point will an NPC ever have a status effect. if its gaining effects, its not an npc, it is a mob (pets are also mobs)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:58:40_

----

while we're here lets take the opportunity to comment the arguments so we know both what the new one is and what the existing ones are.

@ibm2431 It may be worth doing what was done to `addItem()` and overloading a version that accepts a table. Unsure if that causes new problems on the arm64 build though (we should have somebody try the table version of `addItem()`.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 14:03:22_

----

Ah ok, will change this.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 14:05:57_

----

Yeah this was a mistake i made when i was doing some stupid things, ive changed it back now.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 14:07:23_

----

well now i dont need any of these so thats should help the situation some.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 14:08:39_

----

you are right, i dont need any of the effects now, they are all working off of the Colure now.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 14:23:39_

----

I'm going to use 75, i know it was set for trust, but as thats not needed anymore, this shouldnt be a problem, let me know if you feel this should be different.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 14:32:03_

----

I will start commenting these.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 14:39:35_

----

Oh i see why this was 73, its because of the debug break in petutils.cpp, it checks the size of the list, not if the id exsists, so if i set it as 75, it will cause a break, ok let me look into this, i may change this to how i did the trust checking.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 15:35:32_

----

Ok ive redone LoadPet to better handle gaps in petID's.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 17:31:21_

----

Ive had a good look round, i cant see any more and i fixed this one, let me know if you see any more.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 17:32:10_

----

Ok this is done ✔


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 18:16:25_

----

Done it is now in a nice gap, and set as 6040 ✔


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 18:17:06_

----

Set as 75 now


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:26:11_

----

This is done now


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:28:31_

----

It works, im not gonna doubt that, and its stable, tested lots and does the job


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:28:55_

----

lol


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:29:31_

----

yep fixed


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:30:02_

----

yep i agree, i have adjusted them to more retail values


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:31:15_

----

no idea lol, maybe?


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:34:12_

----

Oh i missed this one


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:36:52_

----

Meh tbh its going to be added anyway


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:42:27_

----

This is no longer an issue, you can only have one Colure aura active and ive updated the falgs so it overwrites and all that fun stuff.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:42:59_

----

done


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:46:39_

----

I think its safe to leave this in as its just a placeholder, i can remove it if requested


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:53:46_

----

I'll remove them once ive finnished testing some abilities.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 16, 2020 at 12:17:22_

----

Ok removed now


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 16, 2020 at 12:20:36_

----

ok i checked, this is already in release, so it shouldnt be an issue, i will change it to the release values.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 16, 2020 at 12:22:19_

----

I guess this can be looked at later on, as of right now it does a good job as is.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 16, 2020 at 12:22:38_

----

Removed now.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 08:34:49_

----

Handbell skill should only go up when a handbell is equipped~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 08:38:12_

----

There be tabs here~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 09:49:13_

----

You've got some excess parens going on here~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 09:50:37_

----

`or player:getPetID() ~= 73` if you would!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 09:51:57_

----

We may want to put notes on these effects that these are the copies/buffs used for geomancy (or potentially rename them from _II to _GEO if they're only used for geomancy, which I _believe_ they are)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 09:53:14_

----

Will this always be the correct message? Is it possible for someone with a weird job combination to have a different type of pet out?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 09:56:37_

----

Indenting a little off here 😅 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 10:06:46_

----

Does the amount of regen down change depending on the GEO's level?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 10:14:08_

----

This doesn't need to be done _now_, but the very next thing I'll want to see is a "reverse" enmity container/struct accessible from the entity object which tracks all the mob entities that a player has hate on. This will dramatically cut down on the number of mobs we loop through with distance checks, _and_ @zach2good can use it for trusts to determine if a player has enmity before summoning.

I'm thinking that when that happens, findAllInRange can take a list of potential targets, and then only checks the targets in that list and returns those in range. Auras can then pass in different lists depending on what they want to achieve. And in that case, the allegiance checks wouldn't be needed because tickAuras will already have an appropriate list to check; party members for player buff spheres, "reverse enmity all monsters that hate me" list for player debuffs, and "enmity container all players I hate" list for mob debuffs. I don't know if there's any mobs with buff spheres.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 10:16:18_

----

All these poor status effects~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 10:35:46_

----

What plans are there to use luopanentity that can't be achieved through petentity?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 03:18:46_

----

Hrm, uncertain if tickAuras should be its own function that re-steps through all status effects, or if aura logic should be baked into tickStatus. We can leave this as-is for now, but for _maximum performance_ we should try to reduce entire-list restepping on each tick.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 03:39:11_

----

But I thought addAllInRange was supposed to be doing the distance checks~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 04:06:32_

----

In this case, this is a luopan trying to bestow buff on their pt-less master, right?

I _believe_ that when a GEO dies, their luopan goes as well, _but_ I could be wrong. So I want to say there shouldn't be a case when a luopan is trying to bestow a buff on their dead master (but I suppose we could keep the check if there's any concern that might happen.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 04:11:44_

----

Could potentially save cycles by checking if the mob is dead _before_ we check entity type and ping the mob's enmity container. 😉 

Alternatively: addAllInRange shouldn't return dead entities at all, unless someone can make an argument for a use case where we'd need to be doing something with a pile of corpses.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 04:15:01_

----

Obviously "for later", but we'll want to revisit this to make it more generic so mobs can use it too


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 04:16:18_

----

When expanded so mobs can use auras, will there be problems with resetting their targetfind?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 06:01:17_

----

Those poor adventuring fellows! Denied their ID!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 06:05:33_

----

Is this actually the case (that a luopan's HP is the master's max HP), or was this done just for initial prototyping?

I'm not going to require a change (now) if not, I'd just be a surprised if that _is_ how it worked.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 06:07:56_

----

I'll admit I haven't _stared_ at luopan spawning on retail; do they actually vary in placement instead of being at the exact location of the target?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 06:14:16_

----

Geomancy power is a combination of both Geomancy skill _and_ Handbell skill if a handbell was used during casting of the spell. (Hence why subbing GEO is a bad idea, because only GEO can equip bells.)

I think what we'll want to do with these in the future is have a helper in `tpz.geo` that takes a caster and a skill cap, and returns: potency, geomancy+ total. The helper will handle getting and combining the appropriate skill levels, cap it off if necessary, and return the caster's applicable power and geomancy+ mod. Each individual spell script can then use that information to determine the power of their effects and spawn the bubble/luopan.

On the subject of Poison bubbles, bgwiki says it caps out at 30 dmg/tick if at 600 skill.
`(600 / 30) / 10 = 2`, which is either not right, or I'm missing something here~ 😅 

Also, do we _not_ have spell:getCost()? If not, we'll probably want to add one.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 06:26:26_

----

It seems this is off a little too, as `geo_skill / 20` does produce the stated 30 HP per tick at 600 power, but the further `/10` seems to reduce it down to 3.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 30, 2020 at 16:18:18_

----

They actually spawn just behind the target, i guess this is so you can still target the mob, because if the luopan is directly on the mob, its mesess with targeting.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 30, 2020 at 16:18:49_

----

dont worry, they will make a comeback lol.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 30, 2020 at 16:19:21_

----

This will be rectified in the next commit.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 30, 2020 at 16:20:30_

----

I also noticed that geo skill was being skilled up too, so it was actually skilling up twice.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday May 12, 2020 at 23:02:27_

----

HP was actually 1500 max at 99, luopan is capped at 99 also, you can increase the max hp but only through equipment.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday May 12, 2020 at 23:03:14_

----

this should be all good if you look at the table in geo.lua, all retail values.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday May 12, 2020 at 23:03:47_

----

All good now, potency should be calculated correctly for all spells.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday May 12, 2020 at 23:06:27_

----

apprently not, i know this is odd, im going to look into this more though as i feel it should.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday May 14, 2020 at 23:29:02_

----

none, so its gone poof


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday May 14, 2020 at 23:32:42_

----

This should be able to handle any type of mob or pet now


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday May 24, 2020 at 11:31:43_

----

going to need to change this to cover all elemental magic.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday May 24, 2020 at 11:32:12_

----

Same with this one, cover all elemental magic.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday May 24, 2020 at 11:32:29_

----

And here


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:51:16_

----

Please update with text and info for Full Circle


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:53:32_

----

Now would be a good time to make `tpz.allegiance = {}` in `status.lua` and use that here
https://github.com/project-topaz/topaz/blob/release/scripts/globals/status.lua#L2159

EDIT: Ah, they are available already! Please use those


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:54:19_

----

I feel like this should be done in Core


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:54:35_

----

This is sneaky, I like it


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:54:49_

----

Typo


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:55:26_

----

These prints can probably be removed now. I can only _assume_ this script will be needed for something later on.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:56:01_

----

Should this be one of the new messages? `LUOPAN_ALREADY_PLACED` etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:56:31_

----

This is probably fine for now, but it might be worth moving these calcs into the geo helper later on


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:57:49_

----

~~(Not for now, but)
I guess it must be possible to be under the effect of more than one aura right? So we'll have to jiggle some things around to allow that (later)~~

**EDIT:** I forgot that the aura is the thing that distributes the effect, so you can be under multiple effects, but probably only holding a single aura. Ignore me.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:59:29_

----

Still some leftovers from the GEO quest branch


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 05:59:49_

----

Leftovers from your RUN work?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 06:02:01_

----

I think these are OK for now given the scope of this PR, but afterwards, it would be good to make up some kind of utility that allows you to filter by allegiance, instead of this or my plan of iterating over all the spawn lists


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 06:03:18_

----

I don't remember if this is even used anymore, I think we discovered that the Luopan takes up the pet slot, so it can't be used with other pets (mobs, jugs, fellows, wyverns etc.). Probably best to check that though


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 06:04:14_

----

Would be good to uncomment/update/remove any break_if's where the conditions have changed


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 06:04:56_

----

We have some leftover tabs floating around here (probably from my poor copy-pasting), please replace with 4xspaces


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 06:06:00_

----

Please wrap up these conditions with braces:
```
if (condition)
{
... stuff
}
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 06:07:10_

----

This is the main chunk right here, anyone else reviewing: This is the bit that needs the most scrutiny, as this is the part that will affect performance. (Along with getAllInRange, but not that one so much)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Apr 15, 2020 at 06:07:33_

----

Later we'll handle this better, but for now this is good


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 12:42:06_

----

This is gonna be changed in the next push i do and will get rid of all this.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 13:00:29_

----

Done ✔


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 13:01:50_

----

I'd like to aswell but not really sure the best way yet, ill look into it and update accordingly.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 13:02:56_

----

Done ✔


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 13:08:59_

----

This was a boo boo made by me testing early on, fixed now ✔


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 13:10:00_

----

All Done ✔


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:36:04_

----

reserved for a reason do not steal the ID!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:36:23_

----

look at the next line


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:36:32_

----

```sql

INSERT INTO `pet_list` VALUES (69, 'HarlequinFrame', 5124, 1, 99, 0, 0);
INSERT INTO `pet_list` VALUES (70, 'ValoredgeFrame', 5125, 1, 99, 0, 0);
INSERT INTO `pet_list` VALUES (71, 'SharpshotFrame', 5126, 1, 99, 0, 0);
INSERT INTO `pet_list` VALUES (72, 'StormwakerFrame', 5127, 1, 99, 0, 0);
-- INSERT INTO `pet_list` VALUES (73, 'AdventuringFellow', 0, 1, 99, 0, 0);
-- 74 is Chocobo in the enum..
```
like I've been saying for a long long time now, pet list core code needs changed to not rely on its size and just get the highest ID as the "top" of it so that gaps in the list do not cause issues. 73 was earmarked for the NPC fellow, but nobody commented it in the lua side of things.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:41:16_

----

should not even need any dummy effects to do this on the Geo. may -possibly- still need addStatusEffectEx to hide the icon if the loupan itself doesn't have one when targeted. The COLURE_ACTIVE status can hand out the status ID passed to it in its regular addStatusEffect() arguments (the only thing ex is adding is an argument for the icon separate from the actual status, allowing you to make any status say it is anything else-or- use zero for no icon).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:44:52_

----

It says you already have a pet if you try to cast an avatar, and very obviously uses the same placement for the loupans HP bar, so yeah.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:49:11_

----

unrelated to this PR but: at some point we need to see what exactly happens if we go above this max index the dat has - will the packet even support higher values? will the client use them if given?

We have limited real estate for user, and we have to make use of it cautiously, but we may have more headroom if we can exceed the 1023 "slots" allotted by the dat file.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:51:29_

----

>  will get rid of all this.

:+1: 
was gonna ask why you were checking the status instead of what spell cast it rode in on (which has an element you can switch case).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:53:21_

----

at no point will an NPC ever have a status effect. if its gaining effects, its not an npc, it is a mob (pets are also mobs)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Apr 15, 2020 at 13:58:40_

----

while we're here lets take the opportunity to comment the arguments so we know both what the new one is and what the existing ones are.

@ibm2431 It may be worth doing what was done to `addItem()` and overloading a version that accepts a table. Unsure if that causes new problems on the arm64 build though (we should have somebody try the table version of `addItem()`.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 14:03:22_

----

Ah ok, will change this.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 14:05:57_

----

Yeah this was a mistake i made when i was doing some stupid things, ive changed it back now.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 14:07:23_

----

well now i dont need any of these so thats should help the situation some.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 14:08:39_

----

you are right, i dont need any of the effects now, they are all working off of the Colure now.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 14:23:39_

----

I'm going to use 75, i know it was set for trust, but as thats not needed anymore, this shouldnt be a problem, let me know if you feel this should be different.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 14:32:03_

----

I will start commenting these.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 14:39:35_

----

Oh i see why this was 73, its because of the debug break in petutils.cpp, it checks the size of the list, not if the id exsists, so if i set it as 75, it will cause a break, ok let me look into this, i may change this to how i did the trust checking.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 15:35:32_

----

Ok ive redone LoadPet to better handle gaps in petID's.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 17:31:21_

----

Ive had a good look round, i cant see any more and i fixed this one, let me know if you see any more.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 17:32:10_

----

Ok this is done ✔


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 18:16:25_

----

Done it is now in a nice gap, and set as 6040 ✔


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 18:17:06_

----

Set as 75 now


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:26:11_

----

This is done now


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:28:31_

----

It works, im not gonna doubt that, and its stable, tested lots and does the job


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:28:55_

----

lol


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:29:31_

----

yep fixed


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:30:02_

----

yep i agree, i have adjusted them to more retail values


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:31:15_

----

no idea lol, maybe?


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:34:12_

----

Oh i missed this one


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:36:52_

----

Meh tbh its going to be added anyway


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:42:27_

----

This is no longer an issue, you can only have one Colure aura active and ive updated the falgs so it overwrites and all that fun stuff.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:42:59_

----

done


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:46:39_

----

I think its safe to leave this in as its just a placeholder, i can remove it if requested


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 15, 2020 at 23:53:46_

----

I'll remove them once ive finnished testing some abilities.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 16, 2020 at 12:17:22_

----

Ok removed now


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 16, 2020 at 12:20:36_

----

ok i checked, this is already in release, so it shouldnt be an issue, i will change it to the release values.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 16, 2020 at 12:22:19_

----

I guess this can be looked at later on, as of right now it does a good job as is.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 16, 2020 at 12:22:38_

----

Removed now.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 08:34:49_

----

Handbell skill should only go up when a handbell is equipped~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 08:38:12_

----

There be tabs here~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 09:49:13_

----

You've got some excess parens going on here~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 09:50:37_

----

`or player:getPetID() ~= 73` if you would!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 09:51:57_

----

We may want to put notes on these effects that these are the copies/buffs used for geomancy (or potentially rename them from _II to _GEO if they're only used for geomancy, which I _believe_ they are)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 09:53:14_

----

Will this always be the correct message? Is it possible for someone with a weird job combination to have a different type of pet out?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 09:56:37_

----

Indenting a little off here 😅 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 10:06:46_

----

Does the amount of regen down change depending on the GEO's level?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 10:14:08_

----

This doesn't need to be done _now_, but the very next thing I'll want to see is a "reverse" enmity container/struct accessible from the entity object which tracks all the mob entities that a player has hate on. This will dramatically cut down on the number of mobs we loop through with distance checks, _and_ @zach2good can use it for trusts to determine if a player has enmity before summoning.

I'm thinking that when that happens, findAllInRange can take a list of potential targets, and then only checks the targets in that list and returns those in range. Auras can then pass in different lists depending on what they want to achieve. And in that case, the allegiance checks wouldn't be needed because tickAuras will already have an appropriate list to check; party members for player buff spheres, "reverse enmity all monsters that hate me" list for player debuffs, and "enmity container all players I hate" list for mob debuffs. I don't know if there's any mobs with buff spheres.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 10:16:18_

----

All these poor status effects~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Apr 28, 2020 at 10:35:46_

----

What plans are there to use luopanentity that can't be achieved through petentity?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 03:18:46_

----

Hrm, uncertain if tickAuras should be its own function that re-steps through all status effects, or if aura logic should be baked into tickStatus. We can leave this as-is for now, but for _maximum performance_ we should try to reduce entire-list restepping on each tick.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 03:39:11_

----

But I thought addAllInRange was supposed to be doing the distance checks~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 04:06:32_

----

In this case, this is a luopan trying to bestow buff on their pt-less master, right?

I _believe_ that when a GEO dies, their luopan goes as well, _but_ I could be wrong. So I want to say there shouldn't be a case when a luopan is trying to bestow a buff on their dead master (but I suppose we could keep the check if there's any concern that might happen.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 04:11:44_

----

Could potentially save cycles by checking if the mob is dead _before_ we check entity type and ping the mob's enmity container. 😉 

Alternatively: addAllInRange shouldn't return dead entities at all, unless someone can make an argument for a use case where we'd need to be doing something with a pile of corpses.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 04:15:01_

----

Obviously "for later", but we'll want to revisit this to make it more generic so mobs can use it too


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 04:16:18_

----

When expanded so mobs can use auras, will there be problems with resetting their targetfind?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 06:01:17_

----

Those poor adventuring fellows! Denied their ID!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 06:05:33_

----

Is this actually the case (that a luopan's HP is the master's max HP), or was this done just for initial prototyping?

I'm not going to require a change (now) if not, I'd just be a surprised if that _is_ how it worked.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 06:07:56_

----

I'll admit I haven't _stared_ at luopan spawning on retail; do they actually vary in placement instead of being at the exact location of the target?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 06:14:16_

----

Geomancy power is a combination of both Geomancy skill _and_ Handbell skill if a handbell was used during casting of the spell. (Hence why subbing GEO is a bad idea, because only GEO can equip bells.)

I think what we'll want to do with these in the future is have a helper in `tpz.geo` that takes a caster and a skill cap, and returns: potency, geomancy+ total. The helper will handle getting and combining the appropriate skill levels, cap it off if necessary, and return the caster's applicable power and geomancy+ mod. Each individual spell script can then use that information to determine the power of their effects and spawn the bubble/luopan.

On the subject of Poison bubbles, bgwiki says it caps out at 30 dmg/tick if at 600 skill.
`(600 / 30) / 10 = 2`, which is either not right, or I'm missing something here~ 😅 

Also, do we _not_ have spell:getCost()? If not, we'll probably want to add one.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 06:26:26_

----

It seems this is off a little too, as `geo_skill / 20` does produce the stated 30 HP per tick at 600 power, but the further `/10` seems to reduce it down to 3.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 30, 2020 at 16:18:18_

----

They actually spawn just behind the target, i guess this is so you can still target the mob, because if the luopan is directly on the mob, its mesess with targeting.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 30, 2020 at 16:18:49_

----

dont worry, they will make a comeback lol.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 30, 2020 at 16:19:21_

----

This will be rectified in the next commit.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 30, 2020 at 16:20:30_

----

I also noticed that geo skill was being skilled up too, so it was actually skilling up twice.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday May 12, 2020 at 23:02:27_

----

HP was actually 1500 max at 99, luopan is capped at 99 also, you can increase the max hp but only through equipment.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday May 12, 2020 at 23:03:14_

----

this should be all good if you look at the table in geo.lua, all retail values.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday May 12, 2020 at 23:03:47_

----

All good now, potency should be calculated correctly for all spells.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday May 12, 2020 at 23:06:27_

----

apprently not, i know this is odd, im going to look into this more though as i feel it should.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday May 14, 2020 at 23:29:02_

----

none, so its gone poof


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday May 14, 2020 at 23:32:42_

----

This should be able to handle any type of mob or pet now


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday May 24, 2020 at 11:31:43_

----

going to need to change this to cover all elemental magic.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday May 24, 2020 at 11:32:12_

----

Same with this one, cover all elemental magic.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday May 24, 2020 at 11:32:29_

----

And here


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 29, 2020 at 09:47:50_

----

You can mark this as a WIP if you want, seems i got alot of work to do on it.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 10:06:33_

----

I'd be okay with the _current_ targeting solutions put into a new GEO/aura branch!

My musing on performance improvements are for "before work is done to add more bubbles" not "before I'll hit the merge button"! You should know by now I'm usually a proponent of "if it's a lot of weight for one person, take the code off their hands to be worked on collaboratively later". 😉 

(And the one regarding the "reverse-enmity" container for players should be a new branch based on release _anyway_ so we can merge it into both GEO/aura _and_ trust.)


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 29, 2020 at 11:34:56_

----

I'll work on this some more if you want before you merge it, get some of the issues resolved


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Apr 29, 2020 at 12:38:10_

----

If you want to do some of the easier things, I'll merge after you say "I'm satisfied for now". 😃 


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Wednesday Apr 29, 2020 at 12:53:58_

----

ok that sounds good


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 30, 2020 at 14:38:58_

----

Well i tried to rebase and squash commits, grr, damn git


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 30, 2020 at 14:46:30_

----

thats a bit cleaner, now i can actually work on this


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday Apr 30, 2020 at 14:59:15_

----

Quick note, this wont build until ive fixed some stuff, i made a few changes, so ignore that


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 11:00:14_

----

I'll change the labels to hold/WIP for now so others know you're still working on this!


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Monday May 11, 2020 at 18:57:08_

----

Aww man did the spell list change allready?, damn it


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Thursday May 14, 2020 at 22:52:04_

----

finaly figured out the perpetuation per level cost, so thats all good now for each level, also the hp scale of the luopan.


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Sunday May 24, 2020 at 02:33:33_

----

Ok i think its ready for testing, have at it


----
<a href="https://github.com/Omnione"><img src="https://avatars2.githubusercontent.com/u/10185476?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Omnione](https://github.com/Omnione)**
_Tuesday May 26, 2020 at 13:02:05_

----

Have a few tweaks comming soon, including plates of indi spell item to learn the spells


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Jun 04, 2020 at 22:42:52_

----

Can you split the .sql changes to a separate PR, I guess with status_effects.h as well. That way we can reserve this stuff on `release` and work on GEO in a feature branch.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Jun 06, 2020 at 06:36:54_

----

Okay, this PR is now post-April only, targeting an already merged GEO branch from April, based off our release with most of the SQL/headers in it.

I'll do more butchering later to split bubbles, elemental magic, and abilities.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jun 08, 2020 at 05:12:51_

----

Pushed the final commit for splitting up the branch (geomancer abilities, merits, and adjustments). As the original work in April was merged into our geo branch, going to close this PR so the later work is all fresh new PRs and distinguished from the initial bubble PR.
