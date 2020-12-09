**Labels:**

bug



<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:25_
_Originally opened as: project-topaz/topaz - Issue 301_

----

<a href="https://github.com/zylakitty"><img src="https://avatars2.githubusercontent.com/u/39413396?v=4"  width="96" height="96" hspace="10"></img></a> **Issue by [zylakitty](https://github.com/zylakitty)**
_Wednesday Jun 05, 2019 at 15:53 GMT_
_Originally opened as DarkstarProject/darkstar - Issue 6062_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->

**_I have:_**

- [x] searched existing issues (http://github.com/darkstarproject/darkstar - Issue ) to see if the issue I am posting has already been addressed or opened by another contributor
- [x] checked the commit log to see if my issue has been resolved since my server was last updated


<!-- Issues will be closed without being looked into if the following information is missing (unless its not applicable). -->

**_Client Version_** (type `/ver` in game) **:** 
30190430_0

**_Source Branch_** (master/stable) **:** 
no idea what this even means

<!-- If there is a server you know we can reproduce this on right now, please mention it here. -->
**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 
I am currently playing on the Nocturnal Souls server, where I have run into this issue.

Certain pieces of gear are not displaying their armor models correctly when specifically using the lockstyle function of the in game gearsets. 

These pieces of gear include the Ceremonial Dress, Novennial Dress, and Novennial Boots. 

When equipping these pieces of gear normally, then using the /lockstyle text command, there seems to be no issue with the models displaying correctly. However when one uses the gearset function to stylelock these pieces there are parts that do not display properly.

Shown in the screenshots below are the armor models being displayed correctly when equipping the items normally, and then comparison screenshots of how they incorrectly appear when using the lockstyle function of the in game gearsets.

The Ceremonial Dress does not display the hand area as it normally should, and will instead overlap whichever piece of gear is actually equipped in that slot, or display the naked model for that slot if nothing is equipped there.

The Novennial Dress has the same error in display as the Ceremonial Dress listed above, and as shown in the screenshots below. The Novennial Boots display as if half of the characters legs are clipping over the armor model.

![Ceremonial Dress Correct display](https://user-images.githubusercontent.com/39413396/58970360-4a655380-8787-11e9-925d-868a67244c8f.png)
![Ceremonial Dress incorrect display](https://user-images.githubusercontent.com/39413396/58970379-53562500-8787-11e9-82b9-94ddbeffa8c4.png)
![Novennial Dress and Boots correct display](https://user-images.githubusercontent.com/39413396/58970392-59e49c80-8787-11e9-9b53-12f3c10766f9.png)
![Novennial Dress and Boots incorrect display](https://user-images.githubusercontent.com/39413396/58970402-60731400-8787-11e9-8ee3-b3731a445625.png)

With all of this said, I do realize this isn't a major issue that warrants priority over game breaking issues, but it is something I would not mind seeing addressed should those working on the game have time, and any efforts are appreciated. Thank you.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:26_

----

<a href="https://github.com/zylakitty"><img src="https://avatars2.githubusercontent.com/u/39413396?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zylakitty](https://github.com/zylakitty)**
_Wednesday Jun 05, 2019 at 16:01 GMT_

----

Source Branch (master/stable) : 
Master

Sorry, I got clarification on what this meant.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:27_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Wednesday Jun 05, 2019 at 16:57 GMT_

----

The issue has to do with gear that locks out other slots. Specifically, that gear needs to set the locked slot to the same (offset?) value as the slot the particular equip is in. Currently, locked slots are being set to whatever is in the hands slot, or the default if nothing is set.

As a workaround for in-game use, actually equip the gear and use /lockstyle on, instead of putting the gear in an equipset and using /lockstyleset.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:29_

----

<a href="https://github.com/zylakitty"><img src="https://avatars2.githubusercontent.com/u/39413396?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zylakitty](https://github.com/zylakitty)**
_Wednesday Jun 05, 2019 at 17:44 GMT_

----

Yea, I figured that out in the process of trying to troubleshoot exactly where the issue lay. Thnx for the insight as to what specifically is causing the issue. Should I close this ticket, or leave it to a mod to decide if they want to keep it open?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:30_

----

<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Wednesday Jun 05, 2019 at 17:55 GMT_

----

I'd say leave it open, since there is erroneous behaviour with /lockstyleset.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:31_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jun 05, 2019 at 20:27 GMT_

----

Looking at the dress + THF AF hands: Ignoring /lockstyle, does the hands item get properly removed when _equipping_ the dress (either manually or from an equip set)? Is equipsets allowing you to have both dress and hands in the same equipset? Or is this issue limited just to the display? 



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:32_

----

<a href="https://github.com/zylakitty"><img src="https://avatars2.githubusercontent.com/u/39413396?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zylakitty](https://github.com/zylakitty)**
_Wednesday Jun 05, 2019 at 22:23 GMT_

----

Yes, this only happens when using the lockstyle feature of the in-game gearsets. If you equip the item normally it will display the armor model as it should, which you can then use the /lockstyle text command to lock the gear appearance.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:34_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Jun 05, 2019 at 22:53 GMT_

----

**Ignoring /lockstyle**, are equipsets allowing _both_ items _in the set_?

Can one use /equipset to _equip_ both the dress and hands?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:35_

----

<a href="https://github.com/zylakitty"><img src="https://avatars2.githubusercontent.com/u/39413396?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [zylakitty](https://github.com/zylakitty)**
_Thursday Jun 06, 2019 at 03:31 GMT_

----

The Dress and the hands are the same item, it's an item that has the descriptor of (cannot equip hand gear), which is in theory where the problem lies?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:36_

----

<a href="https://github.com/helixhamin"><img src="https://avatars1.githubusercontent.com/u/2202779?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [helixhamin](https://github.com/helixhamin)**
_Thursday Jun 06, 2019 at 03:38 GMT_

----

Descriptor? No, description don't matter, implemented behavior does. We can remove the reserved slot from the item and allow you to normally equip, as long as the client doesn't freak out.
What he means is, go to an equipset and define both the body and hands, and see if it lets you equip both, even though you should not be able to.



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:37_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Jun 06, 2019 at 03:40 GMT_

----

y'all gettin confused

the equipset is using an item that covers two slots.  the server is forgetting to check for multi-slot items when applying an equipset as lockstyle  (ie. only the model id), causing the actual equipment to show through



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:38_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jun 06, 2019 at 03:42 GMT_

----

teschnei So the problem is only the _display_, and the server isn't forgetting to check for multi-slot items when _equipping_ an equipset?



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:40_

----

<a href="https://github.com/teschnei"><img src="https://avatars3.githubusercontent.com/u/1149183?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [teschnei](https://github.com/teschnei)**
_Thursday Jun 06, 2019 at 03:47 GMT_

----

if that was the case, the fourth picture wouldn't look like that - those are the default (nothing equipped) mithra hands and legs



----
<a href="https://github.com/topaz-bot"><img src="https://avatars3.githubusercontent.com/u/59651103?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [topaz-bot](https://github.com/topaz-bot)**
_Wednesday Jan 08, 2020 at 15:08:41_

----

<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4"  width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Jun 06, 2019 at 04:29 GMT_

----

I fired up my server to play with it some, some things I've noticed thus far:
A) Equipset is allowing you to _define_ pieces in both slots (this does not happen on retail, it will immediately kick the other item off the equipset)

B) Equipset is not letting you _equip_ both slots. You can't trick an equipset to let you equip both Novennial Legs + any feet with either both in the equipset (it will choose the feet slot), or by having the equipset be just one of the items you try to /equipset while you're currently wearing the other item. (This is what I wanted to make sure of.)

C) When attempting to stylelock an invalid equipset (Novennial legs and any defined feet), it will attempt to blend the two items _in the equipset_, not legs + whatever you have currently equipped in feet

D) If you attempt to stylelock with _just_ Novennial legs in the equipset, when currently equipped with any foot item, it will try to blend the legs with your currently equipped foot item

E) If you attempt to stylelock Novennial legs + blank feet in the equip set, when wearing nothing in either slot, it will try to blend Novennial legs with default naked feet

F) E will also occur if you have any non-Novennial legs currently equipped in the legs slot

G) If you attempt to stylelock Novennial legs + blank feet, while having Novennial legs _actually equipped_, you end up with the normal looking Novennial legs only, no blended default feet

H) G also occurs if you have a different foot-locking piece _actually equipped_ (Dinner Hose) when you try to stylelock the Novennial Legs, it doesn't have to be the same piece being locked

I) But if your equipset is Novennial Legs + _Remove_ feet (Red X), you will end up with blended Novennial + Default, even if you're currently equipped with a valid Novennial/Dinner legs



----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Saturday Oct 03, 2020 at 09:24:15_

----

Today I came across this and was bothered. The most important bit for this seems to come from https://github.com/project-topaz/topaz/blob/0d6b74d03a83849bf472d63b0884070fb429dc7a/src/map/packet_system.cpp#L2663-L2699

I don't do C++ and worse, I have no idea what calls, functions and globals are available here, so I ask to @developers : Isn't it possible to check if the key `rslot` of the current itemID is double its `slot` size (see edit below) and if so, then equip the slot to the right with "invisible". This would work for body and legs. No need to go fancy and block the input or anything as long as there's only a way to get the equipset working without clipping into the default/naked hands/feet.

```
            // Get database key 'slot' and 'rslot' of item (last two)
            // If 'rslot' = 'slot' * 2
            // Then make the next slot to the right (also 'slot' * 2) use "invisible"

            // -- Don't know if it helps: In AltanaView "invisible" always directly follows default/naked
            // -- (which comes first, invisible always comes second, doesn't seem to be random)

```

Edit: After a little bit of talking with @jarmengaud and then looking tables up, it seems that the very last key of any equipment item in the database is `rslot` which always is double the value of the slot if it cannot equip additional gear. So for a body that cannot equip hands `rslot` would be always `64` and for a leg item that cannot equip feet it would always be `256` (based on the slot bytes explained in `macroequipset.cpp`) I adjusted the above accordingly.
