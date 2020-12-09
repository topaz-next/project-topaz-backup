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
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Mar 24, 2020 at 19:56:41_

----

Should the highest player level be updated for each member within range? From my reading, the highest level is determined by a call to `dirtyExp`, which seems to only happens on claiming actions - what about a high level WHM that's only throwing cures?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Mar 24, 2020 at 21:08:10_

----

I realize the secondary targets shouldn't, but shouldn't the primary target of the AoE always get claimed?

(Same for magic too)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Mar 24, 2020 at 21:54:46_

----

exp changes should be decided by highest player character to take action on or otherwise effect a mob directly - debuffs, damage (inc damage from spikes), target of JA - but not from actions that have no effect on the mob itself such as curing people from outside their party.

uncertain about damaging undead via cure but I presume it is treated like a nuke on undead and as no effect when on non undead monsters


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Mar 24, 2020 at 23:02:06_

----

I believe I read that mobskills don't actually claim, only normal attacks/magic, but I may be wrong about that. Magic should be claiming the primary target.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Mar 24, 2020 at 23:50:22_

----

Sorry, I should have been more clear; a high level WHM _in_ the party.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Mar 25, 2020 at 00:07:18_

----

The highest level party member is checked in dirtyExp, and also in charutils::DistributeExperiencePoints. So If a high level WHM doesn't physically interact with a mob, they should still be considered when exp is actually split. [Starting around here.](https://github.com/project-topaz/topaz/blob/432058d0ae232b2f0341b1e379e0f9b4a9515eb8/src/map/utils/charutils.cpp#L3265)

Edit: [Sorry it's actually the block above that.](https://github.com/project-topaz/topaz/blob/432058d0ae232b2f0341b1e379e0f9b4a9515eb8/src/map/utils/charutils.cpp#L3245)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 25, 2020 at 03:02:45_

----

Right; but the highest player level is a comparison against the attacker and the currently highest set for the mob:
`mob->m_HiPCLvl = std::max(PAttacker->GetMLevel(), mob->m_HiPCLvl);`
`dirtyExp` does loop through the entire party when a claiming action has been taken, but only to count the number of players in the party; as written it's not keeping track of the highest level player:
```
PAttacker->ForAlliance([&pcinzone, &mob](CBattleEntity* PMember) {
    if (PMember->getZone() == mob->getZone() && distance(PMember->loc.p, mob->loc.p) < 100)
    {
        pcinzone++;
    }
});
```
`DistributeExperiencePoints` does do so, but that only factors the WHM in upon mob death if the WHM or buffer remains in the party.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Mar 25, 2020 at 03:21:41_

----

Is the WHM supposed to factor into the party level if they don't act on the mob directly and they're not in the party when the mob dies? It's easy to change but I was under the impression that a high level WHM could be in the party during a fight, drop party, and not affect exp other than party size, given they don't interact with the mob.

From wiki:
`Party level is the level of the highest level player or pet to have acted on the monster since it was at 100% health with no debilitating status effects.`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 25, 2020 at 03:36:05_

----

I _assumed_ it's supposed to affect exp but should probably have someone confirm~

@project-topaz/researcher 


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Mar 25, 2020 at 03:47:50_

----

just to clarify, the scenario you wish to test is:
player a lvl 50
player b lvl 75
in party together, engage mob, player b takes no action
player b drops party and either:
does nothing (what is xp?)
PLs (what is xp?)



----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Mar 25, 2020 at 03:54:05_

----

Player A can be level 1, Player B can be 99, as long as there's a sufficient difference in level to impact exp. Then party up, have only Player A attack the mob, and have Player B drop party before the mob dies. What does the exp look like when the mob dies? Does anything change if Player B cures/buffs Player A before dropping party?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Mar 24, 2020 at 19:56:41_

----

Should the highest player level be updated for each member within range? From my reading, the highest level is determined by a call to `dirtyExp`, which seems to only happens on claiming actions - what about a high level WHM that's only throwing cures?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Mar 24, 2020 at 21:08:10_

----

I realize the secondary targets shouldn't, but shouldn't the primary target of the AoE always get claimed?

(Same for magic too)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Mar 24, 2020 at 21:54:46_

----

exp changes should be decided by highest player character to take action on or otherwise effect a mob directly - debuffs, damage (inc damage from spikes), target of JA - but not from actions that have no effect on the mob itself such as curing people from outside their party.

uncertain about damaging undead via cure but I presume it is treated like a nuke on undead and as no effect when on non undead monsters


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Tuesday Mar 24, 2020 at 23:02:06_

----

I believe I read that mobskills don't actually claim, only normal attacks/magic, but I may be wrong about that. Magic should be claiming the primary target.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Mar 24, 2020 at 23:50:22_

----

Sorry, I should have been more clear; a high level WHM _in_ the party.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Mar 25, 2020 at 00:07:18_

----

The highest level party member is checked in dirtyExp, and also in charutils::DistributeExperiencePoints. So If a high level WHM doesn't physically interact with a mob, they should still be considered when exp is actually split. [Starting around here.](https://github.com/project-topaz/topaz/blob/432058d0ae232b2f0341b1e379e0f9b4a9515eb8/src/map/utils/charutils.cpp#L3265)

Edit: [Sorry it's actually the block above that.](https://github.com/project-topaz/topaz/blob/432058d0ae232b2f0341b1e379e0f9b4a9515eb8/src/map/utils/charutils.cpp#L3245)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 25, 2020 at 03:02:45_

----

Right; but the highest player level is a comparison against the attacker and the currently highest set for the mob:
`mob->m_HiPCLvl = std::max(PAttacker->GetMLevel(), mob->m_HiPCLvl);`
`dirtyExp` does loop through the entire party when a claiming action has been taken, but only to count the number of players in the party; as written it's not keeping track of the highest level player:
```
PAttacker->ForAlliance([&pcinzone, &mob](CBattleEntity* PMember) {
    if (PMember->getZone() == mob->getZone() && distance(PMember->loc.p, mob->loc.p) < 100)
    {
        pcinzone++;
    }
});
```
`DistributeExperiencePoints` does do so, but that only factors the WHM in upon mob death if the WHM or buffer remains in the party.


----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Mar 25, 2020 at 03:21:41_

----

Is the WHM supposed to factor into the party level if they don't act on the mob directly and they're not in the party when the mob dies? It's easy to change but I was under the impression that a high level WHM could be in the party during a fight, drop party, and not affect exp other than party size, given they don't interact with the mob.

From wiki:
`Party level is the level of the highest level player or pet to have acted on the monster since it was at 100% health with no debilitating status effects.`


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Mar 25, 2020 at 03:36:05_

----

I _assumed_ it's supposed to affect exp but should probably have someone confirm~

@project-topaz/researcher 


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Wednesday Mar 25, 2020 at 03:47:50_

----

just to clarify, the scenario you wish to test is:
player a lvl 50
player b lvl 75
in party together, engage mob, player b takes no action
player b drops party and either:
does nothing (what is xp?)
PLs (what is xp?)



----
<a href="https://github.com/cocosolos"><img src="https://avatars2.githubusercontent.com/u/2593549?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [cocosolos](https://github.com/cocosolos)**
_Wednesday Mar 25, 2020 at 03:54:05_

----

Player A can be level 1, Player B can be 99, as long as there's a sufficient difference in level to impact exp. Then party up, have only Player A attack the mob, and have Player B drop party before the mob dies. What does the exp look like when the mob dies? Does anything change if Player B cures/buffs Player A before dropping party?


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
