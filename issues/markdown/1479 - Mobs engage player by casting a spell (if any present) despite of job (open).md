**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Thursday Nov 05, 2020 at 19:45:17_
_Originally opened as: project-topaz/topaz - Issue 1479_

----

<!-- place 'x' mark between square [] brackets to checkmark box -->
**_I have:_**

- [x] searched existing issues (http://project-topaz.com/issues/) to see if the issue has already been opened
- [x] checked the commit log to see if the issue has been resolved since my server was last updated

If a monster has a spell list and mp > 0 it will currently *always* instantly cast a spell when engaging its target *despite* of its job.
This is clearly a bug as `CMobController::Engage()` even explicitly creates an exception for jobs that have a value set in `MOBMOD_MAGIC_DELAY` (note the comment!):
https://github.com/project-topaz/topaz/blob/f780862f1d957b8fc4c543b80fae51f7b4d789fc/src/map/ai/controllers/mob_controller.cpp#L971-L991

The offending line here is Line 982 where `MAGIC_COOL` and a random number up to `MAGIC_DELAY` get both multiplied by `1000`, then added and the sum subtracted as milliseconds from `m_Tick`.

**The multiplier of `1000` from `getBigModMod()` simply seems to make this result too small** for the comparison with `m_LastMagicTime` later in `CMobController::IsSpellReady()`

I confirmed this by messing around with this value and simply calling with `getMobMod()` instead and manually multiplying you can manually increase/decrease the after-engage-cast-timeout for jobs that have `MAGIC_DELAY` set. This also applies for the special ability check.

It may be questioned how big this timeout should be to be retail accurate, to be able to re-write this formula.

**_Additional Information_** (Steps to reproduce/Expected behavior) **:** 

- Engage *any* mob that is *not* BLM/SMN/BLU/SCH/GEO/RUN, has spells and mp, and observe first action made.
It will always be a cast.
- Only those jobs with `MAGIC_DELAY` unset should be able to behave this way.

(On a side note, this could be questioned to only be the case while out of melee range anyways, after seeing the [recently captured video](https://youtu.be/d3I0jJ_LYLg) on Kuftal Worm (BLM) behavior)




----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Nov 05, 2020 at 20:39:18_

----

its probably worth re-confirming retail behaviors for mobs that cast. tehre were some changes over the years to when a mob chooses to hang back or close for melee, and we need to consider DRK and PLD along with RUN for our "melee casters". IIRC PLD Orcs will open with a cast and them immediately close for melee. I can't think of any RUN mob I can easily check.

The bug may have unintentionally been giving retail accurate behavior..


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Friday Nov 06, 2020 at 19:50:38_

----

I watched a lot of different captures from the capture Discord and made a [spread sheet](https://docs.google.com/spreadsheets/d/17wIamwYjD5Qv4SCkLU6YsY4BsRgFNDC_VE4iBmz5phE/edit?usp=sharing) anybody can comment on
_(see page 3 "capture observations")_

I believe to see the following:
_(my observations only! nothing definitive! would be good to have more observations)
(I watched 24 captures for this and got tired for the moment. Some jobs were not observed at all)_

• BLM seems to depend on the family:
⠀└ Aura Pots would _always_ open with a cast.
⠀└ Worms would open with cast _only if target was out of range_ _(maybe the "range" is simply very small? model size!)_
⠀└ a popped WAR/BLM NM _(huge model)_ opened casting, another popped BLM main NM _(rather large model)_ would not

• RDM seemed to behave mostly like worms but I've seen exceptions _(summoned by NM and in range, opened with cast)_
• DRK opened with cast, always...
• SMN never opened with cast
• WHM seemed to open with cast exclusively to buff up, otherwise (and mostly) wouldn't
• PLD seemed like WHM, but I only saw Ouryu and Jailer of Fortitude.
⠀└ The former would always open with a buff but since it's a BCNM he cannot cast while idle
⠀└ The latter did not, in fact, JoF did not buff up at all

• I did not observe BRD/NIN/BLU/GEO/RUN/SCH mobs
• I feel like defensive magic jobs like PLD and WHM would only open with a cast if they're not on roaming cooldown _(that much is obvious)_ and recently lost a buff
• RDM seemed to be pretty consistent in behaving like worms despite family

More observations are welcome.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Sunday Nov 08, 2020 at 09:17:59_

----

I have some I am in the process of documentation. I'll post back later with the details. So far most everything that can cast or ranged attack opens with those unless player is already in melee range at the start. NMs break the "rules" and do whatever. A few mobs seems to heavily favor specific spells to open with.

> a popped WAR/BLM NM (huge model) opened casting, another popped BLM main NM (rather large model) would not

which mobs were these specifically? I don't trust what wiki says for the jobs - wiki jobs are generally conjecture based on observed abilities a mob has


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Sunday Nov 08, 2020 at 18:43:40_

----

Awesome Teo. Thank you for the shared interest. Sure wikis only estimate, actually in my sheet I was about to put "supposed retail job" but that would've simply been to long a line.
If you wanna double check I was talking of [Apademak](https://youtu.be/bf-i0d9D9GA?t=2880) and [Jailer of Faith](https://youtu.be/uKCiducuHFs).


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Monday Nov 16, 2020 at 19:31:27_

----

K so both Apademek and Jailer of Faith are NMs, as mentions NMs don't always follow regular mob rules. For jobs I trust anything from Jimmayus' spreadsheet says over either wiki if they disagree. Lets hope they don't lol.

Below are my own observations.

***All of the below are observations of mobs that had full HP. Behaviors changes when mob is weakened***

### Magic casting mob checks

Closes for melee before casting anything/will prioritize swinging over castings:
- [x] Desert worm will not cast till I walk out of melee range
- [ ] pending
----

Opens with an immediate cast even if I am within melee range, does not close for melee until below 75% hp, spell chosen seems random:  
- [x] Tunnel Worm, contrary to the desert worm above. Will check more types of Worm.
- [x] Orcish Mesmerizer
- [x] Orcish Neckchopper (drain, bio, poison, stone)
- [x] Orcish Cursemaker
- [x] Bogy
- [x] Goblin Leecher
- [x] Goblin Shaman
- [x] Goblin weaver
- [x] Yagudo Scribe
- [x] Yagodo Accolyte
- [x] magicked bones (scythe)
- [x] Sprinkler (Ru'Aun Gardens - it opened with blaze spikes, Burst, Bio II..)
- [x] Aura Pot (shrine of Ru'Avitau - it opened with Blind, Burn,)
- [ ] pending
----

Opens with an immediate cast even if I am within melee range, will close for melee immediately after initial cast, spell chosen seems random:  
- [x] Orcish Trooper
- [ ] pending
----

Have more to add, not done yet. Also checking mobs that do ranged attacks to see if they always fire off an arrow/bolt/whatever immediately, if they will stay back, or if they will run up and point blank you between swings. I recall some behavior in regards to standing back was changed in the past, so I'm making sure what the game does in the present day for both mages and ranged attackers. ~~Have not delved into hp percent or time based changes in behaviors -yet-~~ I have used Dia to gradually lower mob HP. So far, every one I have checked will close for melee either immediately or after falling below the 75% p bar mark.

### Ranged attack mob checks

Stands back and shoots:
- [x] Orcish Stonechucker - closed for melee below 75% (used dia to lower it gradually)
- [ ] pending

Closes for melee, shoots between melee swings:
- [ ] pending

