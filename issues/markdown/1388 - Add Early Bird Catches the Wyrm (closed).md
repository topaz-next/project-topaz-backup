**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Oct 18, 2020 at 11:23:06_
_Originally opened as: project-topaz/topaz - Issue 1388_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

_ Was missing spells: Absolute Terror, Horrid Roar and Flame Blast
_ Had a wrong default subanimation in the database blocking all skills
_ Flame Blast has a messed up animation ID, all three versions. I adapted the animation ID of Inferno Blast, they're exactly the same
_ Does draw-in with the known perk of being able to pop out of bounds when drawing in while flying, like Tiamat
_ Opens the battle with a mobskill
_ Goes airborne at 66%HP and then evades all melee attacks
_ Uses a different fire magic based ranged attack while in air as well as Flame Blast and Hurricane Wing
_ Hurricane Wing in the air would be a TODO since I couldn't find the right skill for this. The standard wing is a ground animation
_ Flame Blast can be used only while in air and with full TP
_ Uses Touchdown at 33%HP and returns to all the standard wyrm attacks
_ Also gains increase in Eva, Def and M.Def after landing until death
_ Code is commented where it makes sense

The drops are already working so this would make Early Bird Catches the Wyrm complete.
- [x] Tested locally working extensively


----
<a href="https://github.com/Hozu"><img src="https://avatars3.githubusercontent.com/u/12777366?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [Hozu](https://github.com/Hozu)**
_Sunday Oct 18, 2020 at 18:21:18_

----

> _ Hurricane Wing in the air would be a TODO since I couldn't find the right skill for this. The standard wing is a ground animation

I believe the "super buff" move used by Nidhogg is supposed to be the aerial Hurricane Wings move.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 00:33:06_

----

@Hozu Thank you for the pointer, I will check on that.
~~Edit: Does not seem to be the case. Super Buff is indeed a buff. Even though it appears next to skills that Wyrm uses I don't know when this would be used. Videos I have watched of the Wyrm fight do not show a similar animation (mob turns blue temporarily, like it was a 2h, possibly Mighty Strikes; the use of this skill also prevents use of other TP moves.) 
(Also see Teo's comment above about this)~~
Just for the records: Hozu was completely right, I just interpreted this based on less insight. The airborne Hurricane Wing got knowingly hijacked and overwritten at some point. This is now corrected.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Monday Oct 19, 2020 at 05:19:07_

----

I've just gotten a `Themis Orb` on retail, so I'll be able to get caps of this soon. I just need to get someone to PL my /DNC so I can try solo it


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 07:13:11_

----

So far so good.
There's a few things that are **not related to this PR** that I _observed and affects all wyrms in general_:

- When out of player range/"too far away" from the mob, the `Touchdown` animation will not display even though the mob uses it
The magical default ranged attacks while flying have a huge range, which is nice, but easily provoke this behavior
- Draw-In while flying makes the mob move a good amount of yalms to the back, even out of bounds (known)
- SetMobSkillAttack() uses up all TP on every attack since it now uses a mobskill as a regular attack; *huge* flaw
From lua_baseentity.h:
`int32 SetMobSkillAttack(lua_State*); // enable/disable using mobskills as regular attacks`
Additionally as ibm and Teo mentioned, it is confusing that this uses a skill list ID instead of a skill
- Almost all wyrm typical attacks in `global/mobskills/` `return 1` if the AnimationSub is not 0
If any wyrm at any point has its AnimationSub changed to something else (and there's several bits for grounded mode), or a different default it will not use any of these skills
This is desirable when flying but Wyrm had a default of 6 (ground) for example and the skill Touchdown sets it to 2 after executing
- ~~For some reason after Touchdown is used mobskills will be used when reaching 1000TP not 3000TP (as when engaging the fight)~~ *(explained by ibm2431 below, I forgot about how this is natural behavior)*

I created a well commented but very dirty workaround for the TP issue which after a lot of testing feels right during the fight and is better than no TP move at all during the flight phase.

**TO DO for this PR**:
- [x] ~~Wait for Zach to make a capture and see what it yields~~
- [x] ~~Set natural magic resistances (Fire & Ice) and weaknesses (Water & Thunder); I'm simply unsure where to do this~~


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 19, 2020 at 10:24:58_

----

>  Set natural magic resistances (Fire & Ice) and weaknesses (Water & Thunder); I'm simply unsure where to do this

this is currently handled by the mob family table row


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Oct 19, 2020 at 10:27:01_

----

`SetMobSkillAttack` functions how it should in that some mobs use multiple mobskills for their regular attack (ex: Shinryu, August). It should definitely be renamed to be more explanatory.

[It should be functioning without needing 3000 TP](https://github.com/project-topaz/topaz/blob/release/src/map/ai/controllers/mob_controller.cpp#L259-L297). If it's not, something is broken.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Oct 19, 2020 at 10:39:38_

----

> For some reason after Touchdown is used mobskills will be used when reaching 1000TP not 3000TP (as when engaging the fight)

Mobs use TP moves sooner depending on their HP. At 100% HP they won't use TP until they're at 3000 TP. The point at which they're forced to use TP is earlier as their HP% goes down (on retail, they use TP at 1000 when below 25%).


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Monday Oct 19, 2020 at 16:46:11_

----

> [It should be functioning without needing 3000 TP](https://github.com/project-topaz/topaz/blob/release/src/map/ai/controllers/mob_controller.cpp#L259-L297). If it's not, something is broken.


@ibm2431 A humble `print(mob:getTP())` says more than a thousand words:
https://streamable.com/ojrve0
This record was made on a vanilla `release` build (last upstream merge last week) and with the TP hack removed. You can clearly see how once `AnimationSub(1)` plays and `SetMobSkillAttack()` kicks in I'm spamming ranged attack to no avail. Each time a regular attack is used the TP drop to 0.
Hope this helps and maybe someone could check on this.

~~On this note I would also like to point out that **`onMobFight()` fires *way* too often** if one can believe the description in `luautils.h` and `luautils.cpp` where it says:~~
> int32 OnMobFight(CBaseEntity* PMob, CBaseEntity* PTarget);                    // Сalled every 3 sec when a player fight monster

(see comment below) But I still have to make this note that my server calls this 2 to 3 times *every second*, not every 2400ms (2.4s)


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Oct 19, 2020 at 19:00:40_

----

> A humble print(mob:getTP()) says more than a thousand words:

And even if the mob has zero tp mobskill as melee will still go off at its specified melee delay interval. That it is erroneously removing tp when it "melee's" is a bug to be fixed, if that is happening (I believe it is).

> On this note I would also like to point out that onMobFight() fires way too often if one can believe the description in

it fires every ~~2400ms~~ _400ms_ exactly, and this is _intentional_.  The comment was written by someone else that I guess never saw the code that times it. (combat tick is running off the universal server tick rate in `CTaskMgr`)

Edit: ~~intentional and retail accurate too~~ I forgot Kj changed it. The global timer still happens at 2400, but mob ai ticks at 400ms.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 20, 2020 at 07:32:19_

----

Latest commits add and correct the following:

- All KS99 Wyrm specific skills were double-checked and assigned their correct values. Missing ones were added and scripted
- Two new skill lists for this Wyrm have been created. One for TP skills during flight, one for the regular attack during flight
- Someone knowingly overwrote the airborne Hurricane Wing with the Nidhogg 2h skill. This has been moved and corrected
- The Wyrm's HP were adjusted to 50,000 instead of 45,000 getting closer to the recent retail capture, Lvl was also corrected
- The Wyrm received two new traits observed in the retail capture: Regain and Regen. Both with sensible values based on stopwatch measurements
- Draw-In was moved to `onSpawn()` because `mod_modifier.h` says so:
`// 1 - player draw in, 2 - alliance draw in -- only add as a spawn mod!`
- `MOBMOD_SKILL_LIST` is now used to set the corresponding new skill set while flying and then restores it after landing
- The TP workaround was removed. It just doesn't work well in every situation. The real issue should be corrected instead
(not related to this PR though!)

TO DO:
- [x] Make Wyrm face target while flying only
- [x] Improve Touchdown behavior


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Thursday Oct 22, 2020 at 01:53:02_

----

Latest commits add and correct the following:

- Flying wyrms face the target while flying, but not on ground; Jormy and Ouryu are probably missing this too
- Touchdown handles TOO_HIGH effect, default attack and animation model
- After landing the new model animation is with wings up, Touchdown did consider this, but wyrm skills did not
- Standard wyrm skills now only block while flying, not during other ground modes like mode 2 after Touchdown
- Touchdown had a wrong close melee range of Bahamut's Touchdown which does not apply; the target can not escape Touchdown AoE due to Draw-In; Jormy and Ouryu are also missing this
- Touchdown is instant without skill cast animation

For reference see [here](https://www.youtube.com/watch?v=grUFfSbNCHU), [here](https://www.youtube.com/watch?v=6PhIvMTLl4o&feature=youtu.be) and [here](https://www.youtube.com/watch?v=j0uyB9NDhTE&feature=youtu.be)

TO DO:
- [x] Change flying attack message from "The Wyrm uses Flame Blast" to "The Wyrm hits target for x points of damage."


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Friday Oct 23, 2020 at 20:38:48_

----

@TeoTwawki Would appreciate a last review for any errors. As far as mechanics go, this is pretty much done now.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Oct 27, 2020 at 02:00:26_

----

> regression

Edited skill list so only Dragon Breath is in it:
https://youtu.be/YogcdPTTKS4

Did you rebuild?


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Oct 27, 2020 at 04:17:22_

----

Thank you very much for getting back and even providing proof of work @ibm2431 , and even more for pointing me in the right direction. It's the first time I had a newly added global function affect a PR of mine. I should have read way more thoroughly through your PR when it conflicted with this. I apologize.

My build simply didn't find that function of yours. So today I pulled everything in, rebuilt and all is good. I also adapted the Wyrm skills from this PR to use your function instead of the old `isBehind()` and tested them positively.
Also found a typo I made in the database that was fixed.
If you don't see anything else I'd say this is ready now.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Saturday Oct 31, 2020 at 17:38:03_

----

@reviewers Could this be tagged as reviewed and/or approved for merge? This works very well by now, no more changes have been requested. It's just sitting here.


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Saturday Oct 31, 2020 at 18:30:52_

----

Please remember that it's the weekend and staff/reviewers are volunteers. This will get re-reviewed and/or tested when someone has time. 


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Saturday Oct 31, 2020 at 18:54:06_

----

dunno if this needs to be tested maybe it could be merged into canary? have a few lv 99 players that can try the fight. Wish we had lots of players to try it on an alliance at 75.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Oct 31, 2020 at 22:48:26_

----

1. GitHub unfortunately doesn't let non-organization members tag the `project-topaz/reviewer` role. This is a different group of people from `reviewer` or `developer` on GitHub. (Those tags _do_ work in our Discord, though!)

2. Zach and I are the only official developers with write access, and PR reviews and merges are only a fraction of what we do. The reason that some PR reviews and merges take time is because we spend that time on things which are higher priority. There's a lot of history behind this - I've struggled with Zircon many, many times on this very subject - but slower reviews is the current solution to the problems the project faces. It's not from lack of effort - Zach and I spend more time on this project than anyone _should_.

Don't worry - I know you haven't claimed it was, MarianArlt. But I've been hearing of low-key complaining recently (not necessarily from you in particular), and this happens to be the most relevant public place for me to say the above since you mentioned review times.

3. kain, I know that you know how our process works. If you want Canaria to have new content sooner, you're going to have to start cherry-picking, merging your own work, and rebranding yourself as no longer being vanilla canary branch. We're not going to be pressured to merge PRs sooner for the benefit of players on a private server.

4. Onto the contents of the PR: I am killing fake "super buff" on any wyrms. I know the history of how it came to be. I do not care about said history, who did it, or the reasoning why. We're not assigning stuff to arbitrary non-captured skill IDs with the _hope_ it won't cause a problem later. It was a boneheaded decision _then_ because of _this exact problem_ it's posing _now_.

The rule I am imposing going forward is that if it's not seen in a capture from the mob a skill is being assigned to, the skill does not get used, period. It doesn't matter if the skill "appears" free. If it hasn't been captured, it's not used. I am so tired of this codebase "faking it" leading to problems down the line (yes, this _is_ [the paralysis bitterness](https://github.com/project-topaz/topaz/issues/327) talking). It either gets done properly, with evidence we can cite, or not at all.

In the context of Nidhogg, we can:
1. Capture; or
2. If necessary, [assign buffs without using a skill](https://github.com/project-topaz/topaz/blob/release/scripts/zones/Temenos/mobs/Proto-Ultima.lua#L21-L35).

If this results in the loss of a 2 hour animation until we better understand the mechanic behind the animation, then so be it. This fake "super buff" skill has already wasted more of our collective time and energy than it should have - time and energy which would be better spent elsewhere.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Nov 01, 2020 at 01:03:25_

----

I appreciate your comment and everything in it. I hope you saw my Discord comment, I totally understand how much work you guys must have. I did think there were more people reviewing though actually. Thanks for clarification.
Since I innocently just moved "super buff" here in this PR, should I rather revert the line where I put it back to original and only keep flying hurricane wing where it belongs?
I don't feel this PR should be made responsible for this and resolve Nidhogg on the fly, so to say.
Would appreciate further instructions, even if it was "handle Nidhogg please".
Could also remove it here as mentioned and open a new issue to document the change and have it there for later.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 01:49:04_

----

Project Meta:

Official project staff are Zircon, Wiggo, Zach, and myself. Since GitHub doesn't allow us to easily list organization/group members, we keep a list of official staff and non-official "contributor groups" in our Discord's `#resources` channel. Wiggo is currently absent (life circumstances), but he stays out of development anyway (he prefers research). Zircon - as our official project lead figurehead - doesn't allow themselves to make development decisions so there isn't an implicit power imbalance should potential development arguments come up. That leaves just me and Zach at the moment as official write-access developers, absent more official staff.

Some contributors are part of our "organization" so they can be placed in non-official-staff contributor groups (`project-topaz/developer`, `project-topaz/researcher`) and can get pinged on things that might interest them ("hey, developers, we're doing this major change", "is there a researcher that might want to look into this?). This has the unfortunate side effect of badging them as a "Member". So while I _do_ love Teo (and others), they don't have merge/write access. And as before, the mentions don't work on GitHub for anyone who isn't member of the parent organization (no doubt to kain's dismay 😉 )

We've been bouncing around ideas of giving such contributors more ways to assist the project (without giving them full repository write access), but GitHub makes this very difficult (as usual). So our ideas on that front have been stalled pending setup of more automated actions/bots.

----

Actual PR:

If Skill ID 956 is the flying version of hurricane wing (as seen from a capture), then it should stay as what you set it as.

If Skill ID 950 is the flying flame blast (again, from a capture) then that should also be kept to what you set it to.

Unless there's been a capture of Skill ID 949, it shouldn't be used for anything at all. If this means Fafnir no longer has a "spare" skill ID for the fake super buff move, that's fine, because we won't be using one. So you can revert Skill ID 949 back to what it used to be. I presume it was previously named Flame Blast because that's its name in the DAT.

We can fix Fafnir to no longer use the _completely fake_ "super buff" skill (currently in skill ID 956) in a separate PR. We may want to time approvals / merges so they both go in at the same time. I'd _like_ a volunteer for handling Fafnir's buffing properly, but if there isn't one soon-ish I can _try_ to find some time (but I've also been trying to focus on some zone performance work recently).


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Sunday Nov 01, 2020 at 02:25:58_

----

@ibm2431  yeah I unserstand staff has higher priorities, I was just offering to somehow help if this was due to needing some testing.  I think Instead I'll build it locally and provide feedback from there =)

My apologies if my comment felt as I was pressuring this PR.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Nov 01, 2020 at 07:17:41_

----

> the mentions don't work on GitHub for anyone who isn't member of the parent organization

@ibm2431 additional reason I'm unlikely to notice it:
![image](https://user-images.githubusercontent.com/6871475/97797078-cf0c0980-1be7-11eb-8769-74d0f9463620.png)

Subfolder in my inbox.

That 112 is not even a full weeks worth of unread github notifications. One mention tends to get very buried so even if I did get those, I'd be sure to miss it since I subbed to the projects general notices.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Nov 02, 2020 at 01:28:01_

----

I'll retarget to a version with post-super-merge release. The current target was branched from before I merged it.

Hey Teo, I'm remembering to retarget the open PR before deleting the target branch this time. 😉 


----
<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [zach2good](https://github.com/zach2good)**
_Wednesday Nov 04, 2020 at 06:01:23_

----

I'll go through and review this later today 👍 


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Thursday Nov 05, 2020 at 19:11:44_

----

Commenting to add cross reference to #305
