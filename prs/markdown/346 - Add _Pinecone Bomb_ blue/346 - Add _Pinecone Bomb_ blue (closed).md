**Labels:**

focus

merge ready

research needed



<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 16, 2020 at 08:50:17_
_Originally opened as: project-topaz/topaz - Issue 346_

----

Now that the order of operations has been cleaned up for spells,
Pinecone Bomb can be properly implemented. It does damage to the mob
(which may wake it up from a previous slept state), but then can reapply
sleep as described here: https://ffxiclopedia.fandom.com/wiki/Pinecone_Bomb



----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 18, 2020 at 08:29:57_

----

Looking at the description for the spell, it claims that duration is supposed to vary depending on TP. At the moment, this is basing the duration off of attacker INT versus target resistance.

1) Is it supposed to _always_ be affected by TP?
2) Is TP -> duration effect only applicable when under Chain Affinity?
3) What's the base duration of this type of sleep? With or without Chain Affinity?
4) What's the sleep duration at certain TP values? Minimum, maximum?

@Wiggo32 I looked at your capture of you learning Pinecone Bomb and testing it out, but there was no explicit duration testing (the sapling was auto-attacked awake, and the draugar was unaffected)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 18, 2020 at 08:57:31_

----

[Bgwiki has these ftp values as 2.25](https://www.bg-wiki.com/bg/Pinecone_Bomb). My reading of [BluefTP](https://github.com/project-topaz/topaz/blob/master/scripts/globals/bluemagic.lua#L302) has these values coming out as 1.25~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 18, 2020 at 09:13:44_

----

I was going to say that the TP mod for this spell doesn't seem to be critical hit chance, but then I looked at [the blue magic global](https://github.com/project-topaz/topaz/blob/3df25d52158be6d44dfe84f198194b6822b5ebb8/scripts/globals/bluemagic.lua) and it doesn't look like tpmod params are used _at all_.

I did some searches and [found a definition for `params.tpmod = TPMOD_DURATION` for Battle Dance](https://github.com/project-topaz/topaz/blob/3df25d52158be6d44dfe84f198194b6822b5ebb8/scripts/globals/spells/bluemagic/battle_dance.lua), which seems like what we should be using here (again, this param is never checked), but [that specific global value doesn't seem to be defined anyway](https://github.com/project-topaz/topaz/blob/master/scripts/globals/bluemagic.lua#L4-L9).

I'm not going to expect you to fix that fact that these mods don't seem to do anything, but could you change this to at least _claim_ it's supposed to effect duration?


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Feb 18, 2020 at 20:07:47_

----

I believe these values are stale from when I branched this code from another spell.

It should be `2.25`, I believe. FFXIclopedia article also agrees. It has it listed as `multiplier` for pinecone bomb: https://ffxiclopedia.fandom.com/wiki/Calculating_Blue_Magic_Damage


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Feb 18, 2020 at 20:08:39_

----

This was my first time adding a BLU spell, so I'm open to any improvements.

I just copied how sleep was applied in other spells, so it may not be 100% accurate. If you have a reference for how this should be applied, please point me in the right direciton!


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Feb 18, 2020 at 20:11:53_

----

A lot of these BLU enums seems to be in bad shape. I'm happy to clean them up as needed, but need some guidance.

Would you prefer which/any of the following:

- Remove the TPMOD param since it's unused
- Add TPMOD_DURATION value since it's missing, and then reference it here
- Add usage of `params.tpmod` in the global bluemagic.lua (if so, where)

I think the bottom two are probably the *right* approach, assuming this value is supposed to be used somewhere. But if we felt this value is obsolete or unnecessary, perhaps removing it until it's implemented would be less ambiguous?

Also we should probably file an issue for this problem to track these changes, which can be applied ahead of this PR as needed.



----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Feb 19, 2020 at 06:28:45_

----

Also `params.azuretp` does not seem to be used anywhere. From what I can tell. But I'll just set it as `2.25` as well since the damage multiplier seems to be linear.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Feb 19, 2020 at 06:30:40_

----

Added a commit to address this comment.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Feb 19, 2020 at 06:36:06_

----

Filed https://github.com/project-topaz/topaz/issues/354 to track.

Let me know what your preferences are. I'm happy to do an audit or cleanup based on what is preferred. (Although if we want to use the parameters, I could use some pointers since I'm not that familiar with the code and have no retail FFXI)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 19, 2020 at 11:48:41_

----

The commit was on the branch for your PR to DSP 😉 

I'll go ahead and mark this comment as resolved though, assuming a similar commit will make it to this PR.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 19, 2020 at 11:55:08_

----

Yeah, the bottom two are the more time consuming, but overall the best choice. It will require a bit of rework for the Blue Magic global, which desperately needs it.

For the purpose of _this_ PR though, go ahead and add TPMOD_DURATION to both the global and this script (matching the one for Battle Dance), and then after a separate PR hooking up the params to be used, we can work on having spells being able to make use of the mods.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 19, 2020 at 12:00:45_

----

What we'll probably have to do is find some information - or get a capture - on the basic duration of the effect. Even if we can't fully pick apart how TP affects the duration for this (or other) Blue spells, we can at least apply the bare minimum duration for now and add a note in the script (and create a new Issue) that it's still missing duration bonuses from TP.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 04:53:57_

----

Sounds like a plan. Will update this in a commit.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 04:57:55_

----

I added a commit to both branches. I could have sworn I pushed it, but I must have forgot to `git push` or had a typo and didn't notice it failed.

Should be there now.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 04:58:09_

----

Commit added. Please take a look.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 04:59:02_

----

Sounds good.

Should I wait on someone to do a "capture"? Or should I go forward with a TODO note and reference a github issue to update the TP modification of the sleep duration?


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 05:01:28_

----

I left the semicolon here for now. I'm gonna make a new PR to remove all semicolons from this file, since it violates the style recommendations for Lua.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 15:54:11_

----

Need to update this to `damageType` after https://github.com/project-topaz/topaz/commit/b4ed738e8901e0127ffe19b855d6a886f82c476e


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 16:07:26_

----

Done.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 04:58:37_

----

We have some captures. I'll check them out and see what I can determine. Then hopefully someone more experienced can double check me.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 05:16:58_

----

We also need to scale this duration by the resist value.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 19:48:06_

----

Oh wait, we take account into that in the local above. So it should be good.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 19:48:19_

----

Rebasing and removing semicolons.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 18, 2020 at 08:29:57_

----

Looking at the description for the spell, it claims that duration is supposed to vary depending on TP. At the moment, this is basing the duration off of attacker INT versus target resistance.

1) Is it supposed to _always_ be affected by TP?
2) Is TP -> duration effect only applicable when under Chain Affinity?
3) What's the base duration of this type of sleep? With or without Chain Affinity?
4) What's the sleep duration at certain TP values? Minimum, maximum?

@Wiggo32 I looked at your capture of you learning Pinecone Bomb and testing it out, but there was no explicit duration testing (the sapling was auto-attacked awake, and the draugar was unaffected)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 18, 2020 at 08:57:31_

----

[Bgwiki has these ftp values as 2.25](https://www.bg-wiki.com/bg/Pinecone_Bomb). My reading of [BluefTP](https://github.com/project-topaz/topaz/blob/master/scripts/globals/bluemagic.lua#L302) has these values coming out as 1.25~!


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 18, 2020 at 09:13:44_

----

I was going to say that the TP mod for this spell doesn't seem to be critical hit chance, but then I looked at [the blue magic global](https://github.com/project-topaz/topaz/blob/3df25d52158be6d44dfe84f198194b6822b5ebb8/scripts/globals/bluemagic.lua) and it doesn't look like tpmod params are used _at all_.

I did some searches and [found a definition for `params.tpmod = TPMOD_DURATION` for Battle Dance](https://github.com/project-topaz/topaz/blob/3df25d52158be6d44dfe84f198194b6822b5ebb8/scripts/globals/spells/bluemagic/battle_dance.lua), which seems like what we should be using here (again, this param is never checked), but [that specific global value doesn't seem to be defined anyway](https://github.com/project-topaz/topaz/blob/master/scripts/globals/bluemagic.lua#L4-L9).

I'm not going to expect you to fix that fact that these mods don't seem to do anything, but could you change this to at least _claim_ it's supposed to effect duration?


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Feb 18, 2020 at 20:07:47_

----

I believe these values are stale from when I branched this code from another spell.

It should be `2.25`, I believe. FFXIclopedia article also agrees. It has it listed as `multiplier` for pinecone bomb: https://ffxiclopedia.fandom.com/wiki/Calculating_Blue_Magic_Damage


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Feb 18, 2020 at 20:08:39_

----

This was my first time adding a BLU spell, so I'm open to any improvements.

I just copied how sleep was applied in other spells, so it may not be 100% accurate. If you have a reference for how this should be applied, please point me in the right direciton!


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Tuesday Feb 18, 2020 at 20:11:53_

----

A lot of these BLU enums seems to be in bad shape. I'm happy to clean them up as needed, but need some guidance.

Would you prefer which/any of the following:

- Remove the TPMOD param since it's unused
- Add TPMOD_DURATION value since it's missing, and then reference it here
- Add usage of `params.tpmod` in the global bluemagic.lua (if so, where)

I think the bottom two are probably the *right* approach, assuming this value is supposed to be used somewhere. But if we felt this value is obsolete or unnecessary, perhaps removing it until it's implemented would be less ambiguous?

Also we should probably file an issue for this problem to track these changes, which can be applied ahead of this PR as needed.



----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Feb 19, 2020 at 06:28:45_

----

Also `params.azuretp` does not seem to be used anywhere. From what I can tell. But I'll just set it as `2.25` as well since the damage multiplier seems to be linear.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Feb 19, 2020 at 06:30:40_

----

Added a commit to address this comment.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Feb 19, 2020 at 06:36:06_

----

Filed https://github.com/project-topaz/topaz/issues/354 to track.

Let me know what your preferences are. I'm happy to do an audit or cleanup based on what is preferred. (Although if we want to use the parameters, I could use some pointers since I'm not that familiar with the code and have no retail FFXI)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 19, 2020 at 11:48:41_

----

The commit was on the branch for your PR to DSP 😉 

I'll go ahead and mark this comment as resolved though, assuming a similar commit will make it to this PR.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 19, 2020 at 11:55:08_

----

Yeah, the bottom two are the more time consuming, but overall the best choice. It will require a bit of rework for the Blue Magic global, which desperately needs it.

For the purpose of _this_ PR though, go ahead and add TPMOD_DURATION to both the global and this script (matching the one for Battle Dance), and then after a separate PR hooking up the params to be used, we can work on having spells being able to make use of the mods.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Wednesday Feb 19, 2020 at 12:00:45_

----

What we'll probably have to do is find some information - or get a capture - on the basic duration of the effect. Even if we can't fully pick apart how TP affects the duration for this (or other) Blue spells, we can at least apply the bare minimum duration for now and add a note in the script (and create a new Issue) that it's still missing duration bonuses from TP.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 04:53:57_

----

Sounds like a plan. Will update this in a commit.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 04:57:55_

----

I added a commit to both branches. I could have sworn I pushed it, but I must have forgot to `git push` or had a typo and didn't notice it failed.

Should be there now.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 04:58:09_

----

Commit added. Please take a look.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 04:59:02_

----

Sounds good.

Should I wait on someone to do a "capture"? Or should I go forward with a TODO note and reference a github issue to update the TP modification of the sleep duration?


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 05:01:28_

----

I left the semicolon here for now. I'm gonna make a new PR to remove all semicolons from this file, since it violates the style recommendations for Lua.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 15:54:11_

----

Need to update this to `damageType` after https://github.com/project-topaz/topaz/commit/b4ed738e8901e0127ffe19b855d6a886f82c476e


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 16:07:26_

----

Done.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 04:58:37_

----

We have some captures. I'll check them out and see what I can determine. Then hopefully someone more experienced can double check me.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 05:16:58_

----

We also need to scale this duration by the resist value.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 19:48:06_

----

Oh wait, we take account into that in the local above. So it should be good.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 19:48:19_

----

Rebasing and removing semicolons.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Feb 16, 2020 at 10:25:25_

----

Hello, @mrhappyasthma! Thank you for contributing to Project Topaz!

So that we don't use our parent project's brand, we've changed some function and table names to reflect adopting a new brand. I remember seeing that this PR was started prior to Topaz and originally submitted to our parent project - I took the liberty of updating these references for you; you don't need to sweat over them!

Although, I realize after I submitted the push that I should have asked first to make sure I didn't step on your toes. I'm sorry if I did! My intent was to make your contribution experience as painless as possible! 😅 

That said, I haven't had the chance to take a look at the code yet. We try to be relatively swift with reviews though, so I look forward to working with you soon!


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 16, 2020 at 23:25:12_

----

No worries. I look forward to your review.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Tuesday Feb 18, 2020 at 09:30:01_

----

Tagging #269 


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 15:52:57_

----

Question: Do you want me squashing these commits? Or do the mergers handle that for this repo?


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Thursday Feb 20, 2020 at 16:03:37_

----

We can go ahead and squash for you~!


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Feb 20, 2020 at 16:04:43_

----

Awesome. Just wanted to verify! :)


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Sunday Feb 23, 2020 at 19:50:10_

----

Rebased and closed out some of the outstanding comments.

This PR is still waiting on a more accurate TP-based sleep duration.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Wednesday Mar 11, 2020 at 04:01:59_

----

Corrected the attackType to be `RANGED`.

Still need to do a bit of research for the TP-based sleep. Been crazy with work and will be having more travel over the coming weeks. Whenever I can find some downtime I can plot some of the values from the captures and find a reasonable equation.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Saturday Mar 21, 2020 at 14:24:19_

----

Compiled a spreadsheet from the two captures in which Chain Affinity was used:
[Pinecone-Bomb.zip](https://github.com/project-topaz/topaz/files/4363102/Pinecone-Bomb.zip)



----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Saturday Mar 28, 2020 at 02:29:07_

----

BTW I still haven't forgotten about this. Just a crazy time we live in these days... Whenever I get some time I'll dig into those spreadsheets and compile any other data that is needed.


----
<a href="https://github.com/mrhappyasthma"><img src="https://avatars0.githubusercontent.com/u/1547356?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [mrhappyasthma](https://github.com/mrhappyasthma)**
_Thursday Apr 09, 2020 at 20:34:03_

----

Wow thanks for digging so deeply into this. I know my contributions have been sporadic and irregular. So I really appreciate you doing all this work on behalf of this PR.
