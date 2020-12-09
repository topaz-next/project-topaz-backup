**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Nov 01, 2020 at 03:38:26_
_Originally opened as: project-topaz/topaz - Issue 1464_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This PR is tightly tied to https://github.com/project-topaz/topaz/pull/1388 and came to be because that PR was found to be the legitimate use case for skill ID 956
(KS99 Wyrm airborne Hurricane Wing).

In the discussion of that PR it was decided to remove the use of any non-accurate IDs for now and instead encourage the re-factoring of the random defense/resistance buff that Nidhogg can use at will.

I commented out rather than deleting anything for later reference.


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 09:08:50_

----

Oh, Nidhogg was already set up in a local var 2hr format. That makes this a lot easier than I thought.

If proper animation / skill can't be found, then we can leave all of onMobFight as is (active), but replace the `useMobAbility` call with a direct invocation of `mob:addStatusEffectEx(tpz.effect.SUPER_BUFF, 0, 50, 0, 30)`. Then [the "super buff" skill can be deleted altogether](https://github.com/project-topaz/topaz/blob/release/scripts/globals/mobskills/super_buff.lua).

If we don't have a capture, we can go without the animation if it means fixing this wonky skill problem. 

I'd be willing to bet that Nidhogg uses VULTURE2 on retail. 😉 


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Nov 01, 2020 at 21:25:59_

----

I searched tons of functions today to see if there's a method to simply play the animationID 432 without having to call a skill but couldn't find any. Played around with inject functions (all player or NPC targeted) and did some extremely funny things with `independantAnimation()` but none of these can do this. Is there no such function?
(Would be perfectly appropriate here)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 01, 2020 at 22:31:19_

----

From @59blargedy's capture, which I won't link here on GitHub. It's on the Captures Discord. You can see the effect go off at 2:36 in her video. (Also note the animation ID.)
![super_buff](https://user-images.githubusercontent.com/13112942/97816973-52356a00-1c91-11eb-84a4-b6d6c7b37d09.png)

ActionView didn't display anything because its check [against Windower's resource table failed](https://github.com/Windower/Resources/blob/master/resources_data/monster_abilities.lua#L794-L795).

