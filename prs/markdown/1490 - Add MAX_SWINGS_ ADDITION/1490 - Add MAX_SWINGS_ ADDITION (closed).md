**Labels:**



<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Nov 10, 2020 at 02:05:55_
_Originally opened as: project-topaz/topaz - Issue 1490_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

This PR seeks to add:
• a **latent** of name **`JOB_MULTIPLE_8`** for weapons that trigger an effect while the players job is a multiple of 8 _(Octave Club)_
• a **modifier** of name **`ADDITIONAL_SWING_CHANCE`** for weapons that can trigger an additional attack *on top of* other multiple hits like Double Attack as a latent.
• a **modifier** of name **`MAX_SWINGS`** for weapons that increase their hitCount while under a latent effect.
• the latent database entry for Octave Club

As a consequence of this, this PR also had to:
• create conditions for the additional swings in `CAttackRound::CreateAttacks()`
• slightly restructure the conditions of additional swings and how they block each other in that same function
• See 4ea931fc3cf1e8db9e73e5982d087af1bee47341
(Mythic Aftermath was not blocked behind Quad/Triple/Double Attack and latent modifiers for OAT not considered)

In Detail:
• If `MAX_SWINGS` exists (should pretty much only be flagged by a latent) it will overwrite the hitCount of that weapon from the database
• The default swing now functions as a fallback after all else is considered. This improves recognition of priorities
• Quad/Triple/Double attack got their num check removed, they should be rolled in any case, also when a weapon or monster can attack several times. It is the top most priority and does not stack with regular multiple hits or mythic modifiers
• Triple/Double attack from Mythic weapons gets rolled after this if Aftermath is in effect
• Equipment modifiers from Empyrian armor is then considered
• Only if any of these fail will a weapon or monster use regular multiple hits
• In preparation for Amood Great Axes a modifier and a condition has been added especially for these, since they do indeed stack
• After all these considerations, ammo triggered additional swings from weapons like the Jailer weapons are considered, the check itself has not been changed
• All of the above are possible *additional swings*, care has been taken to make sure they can not stack up to more than 8 hits
• At the very end a default hit will always occur

This makes implementation of most weapons that increase their hitCount with a latent or some other effect now possible and secure with these mods. (Although there are extremely few to begin with)

I tested this successfully with the following setups and it works as expected.
• RDM99/PLD49
Regular Weapon: one hit
Joyeuse: occ. 2-3 hits
Kraken Club: occ. 2-8 hits
Octave Club: one hit
• RDM96/PLD48
Octave Club: occ. 2-8 hits
• WAR99/PLD49
Regular Weapon: occ. Double Attack
Joyeuse: occ. 2-3 hits with more 2's than 3's
Kraken Club: occ. 2-8 hits with a few more 2' than others
Octave Club: occ. Double Attack
• THF99/PLD49
All of the above in the same manner but with triple attack
Justice Sword + Virtue Stones: Successfully triggers an additional hit even on top of Triple Attack, making it 4 hits
Vajra + 3000TP Aftermath: occ. 2-3 hits with frequent 2's
• SAM99/PLD49
Hardwood Katana + Zanshin: occ. hits again after missing
_(Zanshin is not a member of the function in question but I wanted to be sure it works)_
Hardwood Katana + Virtue Stone: stones won't get accidentally get used
Hardwood Katana + Zanshin + Triple/Double Attack equip: Zanshin swing stacks

Things I did not implement or I could not figure out but should not be part of this PR:
• Empyrian armor modifiers have various effects on attack swings but there is little people talking about whether it stacks or not
(for now I think it is sensible to treat the Iga Garb condition that was there as if it was a roll on Double Attack)
• Somebody before me who implemented this condition mentioned something about creating a lua function, but it was not very clear what "nitty gritty stuff" refers to. I suppose its the idea of outsourcing these?
• I did not implement the missing condition for Dynamis [D] Follow-Up attack chances
• Octave Club is probably the only item in the game (?) that checks on two different lvl multipliers at the same time. This simply interferes with how the according latent switch statements are written and neither will flag in that condition.
(for now comment the multiplier of 2 out)

I'm well aware that this messes with one of the most basic mechanics of the game. Please take the time to read what I wrote as carefully as I wrote and tested this PR. Much appreciated.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Nov 12, 2020 at 15:35:57_

----

Technically, that should be 6 not 8 still. The clamp stops it from turning into 10, but it might not be obvious to new people looking back at this in the future that the modifier is additive.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Thursday Nov 12, 2020 at 16:47:45_

----

I thought it'd make sense to be more verbose so to make it use the actual desired number, but you're right. Adjusted it accordingly.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Thursday Nov 12, 2020 at 15:35:57_

----

Technically, that should be 6 not 8 still. The clamp stops it from turning into 10, but it might not be obvious to new people looking back at this in the future that the modifier is additive.


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Thursday Nov 12, 2020 at 16:47:45_

----

I thought it'd make sense to be more verbose so to make it use the actual desired number, but you're right. Adjusted it accordingly.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Tuesday Nov 10, 2020 at 02:26:01_

----

Some things you should know before reading this pr: multi hit weapons like Joyeuse were already implemented, it was a field in item_weapon table however I do want to see that column die and it migrate to the mod as is done here. Octave club is a good example of why that should be the case.

I'd like to also see the `job_multple_lv latents` changed slightly: we have a parameter field we can use on a latent. Instead of making it a static 8 for this one item, make it multiple of the specified parameter. Then we don't need a new latent ID used every time we need a different multiple number (there are several right now). `MAINJOB_MULTIPLE` set param and done.


----
<a href="https://github.com/kaincenteno"><img src="https://avatars3.githubusercontent.com/u/26943220?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [kaincenteno](https://github.com/kaincenteno)**
_Tuesday Nov 10, 2020 at 03:33:39_

----

Awesome job =)


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Tuesday Nov 10, 2020 at 23:32:39_

----

As suggested by Teo I also reduced the various JOB_MULTIPLE_X latents into one single latent of name `JOB_MULTIPLE` that takes a divisor (2 for even anyways) or 0 for odd.
Entries in item_latents.sql have been adjusted accordingly. (very few thank god...)
The night check for Eerie cloak has to be separate and was named `JOB_MULTIPLE_AT_NIGHT`.
Eerie cloak had a false duplicate in the database where the NQ version was also given the latent effect. This was removed.

The force pushes corrected a comment and a missing semicolon.


----
<a href="https://github.com/TeoTwawki"><img src="https://avatars0.githubusercontent.com/u/6871475?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [TeoTwawki](https://github.com/TeoTwawki)**
_Wednesday Nov 11, 2020 at 01:33:20_

----

I wish I could per-emptively re-approve for the force pushes I know are coming :x


###### something somethings sql rows and hit count overflows


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Wednesday Nov 11, 2020 at 02:09:14_

----

No need to force push.
• `MAX_SWINGS` has been manually limited to 8 inside of `CAttackRound::CreateAttacks()` because it wouldn't get clamped by `getHitCount()` for some reason. This led to no hit getting added at all. It is a safety measure and doesn't hurt.
• Now that this is sorted Octave Club has been activated for both latent values in the database.
• `JOB_MULTIPLE_AT_NIGHT` was missing its check for odd levels. (is not used currently but makes it future proof)

- [x] Tested locally (not multiple_at_night to be perfectly honest with you)

This closes #1498 and makes me comfortable saying that I consider this done now. (except for any requests of course)


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Friday Nov 13, 2020 at 02:08:49_

----

> so I'll wait for @ibm2431 to check it over

Nothing particularly stands out to me.

So long as it caps at 8 and additional hits are proccing off the correct hand... 🤷 

I think I've telegraphed what might be early targets the next time I touch core after my current work. I'm not gonna get fussed over virtue stones and Amood~


----
<a href="https://github.com/MarianArlt"><img src="https://avatars3.githubusercontent.com/u/1492317?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [MarianArlt](https://github.com/MarianArlt)**
_Saturday Nov 14, 2020 at 21:24:35_

----

last push was a request by @neuromancerxi to avoid a merge conflict with #1478 
modifier identifiers were increase by one since that PR will occupy `977` .
New identifiers for these mods will occupy `978` and `979`. Octave club was adjusted accordingly.
This will leave SPAREs 980-982 after this PR.

_(force push cause I forgot to edit status.lua , sorry)_


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Sunday Nov 22, 2020 at 06:00:16_

----

Merged into release.
