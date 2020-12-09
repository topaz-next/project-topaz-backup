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
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday May 17, 2020 at 07:47:49_

----

Thanks for your fixing this so quick @zach2good  :cat: 
