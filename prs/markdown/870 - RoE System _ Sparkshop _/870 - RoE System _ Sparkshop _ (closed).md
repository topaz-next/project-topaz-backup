**Labels:**



<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [Kreidos](https://github.com/Kreidos)**
_Sunday Jul 19, 2020 at 15:57:28_
_Originally opened as: project-topaz/topaz - Issue 870_

----

From the team that brought you [Magian](https://github.com/project-topaz/topaz/pull/802) and "[That other feature nobody cares about](https://github.com/project-topaz/topaz/pull/645)", we present Records of Eminence. This is a complete base from which the rest of the records may be built. Thanks and credit goes to @Apocarypse for his packet captures, deciphering assistance, supplying the Spark shop and the NPC/Lua helpers. 

### What's in here?
- All UI elements and interactions.
- Taking/Dropping/Progressing/Completing records
- The Spark Shop + Eminence NPC scripts / CS.
- Persistence of all eminence data per player
- C++ / Lua hooks for interacting with the Eminence system
- Early records fully complete-able
- Migrations for existing DBs

### Which records work?
All Topaz-available content from `Tutorial->Basics`, plus one repeatable "Vanquish Multiple Enemies I".
> First Step Forward
Undertake a FoV Training Regime
Heal Without Using Magic
Vanquish One Enemy
Undertake a GoV Training Regime
Vanquish Multiple Enemies I

### What's comes next?
This base is essentially, wholly complete and these records serve as an example of how the system works, as well as an appetizer for players to sink their teeth into. Next steps would be getting the Records implemented. The vast majority of records could be fully realized using only the hooks provided here, but it would be messy. The next course will be to consider a paradigm for how the nearly 1300+ records will be checked. Whether those checks will be in Core or Lua, and what shape such a system would take. Discussion on this would be welcomed in Discord channels, but is technically out of the scope of this PR.

#### Considerations:
- This adds a new column to the `chars` table for eminence data. New sql file + migration python script is provided. The migration **should** be run on all existing databases. 
- The 6 records which are done here should be considered example *teaser* records only. As detailed above, a more comprehensive handling system for records would be the next phase. There are 1300+ records, and there's no expectation that they'd all be handled like the examples here. :)
- All standard records can be taken by a player, even if no logic exists to progress them. In part due to the current lack of a comprehensive check system as well as in the interests of testing. The client controls which records are shown, and there's no way to hide unimplemented records from the server end; please refer to the above list of working records.
<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Sunday Jul 19, 2020 at 20:57:38_

----

This check for whether the player can be given the item must be the first thing done in this function.  Otherwise, with full inventory space, the player could keep attempting to complete, reaping the currency and xp rewards, but never getting the KI or completion.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Sunday Jul 19, 2020 at 21:02:48_

----

local optionToItem, if it's only used in this one file


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jul 19, 2020 at 23:44:48_

----

Looks like this is wrong csid, same with Eternal Flame and Fhelm Jobeizat.


----
<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Apocarypse](https://github.com/Apocarypse)**
_Monday Jul 20, 2020 at 00:14:26_

----

woops, i copy and pasted those in from isakoth after changing a bunch of stuff. i'll fix it


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:08:52_

----

I like individual attribution, but does this have any possible ramifications down the road?
If you had a particularly aggressive employer who tried to claim all your spare time work etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:09:28_

----

Couple of copy/pasted tabs in hiding in these id/size sections


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:09:59_

----

If we aren't putting information in these block comments, do we need them?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:10:48_

----

Love the in-depth explanations around all of this stuff!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:12:08_

----

Thoughts on replacing memcpy and other C-style stuff with std::copy and the like?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:13:10_

----

Gap after if
But also, thoughts on Allman-style bracing, even for single-line statements?
```
while (x == y)
{
    something();
}
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:14:03_

----

Love this black magic 🧙 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:16:24_

----

I haven't dug into the logic for this, and it isn't that brutal of a loop to optimise, but: 
Could active quests be put into a hashmap and retrieved via lookup instead of search?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:17:43_

----

Great API, super clean ⭐ 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:18:33_

----

Do we have a project consensus about static_cast over C-Style casts?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:19:40_

----

I've been in Core too long, on the Lua side, nil is equivalent to False right?
```lua
if not player:getEminenceProgress(19) then
...
end
```
is valid usage?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:20:55_

----

I mentioned this in Discord, and I think I saw someone else mention it, is this 1 going to get tabled later?
`player:getEminenceCompleted(1)`


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:21:54_

----

Please kill these `;`'s


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:23:19_

----

Not everything in this list needs to be correctly implemented, but does everything have a vaguely OK sell price?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:23:52_

----

This is such a clean API 👨‍🍳 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:24:12_

----

Line break plz


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 13:47:06_

----

I'm not sure. (Not a lawyer) I self-attributed based on input from Zircon, and staff. Apparently the FSF deems self-attributing as recommended practice.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 13:52:58_

----

I am pro modern-style, in this instance since much of the code was mixing in with existing functions I wanted to maintain the same dialect since it was performing identical behaviour. I have long wanted to move areas like this to modern options, (ie. this here and especially config file handling .We're still using char*s and strcmp for crying out loud!)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 13:55:12_

----

There wasn't a real consensus on it right now; there's going to be 1300 trials, and they'll mostly be referenced algorithmically once the check system goes in so I'm not sure how much value there is there. Hunts and Regimes don't use enums, and they work similarly too. At any rate, something to keep in mind for phase 2!


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 14:12:56_

----

+1 This is one area I've already optimized and will be pushing a commit for later. I want HasEminenceRecord to be basically-free since it will be called innumerable times once the check systems are written. In doing performance tests, a hashmap was actually about the same speed as this loop. (I assume because of the *hash* part having some overhead, and this loop being very short) I chose to implement a std::bitset of the player's active trials instead, which checking is about 6 times faster than this loop or a map.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 15:13:33_

----

Since it's empty and we aren't adding any of the reclaimers for the other zones either, I'm just going to kill the file; I'm sure @Apocarypse won't mind.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 15:16:33_

----

Not too rusty, I see! nil and false both eval to False but 0 in Lua is True.

That example :100: . Intention was the API having as few hooks, that do the most possible.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 15:19:21_

----

Axe em'!


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 15:44:28_

----

Thanks! And thanks for the review. Good points brought up, particularly about coding standards which I'm sure will come up more often as we increase compiler strictness and deal with additional GCC8/9 warnings.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 15:46:41_

----

Also, as an aside, since these structs are necessarily comprised of only PoD types and sizeof() is used with no magic numbers I'm less bothered by memcpy use in these cases. Just as long as we don't use any complex types which can't handle shallow copies.

PS. SQL's library also does kind of lend itself more to this memcpy method of usage.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 24, 2020 at 00:43:16_

----

becomes problematic for future maintainers (I mean project maintainers) we don't want to maintain a list of everyone who ever touched one file on a file by file basis do we? what happens when I pr a change to "your" file here later. We're basically agreeing to topaz having this anyway. I like my attribution handled by the commit log personally, which the only legal ramifications being the license text itself which are there to ensure it stays free as in freedom.

![image](https://user-images.githubusercontent.com/6871475/88351925-01bf7f80-cd26-11ea-818f-46335ac94125.png)



----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Sunday Jul 19, 2020 at 20:57:38_

----

This check for whether the player can be given the item must be the first thing done in this function.  Otherwise, with full inventory space, the player could keep attempting to complete, reaping the currency and xp rewards, but never getting the KI or completion.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Sunday Jul 19, 2020 at 21:02:48_

----

local optionToItem, if it's only used in this one file


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Sunday Jul 19, 2020 at 23:44:48_

----

Looks like this is wrong csid, same with Eternal Flame and Fhelm Jobeizat.


----
<a href="https://github.com/Apocarypse"><img src="https://avatars1.githubusercontent.com/u/45616576?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Apocarypse](https://github.com/Apocarypse)**
_Monday Jul 20, 2020 at 00:14:26_

----

woops, i copy and pasted those in from isakoth after changing a bunch of stuff. i'll fix it


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:08:52_

----

I like individual attribution, but does this have any possible ramifications down the road?
If you had a particularly aggressive employer who tried to claim all your spare time work etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:09:28_

----

Couple of copy/pasted tabs in hiding in these id/size sections


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:09:59_

----

If we aren't putting information in these block comments, do we need them?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:10:48_

----

Love the in-depth explanations around all of this stuff!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:12:08_

----

Thoughts on replacing memcpy and other C-style stuff with std::copy and the like?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:13:10_

----

Gap after if
But also, thoughts on Allman-style bracing, even for single-line statements?
```
while (x == y)
{
    something();
}
```


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:14:03_

----

Love this black magic 🧙 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:16:24_

----

I haven't dug into the logic for this, and it isn't that brutal of a loop to optimise, but: 
Could active quests be put into a hashmap and retrieved via lookup instead of search?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:17:43_

----

Great API, super clean ⭐ 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:18:33_

----

Do we have a project consensus about static_cast over C-Style casts?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:19:40_

----

I've been in Core too long, on the Lua side, nil is equivalent to False right?
```lua
if not player:getEminenceProgress(19) then
...
end
```
is valid usage?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:20:55_

----

I mentioned this in Discord, and I think I saw someone else mention it, is this 1 going to get tabled later?
`player:getEminenceCompleted(1)`


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:21:54_

----

Please kill these `;`'s


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:23:19_

----

Not everything in this list needs to be correctly implemented, but does everything have a vaguely OK sell price?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:23:52_

----

This is such a clean API 👨‍🍳 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Jul 23, 2020 at 11:24:12_

----

Line break plz


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 13:47:06_

----

I'm not sure. (Not a lawyer) I self-attributed based on input from Zircon, and staff. Apparently the FSF deems self-attributing as recommended practice.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 13:52:58_

----

I am pro modern-style, in this instance since much of the code was mixing in with existing functions I wanted to maintain the same dialect since it was performing identical behaviour. I have long wanted to move areas like this to modern options, (ie. this here and especially config file handling .We're still using char*s and strcmp for crying out loud!)


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 13:55:12_

----

There wasn't a real consensus on it right now; there's going to be 1300 trials, and they'll mostly be referenced algorithmically once the check system goes in so I'm not sure how much value there is there. Hunts and Regimes don't use enums, and they work similarly too. At any rate, something to keep in mind for phase 2!


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 14:12:56_

----

+1 This is one area I've already optimized and will be pushing a commit for later. I want HasEminenceRecord to be basically-free since it will be called innumerable times once the check systems are written. In doing performance tests, a hashmap was actually about the same speed as this loop. (I assume because of the *hash* part having some overhead, and this loop being very short) I chose to implement a std::bitset of the player's active trials instead, which checking is about 6 times faster than this loop or a map.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 15:13:33_

----

Since it's empty and we aren't adding any of the reclaimers for the other zones either, I'm just going to kill the file; I'm sure @Apocarypse won't mind.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 15:16:33_

----

Not too rusty, I see! nil and false both eval to False but 0 in Lua is True.

That example :100: . Intention was the API having as few hooks, that do the most possible.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 15:19:21_

----

Axe em'!


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 15:44:28_

----

Thanks! And thanks for the review. Good points brought up, particularly about coding standards which I'm sure will come up more often as we increase compiler strictness and deal with additional GCC8/9 warnings.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Thursday Jul 23, 2020 at 15:46:41_

----

Also, as an aside, since these structs are necessarily comprised of only PoD types and sizeof() is used with no magic numbers I'm less bothered by memcpy use in these cases. Just as long as we don't use any complex types which can't handle shallow copies.

PS. SQL's library also does kind of lend itself more to this memcpy method of usage.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Jul 24, 2020 at 00:43:16_

----

becomes problematic for future maintainers (I mean project maintainers) we don't want to maintain a list of everyone who ever touched one file on a file by file basis do we? what happens when I pr a change to "your" file here later. We're basically agreeing to topaz having this anyway. I like my attribution handled by the commit log personally, which the only legal ramifications being the license text itself which are there to ensure it stays free as in freedom.

![image](https://user-images.githubusercontent.com/6871475/88351925-01bf7f80-cd26-11ea-818f-46335ac94125.png)



----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Jul 19, 2020 at 17:20:59_

----

> Looks ~good~ _freaking awesome_ to me. Only thing sticks out to me is copyright notice

100%. They were copy-pasted without realizing it. Staff will advise regarding their replacement, I'd prefer the new source files go under AGPL if possible but either way that will be changed. :)


----
<a href="https://github.com/Xaver-DaRed"><img src="https://avatars2.githubusercontent.com/u/60053999?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Xaver-DaRed](https://github.com/Xaver-DaRed)**
_Sunday Jul 19, 2020 at 17:28:59_

----

other than tabling the rewards as we discussed, this looks awesome


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Sunday Jul 19, 2020 at 17:31:06_

----

> other than tabling the rewards as we discussed, this looks awesome

Thanks Xaver! For sure. As we discussed, the 6 records here should be considered as functioning examples only since a proper record-handling system would be phase 2. 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Jul 19, 2020 at 17:35:34_

----

there are a few things we can optimize here later, but everything is gewd :+1: 


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Tuesday Aug 18, 2020 at 05:33:20_

----

I have chosen to rebase due to conflicts introduced by `release` commits over the last month since I opened the PR. I've also changed the base back to `release` for the time being, since the roe branch is stale; this way diffs and reviews can still be made accurately. 


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Aug 20, 2020 at 03:44:42_

----

@project-topaz/developer @project-topaz/reviewer this one could use some review love post fixes. 
