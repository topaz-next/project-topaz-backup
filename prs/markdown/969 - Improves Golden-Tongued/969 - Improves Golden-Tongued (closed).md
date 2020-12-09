**Labels:**



<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [tankfest](https://github.com/tankfest)**
_Tuesday Aug 18, 2020 at 05:42:52_
_Originally opened as: project-topaz/topaz - Issue 969_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Instead of golden-tongue remaining stationary at spawn, he will now follow players and max range cast.  His cast timer is also much more accurate to retail; he gets a cast in every 10-18 seconds, instead of every 5 seconds like he was before (completely broken).

Thanks to Eren@GoldSaucer and Zaz@GoldSaucer for reporting this.


----
<a href="https://github.com/Kreidos"><img src="https://avatars0.githubusercontent.com/u/12466395?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Kreidos](https://github.com/Kreidos)**
_Tuesday Aug 18, 2020 at 06:06:02_

----

Tankfest closed by mistake during a rebase. Reopening at his request!


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Aug 18, 2020 at 12:21:27_

----

I've actually been working on this recently myself, but stopped because i cannot get the interrupt working. Being able to interrupt him by having him switch target midcast is a critical part of the fight.
That being said - i did come up with a way to force the insta death for pets if you want to add it here, it's another big part of their behavior.
function onMobFight(mob,target)
    mob:SetAutoAttackEnabled(false)
    mob:SetMobAbilityEnabled(false)
    if target:isPet() then
        mob:setMod(dsp.mod.FASTCAST, 100)
        mob:castSpell(367, target)
        mob:setMod(dsp.mod.FASTCAST, 10)
    end
end

I'm confused about magic_cool in general, as 6 to me means 6 seconds in between casts. I had changed mine to 13.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Aug 18, 2020 at 16:14:07_

----

I was looking at a different mob I wanted to impliment recently and now seeing this its looking like this would benefit from the same thought I had: per spell slot recast id's, recast times, cast times in the mobs spell list. This would let us change timings per spell as well as put diff sets of spells on shared timers as needed. Default zero for all 3 and if zero default to the behavior we already have now.


----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Tuesday Aug 18, 2020 at 19:32:47_

----

> 
> 
> I've actually been working on this recently myself, but stopped because i cannot get the interrupt working. Being able to interrupt him by having him switch target midcast is a critical part of the fight.
> That being said - i did come up with a way to force the insta death for pets if you want to add it here, it's another big part of their behavior.
> function onMobFight(mob,target)
> mob:SetAutoAttackEnabled(false)
> mob:SetMobAbilityEnabled(false)
> if target:isPet() then
> mob:setMod(dsp.mod.FASTCAST, 100)
> mob:castSpell(367, target)
> mob:setMod(dsp.mod.FASTCAST, 10)
> end
> end
> 
> I'm confused about magic_cool in general, as 6 to me means 6 seconds in between casts. I had changed mine to 13.

magic_cool wasn't working properly when it was being set on his onMobFight, it seems to break him.

Without digging up exactly what it was doing, it seemed to me that it ALLOWS the mob to cast that quickly, doesn't force them to.  I'll definitely include that in this PR because Nireya was telling me that he's supposed to insta-gib pets on him.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Aug 20, 2020 at 04:23:41_

----

i am really bothered about the interrupt thing, so putting out a quick call for help. could something be done in OnMagicCastingCheck so that if hate is drawn while prepping isn't equal to the original, the result returns out of the function? ahh no, because that's at the beginning of the spellcast. ugh do we really not have this functionality? it's one of the fundamental pieces of this fight and why i stopped with what you've done and haven't gone further, personally. 
im ok with moving forward with a partial culberry here, but would so much more love a complete one, wherein if he is casting a spell, and someone draws hate that isn't the spell target, his spell is interrupted. 
