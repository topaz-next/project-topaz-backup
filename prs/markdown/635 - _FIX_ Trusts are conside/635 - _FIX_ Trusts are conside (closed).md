**Labels:**



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Sunday May 17, 2020 at 07:38:51_
_Originally opened as: project-topaz/topaz - Issue 635_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Got an interesting bug report from Kain that Trusts are acting strangely in the Shadow Lord fight, after some investigation:
```
Ok, I've done a full rebuild and db update from canary, indeed: shadow lord fight: Kupipi freaks out:
- When she cast Protectra it doesn't land on the player, which means she's constantly trying to cast it (which is her logic if someone in the party is missing protect/shell)
- When she runs out of MP her casting particle effects stay on for a while (but this is probably the same as retail, look at when a battle ends and their casting is "interrupted", the effect stays on even through the casting ends)
- I think BCNM with Trusts might be using player allegiance in strange ways, causing some issues
Well, my hunch seems correct, there are a bunch of things in the battlefield handler that deal with PC/MOB/NPC/PET
but not trust
Which means  their allegiance is never set
```

@cocosolos spotted it before me, there's a bunch of information that isn't being set on spawnTrust. I'm surprised we made it this far without noticing...

Also a little misc cleanup.



----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday May 22, 2020 at 01:17:31_

----

Is there any mechanism setting the trust as the mob owner? AFAIK right now only a player can be the owner of a mob, and this ID is used in packets so it probably shouldn't be set to a trust. This branch could really use a merge of the claim code.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday May 22, 2020 at 01:29:46_

----

Is the intent to treat trusts like battlefield allies? Right now I think allies are only instanced mobs that help during the fight, like Prishe in the Promathia fight. Player pets aren't stored in the battlefield object at all. I would probably remove both of these additions and change [this line](https://github.com/project-topaz/topaz/blob/7bc656841594711c48f8bbef80e3f66cbc7670ee/src/map/battlefield.cpp#L392) to handle trusts as well.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday May 22, 2020 at 02:18:28_

----

should be the trusts "master" like with pets, even if they do appear on the party roster visually they aren't players and we need to be cautious what we send their way.

(where/how are pets even being handled for owner purposes in battlefields??)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday May 22, 2020 at 05:46:22_

----

So, not in this PR, but I wanted to sneak this in ahead of my _next_ PR. In the next PR Trusts are using full player abilities with all the trimmings. When Naji 'vokes the player would be locked off of the mob without this snippet.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday May 22, 2020 at 14:15:34_

----

Anything other than players should never be set as the owner of a mob. Instead, it should be setting the player as the owner when the trust acts, avoiding this problem completely. This stuff is all centralized in the claim code that needs to get merged into this branch.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday May 22, 2020 at 01:17:31_

----

Is there any mechanism setting the trust as the mob owner? AFAIK right now only a player can be the owner of a mob, and this ID is used in packets so it probably shouldn't be set to a trust. This branch could really use a merge of the claim code.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday May 22, 2020 at 01:29:46_

----

Is the intent to treat trusts like battlefield allies? Right now I think allies are only instanced mobs that help during the fight, like Prishe in the Promathia fight. Player pets aren't stored in the battlefield object at all. I would probably remove both of these additions and change [this line](https://github.com/project-topaz/topaz/blob/7bc656841594711c48f8bbef80e3f66cbc7670ee/src/map/battlefield.cpp#L392) to handle trusts as well.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday May 22, 2020 at 02:18:28_

----

should be the trusts "master" like with pets, even if they do appear on the party roster visually they aren't players and we need to be cautious what we send their way.

(where/how are pets even being handled for owner purposes in battlefields??)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Friday May 22, 2020 at 05:46:22_

----

So, not in this PR, but I wanted to sneak this in ahead of my _next_ PR. In the next PR Trusts are using full player abilities with all the trimmings. When Naji 'vokes the player would be locked off of the mob without this snippet.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Friday May 22, 2020 at 14:15:34_

----

Anything other than players should never be set as the owner of a mob. Instead, it should be setting the player as the owner when the trust acts, avoiding this problem completely. This stuff is all centralized in the claim code that needs to get merged into this branch.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday May 17, 2020 at 07:47:49_

----

Thanks for your fixing this so quick @zach2good  :cat: 
