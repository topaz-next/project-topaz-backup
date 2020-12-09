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

