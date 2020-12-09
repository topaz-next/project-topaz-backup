**Labels:**

focus

merge ready



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Thursday Feb 20, 2020 at 15:51:36_
_Originally opened as: project-topaz/topaz - Issue 364_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](https://github.com/project-topaz/topaz/blob/master/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This PR topaz-ifys @Omnione's PR (with their blessing) and allows trusts to be cast (but they don't do anything).

With contributions also from @Safhaven's Trust PR.

**GOAL:**
- Take the existing work of others and get it into topaz, so it isn't as daunting to start working on trusts.
- Put in basic plumbing, limit checking etc.

**DONE:**
`trustutils`, `CTrustEntity` and some misc trust changes in core
Bindings: `getTrustID` and `getPartyTrusts`, make `getPartyCount` more usable
Audit the mobpools and mob_spell_lists of all trusts, basic nation trusts have correct spell lists
`isValidHealTarget` helper in `magic.lua` to simplify checks going forward
`spell/trust` entries for a bunch of trusts, which are pretty much empty husks for now
`trust.lua` global with `tpz.trust.canCast` which handles:
- Rejecting casting if you're in an alliance
- Rejecting casting if you're not the party leader
- Rejecting you if you try to cast the same trust twice
- Rejecting you if you try to cast related trusts (See all the Shantotto spell/trust entries).
- Rejecting you if you push the party size above 6 (tested with multiple PCs, trusts and combinations thereof)
- Rejecting you if you try to cast more trusts than you have the ROV KI's for (easily removable)

Bindings for trust Spawn/Despawn/Die messages
Commands:  /returnfaith, /refa, /returntrust and /retr (+all) work 
Fix client crash on casting spells directly on trusts. (Seems hacky, but it's stable at least!)
Trusts despawn and die correctly, when you kill them, or when you die/zone
Trusts will wait for you to engage and start an enmity list before they run in and melee your target
Basic spellcasting if a trust has spells assigned in `mob_spell_lists.sql`

**Starter trust missions are being worked on in a branch off of this branch viewable here:**
https://github.com/zach2good/topaz/compare/trust_list...zach2good:trust_starter_quests


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Feb 25, 2020 at 21:43:10_

----

Spaces on BOTH sides?!

We got us a heretic here boys..


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Feb 25, 2020 at 21:52:41_

----

This is returning nil here, and seems like it could be another misc flag added to the enum instead while leaving the duplicate check to the core before we trigger the casting check (its a different message anyway)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Feb 25, 2020 at 21:56:43_

----

It occurs to me we may have the capitalization backwards. IIRC, the 1st field is going to be the script name, and the 2nd is the packet name for instanced objects. So the 2nd would have “proper” name capitalization but no spaces per SE specifications while the first would go full lowercase to avoid posix problems that were run into ages ago (duplicates happened, and git on windows machines got confused) 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Feb 25, 2020 at 21:58:00_

----

Looks like that rebase didn’t go perfectly as planned


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Feb 26, 2020 at 07:41:03_

----

I don't know what the desired message is, but is `return tpz.msg.basic.MAGIC_CANNOT_CAST` a better placeholder?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Feb 26, 2020 at 07:41:51_

----

💣 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Feb 26, 2020 at 07:46:55_

----

![image](https://user-images.githubusercontent.com/1389729/75323117-e63a7080-587c-11ea-9830-afb469fcbe7b.png)



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:01:20_

----

I'm not going to require a solution this particular problem in this PR, but I'll probably want a better way a spell can check for valid entity types, prior to all spells being modified to add trusts to them. It's already a long `or` chain, and if I recall, Fellow branch added its own as well.

Bitflags and an SQL field, masks, I dunno, _something_...!

To quote my past self:
> we'll eventually need a validHealTarget which cuts:
(target:getObjType() == dsp.objType.PC or target:getObjType() == dsp.objType.MOB or target:getObjType() == dsp.objType.TRUST)
Out of every healing script, and also makes sure the trust is a valid target (some trusts can't be targeted with spells).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:03:35_

----

(The following comments apply to all trust spell scripts):


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:05:48_

----

We can probably save ourselves some effort later by calling a globalized function from the trusts global:
```lua
function onMagicCastingCheck(caster, target, spell)
    local message = tpz.trust.castCheck(caster, spell)
    return message
end
```

This example has a local assignment and return because after the "basic" check, you can still check for "duplicate/distinct" trusts while in the spell script, if the "can cast" logic is taken out of core (see later).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:07:30_

----

Trusts are invalid in some areas where pets are (ex: Salvage), so Trusts will need their own misc flags.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:16:00_

----

The message is different, but I don't expect the message IDs to be added in this PR, so just noting it now~

(One benefit of making the check logic a global is that changing the message later should be a one-line edit so someone doesn't need to go through all the scripts.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:28:48_

----

At the moment this is a call to core, but I think we'd be better served if we instead do "can cast" in lua. Core might need a few binds to check trust ID (if they aren't already there), but I believe all other checks can be done without involving core:
```lua
-- pseudo
tpz.trust.canCast = function(caster, spell)
    if not caster:canUseMisc(tpz.zoneMisc.TRUST) then
        return NO_TRUSTS_HERE_MSG
    end

    if not party leader then
        return NOT_LEADER_MSG
    end

    local num_pt, num_trusts
    for players in party do
        if member is trust then
            if member spell id is spell:getID() then
                return DUPLICATE_TRUST_MSG
            else
                num_trusts = num_trusts + 1
            end
        end
        num_pt = num_pt + 1
    end
    if num_pt >= 6 then
        return PT_FULL_MSG
    end
    if num_trusts >= 3 and not player has ROV KI then
        return TOO_MANY_TRUSTS_MSG
    end
end
```

We can also either table "trusts with the same name", or pass the "the other same-trust"'s ID into this call to check for it:
```lua
-- shantotto ii.lua
function onMagicCastingCheck(caster, target, spell)
    tpz.trust.canCast(caster, spell, shantotto_i_spell_id)
end

-- trust global
trust.canCast = function(caster, spell, duplicate_trust_id)
    if (member spell ID is spell:getID) or (member spell ID is duplicate_trust_id) then
        return DUPLICATE_TRUST_MSG
    end
end
```
This gets around core doing the "heuristic" checks based on name; just let lua handle it in the spell script itself~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:45:48_

----

We _could_ globalize this as well, into a `tpz.trust.spawn(caster, spell)`, which at the moment would just be:
```lua
    caster:spawnTrust(spell:getID())
```
But at least it'd be in a global place in case we need to make additions to onSpellCast behavior later. But I'll be honest and admit I'm currently drawing a blank on "global useful" additions that'd necessitate calling a trust global method from the spell script, instead of calling `caster:spawnTrust(spell:getID())` directly from the script.

Maybe buffing the trust if certain conditions are met? Global checks for current campaigns?

Things like "saying special messages based on other trusts in party", "advancing certain quests", and "attach certain AI" would probably need to be done at the individual script level though, so I'm uncertain how well a lua trust global for "onSpellCast" would work out.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:49:22_

----

Did we ever figure out how these messages work on retail?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:57:40_

----

The self-professed master of magic should probably know how to cast Thunder 😉 

Overly picky ibm here: Sorted by spell ID please~! (Fire, Blizzard, Aero, Stone, Thunder, Water)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 12:14:52_

----

Might be best to zero out the IDs for non-existing spell lists for now~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 12:14:59_

----

Are these skill list IDs intentional?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 12:15:19_

----

Shantotto and Shantotto II still have their previously defined spell and skill list IDs; Shantotto looks the same, but it seems Shantotto II's spell list of 276 got taken.

Both of their skill list IDs were taken as well.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 11:01:53_

----

I'm _fairly_ certain that Trusts don't die if the owner mounts; they'll keep up with you.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 11:28:51_

----

I realize now that I've never seen a trust have spellcasting interruptions other than being silenced. I'm not saying 100% it doesn't happen, just that I haven't seen it (because usually trusts don't move while they're casting). It may be hard to confirm though, as I think the only thing that'd cause a mid-spell trust to move would be knockback, and then the "at same location" check might be coming into play.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 11:42:25_

----

We will need a way to hook into trust spawn and despawn events, if only for those special party messages. Listeners in the controller, maybe?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 11:47:36_

----

See above comments regarding if we can potentially implement this in lua; it'd be preferable if so~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 12:25:28_

----

It may be late, but I'm a little confused here: shouldn't a check like this be done higher in the packet? We've already accessed targid and id at this point~

And are we sending out this packet when we _don't_ have a PTrust?

What's going on with the size change?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 12:51:10_

----

I like how even the new functions are getting russian comments now


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 13:04:30_

----

Since this query is pulling from multiple tables, could we make sure all columns are prepended with the source table it's coming from? And can we get the selections grouped by their source table? We've got columns from pools, then some from family, then more from pools.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 13:18:59_

----

I don't think we'll need this function if we have each spell script check for it's known "duplicate" spell IDs


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 13:22:00_

----

Maybe rename this function so it's more clear that it's not merely querying for a trust, but actually building one~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 13:32:43_

----

GitHub won't let me add a review comment to unchanged lines, but will trusts need to be added to `addAllInZone` too?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 13:35:24_

----

You've already returned PTarget if it's a Trust up on 503; the check for validTargetFlags if the target is a trust never gets reached.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 13:45:54_

----

So here's where I say that trusts can't be summoned while in an alliance.

_But_, if it's possible for core to handle trusts in alliances without creating additional overhead or other issues, I would personally be willing to overlook trust compatibility with alliances so long as any `canCast` function rejects the attempt by default~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 13:56:56_

----

Will a trust be in this pet list if they're being put in the trust list down below?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 13:59:06_

----

At this point, can a PTrust ever have an objtype _other_ than `TYPE_TRUST`?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 14:04:43_

----

I'm not as familiar with AI controllers as I'd _like_, but [looking at `ClearTrusts`, it's already calling Despawn()](https://github.com/project-topaz/topaz/blob/release/src/map/entities/charentity.cpp#L490-L499) on the list.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Mar 20, 2020 at 11:58:56_

----

this needs to die, trusts aren't players. there is a trust that is a treant even which would fail here.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Mar 20, 2020 at 12:01:50_

----

as an example, a "taru" trust should simply use family ID 153 or 154 (or make a new one if those stats don't match)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Mar 20, 2020 at 16:20:35_

----

shouldn't you just make `PTrust->GetSLevel()` a variable like you did for mainjob's level to avoid all these repeat calls?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Mar 23, 2020 at 17:45:03_

----

The trailing comma has no effect since it is the final element


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 00:58:41_

----

Mainly to everyone, not necessarily you, Zach:
I'm _okay_ with these new scripts for now as a testing bed, but we're going to have to come up with _some_ solution to trusts having all the same abilities that players do! The last thing I want is additional burden to maintain an additional copy of weaponskills.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:01:29_

----

We might need some additional Unity logic later. I don't know how we'd handle adding/removing Unity trusts. But this is far, far in the future. Just noting it here.

And our favorite head of a criminal organization might need to check for himself.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:02:05_

----

Doesn't our favorite princess need to check for copies of herself?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:02:37_

----

I'm not certain she would be entirely pleased with this label.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:03:07_

----

Balamor would probably be offended as well.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:05:58_

----

Our second-favorite samurai might need to check for herself too~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:08:03_

----

Our... "favorite"... exorcist might want to check for herself~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:08:44_

----

As much as I would love to have as many Irohas as possible, our favorite samurai priestess should probably be bound by the same rules.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:09:02_

----

Our favorite dancer as well


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:09:21_

----

As well as our favorite pirate princess


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:10:31_

----

There can only be one of our favorite pop idol!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:10:53_

----

The thought of one Naja is horrifying enough!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:12:07_

----

Could we make an argument that one of our favorite puppeteer's is actually a very life-like puppet being controlled by the other, letting us have both in the party?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:13:04_

----

As much as I would like to double the pain, we can only have one of our favorite brawler


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:14:32_

----

And only one of our favorite samurai


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:32:11_

----

Is Zeid too scary for Ygnas to want to be around? 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:38:37_

----

I'm thinking that during the "set up abilities" portion of this trust project we may want to consider reserving an entire block for trust skill lists so that they're all together. Not going to worry about it right now though~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:40:16_

----

And in the future, we might also want to make sure that any skills "added" for trusts are the same IDs as captured from retail (and that the skill list uses the right one). According to the Windower resource database, there's three different copies of Provoke in monster_abilities.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 02:10:17_

----

You probably recognize this, Zach, so this is mainly for others:

Trust AI will need quite a bit of work to implement some new systems. As examples, cooldowns should be handled by the entity itself, and available weaponskills should be provided by core upon spawn based on skill lists and the trust's level. What's currently here is probably testing to make sure trusts are able to use abilities alright and that listeners work, rather than being a finalized AI.

I'm okay with these limited placeholders being in for merge (so people working on the branch can see a couple trusts in action for testing), but please no one start copy-pasting for all tank trusts and then open a PR~ 😅 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 02:45:08_

----

This can be a separate PR after this is merged in, but just adding a note here to make sure updating zone flags isn't forgotten~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 02:46:47_

----

There's also the check for if someone has recently joined, but I'm okay with that being put on a TODO list for later. Again, just noting~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 02:48:41_

----

I believe there's a message for reaching the maximum number of allowed trusts. But as the last two notes: "for later"


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 03:04:32_

----

Can probably combine these nested ifs with some `&&` 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 03:24:14_

----

Checking if the topEnmity is the master might not work if the master isn't the tank, and checking if it's not null would cause trusts to engage before the master has hit the mob. Maybe check to see if the master has it as their claimed mob?

Although, that will still run into issues if the mob was claimed by JA or MA. We might end up needing a "has smacked" 😦 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 03:35:02_

----

Making sure: Does this produce positions that are like retail (all fairly close to where the master was upon engage)?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 03:41:00_

----

Disclaimer: I'd have to see this in action, but my hot take is that this might have some interesting results with trusts trying to negotiate who stands where all at the same time. 😅 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 03:43:33_

----

Do we not need to clear the state stack? Or is it being handled elsewhere?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 03:59:19_

----

Making sure: Trusts aren't being double-counted, right? I've forgotten if trusts are inserted as actual members of the party object.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 04:06:44_

----

Is name here our script name, or the packet name?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 04:13:48_

----

I think retail somehow forms a line based off of the master's last position, in that trusts spawn "behind" you, and then behind other trusts. Although it's been a while since I've last watched how they spawn, and this is very clearly "for later", because it's not important.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 04:19:04_

----

`GetMaxSkill(i`?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 04:22:08_

----

Couldn't you find the index by subtracting the base Trust ID from the mob's Trust ID, instead of needing to step through the list?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 05:57:02_

----

Normal Naja should be a MNK, not a THF~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 05:58:32_

----

Anyone have ideas how to handle "dual mains" like Fablinix and King of Hearts?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 06:01:08_

----

Wiki is a bit confusing; the main trust page lists AAHM as WAR/NIN (which is what I'd peg him as), but the specific page lists him as NIN/WAR instead.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 06:02:13_

----

Wiki is similarly confused for Iroha, listing her as SAM on the main page, but weirdly BLM/SAM on her specific page. It also lists her ROV version as WHM/SAM on its individual page, instead of SAM/WHM as it does on the main category listing.

Absent some concrete argument for main mage, I'd very much bet that Iroha is main SAM. Just a feeling 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 06:03:05_

----

Ingrid II here is supposed to be WHM though.

Others: I have checked main/sub jobs for all other trusts as of this commit. You don't need to.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 08:45:14_

----

I remember reading a lot of complaints that JA/MA don't engage trusts anyway. When levelling a caster you still have to run in and take a swing at an enemy, then run away in order to let the trusts do their thing...


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 08:45:55_

----

This would be the sort of thing I'd like to match retail on by default but have a "fix" available in settings


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 08:47:51_

----

The current movement code works about 70% of the time, every time. They do tend to form up like an actual party, but there are still instances of them getting stuck away from the mob, jostling for position, getting trapped by a wall of other trusts and being unable to get to the enemy etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 08:48:49_

----

Like my comment above, there are still instances of trust dance parties and them getting stuck in interesting situations... 

This will be a pretty hefty TODO in the future, but it's fun to play with right now


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 08:52:03_

----

I'll drop into retail later and check


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 09:23:56_

----

Unfortunately not, there is a gap in 1000-1003, so the ID's don't all line up perfectly with their position in TrustList. This can be simplified into `std::find`, I'd rather a search than an if/else for the regions either side of the gap 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 09:33:54_

----

To make matters EVEN worse, when SE added Monberaux, they didn't put him at the end of the second grouping of trusts, they put him _in the gap_.  Eugh.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 09:54:03_

----

I decided not to treat trusts as full party members (they don't exist inside `members` and they don't return with `getParty()`). This might change in the future, but it'll take a lot more plumbing and loads of testing.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Mar 26, 2020 at 16:25:57_

----

Don't forget the weapon type in the core for mobs is currently bs, and that field controls if a mob double swings or not. IIRC hume ark angel dual wields. So you'd have to set his type "wrong" here to get correct behavior in that case.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 16:30:27_

----

"But /NIN gives Dual Wield!"
"Not until main level is 20."

If that's the case, then Luzaf and a few others might encounter difficulties too.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Mar 26, 2020 at 17:40:13_

----

@ibm2431 Mobs, pets, and trusts don't obey those rules so that won't come into play at all. Whatever the pool value says they should do, they will do at any level.

And on retail trusts that dual wield will do so at any level afaik (I haven't seen any example to the contrary).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 21:33:10_

----

Well, sometimes you want to pull the mob away from others without your trusts running forward to plant themselves in the middle of danger!

I think a happy medium might be a GM command.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 21:34:57_

----

Alright, just making sure we were attempting to match retail! 👍 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 21:36:50_

----

Ah yeah, the gap. Good call, then!


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Feb 25, 2020 at 21:43:10_

----

Spaces on BOTH sides?!

We got us a heretic here boys..


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Feb 25, 2020 at 21:52:41_

----

This is returning nil here, and seems like it could be another misc flag added to the enum instead while leaving the duplicate check to the core before we trigger the casting check (its a different message anyway)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Feb 25, 2020 at 21:56:43_

----

It occurs to me we may have the capitalization backwards. IIRC, the 1st field is going to be the script name, and the 2nd is the packet name for instanced objects. So the 2nd would have “proper” name capitalization but no spaces per SE specifications while the first would go full lowercase to avoid posix problems that were run into ages ago (duplicates happened, and git on windows machines got confused) 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Feb 25, 2020 at 21:58:00_

----

Looks like that rebase didn’t go perfectly as planned


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Feb 26, 2020 at 07:41:03_

----

I don't know what the desired message is, but is `return tpz.msg.basic.MAGIC_CANNOT_CAST` a better placeholder?


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Feb 26, 2020 at 07:41:51_

----

💣 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Feb 26, 2020 at 07:46:55_

----

![image](https://user-images.githubusercontent.com/1389729/75323117-e63a7080-587c-11ea-9830-afb469fcbe7b.png)



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:01:20_

----

I'm not going to require a solution this particular problem in this PR, but I'll probably want a better way a spell can check for valid entity types, prior to all spells being modified to add trusts to them. It's already a long `or` chain, and if I recall, Fellow branch added its own as well.

Bitflags and an SQL field, masks, I dunno, _something_...!

To quote my past self:
> we'll eventually need a validHealTarget which cuts:
(target:getObjType() == dsp.objType.PC or target:getObjType() == dsp.objType.MOB or target:getObjType() == dsp.objType.TRUST)
Out of every healing script, and also makes sure the trust is a valid target (some trusts can't be targeted with spells).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:03:35_

----

(The following comments apply to all trust spell scripts):


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:05:48_

----

We can probably save ourselves some effort later by calling a globalized function from the trusts global:
```lua
function onMagicCastingCheck(caster, target, spell)
    local message = tpz.trust.castCheck(caster, spell)
    return message
end
```

This example has a local assignment and return because after the "basic" check, you can still check for "duplicate/distinct" trusts while in the spell script, if the "can cast" logic is taken out of core (see later).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:07:30_

----

Trusts are invalid in some areas where pets are (ex: Salvage), so Trusts will need their own misc flags.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:16:00_

----

The message is different, but I don't expect the message IDs to be added in this PR, so just noting it now~

(One benefit of making the check logic a global is that changing the message later should be a one-line edit so someone doesn't need to go through all the scripts.)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:28:48_

----

At the moment this is a call to core, but I think we'd be better served if we instead do "can cast" in lua. Core might need a few binds to check trust ID (if they aren't already there), but I believe all other checks can be done without involving core:
```lua
-- pseudo
tpz.trust.canCast = function(caster, spell)
    if not caster:canUseMisc(tpz.zoneMisc.TRUST) then
        return NO_TRUSTS_HERE_MSG
    end

    if not party leader then
        return NOT_LEADER_MSG
    end

    local num_pt, num_trusts
    for players in party do
        if member is trust then
            if member spell id is spell:getID() then
                return DUPLICATE_TRUST_MSG
            else
                num_trusts = num_trusts + 1
            end
        end
        num_pt = num_pt + 1
    end
    if num_pt >= 6 then
        return PT_FULL_MSG
    end
    if num_trusts >= 3 and not player has ROV KI then
        return TOO_MANY_TRUSTS_MSG
    end
end
```

We can also either table "trusts with the same name", or pass the "the other same-trust"'s ID into this call to check for it:
```lua
-- shantotto ii.lua
function onMagicCastingCheck(caster, target, spell)
    tpz.trust.canCast(caster, spell, shantotto_i_spell_id)
end

-- trust global
trust.canCast = function(caster, spell, duplicate_trust_id)
    if (member spell ID is spell:getID) or (member spell ID is duplicate_trust_id) then
        return DUPLICATE_TRUST_MSG
    end
end
```
This gets around core doing the "heuristic" checks based on name; just let lua handle it in the spell script itself~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:45:48_

----

We _could_ globalize this as well, into a `tpz.trust.spawn(caster, spell)`, which at the moment would just be:
```lua
    caster:spawnTrust(spell:getID())
```
But at least it'd be in a global place in case we need to make additions to onSpellCast behavior later. But I'll be honest and admit I'm currently drawing a blank on "global useful" additions that'd necessitate calling a trust global method from the spell script, instead of calling `caster:spawnTrust(spell:getID())` directly from the script.

Maybe buffing the trust if certain conditions are met? Global checks for current campaigns?

Things like "saying special messages based on other trusts in party", "advancing certain quests", and "attach certain AI" would probably need to be done at the individual script level though, so I'm uncertain how well a lua trust global for "onSpellCast" would work out.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:49:22_

----

Did we ever figure out how these messages work on retail?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 11:57:40_

----

The self-professed master of magic should probably know how to cast Thunder 😉 

Overly picky ibm here: Sorted by spell ID please~! (Fire, Blizzard, Aero, Stone, Thunder, Water)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 12:14:52_

----

Might be best to zero out the IDs for non-existing spell lists for now~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 12:14:59_

----

Are these skill list IDs intentional?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 12, 2020 at 12:15:19_

----

Shantotto and Shantotto II still have their previously defined spell and skill list IDs; Shantotto looks the same, but it seems Shantotto II's spell list of 276 got taken.

Both of their skill list IDs were taken as well.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 11:01:53_

----

I'm _fairly_ certain that Trusts don't die if the owner mounts; they'll keep up with you.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 11:28:51_

----

I realize now that I've never seen a trust have spellcasting interruptions other than being silenced. I'm not saying 100% it doesn't happen, just that I haven't seen it (because usually trusts don't move while they're casting). It may be hard to confirm though, as I think the only thing that'd cause a mid-spell trust to move would be knockback, and then the "at same location" check might be coming into play.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 11:42:25_

----

We will need a way to hook into trust spawn and despawn events, if only for those special party messages. Listeners in the controller, maybe?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 11:47:36_

----

See above comments regarding if we can potentially implement this in lua; it'd be preferable if so~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 12:25:28_

----

It may be late, but I'm a little confused here: shouldn't a check like this be done higher in the packet? We've already accessed targid and id at this point~

And are we sending out this packet when we _don't_ have a PTrust?

What's going on with the size change?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 12:51:10_

----

I like how even the new functions are getting russian comments now


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 13:04:30_

----

Since this query is pulling from multiple tables, could we make sure all columns are prepended with the source table it's coming from? And can we get the selections grouped by their source table? We've got columns from pools, then some from family, then more from pools.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 13:18:59_

----

I don't think we'll need this function if we have each spell script check for it's known "duplicate" spell IDs


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 13:22:00_

----

Maybe rename this function so it's more clear that it's not merely querying for a trust, but actually building one~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 13:32:43_

----

GitHub won't let me add a review comment to unchanged lines, but will trusts need to be added to `addAllInZone` too?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 13:35:24_

----

You've already returned PTarget if it's a Trust up on 503; the check for validTargetFlags if the target is a trust never gets reached.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 13:45:54_

----

So here's where I say that trusts can't be summoned while in an alliance.

_But_, if it's possible for core to handle trusts in alliances without creating additional overhead or other issues, I would personally be willing to overlook trust compatibility with alliances so long as any `canCast` function rejects the attempt by default~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 13:56:56_

----

Will a trust be in this pet list if they're being put in the trust list down below?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 13:59:06_

----

At this point, can a PTrust ever have an objtype _other_ than `TYPE_TRUST`?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 14, 2020 at 14:04:43_

----

I'm not as familiar with AI controllers as I'd _like_, but [looking at `ClearTrusts`, it's already calling Despawn()](https://github.com/project-topaz/topaz/blob/release/src/map/entities/charentity.cpp#L490-L499) on the list.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Mar 20, 2020 at 11:58:56_

----

this needs to die, trusts aren't players. there is a trust that is a treant even which would fail here.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Mar 20, 2020 at 12:01:50_

----

as an example, a "taru" trust should simply use family ID 153 or 154 (or make a new one if those stats don't match)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Friday Mar 20, 2020 at 16:20:35_

----

shouldn't you just make `PTrust->GetSLevel()` a variable like you did for mainjob's level to avoid all these repeat calls?


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Mar 23, 2020 at 17:45:03_

----

The trailing comma has no effect since it is the final element


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 00:58:41_

----

Mainly to everyone, not necessarily you, Zach:
I'm _okay_ with these new scripts for now as a testing bed, but we're going to have to come up with _some_ solution to trusts having all the same abilities that players do! The last thing I want is additional burden to maintain an additional copy of weaponskills.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:01:29_

----

We might need some additional Unity logic later. I don't know how we'd handle adding/removing Unity trusts. But this is far, far in the future. Just noting it here.

And our favorite head of a criminal organization might need to check for himself.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:02:05_

----

Doesn't our favorite princess need to check for copies of herself?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:02:37_

----

I'm not certain she would be entirely pleased with this label.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:03:07_

----

Balamor would probably be offended as well.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:05:58_

----

Our second-favorite samurai might need to check for herself too~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:08:03_

----

Our... "favorite"... exorcist might want to check for herself~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:08:44_

----

As much as I would love to have as many Irohas as possible, our favorite samurai priestess should probably be bound by the same rules.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:09:02_

----

Our favorite dancer as well


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:09:21_

----

As well as our favorite pirate princess


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:10:31_

----

There can only be one of our favorite pop idol!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:10:53_

----

The thought of one Naja is horrifying enough!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:12:07_

----

Could we make an argument that one of our favorite puppeteer's is actually a very life-like puppet being controlled by the other, letting us have both in the party?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:13:04_

----

As much as I would like to double the pain, we can only have one of our favorite brawler


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:14:32_

----

And only one of our favorite samurai


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:32:11_

----

Is Zeid too scary for Ygnas to want to be around? 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:38:37_

----

I'm thinking that during the "set up abilities" portion of this trust project we may want to consider reserving an entire block for trust skill lists so that they're all together. Not going to worry about it right now though~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 01:40:16_

----

And in the future, we might also want to make sure that any skills "added" for trusts are the same IDs as captured from retail (and that the skill list uses the right one). According to the Windower resource database, there's three different copies of Provoke in monster_abilities.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 02:10:17_

----

You probably recognize this, Zach, so this is mainly for others:

Trust AI will need quite a bit of work to implement some new systems. As examples, cooldowns should be handled by the entity itself, and available weaponskills should be provided by core upon spawn based on skill lists and the trust's level. What's currently here is probably testing to make sure trusts are able to use abilities alright and that listeners work, rather than being a finalized AI.

I'm okay with these limited placeholders being in for merge (so people working on the branch can see a couple trusts in action for testing), but please no one start copy-pasting for all tank trusts and then open a PR~ 😅 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 02:45:08_

----

This can be a separate PR after this is merged in, but just adding a note here to make sure updating zone flags isn't forgotten~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 02:46:47_

----

There's also the check for if someone has recently joined, but I'm okay with that being put on a TODO list for later. Again, just noting~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 02:48:41_

----

I believe there's a message for reaching the maximum number of allowed trusts. But as the last two notes: "for later"


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 03:04:32_

----

Can probably combine these nested ifs with some `&&` 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 03:24:14_

----

Checking if the topEnmity is the master might not work if the master isn't the tank, and checking if it's not null would cause trusts to engage before the master has hit the mob. Maybe check to see if the master has it as their claimed mob?

Although, that will still run into issues if the mob was claimed by JA or MA. We might end up needing a "has smacked" 😦 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 03:35:02_

----

Making sure: Does this produce positions that are like retail (all fairly close to where the master was upon engage)?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 03:41:00_

----

Disclaimer: I'd have to see this in action, but my hot take is that this might have some interesting results with trusts trying to negotiate who stands where all at the same time. 😅 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 03:43:33_

----

Do we not need to clear the state stack? Or is it being handled elsewhere?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 03:59:19_

----

Making sure: Trusts aren't being double-counted, right? I've forgotten if trusts are inserted as actual members of the party object.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 04:06:44_

----

Is name here our script name, or the packet name?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 04:13:48_

----

I think retail somehow forms a line based off of the master's last position, in that trusts spawn "behind" you, and then behind other trusts. Although it's been a while since I've last watched how they spawn, and this is very clearly "for later", because it's not important.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 04:19:04_

----

`GetMaxSkill(i`?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 04:22:08_

----

Couldn't you find the index by subtracting the base Trust ID from the mob's Trust ID, instead of needing to step through the list?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 05:57:02_

----

Normal Naja should be a MNK, not a THF~


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 05:58:32_

----

Anyone have ideas how to handle "dual mains" like Fablinix and King of Hearts?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 06:01:08_

----

Wiki is a bit confusing; the main trust page lists AAHM as WAR/NIN (which is what I'd peg him as), but the specific page lists him as NIN/WAR instead.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 06:02:13_

----

Wiki is similarly confused for Iroha, listing her as SAM on the main page, but weirdly BLM/SAM on her specific page. It also lists her ROV version as WHM/SAM on its individual page, instead of SAM/WHM as it does on the main category listing.

Absent some concrete argument for main mage, I'd very much bet that Iroha is main SAM. Just a feeling 😉 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 06:03:05_

----

Ingrid II here is supposed to be WHM though.

Others: I have checked main/sub jobs for all other trusts as of this commit. You don't need to.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 08:45:14_

----

I remember reading a lot of complaints that JA/MA don't engage trusts anyway. When levelling a caster you still have to run in and take a swing at an enemy, then run away in order to let the trusts do their thing...


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 08:45:55_

----

This would be the sort of thing I'd like to match retail on by default but have a "fix" available in settings


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 08:47:51_

----

The current movement code works about 70% of the time, every time. They do tend to form up like an actual party, but there are still instances of them getting stuck away from the mob, jostling for position, getting trapped by a wall of other trusts and being unable to get to the enemy etc.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 08:48:49_

----

Like my comment above, there are still instances of trust dance parties and them getting stuck in interesting situations... 

This will be a pretty hefty TODO in the future, but it's fun to play with right now


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 08:52:03_

----

I'll drop into retail later and check


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 09:23:56_

----

Unfortunately not, there is a gap in 1000-1003, so the ID's don't all line up perfectly with their position in TrustList. This can be simplified into `std::find`, I'd rather a search than an if/else for the regions either side of the gap 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 09:33:54_

----

To make matters EVEN worse, when SE added Monberaux, they didn't put him at the end of the second grouping of trusts, they put him _in the gap_.  Eugh.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 09:54:03_

----

I decided not to treat trusts as full party members (they don't exist inside `members` and they don't return with `getParty()`). This might change in the future, but it'll take a lot more plumbing and loads of testing.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Mar 26, 2020 at 16:25:57_

----

Don't forget the weapon type in the core for mobs is currently bs, and that field controls if a mob double swings or not. IIRC hume ark angel dual wields. So you'd have to set his type "wrong" here to get correct behavior in that case.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 16:30:27_

----

"But /NIN gives Dual Wield!"
"Not until main level is 20."

If that's the case, then Luzaf and a few others might encounter difficulties too.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Mar 26, 2020 at 17:40:13_

----

@ibm2431 Mobs, pets, and trusts don't obey those rules so that won't come into play at all. Whatever the pool value says they should do, they will do at any level.

And on retail trusts that dual wield will do so at any level afaik (I haven't seen any example to the contrary).


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 21:33:10_

----

Well, sometimes you want to pull the mob away from others without your trusts running forward to plant themselves in the middle of danger!

I think a happy medium might be a GM command.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 21:34:57_

----

Alright, just making sure we were attempting to match retail! 👍 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Mar 26, 2020 at 21:36:50_

----

Ah yeah, the gap. Good call, then!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 25, 2020 at 15:04:39_

----

Merging master into a feature branch might pose problems when it comes time to merge the finished feature into stable - all the unrelated commits in master would becoming too~ 😅 


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 25, 2020 at 19:15:45_

----

Commits from Omnione were originally based off of sidestream, changing Shantotto's file here threw merge conflicts with our master, one thing led to another, and I felt a straight up rebase off of our current master was in order.

I know how it looks, but I didn't _want_ to attach my name to those commits, I swear!


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Sunday Mar 22, 2020 at 09:59:47_

----

@TeoTwawki I had a look in `adventuringfellow` and I see how it's _meant_ to be done, I'll whip all of the fake PT chat out and leave it for my next PR 👍 


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Mar 22, 2020 at 19:02:11_

----

@zach2good just a heads up when you get there, he used showText and it should be messageSpecial - showText is just wrapping messageSpecial to add a few additional things (things which neither fellows nor trusts will need)


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 08:01:04_

----

@ibm2431 Thanks for the in-depth review 🙏 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Thursday Mar 26, 2020 at 10:15:37_

----

After addressing some points from IBM's review, I thought it might be useful to write up some of my choices about this PR for newcomers to this PR (if there are any):

**The crux of this entire PR:**
The packet logic change in `magic_state.cpp`. I don't know if this is correct, I found this while desperately wrestling with the client crash there. It works, it's stable and I haven't noticed any strangeness.

**Design decisions:**
I wanted Core to be totally unrestricted, and any restrictions to exist in Lua. The Lua restricts things down to a retail-like experience, but if operators wanted to clear out all of the restrictions in `tpz.trust.canCast`, there's nothing stopping them:
- Having trusts in Jeuno
- An alliance full of trusts
- 22 Shantottos nuking things

Trusts are "kind of" treated like party members. I've added `ForPartyWithTrusts` and `:getPartyWithTrusts` for anything that might need to iterate over the party including trusts. I did experiment with treating them as full members, but there were all sorts of explosions with Latents, `OnMobDeathEx`, etc. so I skirted around it.

**Magic, Skills and AI:**
What I've put in at the moment is just a fun frame that allows you to play with a party of Kupipi, Naji and Shantotto.

