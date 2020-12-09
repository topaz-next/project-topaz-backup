**Labels:**

reviewed



<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [cocosolos](https://github.com/cocosolos)**
_Tuesday Mar 17, 2020 at 17:36:23_
_Originally opened as: project-topaz/topaz - Issue 431_

----

This attempts to bring claim mechanics closer to retail. Claim is currently applied in several different places, so I moved all of that to one function in battleutils, I also added a separate function to dirty exp based on party size and player level, and another for handling new unclaiming/claim passing mechanics. I tried to get this as close to retail as I could, but there's probably still things to iron out, like all claimed mobs still having the same color name. Some things this will have an effect on is anything that uses the player on mob death. There will be situations where the mob dies while unclaimed and there is no owner, such as a DoT tick.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Mar 24, 2020 at 23:06:28_

----

Switching targets doesn't call relinquishClaim, only actually disengaging from a mob. So if you're the owner and switch targets the mob will go unclaimed unless another party member hits it first. 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 25, 2020 at 03:21:03_

----

Re: Switching targets, a player who has claim attacking another mob calls a clean for the owner ID of the mob they originally had claim on:
```
if (PDefender->isAlive() && attacker->PClaimedMob && attacker->PClaimedMob != PDefender
&& attacker->PClaimedMob->isAlive() && attacker->PClaimedMob->m_OwnerID.id == attacker->id)
    { // unclaim any other living mobs owned by attacker
        attacker->PClaimedMob->m_OwnerID.clean();
        attacker->PClaimedMob->updatemask |= UPDATE_STATUS;
        attacker->PClaimedMob = nullptr;
```
Which, unlike in `RelinquishClaim`, doesn't attempt to find another party member to pass claim onto.

Scenario:
1. Members A and B have taken aggressive action against a mob
2. Member A was the last one to do so, their ID is currently the one set in m_OwnerID
3. Member A, without taking an action which would trigger a `ReliniquishClaim` call, attacks another mob

What happens to the claim which should pass onto Member B?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Mar 25, 2020 at 03:25:52_

----

In that scenario, the mob is supposed to go unclaimed. Unless Member B does an action to become the owner before Member A performs a claiming action on another mob, claim will drop. Member B will still have that mob as their ClaimedMob, but the mob loses its owner. This is supposed to happen.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Mar 25, 2020 at 17:40:47_

----

https://youtu.be/BWZDHvzbns4
perhaps changed at some point. tested: 
lvl 32 rng, lvl 99 rdm. 
lvl 32 engaged sole member of party, received outside cures, xp.
32 engaged, 99 buffed, 99 dropped, no xp.
32 engaged 99 buffed with flurry (in case multiple buffs/regen messing things up), 99 dropped, no xp
32 engaged 99 dropped, cured outside, no xp
32 engaged 99 dropped, no 99 action, no xp
(all on xp bearing mobs


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 17:06:37_

----

> In that scenario, the mob is supposed to go unclaimed.

Even if Member B is still engaged?


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Mar 26, 2020 at 19:42:37_

----

> > In that scenario, the mob is supposed to go unclaimed.
> 
> Even if Member B is still engaged?

Yep, unless they're the owner they basically have no claim over the mob. This is also why Member A could drop party instead of attacking another mob and the mob would become exclusively theirs, Member B would auto disengage.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 21:10:34_

----

What about a scenario of two BLMs who have both (single-target) nuked a mob, but then the one currently listed as the mob's owner decides to nuke a second?

I'm worried about people outside a party trying to yoink an NM if the one single party member who is marked as the claimant tries to deal with an add.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Thursday Mar 26, 2020 at 21:24:58_

----

If the owner nukes another mob, the first mob will go unclaimed. I believe this is intentional. However, anyone not in this party will have to place themselves at the top of the hate list to steal the claim. Any party member of the original owner will be able to reclaim instantly.
