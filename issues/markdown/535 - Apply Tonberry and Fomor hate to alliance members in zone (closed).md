**Labels:**

merge ready



<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [wrenffxi](https://github.com/wrenffxi)**
_Monday Apr 27, 2020 at 09:23:02_
_Originally opened as: project-topaz/topaz - Issue 535_

----

Fomor and Tonberry mixins were only adding hate to the mob's current target at ToD.  Now, it will apply to all alliance members ~within EXP range~ in zone, even if outside of XP range.

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits




----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Apr 27, 2020 at 09:47:03_

----

Actually, I'll admit not being familiar with these mixins - in this context, is `player` the killer, or is this mixin being called for each party member? (I'm currently assuming that player is the killer)


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Monday Apr 27, 2020 at 10:37:12_

----

player passed into DEATH listener is ~the mob's current target~<sup>1</sup>, iirc.  *edit: it's the killer*<sup>2</sup>  DEATH in mixin only runs once per mob death, unlike the onMobDeath function in mob's lua, which runs once per player.

<sup>1</sup>edit: maybe it is the killer.  it's unclear to me how killer is assigned in the core.  Variable is called PKiller, which makes me think killer, but variable is assigned value of m_OwnerID.targid, which makes me think current target.  Either way, it's called once per death, by someone in the alliance.

https://github.com/project-topaz/topaz/blob/eda08f62ca39d00537833a5e4b118886ab46fcbb/src/map/entities/battleentity.cpp#L1181-L1188

<sup>2</sup>edit: looks like it's killer.  translation of russian comment on m_OwnerID: "ID of the attacking entity (after death, it will store the ID of the last strike blower)"


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Apr 27, 2020 at 11:04:16_

----

If not for the in range check I’d say it was a mistake to ever move out of onMobDeath into the mixin. I assume we know for a fact retail only adds fomor hate to in range players - so no parking the at the zone line while preparing for swift belt


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Monday Apr 27, 2020 at 11:46:27_

----

IMO, this is exactly the sort of thing we'd want to use a mixin for, rather than putting the same code in every relevant fomor (increasing) and orc, gigas, and taur (decreasing) mob LUA.

Unfortunately, it seems like most of the information about retail fomor hate is speculative, with player accounts disagreeing with each other  Supposedly your fomor hate affects the radius at which fomors sound-aggro, and that if you have no fomor hate, they won't sound-aggro at all. (We haven't implemented any such mechanic yet.)

But there are many unknowns:

1. How many fomors must you kill before they start sound-aggroing?  Wiki says five, user comments say one.
2. How does increasing fomor hate increase their sound aggro range?  Does it increase linearly until a max range?  Does it jump at certain breakpoints?  Is it just a static range, with an on/off aggro?
3. How does killing fomors increase hate?  Is it a static amount per kill?  Is it a random chance per kill?  If random, that might explain the differing numbers we see in question 1.
4. What levels of fomor hate make [Resauchamet](https://ffxiclopedia.fandom.com/wiki/Resauchamet) give you new dialog?
5. Do fomors killed by pets increase hate?
6. How much does hate reduce when killing orcs, gigas, and taurs in Tavnazian region?  Is it a static amount, or random?  Does it vary by mob species?
7. Does a player's fomor hate also affect the low-HP type aggro of Fomors?
8. What are the conditions for acquiring fomor hate?  Everyone in alliance?  Only those in zone?  Only those in XP range?  Only those participating in battle?  Wiki suggests it's everyone in alliance in zone, regardless of range or participation in battle, so I can change this PR to that if we trust wiki.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Apr 28, 2020 at 00:48:57_

----

I'm not saying we should change away from mixins, I'm saying using our other tools isn't "bad": 
binding use does not necessitate duplicate code. One call to a helper function in `onMobDeath()` avoids the issue you ran into with the hook since it already ran per member - but if we're using a listener hook and it needs a distance check anyways, it may as well be mixin'd instead of doing the utils style. This also means its effectively been broken for non solo ever since the move to a mixin since the listener used wasn't structured to deal with that (maybe it should be for future use cases like this? I dunno).

Regarding the hate mechanics: worth noting it only goes down from beastmen and tauri within the region, and likewise only goes up from fomor in the region. An Aht Urgan fomor for instance will not grant fomor hate and uses generic undead sound/blood agro, and killing a an Orc in Davoi won't reduce any fomor hate.

To determine the how much it takes to change the message, we can count kills and see how many it takes to change tiers. I would bet on it looking similar to fame tiers. Can leave an alt at a zone line to determine if its zone-wide or not as well. if its not zone-wide, I expect exp range is the rule. We just need a volunteer to waste some hours in Lufaise :grin: 


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Tuesday Apr 28, 2020 at 11:32:32_

----

Agree that a function in onMobDeath imported from another file would be good solution too.  Just want to avoid having the actual calculation code repeated in every mob lua.

I believe TPZ has "only in Tavnazia" correct already, but I'll double check that.

Leave this PR for now, and I'll change it to do what wiki indicates - give hate to everyone in zone - and then I'll open an issue with all the unknown questions that ask for retail confirmation.  Might be a day or two before I have time for it though.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday May 07, 2020 at 11:01:39_

----

Gonna slap some hold/WIP labels on this so I remember _not_ to hit the merge button for now!


----
<a href="https://github.com/wrenffxi"><img src="https://avatars1.githubusercontent.com/u/21246949?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [wrenffxi](https://github.com/wrenffxi)**
_Sunday May 17, 2020 at 16:21:31_

----

Updated PR so that it applies hate to all members in zone, even if outside of XP range.  Per [wiki](https://ffxiclopedia.fandom.com/wiki/Fomor_Hate):
```
In the same way that simply being in a party/alliance with people killing Fomor will
increase your Fomor Hate, you do not have to be involved in the fights to have
Fomor Hate reduced by killing beastmen. You do not have to be within range of
earning experience points to have a kill counted.
```
