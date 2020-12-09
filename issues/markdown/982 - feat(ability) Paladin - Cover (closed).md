**Labels:**

reviewed



<a href="https://github.com/jdsmall25"><img src="https://avatars3.githubusercontent.com/u/59858074?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [jdsmall25](https://github.com/jdsmall25)**
_Thursday Aug 20, 2020 at 02:54:56_
_Originally opened as: project-topaz/topaz - Issue 982_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This PR fully implements Cover to the best of my knowledge and should close #233 .  I haven't played retail in some time so I did make some assumptions so please let me know if I've made any mistakes.  I referenced the BG wiki page for details: https://www.bg-wiki.com/bg/Cover

I mirrored the logic after trick attack and introduced equipment checks in the C code because from my understanding the augments only occur if the equipment is on during the cover not on use.  Duration on the other hand is calculated on use.

Please let me know what/if corrections need to be made.



----
<a href="https://github.com/tankfest"><img src="https://avatars1.githubusercontent.com/u/37684138?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [tankfest](https://github.com/tankfest)**
_Thursday Aug 20, 2020 at 04:32:37_

----

The style guide specifies that we should only use parenthesis to clarify order of operations.  ( )'s around if-statement conditions can be deleted.


----
<a href="https://github.com/jdsmall25"><img src="https://avatars3.githubusercontent.com/u/59858074?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jdsmall25](https://github.com/jdsmall25)**
_Thursday Aug 20, 2020 at 05:10:58_

----

Thank you for the feedback @m241dan and @tankfest.  All very good points, I'll work your feedback in. Thanks for your time.


----
<a href="https://github.com/jdsmall25"><img src="https://avatars3.githubusercontent.com/u/59858074?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jdsmall25](https://github.com/jdsmall25)**
_Friday Aug 21, 2020 at 03:42:48_

----

@m241dan I've reworked my code with your feedback.  I found a bug in the process where I didn't re-assign the attack.m_victim which was calculating the damage ratio based on the Cover Ability Target vs the User.

Please let me know if you have any additional feedback. Thanks!

Edit: I forgot to mention that this PR doesn't include calculating the custom cover enmity bonus from MobSkills.  This is simply because I have no idea where to call my new function UpdateEnmityFromCover.  The MobSkill code jumps all over the place and I was having a tough time locating a central spot that made sense.  I'd welcome any advice on where you think this might belong. Thanks!


----
<a href="https://github.com/jdsmall25"><img src="https://avatars3.githubusercontent.com/u/59858074?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jdsmall25](https://github.com/jdsmall25)**
_Monday Aug 24, 2020 at 15:17:50_

----

@m241dan As requested, refactored the absorb dmg to mp logic.  I altered your approach a little bit by letting the function handle giving mp to the defender.  Let me know if you have any more feedback.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Aug 27, 2020 at 22:17:35_

----

merger will just need to be mindful of spares differences. 


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Sunday Sep 06, 2020 at 17:17:45_

----

hey @jdsmall25 i was trying to resolve the conflicts with recently merged items and think maybe your mods got lost in some of this shuffle. I apologize for the delays and issues during vacations, and would like to merge this asap. Can you:
keep mod spares as 972-974, make sure your cover mods are actually in both files, and switch the duration mod to 967 (and any sql mods)?
Looking at this, I should have merged this before the one that took up your 964 mod, but it was done in order of receipt. Apologies and really excited to have working cover on topaz!


----
<a href="https://github.com/jdsmall25"><img src="https://avatars3.githubusercontent.com/u/59858074?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jdsmall25](https://github.com/jdsmall25)**
_Tuesday Sep 08, 2020 at 03:03:03_

----

@59blargedy I've made the requested changes. I'm unsure why the style checks are failing, there are many lines I never touched flagged as issues.


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Tuesday Sep 08, 2020 at 03:25:18_

----

> 
> 
> @59blargedy I've made the requested changes. I'm unsure why the style checks are failing, there are many lines I never touched flagged as issues.

You're fine, don't worry about it. Thanks for updating and sorry about that!


----
<a href="https://github.com/59blargedy"><img src="https://avatars0.githubusercontent.com/u/52636208?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [59blargedy](https://github.com/59blargedy)**
_Thursday Sep 10, 2020 at 04:03:09_

----

@jdsmall25  wanted to provide my testing results here. great work! going to be merging this into both release and canary shortly.
- phys damage cover works
- augmented cover with gallant coronet redirects magic, however the spell will still state it is being cast on the original party
- augmented cover with gallant coronet +1 redirects ranged damage as well
- valor surcoat converts 20% of damage to mp but does not do this to tp moves or magic damage. my guess is tp moves need to have cover added in monstertpmoves lua. (potential followup)
- correctly unable to cover beast or avatar pets, was not able to check trusts
- augmented magic cover works on nin and bard spells, as well as enfeebling magic (unsure if this is correct, noting)
- angle seems appropriate - can cover reasonably even on hilly terrain
- save the queen obtains the appropriate latent of 20 acc when cover used
- cover duration is random between 15-30, and capping out with 400 additional vit caps me at the 30 sec max
- cover duration mods work correctly
- putting 5 merits into cover (+20 seconds) consistently gives me 40 seconds, which lets me pass the max duration of merited cover (35 seconds) per old wiki. per bg wiki, merits add 1 second per merits, so im assuming that means past the cap, so will need addressing. job points are a different story down the line (followup needed)
- using cover while having not engaged the mob does not put the pld on the hate list - if you cover, then cover drops and the person you covered originally dies, the coverer has no hate (followup needed, as i assume it would put you on the hate list?) 


----
<a href="https://github.com/jdsmall25"><img src="https://avatars3.githubusercontent.com/u/59858074?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [jdsmall25](https://github.com/jdsmall25)**
_Friday Sep 11, 2020 at 20:42:40_

----

I appreciate the testing/feedback @59blargedy!

> augmented cover with gallant coronet redirects magic, however the spell will still state it is being cast on the original party

I haven't played retail in some time so I wasn't exactly sure when the cover logic should fire.  My assumption is that the mob will start casting on the original target, if the cover ability user is in the proper cover position when the spell finishes casting, it will successfully cover.  At this point though the "Mob starts casting on original target" message has already been displayed.  If cover was evaluated at the start of casting, that means the ability user would only need to be in the proper position when the casting began and we could send the appropriate message.  Afterwards though the ability user could move where ever and still successfully cover.  It made more sense to me to be assessed OnCastFinished to ensure the positioning was correct and thus I implemented the first approach.  Can anyone confirm how retail works?

>valor surcoat converts 20% of damage to mp but does not do this to tp moves or magic damage. my guess is tp moves need to have cover added in monstertpmoves lua. (potential followup)

Along the same vein, Monster TP moves are also not effected by the cover enmity bonus because I wasn't sure where to place that logic centrally.  The only way the absorb logic fires is if the function "battleutils::TakePhysicalDamage" is called which some abilities do use that I believe?

>using cover while having not engaged the mob does not put the pld on the hate list - if you cover, then cover drops and the person you covered originally dies, the coverer has no hate (followup needed, as i assume it would put you on the hate list?)

According to the bg wiki, the job ability does not trigger the effect on use.  I haven't played retail in a long time, so if someone can confirm how this should work I can fix it.
