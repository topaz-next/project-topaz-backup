**Labels:**

crafting

merge ready



<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [kaincenteno](https://github.com/kaincenteno)**
_Friday Jul 03, 2020 at 07:59:19_
_Originally opened as: project-topaz/topaz - Issue 803_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits (See comments below)

Changes guildshops to be less hacky and more retail accurate by sending the correct information

This is a teamwork with @Kreidos , he has worked on all c and cpp code. :cat:  Thank you @Kreidos 

updated guild vendors to use npc_util (I haven't verified that it doesn't break anything but would appreciate some feedback from a Tester as that's the only part that HASN'T been tested):
Cletae
Celestina




----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Friday Jul 03, 2020 at 08:55:27_

----

fame defaults to 30, so this parameter isn't needed


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Friday Jul 03, 2020 at 08:55:45_

----

var = "theSandCharmVar"


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Friday Jul 03, 2020 at 08:59:17_

----

Undefined variable: FlyerForRegine (this issue existed in the code before you edited it)

The Flyers for Regine quest got a major update on retail at some point -- see recent issue and my related PRs, that implement more retail-accurate behavior.  Now, you don't need to randomly trade flyers to everyone.  Instead, the 15 NPCs who will accept flyers give you a message when you approach them.  I'm guessing that because of this on retail, NPCs who -don't- accept flyers may no longer give refusal messages, so this code block may not be needed any longer.  However, retail confirmation is needed.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Jul 03, 2020 at 19:27:23_

----

fixed thank you @wrenffxi  :cat: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Jul 03, 2020 at 19:27:28_

----

fixed thank you @wrenffxi  :cat: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Jul 03, 2020 at 19:29:23_

----

that's a valid point, i'm going to ask one of the testers to check out if this behavior is still needed, if so a new PR will be posted to focus solely on it. :cat:  thanks for bringing this up @wrenffxi 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jul 13, 2020 at 13:43:06_

----

this will still throw and error in the meantime. may as well just comment out or remove if you aren't going to define the variable you are using till a new pr.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Jul 13, 2020 at 14:34:42_

----

@TeoTwawki  added the var and a also a note.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jul 15, 2020 at 05:20:56_

----

So, the internal rank is just the max skill level attainable at the current rank. The rank numbers in status.lua are just for our convenience and should probably be left as-is since they're used in a few different calculations so it would just shift around where these adjustments are, resulting in needing to do stuff like changing:
```lua
function getAdvImageSupportCost(player,craftID)
    local Rank = player:getSkillRank(craftID)
    return (Rank/100)*30
end
```
to:
```lua
function getAdvImageSupportCost(player,craftID)
    local Rank = player:getSkillRank(craftID)
    return (Rank+1)*30
end
```
So just rearranging where we're doing calculations instead of actually fixing/improving anything. I would just remove this comment. Everything else looks good I think.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Wednesday Jul 15, 2020 at 05:30:05_

----

My intention is to point out why the number was being modified in such a counter-intuitive manner. Ideally, I prefer not having such artificial abstractions, as they cause this kind of confusion whenever that boundary needs to be crossed. It would also be a very simple manner to just redefined the status.lua values to something representing their *real* value after the appropriate changes were made, so I don't think the comment is invalid. I will change it as you request.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jul 15, 2020 at 05:47:35_

----

It's not counter intuitive though, if your rank is 1, your skill cap is 20. These calculations aren't converting rank into the retail accurate version of rank, they're calculating the max skill level available at your rank, or whatever else it needs to calculate (like support pricing) which is similarly derived from your rank.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Jul 15, 2020 at 06:59:13_

----

In the image attached you can see the rank being passed by the packet is at 0, 200, 300, 400, 500 (0 is not joined a guild, 100 is the first rank, i think is amateur)

Hope this helps with the confusion on why its increments of 100. (captures from retail last year)

![image](https://user-images.githubusercontent.com/26943220/87513536-b7efde80-c62d-11ea-89e7-d5c278444645.png)

thanks for the review coco :)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jul 15, 2020 at 07:04:05_

----

It's not actually the rank being passed though, its the skill cap which is derived from the rank. 100 = 10.0


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jul 15, 2020 at 07:42:23_

----

Actually it might even make sense to move the
```cpp
        guildRank = (guildRank + 1) * 100;
```
from addShopItem and doing that calculation in the packet like so
```cpp
        ref<uint16>(i * 12 + 0x12) = (PChar->Container->getGuildRank(slotID) + 1) * 100;
```


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Wednesday Jul 15, 2020 at 07:50:12_

----

I disagree with pushing the reality of the underlying rank value so deep into the stack that it's virtually invisible. I can't help but imagine that at some point, the obfuscating *16-value rank metaphor* we adopt would will lead to issues. That could be someone running into a problem they can't solve due to values not being what they expect, and so may believing (perhaps based on completely accurate packet captures, as Kain did) that they need to write new functions to workaround an imagined limitation.

Edit: If the issue is wanting user-friendly identifiers for the ranks, this would be a use-case for an ENUM.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jul 15, 2020 at 08:12:07_

----

Rank just corresponds to Amateur, Recruit, Initiate, Novice, Apprentice, Journeyman, Craftsman, Artisan, Adept, Veteran, and Expert. The other ranks are not implemented, but that's what a rank is. The value being used in the shop packet is clearly the skill cap corresponding to the rank, why would it make sense to rank up by 100 ranks every time you rank up when a rank is those things listed? Likewise the price of certain things are determined by a different calculation using the rank, and the guild turn in item also determines the item of the day by indexing with the rank. It is very possible PVLV has the [wrong label](https://github.com/ZeromusXYZ/PacketViewerLogViewer/blob/00ffbcc66a373a811255290f0d0a221eed09fdc6/helpers/PacketParsers.cs#L1517), it wouldn't be the first time. There's a lot of stuff that's still unknown or just best guess.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 17, 2020 at 18:43:26_

----

Instead of doing the math in baseentity and calling it the "rank", can instead...


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 17, 2020 at 18:53:17_

----

Perform the math in the outgoing packet here instead. We don't know retail internally represents ranks with values of 100, 200, 300 based on just this packet (but if there's other indications, that's a different story). So long as we're passing the term "guild rank" around core, should probably be kept consistent across different uses (ie: a standard enum of 1-16).

If don't want to do the math each iteration: can do and set it in the binding, but just rename the "guildRank" in the container to something like "skillCap". That way it's clear that it's not to be confused with the 1-16 ranks, and is still an accurate descriptor of what the value might represent.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Jul 20, 2020 at 03:05:44_

----

Adjusted it to be done here at the packet.

One calculation per trade item isn't much so I'm not concerned there, and if we're going to push the rank metaphor down one layer to the variable, may as well push it all the way down to the packet.


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Friday Jul 03, 2020 at 08:55:27_

----

fame defaults to 30, so this parameter isn't needed


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Friday Jul 03, 2020 at 08:55:45_

----

var = "theSandCharmVar"


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Friday Jul 03, 2020 at 08:59:17_

----

Undefined variable: FlyerForRegine (this issue existed in the code before you edited it)

The Flyers for Regine quest got a major update on retail at some point -- see recent issue and my related PRs, that implement more retail-accurate behavior.  Now, you don't need to randomly trade flyers to everyone.  Instead, the 15 NPCs who will accept flyers give you a message when you approach them.  I'm guessing that because of this on retail, NPCs who -don't- accept flyers may no longer give refusal messages, so this code block may not be needed any longer.  However, retail confirmation is needed.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Jul 03, 2020 at 19:27:23_

----

fixed thank you @wrenffxi  :cat: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Jul 03, 2020 at 19:27:28_

----

fixed thank you @wrenffxi  :cat: 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Friday Jul 03, 2020 at 19:29:23_

----

that's a valid point, i'm going to ask one of the testers to check out if this behavior is still needed, if so a new PR will be posted to focus solely on it. :cat:  thanks for bringing this up @wrenffxi 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Jul 13, 2020 at 13:43:06_

----

this will still throw and error in the meantime. may as well just comment out or remove if you aren't going to define the variable you are using till a new pr.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Monday Jul 13, 2020 at 14:34:42_

----

@TeoTwawki  added the var and a also a note.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jul 15, 2020 at 05:20:56_

----

So, the internal rank is just the max skill level attainable at the current rank. The rank numbers in status.lua are just for our convenience and should probably be left as-is since they're used in a few different calculations so it would just shift around where these adjustments are, resulting in needing to do stuff like changing:
```lua
function getAdvImageSupportCost(player,craftID)
    local Rank = player:getSkillRank(craftID)
    return (Rank/100)*30
end
```
to:
```lua
function getAdvImageSupportCost(player,craftID)
    local Rank = player:getSkillRank(craftID)
    return (Rank+1)*30
end
```
So just rearranging where we're doing calculations instead of actually fixing/improving anything. I would just remove this comment. Everything else looks good I think.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Wednesday Jul 15, 2020 at 05:30:05_

----

My intention is to point out why the number was being modified in such a counter-intuitive manner. Ideally, I prefer not having such artificial abstractions, as they cause this kind of confusion whenever that boundary needs to be crossed. It would also be a very simple manner to just redefined the status.lua values to something representing their *real* value after the appropriate changes were made, so I don't think the comment is invalid. I will change it as you request.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jul 15, 2020 at 05:47:35_

----

It's not counter intuitive though, if your rank is 1, your skill cap is 20. These calculations aren't converting rank into the retail accurate version of rank, they're calculating the max skill level available at your rank, or whatever else it needs to calculate (like support pricing) which is similarly derived from your rank.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Wednesday Jul 15, 2020 at 06:59:13_

----

In the image attached you can see the rank being passed by the packet is at 0, 200, 300, 400, 500 (0 is not joined a guild, 100 is the first rank, i think is amateur)

Hope this helps with the confusion on why its increments of 100. (captures from retail last year)

![image](https://user-images.githubusercontent.com/26943220/87513536-b7efde80-c62d-11ea-89e7-d5c278444645.png)

thanks for the review coco :)


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jul 15, 2020 at 07:04:05_

----

It's not actually the rank being passed though, its the skill cap which is derived from the rank. 100 = 10.0


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jul 15, 2020 at 07:42:23_

----

Actually it might even make sense to move the
```cpp
        guildRank = (guildRank + 1) * 100;
```
from addShopItem and doing that calculation in the packet like so
```cpp
        ref<uint16>(i * 12 + 0x12) = (PChar->Container->getGuildRank(slotID) + 1) * 100;
```


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Wednesday Jul 15, 2020 at 07:50:12_

----

I disagree with pushing the reality of the underlying rank value so deep into the stack that it's virtually invisible. I can't help but imagine that at some point, the obfuscating *16-value rank metaphor* we adopt would will lead to issues. That could be someone running into a problem they can't solve due to values not being what they expect, and so may believing (perhaps based on completely accurate packet captures, as Kain did) that they need to write new functions to workaround an imagined limitation.

Edit: If the issue is wanting user-friendly identifiers for the ranks, this would be a use-case for an ENUM.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Jul 15, 2020 at 08:12:07_

----

Rank just corresponds to Amateur, Recruit, Initiate, Novice, Apprentice, Journeyman, Craftsman, Artisan, Adept, Veteran, and Expert. The other ranks are not implemented, but that's what a rank is. The value being used in the shop packet is clearly the skill cap corresponding to the rank, why would it make sense to rank up by 100 ranks every time you rank up when a rank is those things listed? Likewise the price of certain things are determined by a different calculation using the rank, and the guild turn in item also determines the item of the day by indexing with the rank. It is very possible PVLV has the [wrong label](https://github.com/ZeromusXYZ/PacketViewerLogViewer/blob/00ffbcc66a373a811255290f0d0a221eed09fdc6/helpers/PacketParsers.cs#L1517), it wouldn't be the first time. There's a lot of stuff that's still unknown or just best guess.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 17, 2020 at 18:43:26_

----

Instead of doing the math in baseentity and calling it the "rank", can instead...


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Jul 17, 2020 at 18:53:17_

----

Perform the math in the outgoing packet here instead. We don't know retail internally represents ranks with values of 100, 200, 300 based on just this packet (but if there's other indications, that's a different story). So long as we're passing the term "guild rank" around core, should probably be kept consistent across different uses (ie: a standard enum of 1-16).

If don't want to do the math each iteration: can do and set it in the binding, but just rename the "guildRank" in the container to something like "skillCap". That way it's clear that it's not to be confused with the 1-16 ranks, and is still an accurate descriptor of what the value might represent.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Monday Jul 20, 2020 at 03:05:44_

----

Adjusted it to be done here at the packet.

One calculation per trade item isn't much so I'm not concerned there, and if we're going to push the rank metaphor down one layer to the variable, may as well push it all the way down to the packet.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Jul 12, 2020 at 23:13:45_

----

Can i have a review ready tag for this quest since there hasnt been any feedback about the Flyers for Regine, and nothing on it was changed for it besides using npcutils.

thank you =)
